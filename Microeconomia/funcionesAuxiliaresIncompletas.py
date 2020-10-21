# -*- coding: utf-8 -*-



# grafico las dos formulas 
def graficarRestriccion3d(im, ipx, ipy, sujetoA = '', funcObjetivo = ''):
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
    from sympy.plotting import plot3d
    
    limx = im / ipx 
    limy = im / ipy 
    
    saGraficable = sp.solve(sujetoA, 'm')[0] 
    saGraficable = saGraficable.subs({'px' : ipx , 'py' : ipy}) 
    
    
    p1 = plot3d(saGraficable,(x, 0, limx), (y,0,limy), show=False)
    if funcObjetivo:
        p2 = plot3d(funcObjetivo, show=False)    
        p1.append(p2[0])
        # TODO: cambio de color una de las dos para diferenciarlas 

    p1
    p1.show() # TODO: me gustaría poder rotar el gráfico para que sea vea bien el punto en que se intersecan, quizás que se vean sólo líneasen el plano X Y
    return ({ 'Corta eje Y': limy,
             'Corta eje X': limx })





def graficarRestriccion2d(im, ipx, ipy, sujetoA, funcObjetivo = ''):
    
    import sympy as sp
    sp.init_printing()
    m, x, y, px, py, t = sp.symbols('m,x,y,px,py,t')
    from sympy.plotting import plot
    
    limx = im / ipx 
    limy = im / ipy     

    saGraficable = sp.solve(sujetoA, 'm')[0] 
    saGraficable = saGraficable.subs({'px' : ipx , 'py' : ipy}) 
    
    p1 = plot(sujetoA, show = False)
    p1
    p1.show()
    
    return ({ 'Corta eje Y': limy,
             'Corta eje X': limx })
  
    



    
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