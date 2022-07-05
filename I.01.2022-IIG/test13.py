#!/usr/bin/env python
# -*- coding: utf-8 -*-

for nota in [12, 11, 10, 9, 16, 14]:

	print('Tu nota es:', nota)

	if nota > 12:
		print('Estás APROBADO')
		break
	elif nota == 12:
		print('Necesitas preocuparte') 
	else:
		print('Estás DESAPROBADO')

print('FIN')