from app.model.database import ajouter_utilisateur, verifier_utilisateur

class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} ({self.email})"
    
    def creer_utilisateur(nom, email, password):
        return ajouter_utilisateur(nom, email, password)

    def connexion(email, password):
        return verifier_utilisateur(email, password)
