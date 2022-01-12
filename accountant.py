import sys

saldo = 0
saldo_operacje = {}
magazyn = {}
przeglad = []
historia = []
slwownik = {}

while True:
    czynn_gosp = sys.argv[1]
    slownik = {"zakup": nazwa_prod: cena_prod: ilosc, "saldo": wartosc: komentarz, "sprzedaz": nazwa_prod: cena_jedno_produktu_sprzed: ilosc}
    if slownik[czynn_gosp] == "zakup"
    #czynn_gosp = input('Podaj czynność gospodarczą ')
    #if czynn_gosp == "zakup":
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
        historia.append((czynn_gosp, cena_prod, ilosc))
        if nazwa_prod in magazyn:
            magazyn[nazwa_prod] += ilosc
            print('Produkty w magazynie {}'.format(magazyn))
        else:
            magazyn[nazwa_prod] = ilosc
            print('Produkty w magazynie {}'.format(magazyn))

    elif czynn_gosp == "saldo":
        wartosc = int(input("Podaj kwotę "))
        saldo = saldo + wartosc
        komentarz = input('Podaj komentarz ')
        saldo_operacje[komentarz] = wartosc
        historia.append((czynn_gosp, wartosc, komentarz))
        print(saldo_operacje, saldo)

    elif czynn_gosp == "sprzedaz":
        nazwa_prod = input('Podaj nazwę sprzedawanego produktu ')
        if nazwa_prod not in magazyn:
            print('Brak produktu w magazynie {}'.format(magazyn))
            continue
        cena_jedno_produktu_sprzed = int(input(
            'Podaj cenę jendostkową sprzedawanego produktu '))
        if cena_jedno_produktu_sprzed < 0:
            print('Błąd, cena mniejsza od zera\n')
            continue
        ilosc = int(input('Podaj sprzedawaną ilość '))
        if ilosc < 0:
            print('Niesłaściwa ilość \n')
            continue
        if magazyn[nazwa_prod] < ilosc:
            print('Brak wystarczającej ilości produktów na magazynie')
            continue
        saldo += cena_jedno_produktu_sprzed * ilosc
        magazyn[nazwa_prod] -= ilosc
        historia.append((czynn_gosp, nazwa_prod, cena_jedno_produktu_sprzed, ilosc))
        print('Saldo konta {}\n'.format(saldo))

    elif czynn_gosp == "stop":
        print('Koniec')
        print(historia)
        break

    else:
        if czynn_gosp not in ("zakup", "saldo", "sprzedaz"):
            print("Błedne działanie, dozwolone tylko zakup, sprzedaż lub saldo")
            break
