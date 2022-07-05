#!/usr/bin/env python
# -*- coding: utf-8 -*-



for numero in [2, 4, 6, 8, 13, 18]:
	print(numero, end = '\t')
	print(numero**2)

	if numero % 3 == 0:
		print(numero, 'es divisible entre 3')


print('FIN')