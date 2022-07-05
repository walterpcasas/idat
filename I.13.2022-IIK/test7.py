#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = 0

while edad < 18:
	edad = int(input('Ingresar edad:\n'))

	if edad < 18:
		print('No puedes votar, siguiente')
		#break
	else:
		print('Puedes votar')

print('FIN')