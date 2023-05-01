# -*- coding: utf-8 -*-
# Pequenas resistencias caja de conexiones

from numpy import *
from matplotlib.pyplot import *
from math import *

Intensidad = array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4])

def ResContactos(Rt,Rc,sRt,sRc):    #Rt es la resistencia total y Rc solo la del cable
    Rcontactos = (Rt-Rc)/2
    IncRcontactos = sqrt(sRt**2+sRc**2)/2
    return [Rcontactos,IncRcontactos]

def regresionSimpleSenTermoIndependente(x,y):
    """Axusta os datos dos vectore x e y a unha resta dada pola ec. y= bx
    Parametros:
    x vector con medidas da magnitud x
    y vector con medidas da magnitud y
    Devolve:
    b coeficiente b
    sb incerteza de b
    r coeficiente de regresion lineal """
    n=len(x)
    xy=dot(x,y); xx=dot(x,x); xy=dot(x,y); yy=dot(y,y)
    b=xy/xx
    s=sqrt(sum((y-b*x)**2)/(n-1))
    sb=s/sqrt(xx)
    r=xy/sqrt(xx*yy)
    print('b = ',b)
    print('s(b) =',sb)
    print('r = ',r)
    print('s = ',s)
    return [b,sb]


# Cable de 100 mm

"""Vc1 = array([2.1,3.9,5.7,7.5,9.3,11.3,13.4,15,16.9,18.5,20.4,21.9,23.6,26,27.6,29.6,31.1,33,35.3,36.1])

ceroresidual = zeros(20)+0.4

Vc1 = Vc1-ceroresidual

Vc1 = Vc1/1000  #Pasamos de mV a V

print('Datos del cable de 100 mm')
Rc1 = regresionSimpleSenTermoIndependente(Intensidad,Vc1)"""




#Cable de 100 mm + placa

"""Vt1 = array([4.6,9,13.3,17.6,21.9,26.3,30.5,35.2,39.4,43.7,48,52.3,56.6,60.9,64.8,69.1,73.4,77.7,81.9,86.2])

Vt1 = Vt1 - ceroresidual

Vt1 = Vt1/1000

print('Datos del cable de 100 mm y la placa')
Rt1 = regresionSimpleSenTermoIndependente(Intensidad,Vt1)"""


#Plot de las dos graficas (Función)


def plotRegresión(IntensidadT,IntensidadC,VTotal,Vcable,RectaT,RectaC,longitud):
    figure(figsize=(9,4.5))

    subplot(121)
    plot(IntensidadC,Vcable*1000,'o',color='royalblue',label='Puntos experimentales')
    plot(IntensidadC,RectaC*1000,'--',color='navy',label='Recta de regresión')
    grid(True)
    xlabel('Intensidad (A)')
    ylabel('Voltaje (V)')
    legend(loc='lower right')
    title(f'Cable de {longitud}')


    subplot(122)
    plot(IntensidadT,VTotal*1000,'o',color='royalblue',label='Puntos experimentales')
    plot(IntensidadT,RectaT*1000,'--',color='navy',label='Recta de regresión')
    grid(True)
    xlabel('Intensidad (A)')
    ylabel('Voltaje (V)')
    legend(loc='lower right')
    title(f'Cable de {longitud} y caja de conexiones')

    suptitle(f'Representación gráfica de los datos del cable de {longitud}')
    show()

#Plot de las gráficas del primer cable:

l1 = '100 mm'

"""RectaT1 = Intensidad*Total1[0]
RectaC1 = Intensidad*Cable1[0]

plotRegresión(Intensidad,Intensidad,Vt1,Vc1,RectaT1,RectaC1,l1)


#Cálculo de la resistencia entre contactos cable 1

ResCable1 = ResContactos(Total1[0],Cable1[0],Total1[1],Cable1[1])

print('Resistencia entre contactos cable 1 = ',ResCable1[0])
print('Incertidumbre resistencia entre contactos cable 1 = ',ResCable1[1])"""



###########Cable de 600 mm##############

"""l2 = '600 mm'

Vc2 = array([4.2, 8.5, 12.8, 17.1, 21.4, 25.8, 30.1, 34.4, 38.7, 43, 47.4, 51.7, 56.1, 60.4, 64.8, 69.2, 73.6, 77.9, 82.4, 86.8])
Vt2 = array([11.4, 22.8, 34, 45.4, 56.7, 68.1, 79.4, 90.7, 102, 113.3, 124.5, 135.6, 146.7, 157.9, 169.1, 180.3, 191.4])

IntensidadVt2 = array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4])

print('Datos del cable de 600 mm')
Rc2 = regresionSimpleSenTermoIndependente(Intensidad,Vc2/1000) # Hay que pasar a mV

RectaC2 = Rc2[0]*Intensidad

print('Datos del cable de 600 mm y la placa')
Rt2 = regresionSimpleSenTermoIndependente(IntensidadVt2,Vt2/1000)
RectaT2 = Rt2[0] * IntensidadVt2

plotRegresión(IntensidadVt2,Intensidad,Vt2/1000,Vc2/1000,RectaT2,RectaC2,l2)

Rtotal2 = ResContactos(Rt2[0],Rc2[0],Rt2[1],Rt2[1])

print('Resistencia entre contactos del cable de 600 mm = ',Rtotal2[0])
print('Incertidumbre de la resistencia entre contactos del cable de 600 mm = ',Rtotal2[1])"""



######### Cable de 2000 mm ###############

l3 = '2000 mm'

Vc3 = array([0.029, 0.061, 0.093, 0.127, 0.163, 0.196, 0.233,0.267, 0.302, 0.337, 0.372, 0.407, 0.452, 0.489, 0.525, 0.57])
Vt3 = array([0.064, 0.131, 0.194, 0.253, 0.315, 0.356, 0.4,0.423, 0.465, 0.508, 0.532, 0.57, 0.602, 0.623, 0.664])

IntensidadVc3 = array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2])
IntensidadVt3 = array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3])

print('Datos del cable de 2000 mm:')

Rc3 = regresionSimpleSenTermoIndependente(IntensidadVc3,Vc3)  #Ahora ya no hay que dividir entre 1000 por que ya estan en voltios los datos

RectaC3 = IntensidadVc3*Rc3[0]

print(f'Datos del cable de {l3} y la placa:')

Rt3 = regresionSimpleSenTermoIndependente(IntensidadVt3,Vt3)

RectaT3 = IntensidadVt3*Rt3[0]

plotRegresión(IntensidadVt3,IntensidadVc3,Vt3/1000,Vc3/1000,RectaT3/1000,RectaC3/1000,l3)

Rtotal3 = ResContactos(Rt3[0],Rc3[0],Rt3[1],Rt3[1])

print('Resistencia entre contactos del cable de 2000 mm = ',Rtotal3[0])
print('Incertidumbre de la resistencia entre contactos del cable de 22000 mm = ',Rtotal3[1])