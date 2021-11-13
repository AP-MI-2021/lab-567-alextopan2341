from Domain.obiect import to_string, is_number, get_pret
from Logic.CRUD import adauga_obiect, stergere_obiect, modificare_obiect, get_by_id
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
    print("10. Redo")
    print("11.Exercitiul de la  lab")
    print("a. Afisare toate obiectele")
    print("x. Iesire")


def ui_adaugare_obiect(lista, undo_lista, redo_list):
    try:
        id = input("Dati id-ul: ")
        if get_by_id(id, lista) is not None:
            raise ValueError("Id-ul exista deja!")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret_achizitie = float(input("Dati pretul: "))
        locatie = input("Dati locatia: ")
        copie_lista = lista.copy()
        adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
        prepare_undo(undo_lista,redo_list,copie_lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_stergere_obiect(lista, undo_lista, redo_list):
    try:
        id = input("Dati id-ul obiectului de sters: ")
        copie_lista = lista.copy()
        rezultat = stergere_obiect(id, lista)
        prepare_undo(undo_lista, redo_list, copie_lista)
        return rezultat
    except ValueError as ve:
        print("Eroarea este: {}". format(ve))
        return lista


def ui_modificare_obiect(lista, undo_lista, redo_list):
    try:
        id = input("Dati id-ul obiectului de modificat: ")
        if get_by_id(id, lista) is None:
            raise ValueError("Id-ul de modificat nu exista")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret_achizitie = input("Dati pretul: ")
        locatie = input("Dati locatia: ")
        copie_lista = lista.copy()
        rezultat = modificare_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
        prepare_undo(undo_lista, redo_list, copie_lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def ui_concatenare(lista, undo_lista, redo_list):
    string_citit = input("Dati string-ul: ")
    pret_citit = float(input("Dati pretul: "))
    copie_lista = lista.copy()
    prepare_undo(undo_lista, redo_list, copie_lista)
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


def ui_mutare_locatie(lista, undo_lista, redo_list):
    string_old = input("Dati string-ul vechi: ")
    string_new = input("Dati string-ul nou: ")
    copie_lista = lista.copy()
    prepare_undo(undo_lista, redo_list, copie_lista)
    return mutare_locatie(string_new, string_old, lista)


def ui_suma_pret_locatie(lista):
    lista_locatie = lista_locatii(lista)
    lista_suma = suma_pret_locatie(lista)
    for x in range(0, len(lista_suma)):
        print(lista_locatie[x], ": ", lista_suma[x])


def undo_list(lista, undo_lista, redo_lista):
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
        return lista
    else:
        print("Nu se poate face undo!")


def redo_list(lista, undo_lista, redo_lista):
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
        return lista
    else:
        print("Nu se poate face redo!")


def prepare_undo(undo_lista,redo_lista,copie_lista):
    undo_lista.append(copie_lista)
    redo_lista.clear()

def run_menu(lista):
    undo_lista = []
    redo_lista = []

    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            ui_adaugare_obiect(lista, undo_lista, redo_lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista, undo_lista, redo_lista)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista, undo_lista, redo_lista)
        elif optiune == "4":
           lista = ui_mutare_locatie(lista, undo_lista, redo_lista)
        elif optiune == "5":
            lista = ui_concatenare(lista, undo_lista, redo_lista)
        elif optiune == "6":
            ui_pret_maxim_locatie(lista)
        elif optiune == "7":
            ui_ordonare_obiecte(lista)
        elif optiune == "8":
            ui_suma_pret_locatie(lista)
        elif optiune == "9":
            lista = undo_list(lista, undo_lista, redo_lista)
        elif optiune == "10":
            lista = redo_list(lista, undo_lista, redo_lista)
        elif optiune == "11":
            lista = command_line_console(lista)
        elif optiune == "a":
            afisare(lista)
        elif optiune == "x":
            return 0
        else:
            print("Optiunea nu exista! Reincercati!")
