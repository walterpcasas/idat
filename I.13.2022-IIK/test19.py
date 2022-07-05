#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Crear una lista y luego mostrar sus 
elementos, pedir un valor de la lista 
e indicar en que posicion encuentra.
'''

alumnos = ['Paolo', 'Maria', 'Alex', 'Renzo', 'Maria']


for alumno in alumnos:
	print(alumno)

print('-------')


valor = input('Ingrese un valor: ')

contador = 0

for alumno in alumnos:
	if alumno == valor:
		print(alumno, 'esta en la posicion', contador)

	contador+=1