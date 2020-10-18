# -*- coding: utf-8 -*-

""" 
1.2. Las preferencias de un consumidor se resumen en la siguiente función de utilidad:
𝑈(𝑥, 𝑦) = 𝑥. 𝑦^2
 Si los precios de los bienes x e y son $10 y $30 respectivamente, se pide:
"""

import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
Presupuesto = m - px*x - py*y
Utilidad = x * (y**2)


# a) Calcular las cantidades que consumirá de cada uno de los bienes si su renta asciende a $270.
am = 270
apx = 10
apy = 30

ej12a = aux.maximizarRestriccion(Utilidad,
                         Presupuesto,
                         am,
                         apx,
                         apy )

ej12a

# b) Si su renta se incrementa en $135, ¿cuáles serían las nuevas cantidades que consumiría si desea maximizar su nivel de satisfacción?

bm = am + 135 # 405
bpx, bpy = apx, apy
ej12b = aux.maximizarRestriccion(Utilidad,
                         Presupuesto,
                         bm,
                         bpx,
                         bpy )

ej12b

# c) ¿Qué ocurriría con las cantidades consumidas si, además de incrementarse la renta en $90, se incrementaran los precios de cada uno de los bienes x e y a $15 y $45 respectivamente?


cm = am + 90
cpx = 15 # *1.5
cpy = 45 # *1.5

ej12c = aux.maximizarRestriccion(Utilidad,
                         Presupuesto,
                         cm,
                         cpx,
                         cpy )

ej12c


# d) Si el precio del bien x experimenta un alza del 50% en su valor, ¿cuáles serían las nuevas cantidades consumidas por este individuo?

dm = am
dpx = apx * 1.5
dpy = apy

ej12d = aux.maximizarRestriccion(Utilidad,
                         Presupuesto,
                         dm,
                         dpx,
                         dpy )

ej12d
