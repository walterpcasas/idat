#!/usr/bin/env python
# -*- coding: utf-8 -*-


N = int(input('Ingrese N: '))

while N > 0:

	numero = int(input('Ingrese numero: '))
	if numero % 2 == 0:
		print(numero, 'es PAR')
	else:
		print(numero, 'es IMPAR')

	N -= 1

print('FIN')