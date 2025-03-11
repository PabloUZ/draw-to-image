import os
from tkinter import Button, Label
from PIL import Image, ImageTk
import tkinter as tk
from .config.config import params

class ImageReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Revisión de Imágenes")
        self.image_files = self.get_saved()
        self.current_index = 0

        self.image_label = Label(root)
        self.image_label.pack()
        self.question_label = Label(root, text="¿Quieres conservar esta imagen?", font=("Arial", 14))
        self.question_label.pack()
        self.btn_keep = Button(root, text="Conservar", command=lambda: self.decision(True), font=("Arial", 12), bg="green", fg="white")
        self.btn_keep.pack(side=tk.LEFT, padx=20, pady=20)
        self.btn_delete = Button(root, text="Eliminar", command=lambda: self.decision(False), font=("Arial", 12), bg="red", fg="white")
        self.btn_delete.pack(side=tk.RIGHT, padx=20, pady=20)

        self.show_image()

    def get_saved(self):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        total = [{
            "letter": l,
            "numbers": [i for i in range(1, 21) if os.path.exists(os.path.join(base_dir, "OUTPUT", params['IMAGE_PATH'],l,f"{l}{i}.{params['IMAGE_FORMAT']}"))]
        } for l in params['LETTERS']]
        total = [t for t in total if len(t["numbers"]) > 0]
        saved = []
        for t in total:
            for n in t["numbers"]:
                saved.append(os.path.join(base_dir, "OUTPUT", params['IMAGE_PATH'], t['letter'], f"{t['letter']}{n}.{params['IMAGE_FORMAT']}"))
        return saved

    def show_image(self):
        if self.current_index >= len(self.image_files):
            self.root.quit()  # Cierra la ventana cuando termine
            return

        img_path = self.image_files[self.current_index]
        img = Image.open(img_path)
        img = img.resize((500, 500))  # Ajusta el tamaño de la imagen
        img_tk = ImageTk.PhotoImage(img)

        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk  # Mantener referencia para evitar garbage collection

    def decision(self, keep: bool):
        img_path = self.image_files[self.current_index]

        if not keep:
            os.remove(img_path)

        self.current_index += 1
        self.show_image()

def verify():
    root = tk.Tk()
    app = ImageReviewApp(root)
    root.mainloop()
