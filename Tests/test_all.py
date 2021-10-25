from Tests.test_CRUD import test_adauga_obiect, test_stergere_obiect
from Tests.test_domain import test_obiect


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_stergere_obiect()