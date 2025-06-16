# AI Flashcard Generator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

Ứng dụng web giúp tự động tạo flashcard học tập từ tài liệu sử dụng AI (Google Gemini). Ứng dụng cho phép tải lên tài liệu dạng PDF, DOCX hoặc TXT và tự động tạo ra các flashcard học tập với sự hỗ trợ của AI.

🌟 [Demo](#) | 📚 [Documentation](#) | 🐛 [Report Bug](https://github.com/ngcvien/ai_flashcard_generator/issues) | ✨ [Request Feature](https://github.com/ngcvien/ai_flashcard_generator/issues)

## ✨ Tính năng

- 🤖 Tự động tạo flashcard từ file PDF, DOCX, TXT sử dụng AI
- 📝 Cho phép thêm ghi chú hướng dẫn AI tạo flashcard theo ý muốn
- 🔀 Xáo trộn thứ tự học flashcard
- 📊 Theo dõi tiến độ học tập
- ⭐ Đánh giá độ khó của từng thẻ (Dễ, Trung bình, Khó)
- 🔄 Chức năng ôn tập lại các thẻ khó
- ⌨️ Hỗ trợ phím tắt để học nhanh hơn

## 🚀 Bắt đầu

### Prerequisites

- Python 3.8 trở lên
- Pip (Python package installer)
- Google Gemini API key

### Cài đặt

1. Clone repository:
```bash
git clone https://github.com/ngcvien/ai_flashcard_generator.git
cd ai_flashcard_generator
```

2. Tạo và kích hoạt môi trường ảo (khuyến nghị):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:
```bash
pip install -r Requirements.txt
```

4. Cấu hình biến môi trường:
```bash
# Windows
copy .env.example .env

# Linux/MacOS
cp .env.example .env
```

5. Cập nhật các biến trong file `.env`:
```ini
FLASK_SECRET_KEY=your_secret_key_here  # Có thể tạo bằng: python -c "import secrets; print(secrets.token_hex())"
GOOGLE_API_KEY=your_api_key_here       # Lấy từ Google AI Studio
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
├── Requirements.txt    # Các thư viện cần thiết
├── data/              # Lưu trữ các bộ flashcard
├── static/            # File tĩnh (CSS, JS, images)
├── templates/         # Template HTML
│   ├── base.html     # Template cơ sở
│   ├── create.html   # Trang tạo flashcard
│   ├── index.html    # Trang chủ
│   ├── study.html    # Trang học flashcard
│   └── upload.html   # Trang tải lên tài liệu
├── uploads/          # Thư mục tạm cho file upload
└── .env              # File cấu hình (không được commit)
```

## Yêu cầu hệ thống

- Python 3.8+
- Các thư viện trong Requirements.txt
- Google Gemini API key
- Đủ dung lượng ổ cứng để lưu trữ tài liệu và flashcard

## Biến môi trường

| Biến | Mô tả |
|------|--------|
| `FLASK_SECRET_KEY` | Khóa bí mật cho Flask session |
| `GOOGLE_API_KEY` | API key của Google Gemini |

## 🛠️ Công nghệ sử dụng

- [Flask](https://flask.palletsprojects.com/): Web framework
- [Google Generative AI (Gemini)](https://deepmind.google/technologies/gemini/): Tạo flashcard thông minh
- [Bootstrap 5](https://getbootstrap.com/): Giao diện người dùng
- [PyPDF2](https://pypdf2.readthedocs.io/): Đọc file PDF
- [python-docx](https://python-docx.readthedocs.io/): Đọc file DOCX
- [python-dotenv](https://github.com/theskumar/python-dotenv): Quản lý biến môi trường

## 🚧 Roadmap

- [x] Hỗ trợ file PDF, DOCX, TXT
- [x] Tạo flashcard tự động với AI
- [x] Theo dõi tiến độ học tập
- [ ] Xuất flashcard ra file
- [ ] Hỗ trợ nhiều ngôn ngữ
- [ ] API cho ứng dụng mobile

Xem [open issues](https://github.com/ngcvien/ai_flashcard_generator/issues) để biết danh sách đầy đủ các tính năng đề xuất và các vấn đề đã biết.

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh và rất có giá trị. Nếu bạn có đề xuất để cải thiện dự án:

1. Fork dự án
2. Tạo branch cho tính năng của bạn (`git checkout -b feature/AmazingFeature`)
3. Commit các thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📝 License

Được phân phối theo giấy phép MIT. Xem `LICENSE` để biết thêm thông tin.

## 🔒 Bảo mật

- KHÔNG BAO GIỜ commit file `.env` lên repository
- Bảo vệ API key của bạn
- Thường xuyên cập nhật các dependencies
- Backup dữ liệu trong thư mục `data/` định kỳ

## 📧 Liên hệ

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/ngcvien/ai_flashcard_generator](https://github.com/ngcvien/ai_flashcard_generator)
