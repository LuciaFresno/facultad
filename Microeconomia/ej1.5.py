# -*- coding: utf-8 -*-

"""

1.5. La renta de un consumidor es de $2.500 por mes. Esta renta la gasta íntegramente en alimento (𝑥) y vestido (𝑦), cuyos precios son, respectivamente, 𝑃x=5 y 𝑃y=10
"""
im = 2500
ipx = 5
ipy = 10
isx = 2
itr = 500


import sympy as sp
sp.init_printing()


m, x, y, px, py, sx, tr = sp.symbols('m, x, y, px, py, sx, tr')

presupuesto = m - px*x - py*y
presupuesto = sp.solve(presupuesto, y)[0].subs({'m':im, 'px': ipx, 'py': ipy})
"""
a) Exprese y grafique la restricción presupuestaria de este consumidor e indique cuál es
su conjunto presupuestario.

"""
ej15 = sp.plot(show = False)

ej15a = sp.plot(presupuesto,
                (x, 0 , im/(ipx-isx)),
                show = False)
ej15.append(ej15a[0])

""" 
b) Analice gráficamente y comente el efecto sobre la restricción presupuestaria de las siguientes medidas de intervención alternativas: i. Subvencionar el precio de los alimentos por unidad consumida. 
"""


presupuestoPreciodeAlimentosSubvencionado = m - (px-sx)*x - py*y

presupuestoPreciodeAlimentosSubvencionado = sp.solve(presupuestoPreciodeAlimentosSubvencionado, y)[0].subs({'m':im, 'px': ipx, 'py': ipy, 'sx': isx})
ej15bi = sp.plot(presupuestoPreciodeAlimentosSubvencionado,
                 (x, 0 , im/(ipx-isx)),
                line_color = 'red',
                label = 'presupuestoPreciodeAlimentosSubvencionado',                 
                show = False
                )
ej15.append(ej15bi[0])


"""
ii. Conceder gratuitamente cupones para adquirir una cierta cantidad de unidades de
alimentos.
"""
cantidadDeAlimentosGratis = 150
presupuestoAlimentosGratis = m - px * x - py * y
presupuestoAlimentosGratis = sp.solve(presupuestoAlimentosGratis, y)[0].subs({'m':im, 'px': 0, 'py': ipy})
ej15biia = sp.plot(presupuestoAlimentosGratis, 
                  (x, 0, cantidadDeAlimentosGratis),
                  line_color = 'magenta',
                  show = False
                  )

ej15.append(ej15biia[0])


presupuestoAlgunosAlimentosGratis = m - px * x - py * y + px * cantidadDeAlimentosGratis


presupuestoAlgunosAlimentosGratis = sp.solve(presupuestoAlgunosAlimentosGratis, y)[0].subs({'m':im, 'px': ipx, 'py': ipy})
ej15biib = sp.plot(presupuestoAlgunosAlimentosGratis, 
                  (x, cantidadDeAlimentosGratis, im/(ipx-isx)),
                  line_color = 'magenta',
                  show = False)

ej15.append(ej15biib[0])



"""
iii. Dar al individuo una transferencia directa. 
"""

presupuestoTransferenciaDirecta = m + tr - px*x - py*y

presupuestoTransferenciaDirecta = sp.solve(presupuestoTransferenciaDirecta, y)[0].subs({'m':im, 'px': ipx, 'py': ipy, 'tr': 500})
ej15biii = sp.plot(presupuestoTransferenciaDirecta,   
                   (x, 0 , im/(ipx-isx)),
                line_color = 'green',
                label = 'presupuestoTransferenciaDirecta', 
                show = False
                )
ej15.append(ej15biii[0])

ej15.show()