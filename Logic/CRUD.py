from Domain.obiect import creeaza_obiect, valideaza_obiect, get_id


def adauga_obiect(lista, id, nume, descriere, pret_achizitie, locatie):
    '''
    Adauga un obiect nou intr-o lista
    :param lista: lista de obiecte
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul obiectului
    :param locatie: locatia obiectului
    :return: lista actualizata
    '''
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    valideaza_obiect(obiect)
    lista.append(obiect)
    return lista

def get_by_id(id, lista):
    '''
    ia obiectul cu id-ul dat intr-o lista
    :param lista: lista de obiecte
    :param id: string
    :return: obiectul cu id-ul sau o in caz contrar
    '''
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None
def stergere_obiect(id, lista):
    '''
    sterge un obiect dintr-o lista dupa id
    :param id: string
    :param lista: list de obiecte
    :return: lista de obiecte
    '''
    return [obiect for obiect in lista if get_id(obiect) != id]
def modificare_obiect(lista, id, nume, descriere, pret_achizitie, locatie):
    '''
    Modifica lista de obiecte dupa id
    :param id: id-ul unui obiect
    :param nume: noul numele
    :param descriere: noua descrierea
    :param pret_achizitie: noul pretul de achizitie al obiectului
    :param locatie: noua locatia obiectului
    :return:
    '''
    lista_noua = lista
    lista=[]
    for obiect in lista_noua:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, float(pret_achizitie), locatie)
            lista.append(obiect_nou)
        else:
            lista.append(obiect)
    return lista