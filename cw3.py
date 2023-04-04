import math

def imiona_tel(**kwargs):
    for key, value in kwargs.items():
        print("{} ma numer {}.".format(key, value))

def zarobki(**kwargs):
    suma = 0
    ilosc = 0
    zarobki = list(kwargs.values())
    wzrost = []
    for key, value in kwargs.items():
        ilosc += 1
        suma += float(value)
    arytmetyczna = suma/ilosc
    for i in range(len(zarobki)-1):
        wzrost.append((zarobki[i+1]-zarobki[i])/zarobki[i]*100)
    geometryczna = math.prod([(wzrost/100+1) for wzrost in wzrost]) ** (1/len(wzrost))-1

    return arytmetyczna, geometryczna

tel = {"Ola":"123 456 789", "Aleksandra":"987 654 321"}
print(imiona_tel(**tel))

wyplata = {"kwiecien": 3500, "maj":3700, "czerwiec":4000}

arytmetyczna, geometryczna = zarobki(**wyplata)
print(arytmetyczna)
print(geometryczna)