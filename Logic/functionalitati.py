from Domain.obiect import *

def concatenare(lista, pret_citit, string_citit):
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > pret_citit:
            descriere_noua = get_descriere(obiect)
            descriere_noua += " "
            descriere_noua += string_citit
            obiect_nou = creeaza_obiect(get_id(obiect), get_nume(obiect), descriere_noua, get_pret(obiect), get_locatie(obiect))
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua

def lista_locatii(lista):
    lista_noua = []
    for obiect in lista:
        if get_locatie(obiect) not in lista_noua:
            lista_noua.append(get_locatie(obiect))
    return lista_noua

def pret_max_locatie(lista):
    lista_noua = lista_locatii(lista)
    lista_preturi = []
    for x in lista_noua:
        maxim = 0
        for obiect in lista:
            if get_locatie(obiect) == x and get_pret(obiect) > maxim:
                maxim = get_pret(obiect)
        lista_preturi.append(maxim)
    return lista_preturi

def ordonare_obiecte(lista):
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if float(get_pret(lista[i])) > float(get_pret(lista[j])):
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def mutare_locatie(str_new, string_old, lista):
    lista_noua = []
    for obiect in lista:
        if get_locatie(obiect) == string_old:
            obiect1 = creeaza_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect), str_new)
            lista_noua.append(obiect1)
        else:
            lista_noua.append(obiect)
    return lista_noua

def suma_pret_locatie(lista):
    lista_noua = lista_locatii(lista)
    lista_suma = []
    for x in lista_noua:
        suma = 0
        for obiect in lista:
            if get_locatie(obiect) == x:
                suma += float(get_pret(obiect))
        lista_suma.append(suma)
    return lista_suma
