# -*- coding: utf-8 -*-

import sympy as sp
sp.init_printing()

Wc = 1000 # Salario acordado en el contrato de trabajo por hora > 0
Lc = 15 # Horas acordadas de trabajo dentro del contrato > 0
M = 10 # ingreso extra laboral > 0
T = 60 # horas laborables  >= 0 y >Lc
phi = 0.3  # ni idea
N = 500 # Cantidad de billetes disponibles > 0
b = 2 # Precio de 1 billete > 0

VE = (sp.log(Wc * Lc + M)+(phi*(T-Lc))) - (sp.log(M)+ (phi* T))
sp.pprint(VE)
    
if VE >= 0:
    print('agente trabaja')
          
    GC = (1/N) * (sp.log(M + b * (N-1)) + (phi * T)) * (sp.log((Wc*Lc)+ M-b) + (+phi*(T-Lc)))-(sp.log(Wc*Lc+ M)+phi*(T-Lc))
    sp.pprint(f'GC={GC}={sp.solveset(GC)}')

        
    if GC >= 0:
        print('compra ticket') 
        QJ = (sp.log(M+ b * (N-1))+ (phi* T))-(sp.log(Wc * Lc + M + b*(N-1))+(phi*(T-Lc)))
        sp.pprint(QJ)
        
        if QJ >= 0:
            print('deja el trabajo')
        else: 
            print('no deja el trabajo')
    else:
        print('no compra boleto de lotería')
       

else:
    print('no lo vale')
  

x, y, t = sp.symbols('x, y, t')
utilidad = sp.log(x)+ phi* y
renta = Wc*Lc+M

Lagrange = utilidad + t *(renta) 
        
        
        # derivo en función de cada variable 
dx = Lagrange.diff(x)        
dy = Lagrange.diff(y) 
dt = Lagrange.diff(t)  
dx
dy
dt   
        
