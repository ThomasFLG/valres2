import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from .components.xml_loader import load_xml_data  # Composant réutilisable
from . import set_window_size

class MainApplication:
    """Interface principale après connexion"""
    
    def __init__(self, master):
        self.master = master
        set_window_size(self.master)
        self.master.title("Application principale")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Bienvenue !").pack()
        tk.Button(self.master, text="Charger XML", command=self.load_xml).pack()
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def load_xml(self):
        data = load_xml_data()
        if data:
            self.result_label.config(text="\n".join(data))