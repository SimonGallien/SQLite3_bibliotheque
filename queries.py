import sqlite3


def get_livres_disponibles():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    print("Connexion à la base de données réussie")

    cursor.execute(
        """
        SELECT Titre FROM Livres
        WHERE Disponible = 1
        """
    )
    livres = cursor.fetchall()

    conn.close()
    print("Livres disponibles récupérés et connexion fermée")
    return livres


def get_livres_by_date():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    print("Connexion à la base de données réussie")

    cursor.execute(
        """
        SELECT Titre, DatePublication FROM Livres
        ORDER BY DatePublication ASC
        """
    )

    livres = cursor.fetchall()
    conn.close()
    print("Livres trié par date de publication récupérés et connexion fermée.")
    return livres


def get_livres_empruntes_en_cours():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()

    print("Connexion à la database réussi.")

    cursor.execute(
        """
        SELECT Livres.Titre, Emprunts.DateRetourEffective FROM Livres
        INNER JOIN Emprunts ON Livres.LivreID = Emprunts.LivreID
        WHERE Emprunts.DateRetourEffective IS NULL
        """
    )

    livres = cursor.fetchall()
    conn.close()
    print("Livres en cours d'emprunt récupérés et connexion fermée.")
    return livres


def calcul_duree_emprunt():
    conn = sqlite3.connect("bibliotheque.db")
    cursor = conn.cursor()
    print("Connexion à la database réussi.")

    cursor.execute(
        """
        SELECT EmpruntID, LivreID, EmprunteurID, DateEmprunt, DateRetourEffective,
            JULIANDAY(DateRetourEffective) - JULIANDAY(DateEmprunt) AS DureeEmprunt
        FROM Emprunts
        WHERE DateRetourEffective IS NOT NULL
        """
    )

    emprunts = cursor.fetchall()
    conn.close()
    print("Durées d’emprunt récupérées et connexion fermée.")
    return emprunts
