#!/usr/bin/env python
# -*- coding: utf-8 -*-

lado = int(input("Ingrese el numero: "))

while lado != 0:
	texto = '*' * lado
	while lado > 0:
		print(texto)
		lado -= 1

	lado = int(input("Ingrese el numero: "))

print("FIN")