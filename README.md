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
    - `gui.py`  # Contient la classe Application (interface graphique)
    - `logic.py`  # Contient la logique métier (fonction ajouter, etc.)
    - `controller.py`  # Contient la classe Controller
    - **model/**
      - `__init__.py`  # Fichier d'initialisation du package
      - `utilisateur.py`  # Classe Utilisateur et Structure
      - `xml_parser.py`  # Fonction de traitement des fichiers XML
  - **assets/**  # Dossier pour les ressources statiques
    - **images/**  # Contient des images pour l'UI
    - **fonts/**  # Contient des polices
    - `style.css`  # Fichier de style CSS
  - **tests/**  # Dossier pour les tests unitaires
    - `__init__.py`  # Fichier d'initialisation du package
    - `test_gui.py`  # Tests pour l'interface graphique
    - `test_logic.py`  # Tests pour les fonctions de logique métier
    - `test_utilisateur.py`  # Tests pour les classes Utilisateur et Structure
    - `test_xml_parser.py`  # Tests pour le parsing du XML
  - `main.py`  # Point d'entrée du projet
  - `utilisateurs.xml`  # Exemple de fichier XML avec les utilisateurs


### Explication :

1. **Bloc de code (` ``` `)** :
   L'arborescence est mise dans un bloc de code, entourée de triples backticks (\`\`\`). Cela crée un format monospaced et garantit que l'indentation et la structure sont respectées dans le fichier `README.md`.

2. **Indentation** :
   Markdown garde l'indentation correcte dans un bloc de code, ce qui signifie que ton projet sera toujours bien lisible.

3. **Lisibilité** :
   En utilisant des blocs de code, tu évites que le texte ne se mélange avec le reste du contenu de ton fichier `README.md`, ce qui rend l'arborescence du projet plus propre et facile à lire.

### **Autre méthode (listes imbriquées)** :
Si tu préfères utiliser des listes pour décrire chaque dossier et fichier, tu peux aussi opter pour des listes à puces imbriquées, comme suit :

```markdown

Fait par Thomas Font et Joachim Morf, étudiants en 2ème année de BTS SIO