from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect


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
            id = numere[1]
            nume = numere[2]
            descriere = numere[3]
            pret_achizitie = float(numere[4])
            locatie = numere[5]
            lista = adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
            if numere[6] == "showall":
                print(lista)
        elif numere[0] == "change":
            id = numere[1]
            nume = numere[2]
            descriere = numere[3]
            pret_achizitie = float(numere[4])
            locatie = numere[5]
            lista = modificare_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
            if numere[6] == "showall":
                print(lista)
        elif numere[0] == "showall":
            print(lista)
        elif numere[0] == "exit":
            return 0
        elif numere[0] == "delete":
            id = numere[1]
            lista = stergere_obiect(id, lista)
        else:
            print("Optiune gresita! Reincercati!")