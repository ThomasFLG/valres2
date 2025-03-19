import sqlite3
import re

DB_PATH = "data/utilisateurs.db"

def init_db():
    """Crée la table des utilisateurs si elle n'existe pas."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def ajouter_utilisateur(nom, email, password):
    """Ajoute un utilisateur à la base de données."""
    if not valider_email(email):
        return False  # L'email n'est pas valide
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO utilisateurs (nom, email, password) VALUES (?, ?, ?)", (nom, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # L'email existe déjà
    finally:
        conn.close()

def verifier_utilisateur(email, password):
    """Vérifie si l'utilisateur existe et que le mot de passe est correct."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def valider_email(email):
    """Valide l'adresse email à l'aide d'une expression régulière."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
