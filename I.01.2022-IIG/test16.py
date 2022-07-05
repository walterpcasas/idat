#!/usr/bin/env python
# -*- coding: utf-8 -*-

pares = 2

while pares < 100:
	print(pares)
	pares *= 2
	if pares > 10:
		print('Hasta aqui')
		break

print('FIN')