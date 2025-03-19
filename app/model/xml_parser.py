import xml.etree.ElementTree as ET
from app.model.utilisateur import Utilisateur

def lire_utilisateurs(fichier_xml):
    utilisateurs = []
    tree = ET.parse(fichier_xml)
    root = tree.getroot()
    
    for user in root.findall("utilisateur"):
        id_user = user.get("id")
        nom = user.find("nom").text
        prenom = user.find("prenom").text
        structure_id = user.find("structure_id").text
        structure_nom = user.find("structure_nom").text
        structure_adresse = user.find("structure_adresse").text
        mail = user.find("mail").text
        
        utilisateur = Utilisateur(id_user, nom, prenom, structure_id, structure_nom, structure_adresse, mail)
        utilisateurs.append(utilisateur)
    
    return utilisateurs