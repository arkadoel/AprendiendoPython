#funcion que pone lineas vacias
def nuevaLinea():
	print

#pasar un parametro y definir una variable local
def ponerVariable(variable, variable2):
	n1 = int(23 - 3.18)
	print variable + str(n1)

#sentencias if-elif-else
def evaluacion(numero):
	if(numero == 32):
		print "numero correcto 32"
	elif (numero <32):
		print "Numero demasiado bajo"
	else:
		print "numero Mayor"

#funcion con retorno
def retorna(numero):
	n1= numero +3
	return n1;

#funcion retornar True|false
def esNumeroEntero(variable):
	tipo = str(type(variable).__name__)
	if(tipo == "int"):
		return True
	else:
		return False

######### MAIN ################
if __name__ == '__main__':
	nuevaLinea()
	nuevaLinea()

	ponerVariable("pedro",3.18)
	nuevaLinea()

	evaluacion(32)
	evaluacion(13)
	evaluacion(321)

	nuevaLinea()
	print "retornado: " + str( retorna(32) ) 

	nuevaLinea()
	print "Es numero entero? " + str( esNumeroEntero("lol") )
	pass

