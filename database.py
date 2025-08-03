import sqlite3


def create_tables():

    # Créer une connexion à la base de données
    conn = sqlite3.connect("bibliotheque.db")

    # Créer un curseur pour exécuter les requêtes SQL
    cursor = conn.cursor()

    print("Connexion à la base de données réussie")

    # Création des tables
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Auteurs (
            AuteurID INTEGER PRIMARY KEY,
            Nom TEXT,
            Prénom TEXT,
            Pays TEXT
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Genres (
            GenreID INTEGER PRIMARY KEY,
            NomGenre TEXT
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Livres (
            LivreID INTEGER PRIMARY KEY,
            Titre TEXT,
            AuteurID INTEGER,
            GenreID INTEGER,
            DatePublication DATE,
            Disponible BOOLEAN,
            FOREIGN KEY (AuteurID) REFERENCES Auteurs(AuteurID),
            FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Emprunteurs (
            EmprunteurID INTEGER PRIMARY KEY,
            Nom TEXT,
            Prénom TEXT,
            Email TEXT,
            Téléphone TEXT  
        );
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Emprunts (
            EmpruntID INTEGER PRIMARY KEY,
            LivreID INTEGER,
            EmprunteurID INTEGER,
            DateEmprunt DATE,
            DateRetourPrévue DATE,
            DateRetourEffective DATE,
            FOREIGN KEY (LivreID) REFERENCES Livres(LivreID),
            FOREIGN KEY (EmprunteurID) REFERENCES Emprunteurs(EmprunteurID)
        );
        """
    )
    # Valider les modifications
    conn.commit()
    print("Tables créées avec succès")

    conn.close()
    print("Connexion à la base de données fermée")
