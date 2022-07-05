#!/usr/bin/env python
# -*- coding: utf-8 -*-


while numero > 0:

	numero = int(input('Ingrese numero: '))
	
	if numero % 2 == 0 and numero != 0:
		print(numero, 'es PAR')
	elif numero == 0:
		break
	else:
		print(numero, 'es IMPAR')


print('FIN')