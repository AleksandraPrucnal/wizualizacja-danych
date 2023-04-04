import math

def sprawdz_pesel(pesel):
    if len(pesel) != 11:
        return "blad"
    if not pesel.isdigit():
        return "blad"
    wartosci = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma= sum([int(pesel[i])*wartosci[i] for i in range(10)]) % 10
    if suma != 0:
        return "blad"
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel[4:6])
    plec = "mężczyzna" if int(pesel[9]) % 2 == 1 else "kobieta"
    if miesiac > 12:
        rok += 2000
        miesiac -= 20
    else:
        rok += 1900
    return f"Data urodzenia: {dzien, miesiac, rok}, płeć: {plec}"

print(sprawdz_pesel("99040402602"))
