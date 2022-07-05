#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = []

while True:
	elemento = input('Ingrese elemento: ')
	if elemento == '0' or elemento.lower() == 'stop':
		break
	else:
		lista.append(elemento)

print(lista)
indice = input('De quien deseas saber su indice: ')
print(indice, 'esta en la posicion', lista.index(indice))
