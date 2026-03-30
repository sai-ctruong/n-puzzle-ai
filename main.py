import tkinter as tk
from tkinter import messagebox
from puzzle_gui import PuzzleGUI

def start_game(entry_rows, entry_cols, root):
    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        if rows < 2 or cols < 2:
            messagebox.showwarning("Lỗi", "Kích thước phải lớn hơn hoặc bằng 2x2")
            return
    except ValueError:
        messagebox.showwarning("Lỗi", "Vui lòng nhập số nguyên hợp lệ")
        return

    root.destroy()
    new_root = tk.Tk()
    PuzzleGUI(new_root, rows, cols)
    new_root.mainloop()

def on_enter(e):
    e.widget['background'] = '#2980b9'

def on_leave(e):
    e.widget['background'] = '#3498db'

def main():
    root = tk.Tk()
    root.title("N-Puzzle Setup")
    root.geometry("400x380")
    root.configure(bg="#0f172a")  # Dark modern slate
    root.resizable(False, False)
    
    # Center Window
    window_w, window_h = 400, 380
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x_c = int((screen_w/2) - (window_w/2))
    y_c = int((screen_h/2) - (window_h/2))
    root.geometry(f"{window_w}x{window_h}+{x_c}+{y_c}")

    # Header
    header = tk.Label(root, text="N-PUZZLE AI", font=("Helvetica", 24, "bold"), fg="#e2e8f0", bg="#0f172a")
    header.pack(pady=(30, 5))
    
    subtitle = tk.Label(root, text="Thiết lập kích thước bàn cờ", font=("Helvetica", 11), fg="#94a3b8", bg="#0f172a")
    subtitle.pack(pady=(0, 20))

    # Form Container
    frame_input = tk.Frame(root, bg="#1e293b", padx=30, pady=25, relief="flat", bd=0)
    frame_input.pack()

    # Layout for inputs
    tk.Label(frame_input, text="Số hàng", font=("Helvetica", 12, "bold"), fg="#cbd5e1", bg="#1e293b").grid(row=0, column=0, sticky="w", pady=10, padx=(0, 20))
    entry_rows = tk.Entry(frame_input, font=("Helvetica", 14), width=8, justify="center", bg="#334155", fg="white", relief="flat", insertbackground="white")
    entry_rows.grid(row=0, column=1, pady=10, ipady=5)
    entry_rows.insert(0, "3")

    tk.Label(frame_input, text="Số cột", font=("Helvetica", 12, "bold"), fg="#cbd5e1", bg="#1e293b").grid(row=1, column=0, sticky="w", pady=10, padx=(0, 20))
    entry_cols = tk.Entry(frame_input, font=("Helvetica", 14), width=8, justify="center", bg="#334155", fg="white", relief="flat", insertbackground="white")
    entry_cols.grid(row=1, column=1, pady=10, ipady=5)
    entry_cols.insert(0, "3")

    # Start Button Area
    btn_frame = tk.Frame(root, bg="#0f172a")
    btn_frame.pack(pady=25)

    start_btn = tk.Button(btn_frame, text="BẮT ĐẦU TRÒ CHƠI", command=lambda: start_game(entry_rows, entry_cols, root),
                          font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
                          activebackground="#2980b9", activeforeground="white",
                          relief="flat", cursor="hand2", padx=30, pady=10)
    start_btn.pack()
    
    # Hover effect mapping
    start_btn.bind("<Enter>", on_enter)
    start_btn.bind("<Leave>", on_leave)

    root.mainloop()

if __name__ == "__main__":
    main()
