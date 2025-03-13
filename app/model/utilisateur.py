class Utilisateur:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.nom} ({self.email})"
