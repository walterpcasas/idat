#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = int(input('Ingrese su edad: '))

if edad >= 18:
	print('Eres mayor de edad')

	if edad >= 65:
		print('No es obligatorio votar')
	else:
		respuesta = input('Tienes alguna discapacidad: ')       
		
		if respuesta == 'si':
			print('No es obligatorio votar')
		elif respuesta == 'no':
			print('Tienes que ir a votar')
		else:
			print('Error en tu respuesta')

else:
	print('No puedes votar')

	if edad < 12:
		print('Eres un niño')
	else:
		print('Todavia te faltan algunos años')
	
print('Gracias!')
print('FIN')