import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
import copy
import time
from puzzle_logic import PuzzleLogic
from puzzle_solver import PuzzleSolver

class PuzzleGUI:
    def __init__(self, root, rows, cols, start_state=None, goal_state=None):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.logic = PuzzleLogic(rows, cols)
        
        self.image_tiles = None  # Giữ logic ảnh nếu cần sau này

        if start_state is None or goal_state is None:
            self.state = self.logic.generate_default_state()
            self.initial_state = copy.deepcopy(self.state)
        else:
            self.state = copy.deepcopy(start_state)
            self.initial_state = copy.deepcopy(start_state)
            self.logic.goal_state = goal_state
            self.logic.goal_positions = {
                goal_state[i][j]: (i, j)
                for i in range(rows)
                for j in range(cols)
            }

        self.move_count = 0
        self.stop_flag = False
        self.skip_anim_flag = False

        self.solver = PuzzleSolver(
            self.logic, 
            gui_callback=self._gui_update_callback, 
            check_stop_flag=self._check_stop_flag
        )

        self.setup_ui()

    def _gui_update_callback(self):
        try:
            self.root.update()
        except tk.TclError:
            self.stop_flag = True

    def _check_stop_flag(self):
        return self.stop_flag

    def setup_ui(self):
        self.root.title(f"{self.rows*self.cols-1}-Puzzle Game ({self.rows}x{self.cols})")
        self.root.configure(bg="#1a202c")

        title = tk.Label(self.root, text=f"{self.rows*self.cols-1}-PUZZLE GAME",
                         font=("Helvetica", 28, "bold"),
                         fg="#e2e8f0", bg="#1a202c", pady=20)
        title.pack()

        self.frame = tk.Frame(self.root, bg="#2d3748", padx=15, pady=15, relief="flat", bd=5)
        self.frame.pack(pady=10)

        self.label_steps = tk.Label(self.root, text=f"Số bước: {self.move_count}",
                                    font=("Helvetica", 16, "bold"),
                                    fg="#f6e05e", bg="#1a202c", pady=10)
        self.label_steps.pack()

        control_frame = tk.Frame(self.root, bg="#1a202c", pady=10)
        control_frame.pack()

        algo_frame = tk.LabelFrame(control_frame, text="🔍 Thuật toán tìm kiếm", bg="#1a202c", fg="#a0aec0", font=("Helvetica", 10, "bold"), bd=1, relief="ridge", padx=10, pady=5)
        algo_frame.grid(row=0, column=0, padx=10, sticky="n")

        action_frame = tk.LabelFrame(control_frame, text="⚙️ Tiện ích & Cài đặt", bg="#1a202c", fg="#a0aec0", font=("Helvetica", 10, "bold"), bd=1, relief="ridge", padx=10, pady=5)
        action_frame.grid(row=0, column=1, padx=10, sticky="n")

        button_style = {
            "font": ("Helvetica", 11, "bold"),
            "width": 10,
            "height": 1,
            "relief": "flat",
            "bd": 0,
            "fg": "white",
            "activeforeground": "white",
            "cursor": "hand2"
        }

        # Các nút thuật toán
        tk.Button(algo_frame, text="BFS", command=self.solve_puzzle_bfs, bg="#2ecc71", activebackground="#27ae60", **button_style).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(algo_frame, text="DFS", command=self.solve_puzzle_dfs, bg="#e67e22", activebackground="#d35400", **button_style).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(algo_frame, text="IDDFS", command=self.solve_puzzle_iddfs, bg="#c0392b", activebackground="#a93226", **button_style).grid(row=0, column=2, padx=4, pady=4)
        tk.Button(algo_frame, text="UCS", command=self.solve_puzzle_ucs, bg="#8e44ad", activebackground="#6c3483", **button_style).grid(row=0, column=3, padx=4, pady=4)
        
        tk.Button(algo_frame, text="A*", command=self.solve_puzzle_astar, bg="#3498db", activebackground="#2980b9", **button_style).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(algo_frame, text="Greedy", command=self.solve_puzzle_greedy, bg="#16a085", activebackground="#1abc9c", **button_style).grid(row=1, column=1, padx=4, pady=4)
        tk.Button(algo_frame, text="Beam", command=self.solve_puzzle_beam, bg="#9b59b6", activebackground="#8e44ad", **button_style).grid(row=1, column=2, padx=4, pady=4)

        # Các nút điều khiển
        tk.Button(action_frame, text="Skip Anim", command=self.skip_animation, bg="#95a5a6", activebackground="#7f8c8d", **button_style).grid(row=0, column=0, padx=4, pady=4)
        tk.Button(action_frame, text="Tải Ảnh", command=self.load_image_dialog, bg="#8e44ad", activebackground="#6c3483", **button_style).grid(row=0, column=1, padx=4, pady=4)
        tk.Button(action_frame, text="Reset", command=self.reset_puzzle, bg="#e74c3c", activebackground="#c0392b", **button_style).grid(row=1, column=0, padx=4, pady=4)
        tk.Button(action_frame, text="Random", command=self.random_puzzle, bg="#f1c40f", activebackground="#f39c12", **button_style).grid(row=1, column=1, padx=4, pady=4)

        self.result_table = ttk.Treeview(self.root, columns=("algo", "time", "nodes", "visited", "steps"), show="headings", height=6)
        self.result_table.heading("algo", text="Thuật toán")
        self.result_table.heading("time", text="Thời gian (ms)")
        self.result_table.heading("nodes", text="Trạng thái sinh ra")
        self.result_table.heading("visited", text="Trạng thái duyệt")
        self.result_table.heading("steps", text="Số bước")
        self.result_table.pack(pady=10)

        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.create_board()

        self.root.bind("<Up>", lambda e: self.move("Up"))
        self.root.bind("<Down>", lambda e: self.move("Down"))
        self.root.bind("<Left>", lambda e: self.move("Left"))
        self.root.bind("<Right>", lambda e: self.move("Right"))

    def create_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.state[i][j]
                if self.image_tiles and value != 0:
                    tile = self.image_tiles[i][j]
                    self.buttons[i][j] = tk.Button(
                        self.frame, image=tile, width=120, height=120,
                        relief="flat", bd=0
                    )
                else:
                    text = "" if value == 0 else str(value)
                    bg = "#2c3e50" if value == 0 else "#27ae60"
                    fg = "white" if value != 0 else "#2c3e50"
                    self.buttons[i][j] = tk.Button(
                        self.frame, text=text, font=("Helvetica", 24, "bold"),
                        width=6, height=2, bg=bg, fg=fg, relief="flat", bd=0
                    )
                self.buttons[i][j].grid(row=i, column=j, padx=1, pady=1)

    def update_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.state[i][j]
                if self.image_tiles and value != 0:
                    correct_r = (value - 1) // self.cols
                    correct_c = (value - 1) % self.cols
                    tile = self.image_tiles[correct_r][correct_c]
                    self.buttons[i][j].config(
                        image=tile, text="", 
                        width=120, height=120, 
                        bg="#2e4053"
                    )
                else:
                    text = "" if value == 0 else str(value)
                    bg = "#2c3e50" if value == 0 else "#27ae60"
                    fg = "white" if value != 0 else "#2c3e50"
                    if self.image_tiles and value == 0:
                        # Clear image for the blank space using an actual blank image to preserve pixel sizing!
                        self.buttons[i][j].config(image=self.blank_image, text="", bg="#1a252f", width=120, height=120)
                    elif not self.image_tiles:
                        # Text mode
                        self.buttons[i][j].config(image="", text=text, bg=bg, fg=fg, width=6, height=2, font=("Helvetica", 24, "bold"))

        self.label_steps.config(text=f"Số bước: {self.move_count}")

    def load_image_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not file_path:
            return

        try:
            img = Image.open(file_path)
            img = img.resize((self.cols * 120, self.rows * 120))
            self.image_tiles = []
            
            # Khởi tạo ảnh trống ảo để ô số 0 không bị bung form chữ
            empty_img = Image.new("RGB", (120, 120), "#1a252f")
            self.blank_image = ImageTk.PhotoImage(empty_img)
            
            for i in range(self.rows):
                row_tiles = []
                for j in range(self.cols):
                    left, top = j * 120, i * 120
                    right, bottom = (j + 1) * 120, (i + 1) * 120
                    tile = img.crop((left, top, right, bottom))
                    row_tiles.append(ImageTk.PhotoImage(tile))
                self.image_tiles.append(row_tiles)
            
            self.update_board()

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải ảnh:\n{e}")

    def log_result(self, algo_name, elapsed, nodes, visited, steps):
        try:
            self.result_table.insert("", "end", values=(algo_name, f"{elapsed:.2f}", nodes, visited, steps))
        except tk.TclError:
            pass

    def random_puzzle(self):
        self.state = self.logic.generate_default_state()
        self.initial_state = copy.deepcopy(self.state)
        self.move_count = 0
        self.update_board()

    def reset_puzzle(self):
        self.state = copy.deepcopy(self.initial_state)
        self.move_count = 0
        self.update_board()

    def animate_path(self, path, algo_name):
        self.move_count = 0
        total_steps = len(path)
        for i, step in enumerate(path):
            if self.skip_anim_flag and i < total_steps - 5:
                self.move_count += 1
                continue
                
            if self.stop_flag:
                try:
                    messagebox.showinfo("Đã dừng", f"Hoạt ảnh của {algo_name} đã bị hủy!")
                except tk.TclError:
                    pass
                break
            try:
                self.state = step
                self.move_count += 1
                self.update_board()
                self.root.update()
                self.root.after(200)
            except tk.TclError:
                self.stop_flag = True
                break
        else:
            if not self.stop_flag:
                try:
                    messagebox.showinfo("Hoàn thành", f"Đã giải bằng {algo_name} trong {self.move_count} bước!")
                except tk.TclError:
                    pass

    def move(self, direction):
        x, y = next((i,j) for i in range(self.rows) for j in range(self.cols) if self.state[i][j]==0)
        moved = False
        if direction=="Up" and x<self.rows-1: 
            self.state[x][y],self.state[x+1][y] = self.state[x+1][y],self.state[x][y]
            moved=True
        elif direction=="Down" and x>0: 
            self.state[x][y],self.state[x-1][y] = self.state[x-1][y],self.state[x][y]
            moved=True
        elif direction=="Left" and y<self.cols-1: 
            self.state[x][y],self.state[x][y+1] = self.state[x][y+1],self.state[x][y]
            moved=True
        elif direction=="Right" and y>0: 
            self.state[x][y],self.state[x][y-1] = self.state[x][y-1],self.state[x][y]
            moved=True
        if moved: 
            self.move_count+=1
            self.update_board()

    # ---- Các lệnh chạy thuật toán ----
    def skip_animation(self):
        self.skip_anim_flag = True

    def run_algorithm(self, algo_name, solve_func, **kwargs):
        self.stop_flag = False
        self.skip_anim_flag = False
        start_time = time.time()
        
        # Gọi thuật toán với self.state và self.logic.goal_state
        if kwargs:
            path = solve_func(self.state, self.logic.goal_state, **kwargs)
        else:
            path = solve_func(self.state, self.logic.goal_state)
            
        elapsed = (time.time() - start_time) * 1000
        steps = len(path) if path else 0
        
        # IDDFS trả vể path, max_limit hoặc path, used_limit
        if algo_name == "IDDFS":
            # Ta đã chỉnh lại `iddfs_solve` trong solver để trả về tuple (path, used_limit)
            if isinstance(path, tuple):
                path, used_limit = path
                algo_name = f"IDDFS (depth {used_limit})"
                steps = len(path) if path else 0

        self.log_result(algo_name, elapsed, self.solver.generated_nodes, self.solver.visited_nodes, steps)

        if path:
            self.animate_path(path, algo_name)
        else:
            if self.stop_flag:
                messagebox.showinfo("Kết quả", f"Thuật toán {algo_name} đã bị dừng!")
            else:
                messagebox.showinfo("Kết quả", f"Không tìm thấy lời giải bằng {algo_name}!")
        
        self.stop_flag = False

    def solve_puzzle_bfs(self):
        self.run_algorithm("BFS", self.solver.bfs_solve)

    def solve_puzzle_dfs(self):
        depth_limit = 300
        self.run_algorithm(f"DFS (limit={depth_limit})", self.solver.dfs_solve, limit=depth_limit)

    def solve_puzzle_iddfs(self):
        self.run_algorithm("IDDFS", self.solver.iddfs_solve, start_limit=10, max_limit=300)

    def solve_puzzle_ucs(self):
        self.run_algorithm("UCS", self.solver.ucs_solve)

    def solve_puzzle_astar(self):
        self.run_algorithm("A*", self.solver.astar_solve)

    def solve_puzzle_greedy(self):
        self.run_algorithm("Greedy", self.solver.greedy_solve)

    def solve_puzzle_beam(self):
        self.run_algorithm("Beam (k=3)", self.solver.beam_solve, beam_width=3)
