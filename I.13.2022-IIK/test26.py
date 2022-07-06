#!/usr/bin/env python
# -*- coding: utf-8 -*-

grupo = []

while True:
	elemento = int(input('Ingrese valor: '))
	if elemento == 0:
		break
	else:
		grupo.append(elemento)

print(grupo)

grupo.sort()
print(grupo)

eliminar = int(input('Valor a eliminar: '))
indice = grupo.index(eliminar)
grupo.remove(eliminar)

agregar = int(input('Valor a agregar: '))
grupo.insert(indice, agregar)

print(grupo)