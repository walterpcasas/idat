#!/usr/bin/env python
# -*- coding: utf-8 -*-

def multiplicacion(valor):
	resultado = valor * 5
	return resultado


def modulo(valor):
	resultado = valor % 3
	return resultado


print(multiplicacion(5))
print(modulo(8))


for i in range(100):
	print(modulo(i))