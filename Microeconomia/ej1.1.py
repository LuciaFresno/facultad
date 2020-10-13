# -*- coding: utf-8 -*-

"""
1.- Maximización de la Utilidad
1.1. Se sabe que la función de utilidad de un individuo es 𝑈(𝑥, 𝑦) = 𝑥. 𝑦 y que los precios
de los bienes 𝑥 e 𝑦 son $2 y $5 respectivamente. Asimismo, el individuo cuenta con una
renta disponible de $100. Calcule con estos datos las cantidades que debería consumir de
cada uno de los bienes de manera de maximizar su utilidad. 
"""


import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
Presupuesto = m - px*x - py*y
Utilidad = x*y

ej11 = aux.maximizarRestriccion(Utilidad, 
                     Presupuesto,
                     100,
                     2,
                     5)

ej11

aux.graficarRestriccion(Utilidad,
                    Presupuesto,
                    100,
                    2,
                    5)
