import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from app.logic import ajouter

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mon Application")
        self.create_widgets()
    
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