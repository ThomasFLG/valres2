import tkinter as tk
from tkinter import messagebox
from app.model.utilisateur import Utilisateur

class RegistrationWindow(tk.Toplevel):
    """Fenêtre d'inscription"""
    
    def __init__(self, master):
        super().__init__(master)
        self.title("Créer un compte")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nom:").pack()
        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack()

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Mot de passe:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="S'inscrire", command=self.create_account).pack()

    def create_account(self):
        nom = self.nom_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if Utilisateur.creer_utilisateur(nom, email, password):
            messagebox.showinfo("Succès", "Compte créé avec succès !")
            self.destroy()
        else:
            messagebox.showerror("Erreur", "Cet email est déjà utilisé.")