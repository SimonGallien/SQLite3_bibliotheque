from insert_data import insert_data
from database import create_tables
from queries import *

if __name__ == "__main__":
    create_tables()
    insert_data()

    livres = get_livres_disponibles()
    print("\n📚 Livres disponibles :")
    for livre in livres:
        print("-", livre[0])
