#Corriente continua
from numpy import * 
from math import *
from matplotlib.pyplot import *
from pandas import *


datos = genfromtxt('continua.csv',delimiter=';') #Array con todos los datos

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

datos[0,2]=2.60e-06

indice = datos[:,0]

R1=39*10**4

R2=22*10**4

#####Circuito simple

Vsimple = datos[:,1]
Isimple = datos[:,2] #Intensidades en A

#Cicuito serie

circserie = c_[indice,datos[:,3:7]] #Concatenar por columnas

VTserie = circserie[:,1]
V1serie = circserie[:,2]
V2serie = circserie[:,3]
Iserie = circserie[:,4]

#####Circuito en paralelo

circparalelo = c_[indice,datos[:,7:11]]

Vpar = circparalelo[:,1]
I1par = circparalelo[:,2]
I2par = circparalelo[:,3]
ITpar = circparalelo[:,4]

Isimple = Isimple*10**6 #Pasamos a microA para hacer la representación

#####Regresión lineal1

reg1 = regresionSimpleSenTermoIndependente(Isimple,Vsimple)

x1 = linspace(0,25,100)
y1 = x1*reg1[0]


plot(Isimple,Vsimple,'o',label='Datos experimentales')  #Voltaje frente a intensidad
plot(x1,y1,label='Recta de regresión')
xlabel('Intensidad de corriente ($\mu$A)')
ylabel('Voltaje(V)')
title('Voltaje frente a intensidad')
grid(True)
legend(loc='lower right')

show(False)
clf()

print('Coeficiente de regresión 1: ',reg1[2])
print('b = ',reg1[0]*10**6)  #Valor de la resistencia 1
print('s(b) = ',reg1[1])
print('s = ',reg1[3])


#Circuito en serie

Iserie = Iserie*10**6   #Pasamos a microamperios

regSerie = regresionSimpleSenTermoIndependente(Iserie,VTserie)

x2 = linspace(0,16,100)
y2 = x2*regSerie[0]

plot(Iserie,VTserie,'o',label='Datos experimentales')
plot(x2,y2,label='Recta de regresión')
xlabel('Intensidad de corriente ($\mu$A)')
ylabel('Voltaje(V)')
title('Voltaje frente a intensidad (Resistencias en serie)')
grid(True)
legend(loc='lower right')

show(False)
clf()

print('Coeficiente de regresión serie: ',regSerie[2])
print('b = ',regSerie[0]*10**6)  #Valor de la resistencia 1
print('s(b) = ',regSerie[1])
print('s = ',regSerie[3])

#Vamos a comparar los valores de V1+V2 con Vt

sumadeV = V1serie + V2serie

mediaT = mean(VTserie)  #Media del voltaje total
mediaS = mean(sumadeV)  #Media de la suma de voltajes

print('Correlación: ',mediaT/mediaS)

##Circuito en paralelo

Rpar = (R1*R2)/(R1+R2)

print('Valor de la resistencia en paralelo: ', Rpar)

ITpar = ITpar*10**6     #Pasamos a microamperios

regPar = regresionSimpleSenTermoIndependente(ITpar,Vpar)

x3 = linspace(0,72,150)
y3 = x3*regPar[0]

plot(ITpar,Vpar,'o',label='Datos experimentales')
plot(x3,y3,label='Recta de regresión')
xlabel('Intensidad de corriente ($\mu$A)')
ylabel('Voltaje(V)')
title('Voltaje frente a intensidad (Resistencias en paralelo)')
grid(True)
legend(loc='lower right')

show(False)
clf()

print('Coeficiente de regresión paralelo: ',regPar[2])
print('b = ',regPar[0]*10**6)  #Valor de la resistencia 1
print('s(b) = ',regPar[1])
print('s = ',regPar[3])

#Incertidumbre resistencia en paralelo

srpar = sqrt(((R2**2/(R1+R2)**2)**2)*(2*10**4)**2+(R1**2/(R1+R2)**2)*(1.1*10**4)**2)
print(srpar)

#Comparación de los valores de It y I1+I2

sumaI = I1par + I2par

ImediaT = mean(ITpar*10**-6)
ImediaI = mean(sumaI)

print('Correlación intensidades: ',ImediaT/ImediaI)



