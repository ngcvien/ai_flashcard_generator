# AI Flashcard Generator

Ứng dụng web giúp tự động tạo flashcard học tập từ tài liệu sử dụng AI (Google Gemini).

## Tính năng

- 🤖 Tự động tạo flashcard từ file PDF, DOCX, TXT sử dụng AI
- 📝 Cho phép thêm ghi chú hướng dẫn AI tạo flashcard theo ý muốn
- 🔀 Xáo trộn thứ tự học flashcard
- 📊 Theo dõi tiến độ học tập
- ⭐ Đánh giá độ khó của từng thẻ (Dễ, Trung bình, Khó)
- 🔄 Chức năng ôn tập lại các thẻ khó
- ⌨️ Hỗ trợ phím tắt để học nhanh hơn

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/ngcvien/ai_flashcard_generator.git
cd ai_flashcard_generator
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

3. Cấu hình Google Gemini API:
- Tạo file `.env` trong thư mục gốc
- Thêm API key của bạn vào file:
```
GOOGLE_API_KEY=your_api_key_here
```

4. Chạy ứng dụng:
```bash
python app.py
```

Truy cập http://localhost:5000 để bắt đầu sử dụng.

## Cách sử dụng

1. **Tạo Flashcard từ file**
   - Tải lên file (PDF, DOCX, TXT)
   - Nhập tiêu đề cho bộ flashcard
   - Chọn số lượng flashcard muốn tạo
   - Thêm ghi chú hướng dẫn AI (không bắt buộc)
   - Click "Tạo flashcard với AI"

2. **Học với Flashcard**
   - Click để lật thẻ xem đáp án
   - Đánh giá độ khó (Dễ, Trung bình, Khó)
   - Sử dụng phím tắt để học nhanh hơn
   - Theo dõi tiến độ qua thanh progress bar

3. **Phím tắt**
   - Space: Lật thẻ
   - ←: Thẻ trước
   - →: Thẻ tiếp theo
   - 1: Đánh dấu dễ
   - 2: Đánh dấu trung bình
   - 3: Đánh dấu khó

## Cấu trúc thư mục

```
ai_flashcard_generator/
├── app.py              # File chính của ứng dụng
├── requirements.txt    # Các thư viện cần thiết
├── data/              # Lưu trữ các bộ flashcard
├── static/            # File tĩnh (CSS, JS, images)
├── templates/         # Template HTML
├── uploads/          # Thư mục tạm cho file upload
└── .env              # File cấu hình (không được commit)
```

## Yêu cầu hệ thống

- Python 3.8+
- Các thư viện trong requirements.txt
- Google Gemini API key

## Công nghệ sử dụng

- Flask: Web framework
- Google Generative AI (Gemini): Tạo flashcard thông minh
- Bootstrap 5: Giao diện người dùng
- PyPDF2: Đọc file PDF
- python-docx: Đọc file DOCX
