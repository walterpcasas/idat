#!/usr/bin/env python
# -*- coding: utf-8 -*-

nuevo = True

while nuevo:
	respuesta = input('Ingresar mas datos: ')

	if respuesta == 'no':
		print('No mas usuarios')
		nuevo = False

	else:
		print('Puedo poner mas usuarios')

print('FIN')