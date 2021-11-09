from Domain.obiect import get_id, creeaza_obiect
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect, get_by_id


def print_menu():
    print("add. Adaugare obiect")
    print("delete. Stergere obiect")
    print("change. Modificare obiect")
    print("showall. Afisare toate obiectele")
    print("exit")

def command_line_console(lista):
    lista = []
    while True:
        print_menu()
        numere = []
        string_citit = input("Dati optiunea: ")
        numere = string_citit.split(",")
        if numere[0] == "add":
            try:
                id = numere[1]
                nume = numere[2]
                descriere = numere[3]
                pret_achizitie = float(numere[4])
                locatie = numere[5]
                obiect = creeaza_obiect(id,nume,descriere,pret_achizitie,locatie)
                if get_id(obiect) is None:
                    raise ValueError("Nu ati dat ID!")
                elif get_by_id(id, lista) is not None:
                    raise ValueError("Id-ul exista!")
                adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
                if numere[6] == "showall":
                    print(lista)
            except ValueError as ve:
                print("Eroare: {}". format(ve))
        elif numere[0] == "change":
            try:
                id = numere[1]
                nume = numere[2]
                descriere = numere[3]
                pret_achizitie = float(numere[4])
                locatie = numere[5]
                obiect = creeaza_obiect(id,nume,descriere,pret_achizitie,locatie)
                if get_id(obiect) is None:
                    raise ValueError("Nu exista acest ID pentru modificare!")
                lista = modificare_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
                if numere[6] == "showall":
                    print(lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
        elif numere[0] == "showall":
            print(lista)
        elif numere[0] == "exit":
            break
        elif numere[0] == "delete":
            try:
                id = numere[1]
                if get_by_id(id, lista) is None:
                    raise ValueError("Id-ul nu exista!")
                lista = stergere_obiect(id, lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
        else:
            print("Optiune gresita! Reincercati!")
    return lista