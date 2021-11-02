from Domain.obiect import to_string
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect
from Logic.functionalitati import concatenare, lista_locatii, pret_max_locatie, ordonare_obiecte, mutare_locatie, \
    suma_pret_locatie
from UI.command_line_console import command_line_console


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5. Concatenarea unui string citit la toate descrierile cu proprietatea ceruta")
    print("6. Determinarea celui mai mare preț pentru fiecare locație.")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("9. Undo")
    print("10.Exerc. lab")
    print("a. Afisare toate obiectele")
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

def ui_concatenare(lista):
    string_citit = input("Dati string-ul: ")
    pret_citit = float(input("Dati pretul: "))
    return concatenare(lista, pret_citit, string_citit)

def ui_pret_maxim_locatie(lista):
    lista_locatie = lista_locatii(lista)
    lista_pret = pret_max_locatie(lista)
    for x in range(0, len(lista_pret)):
        print(lista_locatie[x], ": ", lista_pret[x])

def ui_ordonare_obiecte(lista):
    afisare(ordonare_obiecte(lista))

def afisare(lista):
    for obiect in lista:
        print(to_string(obiect))

def ui_mutare_locatie(lista):
    string_old = input("Dati string-ul vechi: ")
    string_new = input("Dati string-ul nou: ")
    return mutare_locatie(string_new, string_old, lista)

def ui_suma_pret_locatie(lista):
    lista_locatie = lista_locatii(lista)
    lista_suma = suma_pret_locatie(lista)
    for x in range(0, len(lista_suma)):
        print(lista_locatie[x], ": ", lista_suma[x])

def ui_command_line_console(lista):
    command_line_console(lista)

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
           lista = ui_mutare_locatie(lista)
        elif optiune == "5":
            lista = ui_concatenare(lista)
        elif optiune == "6":
            ui_pret_maxim_locatie(lista)
        elif optiune == "7":
            ui_ordonare_obiecte(lista)
        elif optiune == "8":
            ui_suma_pret_locatie(lista)
        elif optiune == "9":
            print("Optiunea de Undo inca nu este realizata")
        elif optiune == "10":
            lista = ui_command_line_console(lista)
        elif optiune == "a":
            afisare(lista)
        elif optiune == "x":
            return 0
        else:
            print("Optiunea nu exista! Reincercati!")
