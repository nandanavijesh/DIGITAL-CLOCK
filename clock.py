import tkinter as tk
from time import strftime

class ModernClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Modern Clock")
        self.configure(bg='#1E1E2E')  
        self.attributes('-topmost', True)
        self.overrideredirect(True)   
        self.x = None
        self.y = None
        w, h = 500, 220
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        x = (screen_w // 2) - (w // 2)
        y = (screen_h // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.setup_ui()
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)
        self.bind("<Escape>", lambda e: self.destroy())
        self.update_clock()

    def setup_ui(self):
        close_btn = tk.Button(self, text="×", font=('Arial', 16),
                              bg='#1E1E2E', fg='#FF5555', bd=0,
                              activebackground='#1E1E2E', activeforeground='#FF0000',
                              command=self.destroy, cursor="hand2")
        close_btn.place(relx=0.95, rely=0.05, anchor='ne')

        self.time_label = tk.Label(self, font=('JetBrains Mono', 50, 'bold'),
                                   bg='#1E1E2E', fg='#89DCEB')
        self.time_label.pack(pady=(30, 0))

        self.date_label = tk.Label(self, font=('JetBrains Mono', 14),
                                   bg='#1E1E2E', fg='#CBA6F7')
        self.date_label.pack(pady=(0, 10))

        self.msg_label = tk.Label(self, font=('Verdana', 10, 'italic'),
                                  bg='#1E1E2E', fg='#A6ADC8')
        self.msg_label.pack(pady=(0, 20))

    def update_clock(self):
        try:
            self.time_label.config(text=strftime('%I:%M:%S %p'))
            self.date_label.config(text=strftime('%A, %B %d, %Y'))
            
            hour = int(strftime('%H'))
            if 5 <= hour < 12: greeting = "Good Morning! 🌅"
            elif 12 <= hour < 18: greeting = "Good Afternoon! ☕"
            elif 18 <= hour < 22: greeting = "Good Evening! 🌙"
            else: greeting = "Good Night! 💤"
            
            self.msg_label.config(text=greeting)
            self.after(1000, self.update_clock)
        except tk.TclError:
            pass 

    def start_move(self, event): self.x, self.y = event.x, event.y
    def stop_move(self, event): self.x, self.y = None, None
    def do_move(self, event):
        if self.x is None or self.y is None:
            return
        x = self.winfo_x() + (event.x - self.x)
        y = self.winfo_y() + (event.y - self.y)
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    app = ModernClock()
    app.mainloop()