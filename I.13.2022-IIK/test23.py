#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ordenar de manera ascendente [1, 7, 5, 3, 6]


grupo = [1, 7, 5, 3, 6]
ordenado = False

while not ordenado:
	ordenado = True

	for i in range(len(grupo)-1):
		
		if grupo[i] > grupo[i+1]:
			grupo[i], grupo[i+1] = grupo[i+1], grupo[i]
			ordenado = False

print(grupo)