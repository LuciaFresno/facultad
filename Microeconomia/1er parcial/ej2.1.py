# -*- coding: utf-8 -*-
"""
2.1. Suponiendo que las preferencias de un consumidor vengan explicadas por la función de utilidad 𝑈(𝑥, 𝑦) = 𝑥. 𝑦 se pide que 
a) derive en forma teórica las expresiones de la función de demanda de cada uno de los bienes, y que 
b) encuentre la función de demanda hicksiana a partir de la función de utilidad indirecta. 
"""

import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux
m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
presupuesto = m - px * x - py * y
utilidad = x * y

ej21a = aux.maximizarRestriccion(utilidad, presupuesto)

ej21a


