#encoding:utf-8
# Programa en Python que halla la solucion del problema
# Problema: subconjuntos de N, con elementos consecutivos que sumen 91

import sys

def solveProblema(n):
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


if __name__ == '__main__':

	try:
		numero = int(sys.argv[1])
	except:
		print "Error: python concurso.py <int>"
		exit()
	solucion = solveProblema(numero)

	print "Los siguientes subconjuntos en N de numeros consecutivos suman " + str(numero)
	for conjunto in solucion:
		print formatConjunto(conjunto) + " => " + str(sum(conjunto))
