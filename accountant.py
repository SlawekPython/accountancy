import sys

saldo = 0
#saldo_operacje = {}
magazyn = {}
przeglad = []
historia = []

while True:
    czynn_gosp = input()
    if czynn_gosp == "zakup":
        nazwa_prod = input()
        cena_prod = int(input())
        ilosc = int(input())
        if ilosc < 0:
            print("Nieprawidłowa ilość.")
            continue
        if saldo - cena_prod * ilosc < 0:
            print('Brak środków na zakup!')
            continue
        saldo -= cena_prod * ilosc
        historia.append((czynn_gosp, nazwa_prod, cena_prod, ilosc))
        if nazwa_prod in magazyn:
            magazyn[nazwa_prod] += ilosc
            #print('Produkty w magazynie {}'.format(magazyn))
        else:
            magazyn[nazwa_prod] = ilosc
            #print('Produkty w magazynie {}'.format(magazyn))

    elif czynn_gosp == "saldo":
        wartosc = int(input())
        if saldo + wartosc < 0:
            print('Debet na koncie')
        else:
            saldo = saldo + wartosc
            komentarz = input()
            #saldo_operacje[komentarz] = wartosc
            historia.append((czynn_gosp, wartosc, komentarz))
            #print(saldo_operacje, saldo)

    elif czynn_gosp == "sprzedaz":
        nazwa_prod = input()
        if nazwa_prod not in magazyn:
            print('Brak produktu w magazynie {}'.format(magazyn))
            continue
        cena_jedno_produktu_sprzed = int(input())
        if cena_jedno_produktu_sprzed < 0:
            print('Błąd, cena mniejsza od zera\n')
            continue
        ilosc = int(input())
        if ilosc < 0:
            print('Niesłaściwa ilość \n')
            continue
        if magazyn[nazwa_prod] < ilosc:
            print('Brak wystarczającej ilości produktów na magazynie')
            continue
        saldo += cena_jedno_produktu_sprzed * ilosc
        magazyn[nazwa_prod] -= ilosc
        historia.append((czynn_gosp, nazwa_prod, cena_jedno_produktu_sprzed, ilosc))
        #print('Saldo konta {}\n'.format(saldo))

    elif czynn_gosp == "stop":
        for wiersz in historia:
            for linia in wiersz:
                print(linia)
        print(f"Stan konta: ", saldo)
        break

    else:
        if czynn_gosp not in ("zakup", "saldo", "sprzedaz"):
            print("Błedne działanie, dozwolone tylko zakup, sprzedaż lub saldo")
            break

czynn_gosp = sys.argv[1]
if czynn_gosp == "saldo":
    wartosc = int(sys.argv[2])
    if saldo + wartosc < 0:
        print('Debet na koncie')
    else:
        saldo = saldo + wartosc
        komentarz = sys.argv[3]
        saldo_operacje[komentarz] = wartosc
        historia.append((czynn_gosp, wartosc, komentarz))
        print(saldo_operacje, saldo)

elif czynn_gosp == "zakup":
    nazwa_prod = sys.argv[2]
    cena_prod = int(sys.argv[3])
    ilosc = int(sys.argv[4])
    if ilosc < 0:
        print("Nieprawidłowa ilość.")
    if saldo - cena_prod * ilosc < 0:
        print('Brak środków na zakup!')
    saldo -= cena_prod * ilosc
    historia.append((czynn_gosp, nazwa_prod, cena_prod, ilosc))
    if nazwa_prod in magazyn:
        magazyn[nazwa_prod] += ilosc
        print('Produkty w magazynie {}'.format(magazyn))
    else:
        magazyn[nazwa_prod] = ilosc
        print('Produkty w magazynie {}'.format(magazyn))

elif czynn_gosp == "sprzedaz":
    nazwa_prod = sys.argv[2]
    if nazwa_prod not in magazyn:
        print('Brak produktu w magazynie {}'.format(magazyn))
    cena_jedno_produktu_sprzed = int(sys.argv[3])
    if cena_jedno_produktu_sprzed < 0:
        print('Błąd, cena mniejsza od zera\n')
    ilosc = int(sys.argv[4])
    if ilosc < 0:
        print('Niesłaściwa ilość \n')
    if magazyn[nazwa_prod] < ilosc:
        print('Brak wystarczającej ilości produktów na magazynie')
    saldo += cena_jedno_produktu_sprzed * ilosc
    magazyn[nazwa_prod] -= ilosc
    historia.append((czynn_gosp, nazwa_prod, cena_jedno_produktu_sprzed, ilosc))
    print('Saldo konta {}\n'.format(saldo))

elif czynn_gosp == "konto":
    print(saldo)

elif czynn_gosp == "magazyn":
    for nazwa_prod in sys.argv[2:]:
        stan = 0
        if nazwa_prod in magazyn:
            stan = magazyn[nazwa_prod]
        print("{}: {}".format(nazwa_prod, stan))

elif czynn_gosp == "przeglad":
    for wiersz in historia[int(sys.argv[2]):int(sys.argv[3])+1]:
        for linia in wiersz:
            print(linia)
        #print(wiersz)
    #print(historia[int(sys.argv[2]):int(sys.argv[3])+1])

elif czynn_gosp == "stop":
    print('Koniec')
    #print(historia)

else:
    if czynn_gosp not in ("zakup", "saldo", "sprzedaz"):
        print("Błedne działanie, dozwolone tylko zakup, sprzedaż lub saldo")