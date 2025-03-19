from app.gui import LoginWindow, MainApplication
import tkinter as tk

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.show_login()

    def show_login(self):
        self.root.title("Connexion")
        LoginWindow(self.root, on_login_success=self.show_main_app)

    def show_main_app(self):
        self.root.destroy()  # Nettoie l'ancienne fenêtre
        self.root = tk.Tk()  # Recrée une nouvelle fenêtre
        self.root.title("Application principale")
        MainApplication(self.root)
        self.root.mainloop()

    def run(self):
        self.root.mainloop()