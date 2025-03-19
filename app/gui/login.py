import tkinter as tk
from tkinter import messagebox
from app.model.utilisateur import Utilisateur

class LoginWindow:
    """Fenêtre de connexion et gestion des événements"""
    
    def __init__(self, master, on_login_success):
        self.master = master
        self.on_login_success = on_login_success
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Email:").pack()
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        tk.Label(self.master, text="Mot de passe:").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        tk.Button(self.master, text="Se connecter", command=self.login).pack()
        tk.Button(self.master, text="Créer un compte", command=self.open_registration).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if Utilisateur.connexion(email, password):
            messagebox.showinfo("Succès", "Connexion réussie !")
            self.on_login_success()
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects.")

    def open_registration(self):
        from .registration import RegistrationWindow  # Import circulaire géré
        RegistrationWindow(self.master)