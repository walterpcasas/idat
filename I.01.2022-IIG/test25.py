#!/usr/bin/env python
# -*- coding: utf-8 -*-

alumnos = []

n = int(input('Ingrese cantidad de alumnos: '))

for i in range(n):
	nombre = input('Ingrese nombre de alumno: ')
	alumnos.append(nombre)


for alumno in alumnos:
	print(alumno)


valor = input('que nombre desea saber la posicion: ')


contador = 0
for alumno in alumnos:
	if alumno == valor:
		print(contador)
		break
	contador+=1