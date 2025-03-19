from app.gui import Application
from app.model.database import init_db

class Controller:
    def __init__(self):
        init_db()  # Initialiser la base de données
        self.app = Application()

    def run(self):
        self.app.run()
