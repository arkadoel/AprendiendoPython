#prueba while
def pruebaWhile():
	n=0
	while(n<10):
		n +=1
		print "n es", '\t', str(n)
	print "Terminado while, ahora imprimir misma linea"

	#basta con poner una coma al final
	n=0
	while(n<10):
		n +=1
		print '\t', str(n),
	print

#acceso a cadenas de caracteres
def cadenas():
	posicion = 7
	cadena = "ciclopentanoperhidrofenantreno"
	print cadena
	n=0
	while(n<posicion):
		print "",
		n +=1
	print cadena[posicion]

#FOR
def pruebaFOR_EACH():
	cadena = "hola como te llamas"
	for letra in cadena:
		print letra, " ",
	print 

	''' PYTHON NO PERMITE MODIFICAR CADENAS 
		HAY QUE CREARLAS DE NUEVO
	'''
	ncadena = 'J' + cadena[1:]
	print ncadena

if __name__ == '__main__':
	pruebaWhile()
	print

	cadenas()
	print 

	pruebaFOR_EACH()

	pass