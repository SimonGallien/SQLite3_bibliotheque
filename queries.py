import sqlite3

DATABASE = "bibliotheque.db"


def connexion_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    print("Connexion à la base de données réussie")
    return conn, cursor


def get_livres_disponibles():
    conn, cursor = connexion_database()
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
    conn, cursor = connexion_database()
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
    conn, cursor = connexion_database()
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
    conn, cursor = connexion_database()
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


def get_livres_auteurs():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT Livres.Titre, Auteurs.Nom, Auteurs.Prénom FROM Livres
        LEFT JOIN Auteurs ON Livres.AuteurID = Auteurs.AuteurID
        """
    )
    livres = cursor.fetchall()
    conn.close()
    print(f"Livres et leurs auteurs récupérés et connexion fermée.")
    return livres


def get_emprunteurs_livres_non_rendus():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT DISTINCT Emprunteurs.Nom, Emprunteurs.Prénom, Emprunteurs.Email FROM Emprunteurs
        JOIN Emprunts ON Emprunteurs.EmprunteurID = Emprunts.EmprunteurID
        WHERE Emprunts.DateRetourEffective IS NULL
        """
    )
    emprunteurs = cursor.fetchall()
    conn.close()
    print("Emprunteurs avec livres non rendus récupérés et connexion fermée.")
    return emprunteurs


def get_nbr_livres_par_genre():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT Genres.NomGenre, COUNT(Livres.LivreID) as NombreLivres
        FROM Genres
        LEFT JOIN Livres ON Genres.GenreID = Livres.GenreID
        GROUP BY Genres.GenreID
        ORDER BY NombreLivres DESC
        """
    )
    livres = cursor.fetchall()
    conn.close()
    print("Nombre de livres par Genre récupéré et connexion fermée.")
    return livres


def get_duree_moy_emprunt():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT 
            Emprunteurs.Nom, 
            Emprunteurs.Prénom, 
            AVG(JULIANDAY(Emprunts.DateRetourEffective)-JULIANDAY(Emprunts.DateEmprunt)) AS DureeMoyenne
        FROM Emprunteurs
        LEFT JOIN Emprunts ON Emprunteurs.EmprunteurID = Emprunts.EmprunteurID
        GROUP BY Emprunteurs.EmprunteurID
        """
    )
    dureeMoyenne = cursor.fetchall()
    conn.close
    print(
        "Durée moyenne d'emprunt par emprunteurs récupérée et connexion fermée."
    )
    return dureeMoyenne


def get_emprunteurs_livres_et_genres():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT 
            Emprunteurs.Nom, 
            Emprunteurs.Prénom, 
            Livres.Titre, 
            Genres.NomGenre
            FROM Emprunteurs 
            LEFT JOIN Emprunts ON Emprunteurs.EmprunteurID = Emprunts.EmprunteurID
            LEFT JOIN Livres ON Livres.LivreID = Emprunts.LivreID
            LEFT JOIN Genres ON Genres.GenreID = Livres.GenreID
        """
    )
    resultat = cursor.fetchall()
    conn.close()
    print("Données emprunteurs/livres/genres récupérées avec succès.")
    return resultat


def get_top3_livre():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT 
            Livres.Titre, 
            COUNT(Emprunts.LivreID) AS nbrEmprunt 
            FROM Livres
        INNER JOIN Emprunts ON Emprunts.LivreID = Livres.LivreID
        GROUP BY Emprunts.LivreID
        ORDER BY nbrEmprunt DESC
        LIMIT 3
        """
    )
    resultat = cursor.fetchall()
    conn.close()
    print("Top 3 des livres les plus empruntés récupéré et connexion fermée.")
    return resultat


def get_nombre_emprunts_par_emprunteur():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT Emprunteurs.Prénom, Emprunteurs.Nom, 
            COUNT(Emprunts.EmprunteurID) AS nbrEmprunt
            FROM Emprunteurs
        LEFT JOIN Emprunts ON Emprunts.EmprunteurID = Emprunteurs.EmprunteurID
        GROUP BY Emprunteurs.EmprunteurID
        ORDER BY nbrEmprunt DESC
        """
    )
    resultat = cursor.fetchall()
    conn.close()
    print(
        "Nombre total de livres empruntés par chaque emprunteur récupéré et connexion fermée."
    )
    return resultat


def get_livres_jamais_empruntes():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT Livres.Titre
        FROM Livres
        LEFT JOIN Emprunts ON Emprunts.LivreID = Livres.LivreID
        WHERE Emprunts.LivreID IS NULL
        """
    )
    resultat = cursor.fetchall()
    conn.close()
    print("Livres jamais empruntés récupérés et connexion fermée.")
    return resultat


def get_nbr_emprunteurs_par_auteur():
    conn, cursor = connexion_database()
    cursor.execute(
        """
        SELECT 
            Auteurs.Prénom, 
            Auteurs.Nom, 
            COUNT(DISTINCT Emprunts.EmprunteurID) AS nbrEmprunteurs
        FROM Auteurs
        LEFT JOIN Livres ON Livres.AuteurID = Auteurs.AuteurID
        LEFT JOIN Emprunts ON Emprunts.LivreID = Livres.LivreID
        LEFT JOIN Emprunteurs ON Emprunteurs.EmprunteurID = Emprunts.EmprunteurID
        GROUP BY Auteurs.AuteurID
        """
    )
    resultat = cursor.fetchall()
    conn.close()
    print("Nombres d'emprunteurs par Auteur et connexion fermée.")
    return resultat
