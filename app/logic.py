import sqlite3

DB_PATH = "data/valres.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id TEXT PRIMARY KEY,
            nom TEXT,
            prenom TEXT,
            structure_id TEXT,
            structure_nom TEXT,
            structure_adresse TEXT,
            mail TEXT
        )
    """)
    conn.commit()
    conn.close()

def enregistrer_utilisateurs_db(utilisateurs):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for utilisateur in utilisateurs:
        cursor.execute("""
            INSERT OR IGNORE INTO utilisateurs (id, nom, prenom, structure_id, structure_nom, structure_adresse, mail)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (utilisateur.id_user, utilisateur.nom, utilisateur.prenom, utilisateur.structure_id, utilisateur.structure_nom, utilisateur.structure_adresse, utilisateur.mail))
    conn.commit()
    conn.close()

def recuperer_utilisateurs_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nom, prenom, structure_nom, mail FROM utilisateurs")
    utilisateurs = cursor.fetchall()
    conn.close()
    return [f"{prenom} {nom} - {structure} ({mail})" for nom, prenom, structure, mail in utilisateurs]

# Initialisation de la base de données au démarrage
init_db()