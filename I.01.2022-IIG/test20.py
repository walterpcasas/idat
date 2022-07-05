#!/usr/bin/env python
# -*- coding: utf-8 -*-

for numero in [2, 4, 12, 16, 149, 120, 12, 2]:

	print(numero)
	if numero % 2 == 0 and numero > 100:
		print('ALTO')
		break