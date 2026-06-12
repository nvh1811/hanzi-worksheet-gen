# hanzi-worksheet-gen

# Hanzi Worksheet Generator

Công cụ hỗ trợ tạo vở tập viết chữ Hán tự động dành riêng cho người học tiếng Trung. Dự án giúp chuyển đổi từ vựng thành các trang luyện viết chuẩn lưới Mễ tự, hỗ trợ tự động dịch nghĩa và phân tách nét chữ.

## 🚀 Tính năng chính
* **Tự động hóa:** Tự động tra cứu nghĩa tiếng Việt thông qua API dịch thuật.
* **Linh hoạt:** Hỗ trợ cả chữ Phồn thể và Giản thể.
* **Chuẩn sư phạm:** Hiển thị thứ tự nét (stroke order) và lưới luyện viết (Mễ tự).
* **Tùy biến cao:** Cho phép chỉnh sửa trực tiếp nghĩa của từ trên giao diện trước khi in.
* **Xuất PDF:** Tối ưu hóa giao diện để in trực tiếp từ trình duyệt (Print to PDF).

## 🛠 Cách sử dụng
1. Truy cập vào trang web của công cụ.
2. Nhập từ vựng bạn muốn luyện tập vào ô **"Nhập từ vựng cần luyện"**.
3. Tùy chỉnh các thông số:
    * **Số dòng kẻ:** Độ dài của phần luyện viết.
    * **Màu sắc:** Tùy chỉnh màu chữ và màu lưới theo sở thích.
4. Nhấn nút **"Bắt đầu tạo vở"** để hệ thống render các trang tập viết.
5. Kiểm tra và chỉnh sửa trực tiếp nội dung (nghĩa của từ) nếu cần.
6. Nhấn **"Lưu File PDF"** (hoặc Ctrl+P) để in ra giấy hoặc lưu thành file PDF.

## 📦 Yêu cầu hệ thống
* Trình duyệt web hiện đại (Chrome, Edge, Firefox).
* Kết nối Internet (để tải dữ liệu nét chữ và gọi API dịch thuật).

## 📝 Thông tin kỹ thuật
* **Công nghệ:** HTML5, CSS3, JavaScript (Vanilla).
* **Thư viện:** * `HanziWriter`: Hỗ trợ hiển thị nét chữ.
    * `OpenCC`: Hỗ trợ chuyển đổi Phồn/Giản thể.
    * `Google Translate API`: Hỗ trợ dịch nghĩa tự động.

## 🤝 Đóng góp
Dự án được xây dựng bởi [Tên của bạn/Username của bạn]. Nếu bạn có ý tưởng cải tiến hoặc phát hiện lỗi, hãy tạo một **Issue** hoặc **Pull Request** cho repository này.

---
*Hy vọng công cụ này sẽ giúp bạn và các bạn của mình học chữ Hán hiệu quả hơn!*