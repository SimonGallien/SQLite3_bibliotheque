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
