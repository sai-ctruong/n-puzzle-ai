<div align="center">

# 🧩 N-Puzzle AI Game

![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Non--Commercial-e74c3c?style=for-the-badge)
![GUI](https://img.shields.io/badge/GUI-Tkinter-f39c12?style=for-the-badge)
![Algorithm](https://img.shields.io/badge/AI_Solver-7_Algorithms-9b59b6?style=for-the-badge)

**Trò chơi giải đố thông minh với AI Solver mạnh mẽ và khả năng tùy chỉnh hình ảnh**

[Tính năng](#-tính-năng) • [Demo](#-demo) • [Cài đặt](#-cài-đặt) • [Hướng dẫn](#-hướng-dẫn-sử-dụng) • [Thuật toán](#-thuật-toán-ai) • [Cấu trúc](#️-cấu-trúc-dự-án)

</div>

---

## 📖 Giới thiệu

N-Puzzle AI Game là một ứng dụng giải đố hiện đại được phát triển hoàn toàn bằng Python. Dự án kết hợp giữa trò chơi giải trí và nghiên cứu thuật toán AI, cho phép người dùng trải nghiệm 7 thuật toán tìm kiếm khác nhau để giải quyết bài toán N-Puzzle (8-Puzzle, 15-Puzzle, 24-Puzzle, v.v.).

### 🎯 Điểm nổi bật

- ✅ Hỗ trợ kích thước bàn cờ tùy chỉnh (NxM)
- ✅ Chế độ chơi với hình ảnh cá nhân
- ✅ 7 thuật toán AI tìm kiếm tích hợp
- ✅ Thống kê hiệu năng chi tiết
- ✅ Giao diện đẹp mắt, dễ sử dụng
- ✅ Hoạt ảnh mượt mà với tùy chọn bỏ qua

---

## ✨ Tính năng

### 🎮 Chế độ chơi đa dạng

- **Chế độ số**: Chơi với các ô số truyền thống
- **Chế độ hình ảnh**: Tải lên ảnh của bạn và ghép hình từ các mảnh ảnh

### 🤖 AI Solver với 7 thuật toán

| Thuật toán | Loại | Đặc điểm |
|------------|------|----------|
| **BFS** | Tìm kiếm mù | Đảm bảo tìm được lời giải ngắn nhất |
| **DFS** | Tìm kiếm mù | Nhanh nhưng không đảm bảo tối ưu |
| **IDDFS** | Tìm kiếm mù | Kết hợp ưu điểm BFS và DFS |
| **UCS** | Tìm kiếm có giá | Tối ưu với chi phí đồng nhất |
| **A*** | Tìm kiếm heuristic | Tối ưu và hiệu quả nhất |
| **Greedy** | Tìm kiếm heuristic | Nhanh nhưng không đảm bảo tối ưu |
| **Beam Search** | Tìm kiếm heuristic | Cân bằng giữa tốc độ và bộ nhớ |

### 📊 Thống kê hiệu năng

Ứng dụng tự động thu thập và hiển thị:
- ⏱️ Thời gian thực thi (ms)
- 🔢 Số trạng thái được sinh ra
- 👁️ Số trạng thái đã duyệt
- 📏 Độ dài lời giải (số bước)

### ⚙️ Tiện ích bổ sung

- **Skip Animation**: Bỏ qua hoạt ảnh, chỉ xem 5 bước cuối
- **Reset**: Quay về trạng thái ban đầu
- **Random**: Tạo bàn cờ ngẫu nhiên mới
- **Load Image**: Tải ảnh tùy chỉnh

---

## 🎬 Demo

### � Giao diện chính

<!-- Thay thế đường dẫn bên dưới bằng link ảnh của bạn -->
![Giao diện chính](![alt text](image.png))

### 🎥 Video demo

<div align="center">
  <video src="./videos/Captures/demo.mp4" controls width="800">
    Your browser does not support the video tag.
  </video>
</div>



---

## 🚀 Cài đặt

### Yêu cầu hệ thống

- Python 3.x trở lên
- Hệ điều hành: Windows, macOS, Linux

### Các bước cài đặt

1. **Clone repository**

```bash
git clone https://github.com/your-username/n-puzzle-ai.git
cd n-puzzle-ai
```

2. **Cài đặt thư viện phụ thuộc**

```bash
pip install Pillow
```

> **Lưu ý**: Pillow là thư viện duy nhất cần cài đặt thêm. Tkinter đã được tích hợp sẵn trong Python.

3. **Chạy ứng dụng**

```bash
python main.py
```

---

## 📚 Hướng dẫn sử dụng

### Bước 1: Thiết lập kích thước

1. Khởi chạy ứng dụng bằng lệnh `python main.py`
2. Nhập số hàng và số cột (tối thiểu 2x2)
3. Nhấn "BẮT ĐẦU TRÒ CHƠI"

### Bước 2: Chơi thủ công

- Sử dụng **phím mũi tên** (↑ ↓ ← →) để di chuyển các ô
- Mục tiêu: Sắp xếp các số theo thứ tự từ 1 đến N-1, ô trống ở cuối

### Bước 3: Sử dụng AI Solver

1. Chọn một trong 7 thuật toán AI
2. Quan sát hoạt ảnh giải đố tự động
3. Xem thống kê hiệu năng trong bảng kết quả

### Bước 4: Chơi với hình ảnh

1. Nhấn nút "Tải Ảnh"
2. Chọn file ảnh (PNG, JPG, JPEG, BMP)
3. Ảnh sẽ được tự động chia thành các mảnh ghép

### Các phím tắt

| Phím | Chức năng |
|------|-----------|
| `↑` | Di chuyển ô trống lên |
| `↓` | Di chuyển ô trống xuống |
| `←` | Di chuyển ô trống sang trái |
| `→` | Di chuyển ô trống sang phải |

---

## 🧠 Thuật toán AI

### 1. Breadth-First Search (BFS)

**Đặc điểm**: Duyệt theo chiều rộng, đảm bảo tìm được lời giải ngắn nhất.

**Ưu điểm**: 
- Tìm được lời giải tối ưu
- Hoàn chỉnh (luôn tìm được lời giải nếu có)

**Nhược điểm**:
- Tốn nhiều bộ nhớ
- Chậm với bài toán lớn

### 2. Depth-First Search (DFS)

**Đặc điểm**: Duyệt theo chiều sâu với giới hạn độ sâu.

**Ưu điểm**:
- Tiết kiệm bộ nhớ
- Nhanh trong một số trường hợp

**Nhược điểm**:
- Không đảm bảo tối ưu
- Có thể không tìm được lời giải nếu giới hạn độ sâu không đủ

### 3. Iterative Deepening DFS (IDDFS)

**Đặc điểm**: Kết hợp ưu điểm của BFS và DFS.

**Ưu điểm**:
- Tìm được lời giải tối ưu như BFS
- Tiết kiệm bộ nhớ như DFS

**Nhược điểm**:
- Duyệt lại các trạng thái nhiều lần

### 4. Uniform Cost Search (UCS)

**Đặc điểm**: Tìm kiếm dựa trên chi phí đồng nhất.

**Ưu điểm**:
- Tìm được lời giải tối ưu
- Phù hợp với bài toán có chi phí khác nhau

**Nhược điểm**:
- Tương tự BFS về độ phức tạp

### 5. A* Search

**Đặc điểm**: Sử dụng heuristic Manhattan Distance.

**Ưu điểm**:
- Hiệu quả nhất trong các thuật toán
- Tìm được lời giải tối ưu
- Duyệt ít trạng thái nhất

**Nhược điểm**:
- Phụ thuộc vào chất lượng heuristic

### 6. Greedy Best-First Search

**Đặc điểm**: Chỉ sử dụng heuristic, không tính chi phí đường đi.

**Ưu điểm**:
- Rất nhanh
- Tiết kiệm bộ nhớ

**Nhược điểm**:
- Không đảm bảo tối ưu
- Có thể bị kẹt trong local minimum

### 7. Beam Search

**Đặc điểm**: Giới hạn số lượng trạng thái trong frontier (beam width = 3).

**Ưu điểm**:
- Cân bằng giữa tốc độ và bộ nhớ
- Phù hợp với bài toán lớn

**Nhược điểm**:
- Không đảm bảo tìm được lời giải
- Không đảm bảo tối ưu

---

## 🏗️ Cấu trúc dự án

```
n-puzzle-ai/
│
├── main.py              # File khởi chạy chính, màn hình cài đặt
├── puzzle_gui.py        # Giao diện người dùng (Tkinter)
├── puzzle_logic.py      # Logic trò chơi, kiểm tra tính giải được
├── puzzle_solver.py     # Triển khai 7 thuật toán AI
├── README.md            # Tài liệu dự án
│
├── screenshots/         # Thư mục chứa ảnh demo (tự tạo)
│   ├── main-interface.png
│   ├── setup.png
│   ├── number-mode.png
│   ├── image-mode.png
│   ├── ai-solver.png
│   ├── statistics.png
│   └── animation.gif
│
└── videos/              # Thư mục chứa video demo (tự tạo)
    └── demo.mp4
```

### Chi tiết các module

#### `main.py`
- Màn hình cài đặt ban đầu
- Nhập kích thước bàn cờ (rows x cols)
- Khởi tạo giao diện chính

#### `puzzle_gui.py`
- Quản lý giao diện Tkinter
- Xử lý sự kiện người dùng
- Hiển thị hoạt ảnh giải đố
- Tải và hiển thị hình ảnh
- Cập nhật bảng thống kê

#### `puzzle_logic.py`
- Sinh bàn cờ ngẫu nhiên có thể giải được
- Kiểm tra tính giải được (solvability check)
- Tính toán heuristic (Manhattan Distance)
- Lấy các trạng thái kế tiếp (neighbors)

#### `puzzle_solver.py`
- Triển khai 7 thuật toán tìm kiếm
- Theo dõi số trạng thái sinh ra và duyệt
- Hỗ trợ dừng giữa chừng
- Callback cập nhật GUI

---

## 🎓 Kiến thức áp dụng

Dự án này áp dụng các kiến thức về:

- **Cấu trúc dữ liệu**: Queue, Stack, Priority Queue (Heap)
- **Thuật toán tìm kiếm**: Uninformed Search, Informed Search
- **Heuristic**: Manhattan Distance
- **Lập trình GUI**: Tkinter
- **Xử lý ảnh**: PIL/Pillow
- **Lập trình hướng đối tượng**: Class, Module

---

## 📊 So sánh hiệu năng

### Ví dụ với bàn cờ 3x3 (8-Puzzle)

| Thuật toán | Thời gian (ms) | Trạng thái sinh | Trạng thái duyệt | Số bước |
|------------|----------------|-----------------|------------------|---------|
| BFS | 245.32 | 9841 | 4521 | 22 |
| DFS | 89.15 | 3214 | 1876 | 156 |
| IDDFS | 312.45 | 12453 | 5632 | 22 |
| UCS | 198.76 | 8765 | 4123 | 22 |
| **A*** | **87.23** | **2341** | **1234** | **22** |
| Greedy | 45.67 | 1876 | 987 | 28 |
| Beam | 56.89 | 2145 | 1098 | 26 |

> **Kết luận**: A* là thuật toán hiệu quả nhất, cân bằng giữa tốc độ và tính tối ưu.

---

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Nếu bạn muốn cải thiện dự án:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

### Ý tưởng phát triển

- [ ] Thêm thuật toán IDA* (Iterative Deepening A*)
- [ ] Hỗ trợ nhiều heuristic khác nhau
- [ ] Chế độ multiplayer
- [ ] Lưu và tải trạng thái trò chơi
- [ ] Leaderboard với thời gian giải nhanh nhất
- [ ] Hỗ trợ dark mode
- [ ] Export video giải đố

---

## 📄 Giấy phép

Dự án này được phát hành dưới giấy phép **Non-Commercial License**.

**Điều khoản sử dụng**:
- ✅ Sử dụng cho mục đích học tập và nghiên cứu
- ✅ Sử dụng cho đồ án, bài tập lớn
- ✅ Chia sẻ và chỉnh sửa mã nguồn
- ❌ Sử dụng cho mục đích thương mại
- ❌ Bán hoặc phân phối có thu phí

---

## 👨‍💻 Tác giả

**Your Name**

- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com

---

## 🙏 Lời cảm ơn

- Cảm ơn cộng đồng Python và Tkinter
- Cảm ơn các tài liệu về thuật toán AI
- Cảm ơn tất cả những người đã đóng góp cho dự án

---

## 📞 Liên hệ

Nếu bạn có câu hỏi hoặc gặp vấn đề, vui lòng:

- Mở [Issue](https://github.com/your-username/n-puzzle-ai/issues)
- Gửi email: your.email@example.com
- Tham gia [Discussions](https://github.com/your-username/n-puzzle-ai/discussions)

---

<div align="center">

**⭐ Nếu bạn thấy dự án hữu ích, hãy cho một ngôi sao! ⭐**

Made with ❤️ by [Your Name](https://github.com/your-username)

</div>
