def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    '''
    Creeaza un dictionar ce retine un obiect
    :param id: id-ul dictionarului - string
    :param nume: numele obiectului - string
    :param descriere: descrierea obiectului -string
    :param pret_achizitie: pretul achizitiei - float
    :param locatie: locatia obiectului - string
    :return: un dictionar ce retine un obiect
    '''
    return [id, nume, descriere, pret_achizitie, locatie]
    #return {
        #"id": id,
        #"nume": nume,
        #"descriere": descriere,
        #"pret": pret_achizitie,
        #"locatie": locatie
    #}
def get_id(obiect):
    '''
    returneaza id-ul obiectului
    :param obiect: un dictionar de tip obiect
    :return: id-ul obiectului - string
    '''
    #return obiect["id"]
    return obiect[0]

def get_nume(obiect):
    '''
    returneaza numele obiectului
    :param obiect:  un dictionar de tip obiect
    :return: numele obiectului - string
    '''
    #return obiect["nume"]
    return obiect[1]

def get_descriere(obiect):
    '''
    returneaza descrierea obiectului
    :param obiect: un dictionar de tip obiect
    :return: descrierea obiectului - string
    '''
    #return obiect["descriere"]
    return obiect[2]
def get_pret(obiect):
    '''
    returneaza pretul obiectului
    :param obiect: un dictionar de tip obiect
    :return: pretul obiectului - float
    '''
    #return obiect["pret"]
    return obiect[3]

def get_locatie(obiect):
    '''
    returneaza locatia obiectului
    :param obiect: un dictionar de tip obiect
    :return: locatia obiectului - string
    '''
    #return obiect["locatie"]
    return obiect[4]

def to_string(obiect):
    ob = {"id": get_id(obiect), "nume": get_nume(obiect), "descriere": get_descriere(obiect), "pret": get_pret(obiect), "locatie": get_locatie(obiect)}
    li = list(ob.items())
    return li
    '''
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie:{}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )
    '''
def valideaza_locatie(obiect):
    if len(get_locatie(obiect)) > 4:
        raise ValueError("Locatia trebuie sa aiba maxim 4 caractere!")
    elif len(get_locatie(obiect)) == 0:
        raise ValueError("Locatia nu poate fi nula!")

def valideaza_nume(obiect):
    if len(get_nume(obiect)) == 0:
        raise ValueError("Numele nu poate fi nul!")

def valideaza_id(obiect):
    if get_id(obiect) is not None:
        raise ValueError("ID-ul exista deja!")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def valideaza_pret(obiect):
    if is_number(get_pret(obiect)) is False:
        raise ValueError("Pretul nu poate contine string-uri")