import tkinter as tk
from tkinter import filedialog
from .components.xml_loader import load_xml_data
from . import set_window_size  # Importer la fonction utilitaire

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

        # Bouton pour charger un fichier XML
        load_button = tk.Button(navbar, text="Charger XML", command=self.load_xml)
        load_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour afficher les utilisateurs (exemple)
        users_button = tk.Button(navbar, text="Utilisateurs", command=self.show_users)
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

    def load_xml(self):
        """Charge un fichier XML et affiche les résultats."""
        data = load_xml_data()
        if data:
            # Afficher les résultats dans le contenu principal
            for widget in self.content_frame.winfo_children():
                widget.destroy()  # Nettoyer le contenu précédent
            result_label = tk.Label(self.content_frame, text="\n".join(data))
            result_label.pack()

    def show_users(self):
        """Affiche la liste des utilisateurs (exemple)."""
        # Nettoyer le contenu précédent
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Exemple : Afficher une liste d'utilisateurs
        users_label = tk.Label(self.content_frame, text="Liste des utilisateurs :\n- Utilisateur 1\n- Utilisateur 2")
        users_label.pack(pady=20)

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la fenêtre de connexion."""
        self.master.destroy()  # Ferme la fenêtre principale
        from .login import LoginWindow  # Import circulaire géré
        login_window = tk.Tk()
        LoginWindow(login_window, on_login_success=self.master.quit)  # Revenir à la fenêtre de connexion
        login_window.mainloop()