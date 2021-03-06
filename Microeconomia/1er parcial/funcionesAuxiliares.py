# -*- coding: utf-8 -*-
def maximizarRestriccion(funcObjetivo, sujetoA, im = '', ipx = '', ipy = ''):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t , xoptimo, yoptimo = sp.symbols('m, x, y, px, py, t, xoptimo, yoptimo')
    #Precios relativos : Tasa a la cual el mercado te exige intercambiar un bien por otro
    if ipy and ipx:
        preciosRelativos = sp.Rational( ( -ipx ), ipy )
    else:
        preciosRelativos = -px/py
    
    cumpleC1O(funcObjetivo, px, py)
    
    # armo el lagrangiano
    Lagrange = funcObjetivo + t *(sujetoA) 
    
    
    # derivo en función de cada variable 
    dx = Lagrange.diff(x)        
    dy = Lagrange.diff(y) 
    dt = Lagrange.diff(t)     
    
    # igualo a cero dx y dy y las dx y dy como funciones de t
    t1 = sp.solve(dx, t) 
    t2 = sp.solve(dy, t)   
       
    # igualo los resultados
    ig = sp.Eq(t1[0] , t2[0])
    
    sp.pprint(f"ig: {ig}") # ¿Por qué a veces la formula esta en primer posición (1.1) ig[0] y otras veces (1.2) está en la segunda posicion de ig[1]
    
    
        
    # despejo la igualdad en función de x y de y para encontrar x e y óptimos
    ystar = sp.solve(ig, y)[0]
    if ystar == 0:
        ystar = sp.solve(ig, y)[1]
    xstar = sp.solve(ig, x)[0]
    
    
    # reemplazo xstar en dt para encontrar el y óptimo
    yoptimo = dt.subs(x, xstar)
    
    # igualo a cero y pongo dt en función de y
    yoptimo = sp.solve(yoptimo, y) 

    # otorgo valores para averiguar el valor de y en el punto de optimización
    yoptimo = yoptimo[0].subs({'px': ipx, 'py': ipy , 'm': im})


    # reemplazo xstar en dt para encontrar el x óptimo
    xoptimo = dt.subs({'y': ystar})  
     
    # igualo a cero y pongo dt en función de x
    xoptimo = sp.solve(xoptimo, x)
    
    # otorgo valores para averiguar el valor de x en el punto de optimización
    xoptimo = xoptimo[0].subs({'px': ipx, 'py': ipy , 'm': im})
    
    
    return ({'Precios relativos': preciosRelativos,
             'Formula Lagrange': Lagrange, 
             'Lx': dx, 
             'Ly': dy, 
             'Lt': dt, 
             'igualdad': ig, 
             'xstar': xstar,  
             'ystar': ystar, 
             'xoptimo': float(xoptimo),
             'yoptimo': float(yoptimo)   })


def cumpleC1O(funcObjetivo, px, py):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
    if funcObjetivo.diff(x)/funcObjetivo.diff(y) == px/py:
        C1O = True
    else:
        C1O = False
        
    sp.pprint(funcObjetivo.diff(x)/funcObjetivo(y))
    
    # evalúo condicion de primer orden 
    # Muestra en que punto, la tasa a la que el mercado intercambia un bien por otro es igual a la tasa a la que el consumidor lo hace. Muestra en que punto  e encuentra la cesta de bienes que maximiza la utilidad del consumidor ya que gasta toda su renta
    # La condición de optimalidad indica que la tasa a la que el individuo intercambia un bien por otro es igual a la tasa a la que el mercado lo hace, esto no tiene nada que ver con el valor de la renta que percibe
    
    return C1O