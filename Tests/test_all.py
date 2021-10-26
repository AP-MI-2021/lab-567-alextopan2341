from Tests.test_CRUD import test_adauga_obiect, test_stergere_obiect, test_modificare_obiect, test_get_by_id
from Tests.test_domain import test_obiect


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()
    test_modificare_obiect()
    test_get_by_id()