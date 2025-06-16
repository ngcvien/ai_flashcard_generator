from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import json
import uuid
from datetime import datetime
import PyPDF2
import docx
import google.generativeai as genai
from werkzeug.utils import secure_filename
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Tạo thư mục uploads nếu chưa có
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('data', exist_ok=True)

# Cấu hình Google Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    """Trích xuất text từ file PDF"""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Lỗi khi đọc PDF: {e}")
    return text

def extract_text_from_docx(file_path):
    """Trích xuất text từ file DOCX"""
    text = ""
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Lỗi khi đọc DOCX: {e}")
    return text

def extract_text_from_txt(file_path):
    """Trích xuất text từ file TXT"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()
        except Exception as e:
            print(f"Lỗi khi đọc TXT: {e}")
            return ""

def generate_flashcards_with_ai(text, num_cards=10, user_note=None):
    """Sử dụng Google Gemini để tạo flashcard từ text"""
    try:
        # Tạo phần yêu cầu đặc biệt nếu có
        special_request = f"Yêu cầu đặc biệt từ người dùng:\n{user_note}\n" if user_note else ""
        
        prompt = f"""
        Bạn là một giáo viên giàu kinh nghiệm trong việc tạo flashcard học tập hiệu quả.
        Từ nội dung được cung cấp, hãy tạo {num_cards} thẻ flashcard chất lượng cao để học tập.

        Quy tắc quan trọng:
        - PHẢI trả về chính xác cú pháp JSON array
        - Mỗi phần tử trong array là một object với 2 field: "question" và "answer"
        - KHÔNG được thêm bất kỳ text nào khác ngoài JSON array
        - KHÔNG được thêm ``` hoặc markdown block
        - Đảm bảo dấu phẩy ngăn cách giữa các object là đúng cú pháp JSON

        Format phải chính xác như sau:
        [
            {{"question": "Câu hỏi 1", "answer": "Câu trả lời 1"}},
            {{"question": "Câu hỏi 2", "answer": "Câu trả lời 2"}},
            ...
        ]

        {special_request}
        
        Yêu cầu quan trọng về format:
        - Trả về dưới dạng JSON với format: [{{"question": "Câu hỏi", "answer": "Câu trả lời"}}, ...]
        - KHÔNG được thêm bất kỳ text nào ngoài JSON array

        Yêu cầu về nội dung:
        1. Câu hỏi:
           - Phải rõ ràng, cụ thể và dễ hiểu
           - Tập trung vào một khái niệm/ý tưởng chính
           - Nên sử dụng các từ hỏi: Là gì? Tại sao? Như thế nào? Giải thích? So sánh?
        
        2. Câu trả lời:
           - Ngắn gọn nhưng đầy đủ thông tin quan trọng
           - Dễ nhớ, tránh các câu dài và phức tạp
           - Nên dùng cấu trúc liệt kê nếu có nhiều điểm
        
        3. Độ khó:
           - Đa dạng từ dễ đến khó
           - 30% câu hỏi cơ bản (định nghĩa, khái niệm)
           - 40% câu hỏi trung bình (giải thích, ví dụ)
           - 30% câu hỏi nâng cao (phân tích, so sánh)
        
        4. Bố cục:
           - Sắp xếp theo thứ tự từ dễ đến khó
           - Các flashcard phải độc lập với nhau
           - Tránh lặp lại thông tin giữa các thẻ

        Nội dung cần tạo flashcard:
        {text[:3000]}  # Giới hạn 3000 ký tự
        
        Nội dung:
        {text[:3000]}  # Giới hạn 3000 ký tự
        """
        
        response = model.generate_content(prompt)        # Trích xuất JSON từ response
        content = response.text.strip()
        
        # Loại bỏ các markdown code block nếu có
        content = re.sub(r'```json\s*|\s*```', '', content)
        
        # Tìm JSON array trong response
        json_match = re.search(r'\[\s*\{.*?\}\s*\]', content, re.DOTALL)
        if json_match:
            try:
                flashcards_json = json_match.group()
                
                # Chuẩn hóa JSON string
                flashcards_json = flashcards_json.replace('\n', ' ')  # Xóa xuống dòng
                flashcards_json = flashcards_json.replace('\'', '"')  # Thay nháy đơn bằng nháy kép
                
                # Đảm bảo tên thuộc tính được bọc trong dấu ngoặc kép
                flashcards_json = re.sub(r'(\{|\,)\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*:', r'\1 "\2":', flashcards_json)
                
                # Clean up khoảng trắng thừa
                flashcards_json = re.sub(r'\s+', ' ', flashcards_json)
                
                # print("JSON sau khi format:", flashcards_json)  # Debug
                
                flashcards = json.loads(flashcards_json)
                
                # Validate cấu trúc flashcard
                valid_flashcards = []
                for card in flashcards:
                    if isinstance(card, dict) and 'question' in card and 'answer' in card:
                        valid_flashcards.append(card)
                    else:
                        print("Bỏ qua flashcard không hợp lệ:", card)
                
                return valid_flashcards if valid_flashcards else []
                
            except json.JSONDecodeError as e:
                print(f"Lỗi parse JSON: {e}")
                print("JSON sau khi format:", flashcards_json)
                return []
        else:
            print("Không tìm thấy JSON trong response")
            return []
            
    except Exception as e:
        print(f"Lỗi khi tạo flashcard với AI: {e}")
        # Fallback: tạo flashcard đơn giản từ text
        return generate_simple_flashcards(text, num_cards)

def generate_simple_flashcards(text, num_cards=10):
    """Tạo flashcard đơn giản khi AI không khả dụng"""
    sentences = text.split('.')
    flashcards = []
    
    for i, sentence in enumerate(sentences[:num_cards]):
        sentence = sentence.strip()
        if len(sentence) > 20:  # Chỉ lấy câu có độ dài hợp lý
            words = sentence.split()
            if len(words) > 5:
                # Tạo câu hỏi bằng cách ẩn một phần câu
                question = f"Hoàn thành câu: {' '.join(words[:3])} ____"
                answer = sentence
                flashcards.append({"question": question, "answer": answer})
    
    return flashcards

def save_flashcard_set(title, flashcards):
    """Lưu bộ flashcard vào file"""
    flashcard_id = str(uuid.uuid4())
    data = {
        'id': flashcard_id,
        'title': title,
        'created_at': datetime.now().isoformat(),
        'flashcards': flashcards
    }
    
    with open(f'data/{flashcard_id}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return flashcard_id

def load_flashcard_set(flashcard_id):
    """Tải bộ flashcard từ file"""
    try:
        with open(f'data/{flashcard_id}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def get_all_flashcard_sets():
    """Lấy danh sách tất cả bộ flashcard"""
    flashcard_sets = []
    for filename in os.listdir('data'):
        if filename.endswith('.json'):
            flashcard_id = filename[:-5]  # Bỏ phần .json
            data = load_flashcard_set(flashcard_id)
            if data:
                flashcard_sets.append({
                    'id': data['id'],
                    'title': data['title'],
                    'created_at': data['created_at'],
                    'count': len(data['flashcards'])
                })
    
    return sorted(flashcard_sets, key=lambda x: x['created_at'], reverse=True)

@app.route('/')
def index():
    flashcard_sets = get_all_flashcard_sets()
    return render_template('index.html', flashcard_sets=flashcard_sets)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'Không có file được chọn'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Không có file được chọn'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Trích xuất text từ file
            file_ext = filename.rsplit('.', 1)[1].lower()
            if file_ext == 'pdf':
                text = extract_text_from_pdf(file_path)
            elif file_ext == 'docx':
                text = extract_text_from_docx(file_path)
            elif file_ext == 'txt':
                text = extract_text_from_txt(file_path)
              # Tạo flashcard với AI
            num_cards = int(request.form.get('num_cards', 10))
            user_note = request.form.get('user_note')
            flashcards = generate_flashcards_with_ai(text, num_cards, user_note)
            
            # Lưu flashcard
            title = request.form.get('title', f'Flashcard từ {filename}')
            flashcard_id = save_flashcard_set(title, flashcards)
            
            # Xóa file tạm
            os.remove(file_path)
            
            return jsonify({
                'success': True,
                'flashcard_id': flashcard_id,
                'count': len(flashcards)
            })
        else:
            return jsonify({'error': 'File không được hỗ trợ'}), 400
    
    return render_template('upload.html')

@app.route('/study/<flashcard_id>')
def study(flashcard_id):
    data = load_flashcard_set(flashcard_id)
    if not data:
        return redirect(url_for('index'))
    
    return render_template('study.html', data=data)

@app.route('/create', methods=['GET', 'POST'])
def create_manual():
    if request.method == 'POST':
        title = request.form.get('title')
        flashcards_data = request.form.get('flashcards')
        
        try:
            flashcards = json.loads(flashcards_data)
            flashcard_id = save_flashcard_set(title, flashcards)
            return redirect(url_for('study', flashcard_id=flashcard_id))
        except:
            return render_template('create.html', error='Dữ liệu flashcard không hợp lệ')
    
    return render_template('create.html')

@app.route('/delete/<flashcard_id>', methods=['POST'])
def delete_flashcard_set(flashcard_id):
    try:
        os.remove(f'data/{flashcard_id}.json')
        return jsonify({'success': True})
    except:
        return jsonify({'error': 'Không thể xóa'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)