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

print(alumnos.index(valor))