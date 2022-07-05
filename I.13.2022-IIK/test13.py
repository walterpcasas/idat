#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Muestren todos los numeros multiplos de 6 
que sean mayores que 1 y menores que 100
'''

n = 1

while n < (100/6):
	print(n*6)
	n += 1

print('FIN')

########################

m = 1

while m < 100:
	if m % 6 == 0:
		print(m)
	m+=1
print('FIN')