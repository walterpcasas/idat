#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 1

while x < 101:
	if x % 3 == 0 and x % 2 != 0:
		print(x)
	x += 1

print('FIN')