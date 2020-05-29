def sprawdz(tekst):
    ma_cyfre = False
    for x in tekst:
        if x.isdigit():
            ma_cyfre = True
            break
    if ma_cyfre == True:
        print("Zdanie nie moze zawierac cyfr")
        return False
    else: 
        return True