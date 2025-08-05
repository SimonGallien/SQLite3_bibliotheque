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
