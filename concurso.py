# -*- coding: utf-8 -*-
# author: Ricardo Ruiz

# Programa en Python que halla la solucion del problema
# Problema: subconjuntos de N, con elementos consecutivos que sumen 91

import sys


isnatural = lambda num: isinstance(num, int) and num > 0

def solveProblema(n):
	'''N must be a natural number'''

	if not isnatural(n): raise ValueError("El numero tiene que ser natural")

	posibles = []
	conjuntos = []

	for primero in range(1, n+1):
		for siguiente in range(primero, n+1):
			posibles.append(siguiente)
			if sum(posibles) == n:
				conjuntos.append(posibles[:])
		posibles = []
	return [conjunto for conjunto in conjuntos if len(conjunto) > 1]

def formatConjunto(conjunto):
	return '{'+str(conjunto[0]) + ', ... ' + str(conjunto[-1]) + '}'


def consultarNumero():

	try: 
		numero = int(raw_input("Número a ingresar: "))
	except ValueError:
		print("Debe ser un numero natural")
		exit()
	except KeyboardInterrupt:
		print("\nPrograma terminado")
		exit()

	return numero


if __name__ == '__main__':

	try:
		numero = int(sys.argv[1])
	except:
		numero = consultarNumero()

	solucion = solveProblema(numero)

	print "Los siguientes subconjuntos en N de numeros consecutivos suman " + str(numero)
	for conjunto in solucion:
		print formatConjunto(conjunto) + " => " + str(sum(conjunto))
