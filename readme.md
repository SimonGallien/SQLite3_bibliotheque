# 📚 Projet Bibliothèque – SQLite + Python

Ce projet est un mini système de gestion de bibliothèque, développé en Python 3.12 avec une base de données SQLite3.  
Il permet d’explorer les bases de la manipulation de données relationnelles et des requêtes SQL à travers une structure de code claire et modulaire.

---

## 🚀 Fonctionnalités

- Création automatique des tables (`Auteurs`, `Genres`, `Livres`, `Emprunteurs`, `Emprunts`)
- Insertion de données d’exemple (auteurs, livres, emprunts, etc.)
- Structure modulaire avec `database.py`, `insert_data.py`, `queries.py` et `main.py`
- Projet isolé dans un environnement virtuel Poetry + pyenv (Python 3.12)
- Requêtes SQL prêtes à l’emploi :
  - `get_livres_disponibles()` → récupère tous les livres disponibles

---

## 🛠️ Installation

### Prérequis

- Python 3.12 (géré via [pyenv](https://github.com/pyenv/pyenv))
- [Poetry](https://python-poetry.org/)

### Étapes

```bash
# 1. Installer la version Python si elle n’est pas encore disponible
pyenv install 3.12.3

# 2. (Facultatif) Vérifier que .python-version est bien pris en compte
pyenv local

# 3. Installer les dépendances avec Poetry
poetry install

# 4. Entrer dans l’environnement virtuel
poetry shell
