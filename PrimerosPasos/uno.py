import sys

'''
	Las variables globales se definen dentro de los metodos 
	y despues se pone global. No se admite inicializarlas al
	mismo tiempo, ha de hacerse en dos lineas distintas.
'''
def imprimeMenu():
	print ("Menu")
	print ("\t1.- meter numeros")
	print ("\t2.- sumar")
	print ("\t9.- Salir")
	opcion = input("\topcion>")

	return int(opcion)

def sumarNumeros():
	resultado = n1 + n2
	return resultado

def pedirNumeros():
	global n1 
	n1 = int( input("Pon el primer numero: "))
	global n2 
	n2= int( input("Pon el segundo numero: "))
	#como son variables globales ya esta

if __name__ == '__main__':
	seguir = True

	while(seguir):
		
		opcion = imprimeMenu()

		if(opcion == 1):
			pedirNumeros()
		elif (opcion==2):
			print ( str(sumarNumeros()) )
		elif (opcion==9):
			seguir = False
		else:
			print ("Elige una opcion correcta")

	pass
