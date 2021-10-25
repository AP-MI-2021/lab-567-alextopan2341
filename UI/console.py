from Domain.obiect import to_string
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Afisare toate obiectele")
    print("x. Iesire")


def ui_adaugare_obiect(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret_achizitie = float(input("Dati pretul: "))
    locatie = input("Dati locatia: ")
    return adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)


def ui_stergere_obiect(lista):
    id = input("Dati id-ul obiectului de sters: ")
    return stergere_obiect(id, lista)


def ui_modificare_obiect(lista):
    id = input("Dati id-ul obiectului de modificat: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret_achizitie = input("Dati pretul: ")
    locatie = input("Dati locatia: ")
    return modificare_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

def afisare(lista):
    for obiect in lista:
        print(to_string(obiect))

def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista)
        elif optiune == "4":
            afisare(lista)
        elif optiune == "x":
            return 0
        else:
            print("Optiunea nu exista! Reincercati!")
