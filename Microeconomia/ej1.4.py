"""
1.4. Pedro es un consumidor cuyas preferencias están representadas por la Tasa Marginal de Sustitución 𝑇𝑀𝑆 = 2𝑦/x  . Si los precios son 𝑃x = 3 y 𝑃y =1, y tiene un ingreso de $ 180, 
¿cuál es la canasta de bienes que maximiza su utilidad?

"""
# -*- coding: utf-8 -*-


import sympy as sp
sp.init_printing()
import funcionesAuxiliares as aux


m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')

Presupuesto = m - px*x - py*y
TMS = 2y/x
# RMS o TMS Si en la representación de las curvas de indiferencia y de la relación marginal de sustitución, el bien 1 representa el consumo de "todos los demás bienes" y se mide en la cantidad de $ que podemos gastar en ellos, la relación marginal de sustitución se entendería como la cantidad que el consumidor está dispuesto a pagar por una unidad adicional del bien 2. (Costo de oportunidad)
# la pendiente de la curva de indiferencia, la relación marginal de sustitución mide la relación en la que al consumidor le es igual intercambiar o no los dos bienes. Con cualquier otra relación de intercambio que no sea la relación marginal de sustitución, deseará intercambiar un bien por el otro. Pero si la relación de intercambio es idéntica a la relación marginal de sustitución, deseará permanecer en el mismo punto.


im =  180
ipx = 3
ipy = 1


def canastaOptima(TMS, 
                  Presupuesto , 
                  im , 
                  ipx , 
                  ipy):
    # TMS(x,y) = sp.Eq((dy/dx), (UMgx/UMgy)) 
    # 
    pass

canastaOptima(TMS, Presupuesto , im , ipx , ipy)


