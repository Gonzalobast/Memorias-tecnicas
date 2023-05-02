from numpy import *
from matplotlib.pyplot import *
from math import *

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
    print('s(b) =',b)
    print('r = ',r)
    print('s = ',s)
    return [b, sb, r, s]



#Cálculo de la constante del resorte

def Gradosradianes(angulo):
    angulorad = angulo*(pi/180)
    return angulorad

angulo = array([90,100,105,115,120,130,145,160,165,180]) #Ne grados, hay que pasarlo a radianes!!!!!!!!!!!

print(f'Ángulos en radianes: {around(Gradosradianes(angulo),decimals=3)}')

IncAngulo = 5 #Grados

fuerza = array([0.19,0.23,0.24,0.25,0.27,0.29,0.31,0.33,0.34,0.4]) #newtons

#Momento de las fuerzas

Momento = (14.95/100)*fuerza 

print(f'Momento de las fuerzas: {Momento}')

incFuerza = 0.01 #Newton

constante = regresionSimpleSenTermoIndependente(fuerza,angulo)

print(constante[2])

#plot(fuerza,angulo,'o')

#Disco

masaDisco = 381.39

DiamDisco = 29.9

IncMasa = 0.01

disco = array([1.429,1.441,1.446,1.449,1.446,1.445,1.441,1.431,1.425,1.424,1.417,1.415,1.406,1.406,1.428]) #Medidas del semiperiodo del disco (s

IncDisco = 0.001 #Segundos

print(len(disco))


#Esfera

masaEsfera = 659.23

esferaSemiT = array([0.727,0.726,0.727,0.727,0.726,0.728,0.727,0.729,0.729,0,730,0,729,0.729,0.728])

print(len(esferaSemiT))

DiamEsfera = 13.8 #centimetros

IncD = 0.001 #metros

###### Cilindro
masaCilindro=384,29

DiamCil = 10

semiTcil = array([0.436,0.436,0.435,0.431,0.429,0.432,0.436,0.438,0.435,0.435,0.433,0.433,0.437,0.435,0.435,0.435])



############## Teorema de Steiner #############

#Disco con las diferentes posiciones

d1 = 3 # cm

Datosd1 = array([1.475,1.477,1.479,1.481,1.479,1.481,1.485,1.481,1.484,1.479,1.483,1.486,1.486,1.487,1.484])  #Semiperiodo del disco con d = 3cm

print(len(Datosd1))

d2 = 6

Datosd2 = array([1.685,1.687,1.691,1.692,1.692,1.659,1.680,1.678,1.679,1.684,1.688,1.693,1.686,1.679,1.672])

print(len(Datosd2))


d3 = 9

Datosd3 = array([1.928,1.954,1.925,1.956,1.958,1.948,1.937,1.910,1.916,1.917,1.940,1.954,1.943,1.942,1.946])

d4 = 12

Datosd4 = array([2.396,2,414,2.401,2.463,2.376,2.395,2.436,2.463,2.439,2.444,2.470,2.493,2.474,2.491,2.483])



# Barra

#Datos del centro de masas
#cada distancia varía en un cm
longitudbarra=0.657
semiTCM = array([1.565,1.630,1.627,1.635,1.636,1.636,1.634,1.633,1.635,1.638,1.632,1.633,1.632,1.634,1.638])
semiT1 = array([1.628,1.630,1.627,1.635,1.636,1.636,1.634,1.633,1.635,1.638,1.632,1.633,1.632,1.634,1.638])
semiT2 = array([1.670,1.671,1.673,1.680,1.676,1.673,1.669,1.676,1.677,1.687,1.691,1.701,1.684,1.683,1.675])
semiT3 = array([1.777,1.763,1.755,1.756,1.775,1.778,1.801,1.793,1.800,1.794,1.800,1.790,1.807,1.803,1.791])
semiT4 = array([1.824,1.849,1.824,1.825,1.834,1.836,1.857,1.876,1.882,1.868,1.836,1.835,1.889,1.891,1.876])
semiT5 = array([])
semiT6 = array([])
semiT7 = array([])
semiT8= array([])
semiT9 = array([])
semiT10 = array([])



semiTCM = array([1.595,1.596,1.595,1.600,1.595,1.596,1.561,])
semiT1 = array([1.606,1.606,1.606,1.607])
semiT2 = array([1.625,1.633,1.627,1.629,1.632])
semiT3 = array([1.649,1.643,1.648,1.651,1.646,1.661])
semiT4 = array([1.689,1.686,1.677,1.685,1.671])
semiT5 = array([1.681,1,688,1.1681,1.682,1.680])
semiT6 = array([1.697,1.710,1.703,1.700,1.703])
semiT7 = array([1.738,1.732,1.738,1.732,1.729,1.724])
semiT8= array([1.772,1.785,1.782,1.781,1.777])
semiT9 = array([1.826,1.829,1.833,1.831,1.825])
semiT10 = array([1.866,1.871,1.876,1.879,.870])