# -*- coding: utf-8 -*-

"""
1.- Maximización de la Utilidad
1.1. Se sabe que la función de utilidad de un individuo es 𝑈(𝑥, 𝑦) = 𝑥. 𝑦 y que los precios
de los bienes 𝑥 e 𝑦 son $2 y $5 respectivamente. Asimismo, el individuo cuenta con una
renta disponible de $100. Calcule con estos datos las cantidades que debería consumir de
cada uno de los bienes de manera de maximizar su utilidad. 
"""


import sympy as sp
from sympy.plotting import plot3d

sp.init_printing()


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
SujetoA = m - px*x - py*y
FuncObjetivo = x*y

m = 100
px = 2
py = 5



# armo el lagrangiano
Lagrange = FuncObjetivo + t *(SujetoA) # t⋅(m - px⋅x - py⋅y) + x⋅y

# derivo en función de cada variable 
dx = Lagrange.diff(x) # -px⋅t + y
dy = Lagrange.diff(y) # -py⋅t + x
dt = Lagrange.diff(t) # m - px⋅x - py⋅y

# igualo a cero dx y dy y las dx y dy como funciones de t
t1 = sp.solve(dx, t) # [ y / px ]
t2 = sp.solve(dy, t) # [ x / py ]

# igualo los resultados
ig = sp.Eq(t1[0], t2[0]) # y / px = x / py


# despejo la igualdad en función de x y de y para encontrar x e y óptimos
xstar = sp.solve(ig, x)[0] # xstar = ￼￼￼py * y / px
ystar = sp.solve(ig, y)[0] # ystar = px * x / py

# evalúo condicion de primer orden 
# Muestra en que punto, la tasa a la que el mercado intercambia un bien por otro es igual a la tasa a la que el consumidor lo hace. Muestra en que punto  e encuentra la cesta de bienes que maximiza la utilidad del consumidor ya que gasta toda su renta
# La condición de optimalidad indica que la tasa a la que el individuo intercambia un bien por otro es igual a la tasa a la que el mercado lo hace, esto no tiene nada que ver con el valor de la renta que percibe

# u'x / u'y == px / py
C1O = False

if ( ystar / x ) == ( px / py ):
    C1O = True



# evalúo condición de segundo orden
# https://stackoverflow.com/questions/26798615/determinant-using-sympy


# evalúo la relación entre los bienes x e y 





# reemplazo xstar en dt para encontrar el y óptimo
yoptimo = dt.subs(x, xstar)  # ￼m - 2 * py * y


# igualo a cero y pongo dt en función de y
yoptimo = sp.solve(yoptimo, y)[0] # [￼m / 2 * py]

# otorgo valores para averiguar el valor de y en el punto de optimización
yoptimo = yoptimo.subs({'px': px, 'py': py , 'm': m})
yoptimo

# grafico las dos formulas 


limx = m/px # 50.0
limy = m/py # 20.0

SAGraficable = sp.solve(SujetoA, 'm')[0] # px * x + py * y
SAGraficable = SAGraficable.subs({'px' : px , 'py' : py}) # 2*x + 5*y


p1 = plot3d(FuncObjetivo,(x, 0, limx), (y,0,limy), show=False)
p2 = plot3d(SAGraficable, show=False)
p1.append(p2[0])
p1
p1.show() # me gustaría poder rotar el gráfico para que sea vea bien el punto en que se intersecan

