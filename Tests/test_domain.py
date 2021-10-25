from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "ciocan", "lemn", 58, "Cluj")
    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "ciocan"
    assert get_descriere(obiect) == "lemn"
    assert get_pret(obiect) == 58
    assert get_locatie(obiect) == "Cluj"
