from Domain.obiect import creeaza_obiect
from Logic.CRUD import adauga_obiect
from UI.console import undo_list, prepare_undo, redo_list


def test_undo_redo():
    undo_lista = []
    redo_lista = []
    lista = []

    id = "1"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 10
    locatie = "Roma"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

    id = "2"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 20
    locatie = "Arad"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

    id = "3"
    nume = "surubelnita1"
    descriere = "metalica1"
    pret_achizitie = 30
    locatie = "Roma"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

    assert len(lista) == 3
    lista = undo_list(lista, undo_lista, redo_lista)
    lista = undo_list(lista, undo_lista, redo_lista)
    lista = undo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 0

    id = "1"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 10
    locatie = "Roma"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

    id = "2"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 20
    locatie = "Arad"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)

    id = "3"
    nume = "surubelnita1"
    descriere = "metalica1"
    pret_achizitie = 30
    locatie = "Roma"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    assert len(lista) == 3

    lista = undo_list(lista, undo_lista, redo_lista)
    lista = undo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 1

    lista = redo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 2

    lista = redo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 3

    lista = undo_list(lista, undo_lista, redo_lista)
    lista = undo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 1

    id = "4"
    nume = "caiet"
    descriere = "universal"
    pret_achizitie = 40
    locatie = "Cluj"
    prepare_undo(undo_lista, redo_lista, lista.copy())
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    assert len(lista) == 2

    lista = undo_list(lista, undo_lista, redo_lista)
    assert len(lista) == 1
    lista = undo_list(lista, undo_lista, redo_lista)

    assert len(lista) == 0
