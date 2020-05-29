import collections
def top3(tekst):
    tekst_lower = tekst.lower()
    tekst_lower = tekst_lower.replace(" ","")

    x = collections.Counter(tekst_lower.strip()).most_common(3)
    print(f"Najczesciej uzyte litery to:\n#1 {x[0][0]}: {x[0][1]} razy\n#2 {x[1][0]}: {x[1][0]} razy\n#3 {x[2][0]}: {x[2][1]} razy")
    
