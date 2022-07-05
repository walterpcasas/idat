#!/usr/bin/env python
# -*- coding: utf-8 -*-

numeroHoras = 2
numeroMinutos = 20
numeroSegundos = 15

segundosEnHora = 60 * 60
segundosEnMinuto = 60

tiempoEnSegundos = (numeroHoras * segundosEnHora +
					numeroMinutos * segundosEnMinuto +
					numeroSegundos)

print(tiempoEnSegundos)