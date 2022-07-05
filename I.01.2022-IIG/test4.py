#!/usr/bin/env python
# -*- coding: utf-8 -*-

edad = int(input('Ingrese su edad: '))

# Este bloque valida la edad
if edad >= 65:
	print('No está obligado a votar')

elif edad >= 18:
	print('Debes ir a votar')

else:
	print('No puedes votar')
	print('Gracias')

print('Gracias!')
print('FIN')