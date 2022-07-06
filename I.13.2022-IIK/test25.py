#!/usr/bin/env python
# -*- coding: utf-8 -*-


grupo = ['hola', 2, 3.14, False]

print(len(grupo))

print(grupo.index(3.14))

print(grupo)
grupo.append('FIN')
print(grupo)

grupo.insert(1, True)
print(grupo)

grupo.remove('hola')
print(grupo)

numeros = [2, 5, 7, 1]
numeros.sort()
print(numeros)