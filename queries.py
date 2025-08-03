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
