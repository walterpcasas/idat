#!/usr/bin/env python
# -*- coding: utf-8 -*-

lado = int(input("Ingrese el numero: "))

while 1:
	if lado == 2:
		print("**\n**")

	elif lado == 4:
		print("****")
		print("****")
		print("****")
		print("****")

	elif lado == 6:
		print("******")
		print("******")
		print("******")
		print("******")
		print("******")
		print("******")

	elif lado == 0:
		break

	lado = int(input("Ingrese el numero: "))

print("FIN")