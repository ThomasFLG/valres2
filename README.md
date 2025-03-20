# Projet Valres2

## Instructions d'exécution

1. **Installer Python** :  
   Télécharge la version Python 3.13.2 depuis [le site officiel](https://www.python.org/downloads/release/python-3132/).

2. **Exécuter le fichier `main.py`** :  
   Après avoir installé Python, exécute le fichier `main.py` pour lancer l'application.

### Structure du projet

Voici un aperçu de la structure du projet :

- **valres2/**
  - **app/**
    - `__init__.py`  # Fichier d'initialisation du package
    - **gui/**  # Dossier pour les composants de l'interface graphique
      - `__init__.py`  # Fichier d'initialisation du package GUI
      - `login.py`  # Gère la fenêtre de connexion
      - `registration.py`  # Gère la fenêtre d'inscription
      - `main_window.py`  # Gère l'application principale
      - **components/**  # Dossier pour les composants réutilisables
        - `xml_loader.py`  # Gestion du chargement de fichiers XML
    - `controller.py`  # Contient la classe Controller
    - `logic.py`  # Contient la logique métier (fonctions utilitaires)
    - **model/**  # Dossier pour les modèles de données
      - `__init__.py`  # Fichier d'initialisation du package
      - `utilisateur.py`  # Classe Utilisateur et Structure
      - `xml_parser.py`  # Fonction de traitement des fichiers XML
  - **assets/**  # Dossier pour les ressources statiques
    - **images/**  # Contient des images pour l'UI
    - **fonts/**  # Contient des polices
    - `style.css`  # Fichier de style CSS
  - **data/**  # Dossier pour les fichiers de données
    - `utilisateurs.db`  # Base de données des utilisateurs
  - **tests/**  # Dossier pour les tests unitaires
    - `__init__.py`  # Fichier d'initialisation du package
    - `test_gui.py`  # Tests pour l'interface graphique
  - `main.py`  # Point d'entrée du projet

Fait par Thomas Font et Joachim Morf, étudiants en 2ème année de BTS SIO

Lien vers la fiche d'activité
```markdown
https://docs.google.com/document/d/1brFT_2QU-twPgBw3h5RoUS3VCu_Rcw7VeMgN08du_zc/edit?usp=sharing
