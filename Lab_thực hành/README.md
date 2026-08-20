# Dự Án: Chương Trình Quản Lý Sinh Viên (AI Coding)

## 1. Nhật Ký Prompt & Tiến Trình AI
* **Phân tích & Thiết kế**: Prompt: "Phân tích requirements ứng dụng CRUD sinh viên bằng Python sử dụng CSDl SQLite đơn giản."
* **Sinh Code**: Prompt: "Viết ứng dụng CLI Python kết nối SQLite gồm chức năng Thêm, Xóa, Xem danh sách sinh viên."
* **Debug**: Phát hiện lỗi crash chương trình khi nhập trùng khóa chính (Mã SV).
* **Viết Test**: Prompt: "Viết tệp unittest cho hàm thêm và xóa sinh viên trong Python."
* **Refactor**: Dùng khối `try-except` để bắt lỗi `sqlite3.IntegrityError` thay vì để ứng dụng bị crash.

## 2. Nhận Xét AI (Đúng / Sai)
* **AI làm ĐÚNG**: Sinh cấu trúc SQL chuẩn, tạo giao diện dòng lệnh (CLI) dễ dùng, viết Unit Test bao phủ tốt logic cốt lõi.
* **AI làm SAI/THIẾU**: Ban đầu AI chưa xử lý ngoại lệ khi người dùng nhập sai kiểu dữ liệu (vd: nhập chữ vào phần Tuổi/GPA) hoặc nhập trùng Mã SV khiến chương trình bị dừng đột ngột.

## 3. Hướng Dẫn Chạy Test
1. Chạy chương trình chính: `python app.py`
2. Chạy kiểm thử tự động: `python test_app.py`

## 4. License
MIT License