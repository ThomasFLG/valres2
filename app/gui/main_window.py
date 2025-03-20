import tkinter as tk
from tkinter import filedialog, messagebox
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
        
        # Initialiser le cadre de contenu principal
        self.content_frame = tk.Frame(self.master)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Afficher la page d'accueil par défaut
        self.show_accueil()

    def create_navbar(self):
        """Crée une barre de navigation en haut de la fenêtre."""
        navbar = tk.Frame(self.master, bg="lightgray", height=50)
        navbar.pack(fill=tk.X, side=tk.TOP)

        # Bouton pour la page d'accueil
        home_button = tk.Button(navbar, text="Accueil", command=self.show_accueil)
        home_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour importation utilisateur XML
        load_button = tk.Button(navbar, text="Importer Utilisateurs", command=self.importer_utilisateurs)
        load_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour afficher les utilisateurs
        users_button = tk.Button(navbar, text="Utilisateurs", command=self.show_utilisateurs)
        users_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour se déconnecter
        logout_button = tk.Button(navbar, text="Déconnexion", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def show_accueil(self):
        """Affiche la page d'accueil."""
        # Nettoyer le contenu précédent
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Message de bienvenue
        welcome_label = tk.Label(self.content_frame, text="Bienvenue dans l'application !")
        welcome_label.pack(pady=20)

    def show_utilisateurs(self):
        """Affiche la liste des utilisateurs."""
        # Nettoyer le contenu précédent
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Créer un Listbox pour afficher les utilisateurs
        self.listbox_utilisateurs = tk.Listbox(self.content_frame, width=80, height=15)
        self.listbox_utilisateurs.pack(pady=10)

        # Récupérer et afficher les utilisateurs
        utilisateurs = recuperer_utilisateurs_db()
        for utilisateur in utilisateurs:
            self.listbox_utilisateurs.insert(tk.END, utilisateur)

    def logout(self):
        """Déconnecte l'utilisateur et retourne à la fenêtre de connexion."""
        self.master.destroy()  # Ferme la fenêtre principale
        from .login import LoginWindow  # Import circulaire géré
        login_window = tk.Tk()
        LoginWindow(login_window, on_login_success=self.master.quit)  # Revenir à la fenêtre de connexion
        login_window.mainloop()

    def importer_utilisateurs(self):
        """Importe des utilisateurs depuis un fichier XML."""
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers XML", "*.xml")])
        if fichier:
            utilisateurs = lire_utilisateurs(fichier)
            enregistrer_utilisateurs_db(utilisateurs)  # Enregistrer en base de données

            # Si la vue des utilisateurs est active, mettre à jour le Listbox
            if hasattr(self, 'listbox_utilisateurs'):
                self.listbox_utilisateurs.delete(0, tk.END)  # Effacer les anciens éléments
                for utilisateur in utilisateurs:
                    self.listbox_utilisateurs.insert(tk.END, str(utilisateur))

            messagebox.showinfo("Succès", f"{len(utilisateurs)} utilisateurs importés avec succès !")