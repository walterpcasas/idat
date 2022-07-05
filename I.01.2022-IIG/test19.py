#!/usr/bin/env python
# -*- coding: utf-8 -*-

alto = input('Ingrese el nombre del alumno: ')

for nombre in ['Roberto', 'Ricardo', 'Luis', 'Michael']:
	print('El alumno se llama: ', end = '\t')
	print(nombre)
	if nombre == alto:
		print('Encontre al alumno')
		break


print('FIN')



# Recorrer un conjunto y parar cuando sea
# par y mayor que 100