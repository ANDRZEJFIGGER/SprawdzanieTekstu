import ilosc_spacji, ilosc_znakow, top3_znaki, sprawdzenie_tekstu, samo_spol, palindrom, python


print("Podaj zdanie do analizy: ")
while 1: 
    tekst = input()
    if sprawdzenie_tekstu.sprawdz(tekst) == True: 
        break


ilosc_znakow.znaki(tekst)
ilosc_spacji.ilosc(tekst)
top3_znaki.top3(tekst)
samogloski_spolgloski.samo(tekst)
palindrom.palindrom(tekst)
python.zliczPython(tekst)


