import ilosc_spacji, ilosc_znakow, top3_znaki, sprawdzenie_tekstu, samogloski_spolgloski


print("Podaj zdanie do analizy: ")
while 1: 
    tekst = input()
    if sprawdzenie_tekstu.sprawdz(tekst) == True: 
        break


ilosc_znakow.znaki(tekst)
ilosc_spacji.ilosc(tekst)
top3_znaki.top3(tekst)
samogloski_spolgloski.samo(tekst)


