# AI Flashcard Generator

Ứng dụng web giúp tự động tạo flashcard học tập từ tài liệu sử dụng AI (Google Gemini). Ứng dụng cho phép tải lên tài liệu dạng PDF, DOCX hoặc TXT và tự động tạo ra các flashcard học tập với sự hỗ trợ của AI.

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
pip install -r Requirements.txt
```

3. Cấu hình biến môi trường:
- Tạo file `.env` trong thư mục gốc
- Thêm các biến môi trường cần thiết vào file:
```
FLASK_SECRET_KEY=your_secret_key_here
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

## Công nghệ sử dụng

- Flask: Web framework
- Google Generative AI (Gemini): Tạo flashcard thông minh
- Bootstrap 5: Giao diện người dùng
- PyPDF2: Đọc file PDF
- python-docx: Đọc file DOCX
- python-dotenv: Quản lý biến môi trường

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng:

1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## Bảo mật

- Không bao giờ commit file `.env` lên repository
- Bảo vệ API key của bạn
- Thường xuyên kiểm tra và cập nhật các dependencies
