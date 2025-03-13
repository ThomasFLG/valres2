projet/
│
├── app/
│   ├── __init__.py                # Fichier d'initialisation du package
│   ├── gui.py                     # Contient la classe Application (interface graphique)
│   ├── logic.py                   # Contient la logique métier (fonction ajouter, etc.)
│   ├── controller.py              # Contient la classe Controller
│   └── model/                     # Dossier pour les classes de données (POO)
│       ├── __init__.py            # Fichier d'initialisation du package
│       ├── utilisateur.py         # Classe Utilisateur et Structure
│       └── xml_parser.py          # Fonction de traitement des fichiers XML
│
├── assets/                        # Dossier pour les ressources statiques (si nécessaire)
│   ├── images/                    # Contient des images pour l'UI (si nécessaire)
│   ├── fonts/                     # Contient des polices (si nécessaire)
│   └── style.css                  # Fichier de style CSS (si nécessaire)
│
├── tests/                         # Dossier pour les tests unitaires
│   ├── __init__.py                # Fichier d'initialisation du package
│   ├── test_gui.py                # Tests pour l'interface graphique
│   ├── test_logic.py              # Tests pour les fonctions de logique métier
│   ├── test_utilisateur.py        # Tests pour les classes Utilisateur et Structure
│   └── test_xml_parser.py         # Tests pour le parsing du XML
│
├── main.py                        # Point d'entrée du projet
└── utilisateurs.xml               # Exemple de fichier XML avec les utilisateurs
