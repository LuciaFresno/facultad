"""
1.4. Pedro es un consumidor cuyas preferencias están representadas por la Tasa Marginal de Sustitución 𝑇𝑀𝑆 = 2𝑦/x  . Si los precios son 𝑃x = 3 y 𝑃y =1, y tiene un ingreso de $ 180, ¿cuál es la canasta de bienes que maximiza su utilidad?

"""
# -*- coding: utf-8 -*-


import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')

Presupuesto = m - px*x - py*y
TMS = 2y/x

im =  180
ipx = 3
ipy = 1


