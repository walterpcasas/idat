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
eliminar = input('Ingresa el valor a eliminar: ')
indice = lista.index(eliminar)

nuevo = input('Ingresa el nuevo valor: ')
lista.remove(eliminar)
lista.insert(indice, nuevo)

print(lista)
