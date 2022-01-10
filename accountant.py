import sys

saldo = 0
saldo_operacje = []
magazyn = {}
przeglad = []

while True:
    czynn_gosp = input('Podaj czynność gospodarczą ')
    if czynn_gosp == "zakup":
        nazwa_prod = input('Podaj nazwę produktu ')
        cena_prod = int(input('Podaj cenę produktu '))
        ilosc = int(input('Podaj kupowaną ilość '))
        if saldo - cena_prod * ilosc < 0:
            print('Brak środków na zakup!')
            continue
        saldo -= cena_prod * ilosc
        if nazwa_prod in magazyn:
            magazyn[nazwa_prod] += ilosc
        else:
            magazyn[nazwa_prod] = ilosc

    if czynn_gosp == "saldo":
        kwota = int(input("Podaj kwotę "))
        saldo = saldo + kwota
        komentarz = input('Podaj komentarz ')
        saldo_operacje.append([komentarz, kwota])

    else:
        break