from Tests.test_CRUD import test_adauga_obiect, test_stergere_obiect, test_modificare_obiect, test_get_by_id
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_concatenare, test_lista_locatii, test_pret_max_locatie, \
    test_ordonare_obiecte, test_mutare_locatie, test_suma_pret_locatie, test_undo_redo


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()
    test_modificare_obiect()
    test_get_by_id()
    test_concatenare()
    test_lista_locatii()
    test_pret_max_locatie()
    test_ordonare_obiecte()
    test_mutare_locatie()
    test_suma_pret_locatie()
    test_undo_redo()
