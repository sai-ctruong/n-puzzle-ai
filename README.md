<div align="center">

# 🧩 N-Puzzle AI Game

![Python Version](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Non--Commercial-e74c3c?style=for-the-badge)
![GUI](https://img.shields.io/badge/GUI-Tkinter-f39c12?style=for-the-badge)
![Algorithm](https://img.shields.io/badge/AI_Solver-7_Algorithms-9b59b6?style=for-the-badge)

*Một ứng dụng giải đố thông minh với khả năng cá nhân hóa hình ảnh và nền tảng AI mạnh mẽ.*

</div>

---

Một tựa game giải đố N-Puzzle (8-Puzzle, 15-Puzzle, v.v.) hiện đại được thiết kế hoàn toàn bằng Python. Phiên bản này đi kèm theo hệ thống trí tuệ nhân tạo (AI) giúp bạn tự động giải bàn cờ bằng 7 thuật toán tìm kiếm phổ biến nhất, cùng với khả năng tuỳ biến chơi bằng hình ảnh của riêng mình.

## ✨ Tính năng nổi bật

* **📐 Tuỳ chỉnh kích thước đa dạng:** Bạn không bị gò bó trong tỷ lệ 3x3 hay 4x4 truyền thống. Khởi tạo một bàn cờ có độ lớn tuỳ ý (NxM).
* **🖼️ Chế độ chơi Hình ảnh (Image Mode):** Cảm thấy những con số quá nhàm chán? Tải lên bất kì bức ảnh nào (`png`, `jpg`) từ máy tính, nó sẽ được tự động crop vuông và chia cắt thành từng mảnh ghép hoàn hảo.
* **🤖 Chế độ tự động giải (AI Solver):** Tích hợp sườn lý thuyết đồ thị hiện đại để cho phép máy tính tự giải bàn cờ, theo dõi trực quan các bước đi bằng hoạt ảnh.
  * *Các thuật toán hỗ trợ:*
    * **Tìm kiếm mù:** Chẩn đoán theo chiều rộng (BFS), chiều sâu (DFS), và sâu dần (IDDFS).
    * **Tìm kiếm có giá:** Uniform Cost Search (UCS).
    * **Tìm kiếm có định hướng (Heuristic Search):** A* (A-Star), Tìm kiếm tham lam (Greedy Search), và Beam Search.
* **⏩ Bỏ qua hoạt ảnh (Skip Anim):** Cực kì hữu ích khi AI tìm ra một đường đi quá dài, nhảy ngay đến 5 bước cuối thay vì ngồi lãng phí thời gian xem máy tính "trình diễn".
* **📊 Thống kê hiệu năng:** Bảng dữ liệu tự động thống kê thời gian duyệt (ms), số trạng thái sinh ra, số trạng thái đã duyệt và độ dài kết quả giúp bạn đánh giá trực quan ưu/nhược điểm từng thuật toán.

## 🚀 Hướng dẫn cài đặt

Bạn cần cài đặt **Python 3.x** trên hệ thống máy tính của mình.

1. **Clone mã nguồn về máy** (Hoặc tải tệp ZIP):
   ```bash
   git clone https://github.com/sai-ctruong/n-puzzle-ai.git
   cd n-puzzle-ai
   ```

2. **Cài đặt thư viện xử lý ảnh Pillow** (Bắt buộc dùng cho chế độ Hình ảnh):
   ```bash
   pip install Pillow
   ```

3. **Chạy trò chơi:**
   ```bash
   python main.py
   ```

## 🏗️ Cấu trúc dự án

Dự án này được tối ưu hoá cấu trúc theo hướng phân rã (modular) để dễ dàng theo dõi và nâng cấp:

- 🪟 `main.py`: Tệp khởi chạy chính. Thiết lập và hiển thị màn hình cài đặt cấu hình số Hàng x Cột bằng giao diện hiện đại.
- 🎨 `puzzle_gui.py`: Trái tim hiển thị của trò chơi (`tk`). Phụ trách việc vẽ giao diện, di chuyển ma trận, gọi các file thuật toán thao tác và hiển thị hoạt ảnh mượt mà trên bàn cờ.
- 🧠 `puzzle_solver.py`: Bộ máy AI hoàn toàn tách biệt. Đón nhận đầu vào State, chạy các thuật toán Search Logic với `heapq` / `deque` và trả về danh sách các Node cần đi để đến đích nhanh nhất.
- ⚙️ `puzzle_logic.py`: Chứa các hàm nghiệp vụ tiện ích cơ bản nhưng đặc biệt cấp thiết: Kiểm tra tính giải được của bàn cờ (Inversions parity check), lấy các ô lân cận (neighbors) và sinh bảng xáo trộn.

## 🎮 Cách tận hưởng trò chơi
- Tại cửa sổ Settings, điền số cột và số hàng hợp lệ (`>=2`) và ấn "Bắt đầu".
- Điều hướng các mảnh ghép bằng **4 phím di chuyển Mũi Tên** (Arrow Keys) trên bàn phím.
- Lắp lần lượt từng khối theo thứ tự hoặc chắp vá lại chân dung của bức ảnh bạn vừa tải. 
- Nếu cảm thấy bế tắc, hãy nhờ đến một trong các thuật toán AI ở dãy công cụ bên dưới! 

## 📝 Giấy phép (License)
Dự án này phục vụ hoàn toàn cho mục đích học tập, nghiên cứu và phát triển giáo dục. **Nghiêm cấm mọi hình thức sử dụng dự án với mục đích thương mại (Non-Commercial)**. Bạn có thể tự do tải mã nguồn về để tạo đồ án, làm bài tập lớn và giao lưu mã nguồn mở.
