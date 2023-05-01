# Práctica pequeñas resistencias

from numpy import *
from matplotlib.pyplot import *
from math import *

#Fórmula resistividad

def resistividad(R,radio,L,sR):
    S = pi*(radio**2)
    res = R*S/L
    
    sRegla = 0.0005
    sS = 2*pi*radio*(sRegla/2)
    
    
    IncRes = sqrt(((S/L)**2)*(sR**2)  +  (((R*S)/(L**2))**2)*(sRegla**2) + ((R/L)**2)*(sS**2))
    
    return [res,IncRes,sS]



#Resistividad del cobre

amplificación = 100

r = 1.25 #cm
r = r/100 #Pasamos a m

L = 0.325 #Distancia entre contactos en metros

Intensidad = array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4])

Vcu = array([0.5, 0.7, 0.9, 1.3, 1.5, 1.6, 1.8, 2, 2.3, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4.1, 4.3, 4.6, 4.8])

Vcu = Vcu/100000 #Pasamos a voltios de mV y quitamos la amplificación

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
    return [b, sb, r, s]

"""cobre = regresionSimpleSenTermoIndependente(Intensidad, Vcu)

print('Datos del cobre')
print('b = ',cobre[0])
print('sb = ', cobre[1])
print('r = ',cobre[2])
print('s = ',cobre[3])

RectaCu = Intensidad*cobre[0]

plot(Intensidad,Vcu*1000,'o',color='royalblue',label='Puntos experimentales')
plot(Intensidad,RectaCu*1000,'--',color='navy',label='Recta de regresión')
xlabel('Intensidad (A)')
ylabel('Voltaje (mV)')
title('Barra de cobre')
grid(True)
legend(loc='lower right')

ResCobre = resistividad(cobre[0],r,L,cobre[1])

print('Resistividad del cobre = ',ResCobre[0])
print('Incertidumbre de la resistividad del cobre = ',ResCobre[1])
print('Incertidumbre de la sección = ',ResCobre[2])"""


# Resistividad del aluminio

VAl = array([0.2, 0.5, 1, 1.5, 1.7, 2, 2.3, 2.8, 3.1, 3.5, 3.9, 4.1, 4.5, 4.8, 5.1, 5.4, 5.8, 6.1, 6.5, 6.9])

VAl = VAl/100000 #Pasamos a voltios y quitamos el efecto de la amplificación

aluminio = regresionSimpleSenTermoIndependente(Intensidad, VAl)

print('Datos del aluminio')
print('b = ',aluminio[0])
print('sb = ', aluminio[1])
print('r = ',aluminio[2])
print('s = ',aluminio[3])

RectaAl = Intensidad*aluminio[0]

clf()

plot(Intensidad,VAl*1000,'o',color='royalblue',label='Puntos experimentales')
plot(Intensidad,RectaAl*1000,'--',color='b',label='Recta de regresión')
xlabel('Intensidad (A)')
ylabel('Voltaje (mV)')
title('Barra de aluminio')
grid(True)
legend(loc='lower right')
show()

ResAluminio = resistividad(aluminio[0],r,L,aluminio[1])

print('Resistividad del aluminio = ',ResAluminio[0])
print('Incertidumbre de la resistividad del aluminio = ',ResAluminio[1])
