import tkinter as tk
from tkinter import filedialog, messagebox
from .components.xml_loader import load_xml_data
from . import set_window_size
from app.model.xml_parser import lire_utilisateurs
from app.logic import enregistrer_utilisateurs_db, recuperer_utilisateurs_db

class MainApplication:
    def __init__(self, master):
        self.master = master
        set_window_size(self.master)
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

        home_button = tk.Button(navbar, text="Accueil", command=self.show_home_page)
        home_button.pack(side=tk.LEFT, padx=10, pady=5)

        xml_button = tk.Button(navbar, text="Charger XML", command=self.show_xml_page)
        xml_button.pack(side=tk.LEFT, padx=10, pady=5)

        users_button = tk.Button(navbar, text="Utilisateurs", command=self.show_users_page)
        users_button.pack(side=tk.LEFT, padx=10, pady=5)

        logout_button = tk.Button(navbar, text="Déconnexion", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def create_pages(self):
        """Crée les différentes pages de l'application."""
        self.pages = {}

        # Page d'accueil
        self.pages["home"] = tk.Frame(self.master)
        tk.Label(self.pages["home"], text="Bienvenue dans l'application !").pack(pady=20)

        # Page pour charger XML
        self.pages["xml"] = tk.Frame(self.master)
        tk.Button(self.pages["xml"], text="Importer un fichier XML", command=self.importer_utilisateurs).pack(pady=10)
        self.xml_content = tk.Label(self.pages["xml"], text="")
        self.xml_content.pack(pady=10)

        # Page des utilisateurs
        self.pages["users"] = tk.Frame(self.master)
        self.listbox_utilisateurs = tk.Listbox(self.pages["users"], width=80, height=15)
        self.listbox_utilisateurs.pack(pady=10)
        tk.Button(self.pages["users"], text="Rafraîchir", command=self.utilisateurs).pack()

    def show_home_page(self):
        """Affiche la page d'accueil."""
        self.hide_all_pages()
        self.pages["home"].pack(fill=tk.BOTH, expand=True)

    def show_xml_page(self):
        """Affiche la page XML."""
        self.hide_all_pages()
        self.pages["xml"].pack(fill=tk.BOTH, expand=True)

    def show_users_page(self):
        """Affiche la page des utilisateurs."""
        self.hide_all_pages()
        self.pages["users"].pack(fill=tk.BOTH, expand=True)
        self.utilisateurs()  # Rafraîchir automatiquement

    def hide_all_pages(self):
        """Cache toutes les pages."""
        for page in self.pages.values():
            page.pack_forget()

    def importer_utilisateurs(self):
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers XML", "*.xml")])
        if fichier:
            utilisateurs = lire_utilisateurs(fichier)
            enregistrer_utilisateurs_db(utilisateurs)
            self.xml_content.config(text=f"{len(utilisateurs)} utilisateurs importés avec succès !")
            self.utilisateurs()  # Rafraîchir la liste

    def utilisateurs(self):
        utilisateurs = recuperer_utilisateurs_db()
        self.listbox_utilisateurs.delete(0, tk.END)
        for user in utilisateurs:
            self.listbox_utilisateurs.insert(tk.END, f"{user.nom} - {user.email}")
        messagebox.showinfo("Succès", f"{len(utilisateurs)} utilisateurs chargés !")

    def logout(self):
        self.master.destroy()
        from .login import LoginWindow
        login_window = tk.Tk()
        LoginWindow(login_window, on_login_success=self.master.quit)
        login_window.mainloop()