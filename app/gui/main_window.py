import tkinter as tk
from tkinter import filedialog,messagebox
from .components.xml_loader import load_xml_data
from . import set_window_size  # Importer la fonction utilitaire
from app.model.xml_parser import lire_utilisateurs
from app.logic import enregistrer_utilisateurs_db, recuperer_utilisateurs_db

class MainApplication:
    def __init__(self, master):
        self.master = master
        set_window_size(self.master)  # Appliquer la taille de la fenêtre
        self.master.title("Application principale")
        
        # Créer la navbar
        self.create_navbar()
        
        # Créer le contenu principal
        self.create_widgets()

    def create_navbar(self):
        """Crée une barre de navigation en haut de la fenêtre."""
        navbar = tk.Frame(self.master, bg="lightgray", height=50)
        navbar.pack(fill=tk.X, side=tk.TOP)

        # Bouton pour importation utilisateur XML
        load_button = tk.Button(navbar, text="Importer Utilisateurs", command=self.importer_utilisateurs)
        load_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour afficher les utilisateurs (exemple)
        users_button = tk.Button(navbar, text="Utilisateurs", command=self.utilisateurs)
        users_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour se déconnecter
        logout_button = tk.Button(navbar, text="Déconnexion", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def create_widgets(self):
        """Crée le contenu principal de la fenêtre."""
        self.content_frame = tk.Frame(self.master)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Message de bienvenue
        welcome_label = tk.Label(self.content_frame, text="Bienvenue dans l'application !")
        welcome_label.pack(pady=20)

        self.listbox_utilisateurs = tk.Listbox( width=80, height=15)
        self.listbox_utilisateurs.pack(pady=10)

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la fenêtre de connexion."""
        self.master.destroy()  # Ferme la fenêtre principale
        from .login import LoginWindow  # Import circulaire géré
        login_window = tk.Tk()
        LoginWindow(login_window, on_login_success=self.master.quit)  # Revenir à la fenêtre de connexion
        login_window.mainloop()

    def importer_utilisateurs(self):
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers XML", "*.xml")])
        if fichier:
            utilisateurs = lire_utilisateurs(fichier)
            enregistrer_utilisateurs_db(utilisateurs)  # Enregistrer en base de données
            self.listbox_utilisateurs.delete(0, tk.END)  # Effacer les anciens éléments
            for utilisateur in utilisateurs:
                self.listbox_utilisateurs.insert(tk.END, str(utilisateur))
            messagebox.showinfo("Succès", f"{len(utilisateurs)} utilisateurs importés avec succès !")

    def utilisateurs(self):
        utilisateurs = recuperer_utilisateurs_db()
        self.listbox_utilisateurs.delete(0, tk.END)  # Effacer les anciens éléments
        for utilisateur in utilisateurs:
            self.listbox_utilisateurs.insert(tk.END, utilisateur)
        messagebox.showinfo("Succès", f"{len(utilisateurs)} utilisateurs chargés depuis la base de données !")
