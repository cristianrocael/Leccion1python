#!/usr/bin/env python
# -*- coding: utf-8 -*-
Nombre_Usuario = raw_input("ingrese nombre de Usuario: ")
Anio_Actual = input ("ingrese anio Actual: ")
Anio_de_Nacimiento = input ("ingrese año de nacimiento: ")
Edad = Anio_Actual - Anio_de_Nacimiento
print Nombre_Usuario + " Su edad es de : " + str(Edad)
if Edad <= 12:
	print Nombre_Usuario + "usted es ninio"
else:
	print Nombre_Usuario  +  " usted es adolecente"
	