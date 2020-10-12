# -*- coding: utf-8 -*-

""" 
1.2. Las preferencias de un consumidor se resumen en la siguiente función de utilidad:
𝑈(𝑥, 𝑦) = 𝑥. 𝑦^2
 Si los precios de los bienes x e y son $10 y $30 respectivamente, se pide:
a) Calcular las cantidades que consumirá de cada uno de los bienes si su renta asciende a
$270.
b) Si su renta se incrementa en $135, ¿cuáles serían las nuevas cantidades que consumiría
si desea maximizar su nivel de satisfacción?
c) ¿Qué ocurriría con las cantidades consumidas si, además de incrementarse la renta en
$90, se incrementaran los precios de cada uno de los bienes x e y a $15 y $45
respectivamente?
d) Si el precio del bien x experimenta un alza del 50% en su valor, ¿cuáles serían las
nuevas cantidades consumidas por este individuo?
"""




import sympy as sp

sp.init_printing()


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
SujetoA = m - px*x - py*y
FuncObjetivo = x * (y**2)

m = 270
px = 10
py = 30


