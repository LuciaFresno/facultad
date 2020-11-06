"""1.3. 
Un consumidor cuyas preferencias viene representadas por la función de utilidad 𝑈(𝑥, 𝑦) = 3𝑙𝑛 𝑥 + 𝑙𝑛 𝑦, desea maximizar la utilidad que obtiene del consumo de ambos bienes. Siendo los precios a los que se enfrenta px = py = $3  y disponiendo de unos ingresos de $120, ¿cuáles serían las cantidades óptimas a consumir? 
"""


import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
Presupuesto = m - px*x - py*y
Utilidad = 3*sp.log(x) + sp.log(y)

im = 120
ipx = ipy = 3

ej13 = aux.maximizarRestriccion(Utilidad,
                         Presupuesto,
                         im,
                         ipx,
                         ipy )

ej13