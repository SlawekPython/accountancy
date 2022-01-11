import sys

saldo = 0
saldo_operacje = {}
magazyn = {}
przeglad = []

while True:
    czynn_gosp = input('Podaj czynność gospodarczą ')
    if czynn_gosp == "zakup":
        nazwa_prod = input('Podaj nazwę produktu ')
        cena_prod = int(input('Podaj cenę produktu '))
        ilosc = int(input('Podaj kupowaną ilość '))
        if ilosc < 0:
            print("Nieprawidłowa ilość.")
            continue
        if saldo - cena_prod * ilosc < 0:
            print('Brak środków na zakup!')
            continue
        saldo -= cena_prod * ilosc
        if nazwa_prod in magazyn:
            magazyn[nazwa_prod] += ilosc
            print('Produkty w magazynie {}'.format(magazyn))
        else:
            magazyn[nazwa_prod] = ilosc
            print('Produkty w magazynie {}'.format(magazyn))

    if czynn_gosp == "saldo":
        wartosc = int(input("Podaj kwotę "))
        saldo = saldo + wartosc
        komentarz = input('Podaj komentarz ')
        saldo_operacje[komentarz] = wartosc
        print(saldo_operacje, saldo)

    if czynn_gosp == "sprzedaz":
        nazwa_prod = input('Podaj nazwę sprzedawanego produktu ')
        cena_jedno_produktu_sprzed = int(input('Podaj cenę jendostkową sprzedawanego produktu '))
        if cena_jedno_produktu_sprzed < 0:
            print('Błąd, cena mniejsza od zera\n')
            continue
        ilosc = int(input('Podaj sprzedawaną ilość '))
        if ilosc < 0:
            print('Niesłaściwa ilość \n')
            continue
        saldo += cena_jedno_produktu_sprzed * ilosc
        print('Saldo konta {}\n'.format(saldo))
        if nazwa_prod in magazyn:
            magazyn[nazwa_prod] -= ilosc
            print('Produkty w magazynie {}'.format(magazyn))
        else:
            magazyn[nazwa_prod] = ilosc
            print('Produkty w magazynie {}'.format(magazyn))

    else:
        if not czynn_gosp == "zakup" or czynn_gosp == "saldo" or czynn_gosp == "sprzedzaz":
            print("Błedne działanie, dozwolone tylko zakup, sprzedaż lub saldo")
            break