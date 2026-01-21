import tkinter as tk
from tkinter import messagebox
from gui.dashboard import Dashboard
from PIL import Image, ImageTk
import os


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("ALPR Login")
        self.root.geometry("800x450")
        self.root.resizable(False, False)

        # BACKGROUND IMAGE
        base_dir = os.path.dirname(os.path.dirname(__file__))
        img_path = os.path.join(base_dir, "assets", "bg_login.jpg")

        if not os.path.exists(img_path):
            messagebox.showerror("Error", "Login background image not found")
            return

        # LOAD & KEEP IMAGE REFERENCE
        bg = Image.open(img_path)
        bg = bg.resize((800, 450))
        self.bg_img = ImageTk.PhotoImage(bg)

        # CANVAS
        canvas = tk.Canvas(root, width=800, height=450)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        # TITLE
        canvas.create_text(
            400, 80,
            text="ALPR SYSTEM LOGIN",
            font=("Arial", 24, "bold"),
            fill="white"
        )

        # INPUT FIELDS 
        self.username = tk.Entry(root, font=("Arial", 14))
        self.password = tk.Entry(root, font=("Arial", 14), show="*")

        canvas.create_window(400, 200, window=self.username, width=250)
        canvas.create_window(400, 250, window=self.password, width=250)

        # LOGIN BUTTON
        login_btn = tk.Button(
            root,
            text="Login",
            width=15,
            font=("Arial", 12),
            command=self.login
        )
        canvas.create_window(400, 320, window=login_btn)

    # LOGIN LOGIC 
    def login(self):
        USERNAME = "vedang"
        PASSWORD = "123456789"

        if self.username.get() == USERNAME and self.password.get() == PASSWORD:
            self.root.destroy()
            new_root = tk.Tk()
            Dashboard(new_root)
            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
