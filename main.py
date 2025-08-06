from insert_data import insert_data
from database import create_tables
from queries import *

if __name__ == "__main__":
    create_tables()
    insert_data()

    livresDiponible = get_livres_disponibles()
    print("\n📚 Livres disponibles :")
    for livre in livresDiponible:
        print(f"- {livre[0]}")

    livresTrie = get_livres_by_date()
    print("\n📅 Livres triés par date de publication :")
    for titre, date in livresTrie:
        print(f"- {titre} ({date})")

    livreEmprunte = get_livres_empruntes_en_cours()
    print("\n📚 Livres en cours d'emprunt :")
    for livre, dateRetourEffective in livreEmprunte:
        print(f"- {livre} - {dateRetourEffective}")

    dureeEmprunt = calcul_duree_emprunt()
    print("\n📅 Durée d'emprunts des livres rendus :")
    print(
        f"{'ID':<4} | {'Livre':<6} | {'Emprunteur':<12} | {'Début':<12} | {'Retour':<12} | {'Durée (j)':<10}"
    )
    print("-" * 72)

    for (
        EmpruntID,
        LivreID,
        EmprunteurID,
        DateEmprunt,
        DateRetourEffective,
        dureeEmprunt,
    ) in dureeEmprunt:
        print(
            f"{EmpruntID:<4} | {LivreID:<6} | {EmprunteurID:<12} | {DateEmprunt:<12} | {DateRetourEffective:<12} | {dureeEmprunt:<10.0f}"
        )

    LivresAuteurs = get_livres_auteurs()
    print("\n📖 Livres avec leurs Auteurs :")
    print(f"{'Livre':<35} | {'Nom'} et {'Prénom de l\'auteur'}")
    print("-" * 64)
    for livre, nomAuteur, prenomAuteur in LivresAuteurs:
        print(f"{livre:<35} | {prenomAuteur} {nomAuteur}")

    emprunteursLivresNonRendu = get_emprunteurs_livres_non_rendus()
    emprunteursLivresNonRendu = get_emprunteurs_livres_non_rendus()

    print("\n👤 Emprunteurs n'ayant pas encore rendu leur livre :")
    print(f"{'Prénom':<15} | {'Nom':<15} | {'Email'}")
    print("-" * 55)

    for prenom, nom, email in emprunteursLivresNonRendu:
        print(f"{prenom:<15} | {nom:<15} | {email}")

    nbrLivresParGenre = get_nbr_livres_par_genre()
    print("\n📖 Nombre de livres par genre :")
    print(f"{'Genre':<18} | {'Nbr de livre(s)':<6}")
    print("-" * 37)
    for genre, nbrLivre in nbrLivresParGenre:
        print(f"{genre:<18} | {nbrLivre:<6}")

    dureeMoyenneEmprunt = get_duree_moy_emprunt()
    print("\n🕰️ Durée moyenne d'emprunt par emprunteurs :")
    print(f"{'Prénom':<10} | {'Nom':<10} | Durée moyenne d'emprunt (jour)")
    print("-" * 45)
    for nom, prenom, duree in dureeMoyenneEmprunt:
        print(f"{prenom:<10} | {nom:<10} | {duree}")

    historiqueEmprunt = get_emprunteurs_livres_et_genres()
    print("\n 📅 Historique des emprunts :")
    print(
        f"{'Prénom':<10} | {'Nom':<10} | {'Titre du livre':<32} | {'Genre du livre'}"
    )
    print("-" * 70)
    for nom, prenom, titre, genre in historiqueEmprunt:
        titre_str = f"{titre}" if titre is not None else "Aucun"
        print(f"{prenom:<10} | {nom:<10} | {titre_str:<32} | {genre}")

    top3 = get_top3_livre()
    print("\n🏆 Top 3 des livres les plus empruntés :")
    print(f"{'Titre':<35} | {'Nombre d\'emprunts'}")
    print("-" * 50)
    for titre, count in top3:
        print(f"{titre:<35} | {count}")

    nbrLivreParEmprunteur = get_nombre_emprunts_par_emprunteur()
    print("\n📖 Nombre total de livres empruntés par chaque emprunteur :")
    print(f"{'Prénom':<12} | {'Nom':<12} | {'Nombre total d\'emprunts'}")
    print("-" * 42)
    for prenom, nom, nbrEmprunt in nbrLivreParEmprunteur:
        print(f"{prenom:<12} | {nom:<12} | {nbrEmprunt}")

    livresJamaisEmpruntés = get_livres_jamais_empruntes()
    print("\n📖 Livres jamais empruntés :")
    for livre in livresJamaisEmpruntés:
        print(f"- {livre[0]}")
