# controller.py
from app.gui import Application  # Assure-toi d'importer Application ici
from app.logic import ajouter

class Controller:
    def __init__(self):
        # Créer une instance de l'application
        self.app = Application()
    
    def on_button_click(self):
        # Exécuter la logique de l'application (ici, addition simple)
        result = ajouter(2, 3)
        print(f"Le résultat est {result}")
    
    def run(self):
        # Lancer l'application GUI
        self.app.run()
