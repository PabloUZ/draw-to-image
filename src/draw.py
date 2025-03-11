import os
import tkinter as tk
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root, letter, number):
        self.letter = letter
        self.number = number
        self.end = False
        self.root = root
        self.root.title(f"Draw the letter {self.letter}, press 's' to save and 'q' to quit")

        self.canvas = tk.Canvas(root, bg="white", width=150, height=150)
        self.canvas.pack()

        self.image = Image.new("RGB", (150, 150), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.root.bind("s", self.save_image)
        self.root.bind("q", self.quit)

    def paint(self, event):
        x1, y1 = event.x - 2, event.y - 2
        x2, y2 = event.x + 2, event.y + 2
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")
        self.draw.ellipse([x1, y1, x2, y2], fill="black", outline="black")

    def save_image(self, event):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        save_dir = os.path.join(base_dir, "vowels", self.letter)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        self.image.save(os.path.join(save_dir, f"{self.letter}{self.number}.png"))
        print(f"Imagen guardada como {self.letter}{self.number}.png")
        self.root.destroy()

    def quit(self, event):
        self.root.destroy()
        self.end = True

def open_new_window(number, letter):
    new_root = tk.Tk()
    app = DrawingApp(new_root, letter, number)
    new_root.mainloop()
    return app.end