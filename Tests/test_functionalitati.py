from Domain.obiect import creeaza_obiect, get_descriere, get_nume, get_pret
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitati import concatenare, lista_locatii, pret_max_locatie, ordonare_obiecte


def test_concatenare():
    lista1 = []
    lista = []
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "5"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 1246
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    pret_citit = 100
    string_citit = "Mare"
    lista1 = concatenare(lista, pret_citit, string_citit)
    assert get_nume(get_by_id("5", lista1)) == "macara"
    assert get_descriere(get_by_id("5", lista1)) == "fier Mare"
    assert get_descriere(get_by_id("4", lista1)) == "metalica"
    assert get_descriere(get_by_id("5", lista)) == "fier"

def test_lista_locatii():
    lista1 = []
    lista = []
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "5"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 1246
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "6"
    nume = "surubelnita1"
    descriere = "metalica1"
    pret_achizitie = 176
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "7"
    nume = "macara1"
    descriere = "fier1"
    pret_achizitie = 146
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    lista1 = lista_locatii(lista)
    assert len(lista1) == 2
    assert lista1[0] == "Roma"
    assert lista1[1] == "Arad"

def test_pret_max_locatie():
    lista1 = []
    lista = []
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "5"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 1246
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "6"
    nume = "surubelnita1"
    descriere = "metalica1"
    pret_achizitie = 176
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "7"
    nume = "macara1"
    descriere = "fier1"
    pret_achizitie = 146
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    lista1 = pret_max_locatie(lista)
    assert lista1[0] == 176
    assert lista1[1] == 1246

def test_ordonare_obiecte():
    lista = []
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "5"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 1246
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "6"
    nume = "surubelnita1"
    descriere = "metalica1"
    pret_achizitie = 176
    locatie = "Roma"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "7"
    nume = "macara1"
    descriere = "fier1"
    pret_achizitie = 146
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    ordonare_obiecte(lista)
    assert get_pret(lista[0]) == 76
    assert get_pret(lista[1]) == 146
    assert get_pret(lista[2]) == 176
    assert get_pret(lista[3]) == 1246