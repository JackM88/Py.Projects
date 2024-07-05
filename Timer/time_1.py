import tkinter as tk
from tkinter import messagebox
import time
# from playsound import playsound

work_interval = 25 * 60
short_interval = 5 * 60
long_interval = 15 * 60
cycles = 4

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        self.timer_label = tk.Label(root, text='Timer', font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text='Start', command=self.start_timer)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=10)

        self.reset_button = tk.Button(root, text='Reset', command=self.reset_timer)
        self.reset_button.pack(pady=10)

        self.time_left = work_interval
        self.running = False
        self.cycles_completed = 0

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.time_left = work_interval
        self.timer_label.config(text=self.format_time(self.time_left))

    def pause_timer(self):
        if self.running:
            self.running = False
            self.paused = True

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                self.time_left -= 1
                self.timer_label.config(text=self.format_time(self.time_left))
                self.root.after(1000, self.update_timer)
            else:
                self.cycles_completed += 1
                if self.cycles_completed % cycles == 0:
                    self.time_left = long_interval
                    messagebox.showinfo("Break", "Time for a 15 min break!")
                else:
                    self.time_left = short_interval
                    messagebox.showinfo("Break", "Time for a short break")
                self.running = False
                # playsound("boop.wav")

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()