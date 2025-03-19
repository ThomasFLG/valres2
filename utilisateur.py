from app.model.database import ajouter_utilisateur, verifier_utilisateur

class Utilisateur:
    def __init__(self, id_user, nom, prenom, structure_id, structure_nom, structure_adresse, mail):
        self.id_user = id_user
        self.nom = nom
        self.prenom = prenom
        self.structure_id = structure_id
        self.structure_nom = structure_nom
        self.structure_adresse = structure_adresse
        self.mail = mail
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.structure_nom} ({self.mail})"
    
    def creer_utilisateur(nom, email, password):
        return ajouter_utilisateur(nom, email, password)

    def connexion(email, password):
        return verifier_utilisateur(email, password)
