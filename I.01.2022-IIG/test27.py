#!/usr/bin/env python
# -*- coding: utf-8 -*-

alumnos = []

nombre = ""

while nombre != 0 and nombre.lower() != "stop":
	
	nombre = input('Ingrese nombre de alumno: ')

	if nombre.lower() != "stop":
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