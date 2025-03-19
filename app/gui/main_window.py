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

        # Créer les pages
        self.create_pages()
        
        # Afficher la page d'accueil par défaut
        self.show_home_page()

    def create_navbar(self):
        """Crée une barre de navigation en haut de la fenêtre."""
        navbar = tk.Frame(self.master, bg="lightgray", height=50)
        navbar.pack(fill=tk.X, side=tk.TOP)

        # Bouton pour la page d'accueil
        home_button = tk.Button(navbar, text="Accueil", command=self.show_home_page)
        home_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour charger un fichier XML
        xml_button = tk.Button(navbar, text="Charger XML", command=self.show_xml_page)
        xml_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour afficher les utilisateurs
        users_button = tk.Button(navbar, text="Utilisateurs", command=self.show_users_page)
        users_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour se déconnecter
        logout_button = tk.Button(navbar, text="Déconnexion", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def create_pages(self):
        """Crée les différentes pages de l'application."""
        self.pages = {}

        # Page d'accueil
        self.pages["home"] = tk.Frame(self.master)
        tk.Label(self.pages["home"], text="Bienvenue dans l'application !").pack(pady=20)

        # Page pour charger un fichier XML
        self.pages["xml"] = tk.Frame(self.master)
        self.xml_content = tk.Label(self.pages["xml"], text="")
        self.xml_content.pack(pady=20)
        tk.Button(self.pages["xml"], text="Charger un fichier XML", command=self.load_xml).pack()

        # Page pour afficher les utilisateurs
        self.pages["users"] = tk.Frame(self.master)
        self.users_content = tk.Label(self.pages["users"], text="")
        self.users_content.pack(pady=20)
        self.refresh_users_list()  # Rafraîchir la liste des utilisateurs

    def show_home_page(self):
        """Affiche la page d'accueil."""
        self.hide_all_pages()
        self.pages["home"].pack(fill=tk.BOTH, expand=True)

    def show_xml_page(self):
        """Affiche la page pour charger un fichier XML."""
        self.hide_all_pages()
        self.pages["xml"].pack(fill=tk.BOTH, expand=True)

    def show_users_page(self):
        """Affiche la page des utilisateurs."""
        self.hide_all_pages()
        self.pages["users"].pack(fill=tk.BOTH, expand=True)
        self.refresh_users_list()  # Rafraîchir la liste des utilisateurs

    def hide_all_pages(self):
        """Cache toutes les pages."""
        for page in self.pages.values():
            page.pack_forget()

    def load_xml(self):
        """Charge un fichier XML et affiche les résultats."""
        data = load_xml_data()
        if data:
            self.xml_content.config(text="\n".join(data))
        else:
            self.xml_content.config(text="Aucun fichier sélectionné ou erreur de chargement.")

    def refresh_users_list(self):
        """Rafraîchit la liste des utilisateurs."""
        # Exemple : Récupérer la liste des utilisateurs depuis la base de données
        users = ["Utilisateur 1", "Utilisateur 2", "Utilisateur 3"]  # Remplacez par une vraie requête
        self.users_content.config(text="Liste des utilisateurs :\n" + "\n".join(users))

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la fenêtre de connexion."""
        self.master.destroy()  # Ferme la fenêtre principale
        from .login import LoginWindow  # Import circulaire géré
        login_window = tk.Tk()
        LoginWindow(login_window, on_login_success=self.master.quit)  # Revenir à la fenêtre de connexion
        login_window.mainloop()