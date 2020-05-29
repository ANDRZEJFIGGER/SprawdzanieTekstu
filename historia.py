import time
def zapisz(tekst):
    historia = open("historia.txt", 'a+')
    czas = time.ctime()
    historia.write(czas+ ": " +tekst+"\n")