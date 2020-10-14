# -*- coding: utf-8 -*-
def maximizarRestriccion(FuncObjetivo, SujetoA, im, ipx, ipy):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t , xoptimo, yoptimo = sp.symbols('m, x, y, px, py, t, xoptimo, yoptimo')

    # armo el lagrangiano
    Lagrange = FuncObjetivo + t *(SujetoA) 
    
    
    # derivo en función de cada variable 
    dx = Lagrange.diff(x)        
    dy = Lagrange.diff(y) 
    dt = Lagrange.diff(t) 
    
    
    # igualo a cero dx y dy y las dx y dy como funciones de t
    t1 = sp.solve(dx, t) 
    t2 = sp.solve(dy, t) 
       
    # igualo los resultados
    ig = sp.Eq(t1[0], t2[0])
    # verificarC1O(ig)
        
    # despejo la igualdad en función de x y de y para encontrar x e y óptimos
    xstar = sp.solve(ig, x)[0] 
    
    # reemplazo xstar en dt para encontrar el y óptimo
    yoptimo = dt.subs(x, xstar) 
    
    # igualo a cero y pongo dt en función de y
    yoptimo = sp.solve(yoptimo, y)[0] 
    
    # otorgo valores para averiguar el valor de y en el punto de optimización
    yoptimo = yoptimo.subs({'px': ipx, 'py': ipy , 'm': im})
    
    
    
    
    ystar = sp.solve(ig, y)[0] 
    if ystar == 0: # TODO: entender por qué a veces ystar da 0
        xoptimo = dt.subs({'y': yoptimo})
    else:        
        # reemplazo xstar en dt para encontrar el x óptimo
        xoptimo = dt.subs(y, ystar)  
    
    # igualo a cero y pongo dt en función de y
    xoptimo = sp.solve(xoptimo, x)[0]  
    
    # otorgo valores para averiguar el valor de y en el punto de optimización
    xoptimo = xoptimo.subs({'px': ipx, 'py': ipy , 'm': im})
    
    
    return ({'Formula Lagrange': Lagrange, 
             'Lx': dx, 
             'Ly':  dy, 
             'Lt': dt, 
             'igualdad': ig, 
             'xstar': xstar,  
             'ystar': ystar, 
             'xoptimo': float(xoptimo),
             'yoptimo': float(yoptimo)})

# grafico las dos formulas 
def graficarRestriccion(FuncObjetivo, SujetoA, im, ipx, ipy):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
    from sympy.plotting import plot3d
    
    limx = im / ipx 
    limy = im / ipy 
    
    SAGraficable = sp.solve(SujetoA, 'm')[0] 
    SAGraficable = SAGraficable.subs({'px' : ipx , 'py' : ipy}) 
    
    
    p1 = plot3d(FuncObjetivo,(x, 0, limx), (y,0,limy), show=False)
    p2 = plot3d(SAGraficable, show=False)
    # TODO: cambio de color una de las dos para diferenciarlas 
    
    p1.append(p2[0])
    p1
    p1.show() # TODO: me gustaría poder rotar el gráfico para que sea vea bien el punto en que se intersecan
    


def verificarC1O(igualdad):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
    
    # evalúo condicion de primer orden 
    # Muestra en que punto, la tasa a la que el mercado intercambia un bien por otro es igual a la tasa a la que el consumidor lo hace. Muestra en que punto  e encuentra la cesta de bienes que maximiza la utilidad del consumidor ya que gasta toda su renta
    # La condición de optimalidad indica que la tasa a la que el individuo intercambia un bien por otro es igual a la tasa a la que el mercado lo hace, esto no tiene nada que ver con el valor de la renta que percibe
    
    sp.pprint(f'Igualdad para verificar la 1er cond de optimalidad: {igualdad}')
    ig = sp.solve(igualdad, y)[0]
    sp.pprint(f"ig: {ig}")
    C1O = False    
    if ig == px*x/y: # TODO: arreglar esto , algo no está evaluando bien
        C1O = True
    
    sp.pprint(C1O)
    return ({'C1O': C1O})
    
    
    
    
# =============================================================================
#     # TODO: evalúo condición de segundo orden
#     # https://stackoverflow.com/questions/26798615/determinant-using-sympy
#     C2O = True
#     
#     # TODO: evalúo la relación entre los bienes x e y 
#     relacion = 'normal'
#     
#     
# =============================================================================