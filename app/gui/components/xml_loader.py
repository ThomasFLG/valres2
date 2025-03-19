import xml.etree.ElementTree as ET
from tkinter import filedialog

def load_xml_data():
    """Charge et parse un fichier XML (composant réutilisable)"""
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers XML", "*.xml")])
    if not file_path:
        return None

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return [f"{book.find('title').text} - {book.find('author').text}" for book in root.findall('book')]
    except Exception as e:
        return [f"Erreur: {str(e)}"]