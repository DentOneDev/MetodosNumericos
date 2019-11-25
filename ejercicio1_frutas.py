n =1
while n >= 1 :

	fruta =str(raw_input("Escribe el nombre de una fruta:  "))
	if fruta:
		lista = []
		lista.append(fruta)
		print lista 
		n = n+1

	else:
		print len(lista)
		break

