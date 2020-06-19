def palindrom(tekst):
	slowa = tekst.split(' ')
	print("SÅ‚owa napisane na wspak:")
	for slowo in slowa:
		dlugosc = len(slowo)
		nowe = ""
		for i in range(dlugosc):
			nowe += slowo[dlugosc - i - 1]
		print(nowe)