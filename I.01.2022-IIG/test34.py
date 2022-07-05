#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = []

while True:
	elemento = int(input('Ingrese elemento: '))
	if elemento == 0:
		break
	else:
		lista.append(elemento)

print(lista)

ordenado = False

while not ordenado:
	ordenado = True

	for i in range(len(lista) - 1):

		if lista[i] > lista[i+1]:
			lista[i], lista[i+1] =lista[i+1], lista[i]
			ordenado = False

print(lista)

