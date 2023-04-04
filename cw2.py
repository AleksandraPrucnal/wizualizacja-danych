import math

def iloczyn(*args):
    iloczyn=1
    for i in args:
        iloczyn *= i
    return iloczyn

def suma_poteg(n, *args):
    suma = 0
    for i in args:
        suma += i**n
    return suma

def mean(*args):
    suma = 0
    ilosc = 0
    for i in args:
        suma += i
        ilosc += 1
    return suma/ilosc

def gmean(*args):
    iloczyn = 1
    ilosc = 0
    for i in args:
        iloczyn *= i
        ilosc += 1
    return pow(iloczyn, 1/ilosc)

def dlugosc_sum(*args):
    dlugosc = 0
    for i in args:
        dlugosc += len(i)
    return dlugosc


print(iloczyn(2,4,5))
print(suma_poteg(2,4,5,3))
print(mean(4,5,6,7,8))
print(gmean(5,6,7,8,9,10))
print(dlugosc_sum("Ala ma kota", "bla bla", "tekst"))