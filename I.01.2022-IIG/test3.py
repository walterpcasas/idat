#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = int(input('Ingrese su edad: '))

pais = input('donde naciste: ')

if edad > 65:
	print('No es obligatorio sufragar')
elif edad > 18:
	print('Debe sufragar')
else:
	print('Fin')


if pais == 'Peru':
	print('Eres peruano')
else:
	print('Eres extranjero')


#print('fin')