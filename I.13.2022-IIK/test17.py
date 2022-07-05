#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Creen un grupo para un for y que la variable recorra el grupo y pare con el valor o palabra ingresada
'''

valor = input('Ingrese un valor: ')

for nombre in ['Paolo', 'Maria', 'Alex', 'Renzo']:
	print(nombre)

	if nombre == valor:
		break


print('FIN')