from Logic.CRUD import adauga_obiect, stergere_obiect

def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("a. Afisare toate obiectele")


def command_line_console(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "add":
            id = input("Dati id: ")
            nume = input("Dati nume: ")
            descriere = input("Dati descriere: ")
            pret_achizitie = float(input("Dati pretul: "))
            locatie = input("Dati locatie: ")
            lista = adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
        elif optiune == "showall":
            print(lista)
        elif optiune == "stop":
            return 0
        elif optiune == "delete":
            id = input("Dati id-ul dorit: ")
            lista = stergere_obiect(id, lista)
        else:
            print("Optiune gresita! Reincercati!")