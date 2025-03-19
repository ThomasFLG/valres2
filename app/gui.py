import tkinter as tk
from tkinter import filedialog,messagebox
import xml.etree.ElementTree as ET
from app.model.utilisateur import Utilisateur

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connexion")
        self.window.geometry("500x350")  # Taille initiale (ajuste cette valeur)
        self.window.minsize(500, 350)    # Taille minimale
        self.window.maxsize(800, 600)    # Taille maximale
        self.create_login_widgets()
    
    def create_login_widgets(self):
        """Crée l'interface de connexion."""
        tk.Label(self.window, text="Email:").pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()

        tk.Label(self.window, text="Mot de passe:").pack()
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.window, text="Se connecter", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self.window, text="Créer un compte", command=self.register)
        self.register_button.pack()

    def login(self):
        """Vérifie les identifiants et ouvre l'application si connexion réussie."""
        email = self.email_entry.get()
        password = self.password_entry.get()

        if Utilisateur.connexion(email, password):
            messagebox.showinfo("Succès", "Connexion réussie !")
            self.open_main_application()
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects.")

    def register(self):
        """Affiche la fenêtre de création de compte."""
        register_window = tk.Toplevel(self.window)
        register_window.title("Créer un compte")

        tk.Label(register_window, text="Nom:").pack()
        nom_entry = tk.Entry(register_window)
        nom_entry.pack()

        tk.Label(register_window, text="Email:").pack()
        email_entry = tk.Entry(register_window)
        email_entry.pack()

        tk.Label(register_window, text="Mot de passe:").pack()
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack()

        def create_account():
            """Crée un nouvel utilisateur."""
            nom = nom_entry.get()
            email = email_entry.get()
            password = password_entry.get()

            if Utilisateur.creer_utilisateur(nom, email, password):
                messagebox.showinfo("Succès", "Compte créé avec succès !")
                register_window.destroy()
            else:
                messagebox.showerror("Erreur", "Cet email est déjà utilisé.")

        tk.Button(register_window, text="S'inscrire", command=create_account).pack()

    def open_main_application(self):
        """Ouvre l'interface principale après connexion réussie."""
        self.window.destroy()  # Ferme la fenêtre de connexion
        main_window = tk.Tk()
        main_window.title("Application principale")
        tk.Label(main_window, text="Bienvenue !").pack()
        main_window.mainloop()

    
    def create_widgets(self):
        # Label d'accueil
        self.label = tk.Label(self.window, text="Bonjour!")
        self.label.pack()
        
        # Bouton pour charger un fichier XML
        self.load_button = tk.Button(self.window, text="Charger un fichier XML", command=self.load_xml)
        self.load_button.pack()
        
        # Zone pour afficher les résultats
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
    
    def load_xml(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier XML
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers XML", "*.xml")])
        
        if file_path:
            # Lire et traiter le fichier XML
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Extraction des données du XML (par exemple, ici nous prenons les livres)
                books_info = []
                for book in root.findall('book'):
                    title = book.find('title').text
                    author = book.find('author').text
                    price = book.find('price').text
                    books_info.append(f"{title} by {author}, Price: {price}")
                
                # Afficher les résultats extraits du fichier XML dans l'interface
                self.result_label.config(text="\n".join(books_info))
            except Exception as e:
                self.result_label.config(text=f"Erreur lors de la lecture du fichier XML : {e}")
    
    def run(self):
        self.window.mainloop()