import tkinter as tk
import time
import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing fast is a useful skill for coders.",
    "Always aim for accuracy before speed."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Calculator")
        self.root.geometry("600x300")

        self.sample_text = random.choice(TEXTS)
        self.start_time = None

        self.label = tk.Label(root, text="Typing Speed Test", font=("Arial", 16))
        self.label.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, wraplength=500, font=("Arial", 12))
        self.text_display.pack(pady=10)

        self.entry = tk.Text(root, height=4, width=70)
        self.entry.pack()
        self.entry.bind("<FocusIn>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.button = tk.Button(root, text="Submit", command=self.check_speed)
        self.button.pack(pady=5)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def check_speed(self):
        typed_text = self.entry.get("1.0", tk.END).strip()
        end_time = time.time()
        time_taken = end_time - self.start_time

        words = typed_text.split()
        word_count = len(words)
        wpm = word_count / (time_taken / 60)

        correct_chars = 0
        for i, c in enumerate(typed_text):
            if i < len(self.sample_text) and c == self.sample_text[i]:
                correct_chars += 1
        accuracy = (correct_chars / len(self.sample_text)) * 100

        self.result_label.config(
            text=f"Time Taken: {time_taken:.2f} seconds\nSpeed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )

        self.start_time = None
        self.button.config(state=tk.DISABLED)

root = tk.Tk()
app = TypingSpeedApp(root)
root.mainloop()
