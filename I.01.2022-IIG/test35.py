#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(5**2 + 10*5 - 5)
print(3**2 + 10*3 - 3)
print(7**2 + 10*7 - 7)
print(11**2 + 10*11 - 11)

print('-----')

x = 5
print(x**2 + 10*x - x)
x = 3
print(x**2 + 10*x - x)
x = 7
print(x**2 + 10*x - x)
x = 11
print(x**2 + 10*x - x)

print('-----')

def operacion(x):
	resultado = x**2 + 10*x - x
	return resultado

def elevar_cuadrado(x):
	cuadrado = x * x
	return cuadrado

print(operacion(5))
print(operacion(3))
print(operacion(7))
print(elevar_cuadrado(11))
