from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, get_by_id, stergere_obiect, modificare_obiect


def test_adauga_obiect():
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    lista = []
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    assert len(lista) == 1
    assert lista == [obiect]
    assert get_id(get_by_id("4", lista)) == "4"
    assert get_nume(get_by_id("4", lista)) == "surubelnita"
    assert get_descriere(get_by_id("4", lista)) == "metalica"
    assert get_pret(get_by_id("4", lista)) == 76
    assert get_locatie(get_by_id("4", lista)) == "Roma"

def test_get_by_id():
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
    assert get_id(get_by_id("4", lista)) == "4"
    assert get_id(get_by_id("5", lista)) == "5"

def test_stergere_obiect():
    lista = []
    id = "4"
    nume = "surubelnita"
    descriere = "metalica"
    pret_achizitie = 76
    locatie = "Roma"
    lista = []
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    id = "5"
    nume = "macara"
    descriere = "fier"
    pret_achizitie = 1246
    locatie = "Arad"
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie)
    lista = stergere_obiect("4", lista)
    assert len(lista) == 1
    assert get_by_id("4", lista) is None
    assert get_by_id("5", lista) is not None

def test_modificare_obiect():
    lista=[]
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
    lista=modificare_obiect(lista, "5", "vopsea", "rosie",45, "ro")
    assert get_id(get_by_id("4", lista)) == "4"
    assert get_pret(get_by_id("5", lista)) == 45
    assert get_nume(get_by_id("5", lista)) == "vopsea"