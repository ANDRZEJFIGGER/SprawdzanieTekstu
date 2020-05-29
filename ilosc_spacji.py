def ilosc(tekst):
    spacje = 0
    for i in range(len(tekst)):
        if tekst[i] == " ":
            spacje += 1 
    print(f"w tekscie uzyto {spacje} spacji")