#!/usr/bin/env python
# -*- coding: utf-8 -*-

def funcion1(x):
	resultado = x * 10
	return resultado

def funcion2(x):
	resultado = x % 3
	return resultado


while True:
	operacion = input('Ingrese la operacion [multiplicar/modulo]: ')
	if operacion == 'STOP' or operacion == '0':
		break
	
	valor = int(input('Ingrese el numero a operar: '))

	if operacion == 'multiplicar':
		print(funcion1(valor))

	elif operacion == 'modulo':
		print(funcion2(valor))
print('FIN')