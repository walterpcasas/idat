#!/usr/bin/env python
# -*- coding: utf-8 -*-

valor1 = 0
valor2 = 10

while valor2 > 3 and valor1 < 7:
	print(valor1," ", valor2)
	valor1 +=1
	valor2 -=2


print("------")

valor1 = 0
valor2 = 10

while valor2 > 3 or valor1 < 7:
	print(valor1," ", valor2)
	valor1 +=1
	valor2 -=2