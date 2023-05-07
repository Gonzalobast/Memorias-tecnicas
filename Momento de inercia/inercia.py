import numpy as np
from matplotlib.pyplot import *
from math import *
import pandas as pd


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
    xy=np.dot(x,y); xx=np.dot(x,x); xy=np.dot(x,y); yy=np.dot(y,y)
    b=xy/xx
    s=sqrt(sum((y-b*x)**2)/(n-1))
    sb=s/sqrt(xx)
    r=xy/sqrt(xx*yy)
    print('b = ',b)
    print('s(b) =',sb)
    print('r = ',r)
    print('s = ',s)
    return [b, sb, r, s]



#Cálculo de la constante del resorte

def Gradosradianes(angulo):
    angulorad = angulo*(pi/180)
    return angulorad

angulo = np.array([90,100,105,115,120,130,145,160,165,180]) #Ne grados, hay que pasarlo a radianes!!!!!!!!!!!

print(f'Ángulos en radianes: {np.around(Gradosradianes(angulo),decimals=3)}')

IncAngulo = 5 #Grados

fuerza = np.array([0.19,0.23,0.24,0.25,0.27,0.29,0.31,0.33,0.34,0.4]) #newtons

#####Momento de las fuerzas

Momento = (14.95/100)*fuerza 

print(f'Momento de las fuerzas: {Momento}')

incFuerza = 0.01 #Newton

incMomento = np.sqrt(np.square(fuerza)*(0.0005**2) + (29.9/200)**2*incFuerza**2)
print(f'Incertidumbre de los momentos: {incMomento}')

constante = regresionSimpleSenTermoIndependente(Gradosradianes(angulo),Momento)

print(f'Valor de la constante D: {constante[0]}')

#Disco

masaDisco = 381.39/1000 #Pasamos a kg

DiamDisco = 29.9/100 #Pasamos a m

IncMasa = 0.01

MIdiscoT = (masaDisco*(DiamDisco/2)**2)/2

IncMIdiscoT = sqrt(((DiamDisco/4)**2)*(0.01/1000)**2 + ((DiamDisco/2)*(masaDisco)**2)*(0.0005**2))
print(f'El MI teórico del disco es {MIdiscoT} Incertidumbre del MI teorico del disco {IncMIdiscoT}')

disco = np.array([1.429,1.441,1.446,1.449,1.446,1.445,1.441,1.431,1.425,1.424,1.417,1.415,1.406,1.406,1.428]) #Medidas del semiperiodo del disco (s

IncDisco = 0.001 #Segundos

print(len(disco))

# Mierdas estadisticas!!!!!!


def VariasMedidas(x):   
    k = 2 #Factor de cobertura
    
    sb = 0.001
    
    media1 = np.mean(x)
    desviacion1 = np.std(x)
    n = len(x)
    
    #Vamos a crear el intervalo de confianza
    
    limInferior = media1 - k*desviacion1
    limSuperior = media1 + k*desviacion1
    
    datos=[];excluidos=[]
    
    for i in range(n):
        if ((x[i] >= limInferior) and (x[i] <= limSuperior)):
            datos.append(x[i])  #Lista con los datos filtrados
        else:
            excluidos.append(x[i])  #Lista con los datos excluidos
    
    if len(datos) == len(x):
        excluidos.append(0)
            
    media2 = np.mean(datos)    #Nuevo valor de la media
    
    sa = np.std(datos)/sqrt(len(datos)) #Incertidumbre de tipo a de la media
    
    sc = sqrt(sa**2 + sb**2)    #Incertidumbre combinada

    print(f'Datos de la muestra:')
    print(f'media inicial: {media1}')
    print(f'Desv tipica inicial: {desviacion1}')
    print(f'sb: {sb}')
    print(f'Datos excluidos: {excluidos}')
    print(f'Datos finales: {datos}')
    print(f'Media final: {media2}')
    print(f'Desv tipica final de la muestra: {np.std(datos)}')
    print(f'sa de la media {sa}')
    print(f'sc de la muestra: {sc}')
    
    return [sa,sb,sc,media2,excluidos,datos,media1,desviacion1,np.std(datos)]

def datostabla(x): # Cogemos los datos que nos interesan para la tabla
    datos = np.array([x[0],x[1],x[2],x[3],x[6],x[7],x[8]])
    return datos

#incertidumbresDisco = VariasMedidas(disco)


#### Cálculo del momento de inercia

def inercia(D,semiT):
    I = D*(semiT/pi)**2
    return I

def IncInercia(D,semiT,IncD):
    IncT = 0.001
    sI = sqrt(((semiT/pi)**4)*IncD**2 + ((2*semiT*D)/pi**2)**2*IncT**2) 
    return sI



"""InerciaDisco = (inercia(constante[0],incertidumbresDisco[3]),IncInercia(constante[0],incertidumbresDisco[3],constante[1]))
print(f'Momento de inercia del disco y inc: {InerciaDisco}')"""

#Esfera

"""masaEsfera = 659.23/1000

esferaSemiT = np.array([0.727,0.726,0.727,0.727,0.726,0.728,0.727,0.729,0.729,0.730,0.729,0.729,0.728])

print(len(esferaSemiT))

DiamEsfera = 13.8/100 #centimetros a m

IncD = 0.001 #metros

MIesferaT = (2*masaDisco*(DiamEsfera/2)**2)/5

print('Datos de la esfera')
incertidumbresEsfera = VariasMedidas(esferaSemiT)

IncMIesferaT = sqrt(((2*(DiamEsfera/2)**2)/5)**2*(0.01/1000)**2 + ((4*masaEsfera*(DiamEsfera/2))/2)**2*(0.0005**2))
print(f'El MI teórico de la esfera es {MIesferaT} y la incertidumbre del MI teórico de la esfera {IncMIesferaT}')

InerciaEsfera = (inercia(constante[0],incertidumbresEsfera[3]),IncInercia(constante[0],incertidumbresEsfera[3],constante[1]))
print(f'Momento de inercia de la esfera y inc: {InerciaEsfera}')

###### Cilindro
masaCilindro=384.29/1000

DiamCil = 10/100

semiTcil = np.array([0.436,0.436,0.435,0.431,0.429,0.432,0.436,0.438,0.435,0.435,0.433,0.433,0.437,0.435,0.435,0.435])

MIcilindroT = (masaCilindro*(DiamCil/2)**2)/2

IncMIcilindroT = sqrt(((DiamCil/4)**2)*(0.01/1000)**2 + ((DiamCil/2)*(masaCilindro/1000)**2)*(0.0005**2))
print(f'El MI teórico del cilindro es {MIcilindroT} y la incertidumbre del MI teórico del cilindro es: {IncMIcilindroT}')

print('Datos del cilindro')
incertidumbresCilindro = VariasMedidas(semiTcil)

InerciaCilindro = (inercia(constante[0],incertidumbresCilindro[3]),IncInercia(constante[0],incertidumbresCilindro[3],constante[1]))
print(f'Momento de inercia del cilindro y inc: {InerciaCilindro}')"""


############## Teorema de Steiner #############

class Steiner:
    def __init__(self,datos,d) -> None:
        self.d = d
        self.datos= datos
    def MI(self):
        print(f'Datos para d = {self.d}')
        D = constante[0]
        IncD = constante[3]
        semiT = VariasMedidas(self.datos)
        MI = inercia(D,semiT[3])
        IncMI = IncInercia(D,semiT[3],IncD)
        print(f'Momento de inercia: {MI} y su incertidumbre{IncMI}')
        tabla = datostabla(semiT)
        return tabla



#Disco con las diferentes posiciones

"""d1 = 3 # cm

Datosd1 = np.array([1.475,1.477,1.479,1.481,1.479,1.481,1.485,1.481,1.484,1.479,1.483,1.486,1.486,1.487,1.484])  #Semiperiodo del disco con d = 3cm

SteinerD1= Steiner(Datosd1,d1)
MID1 = SteinerD1.MI()

d2 = 6

Datosd2 = np.array([1.685,1.687,1.691,1.692,1.692,1.659,1.680,1.678,1.679,1.684,1.688,1.693,1.686,1.679,1.672])

SteinerD2 = Steiner(Datosd2,d2)
MID2 = SteinerD2.MI()




d3 = 9

Datosd3 = np.array([1.928,1.954,1.925,1.956,1.958,1.948,1.937,1.910,1.916,1.917,1.940,1.954,1.943,1.942,1.946])

SteinerD3 = Steiner(Datosd3,d3)
MID3 = SteinerD3.MI()

d4 = 12

Datosd4 = np.array([2.396,2.414,2.401,2.463,2.376,2.395,2.436,2.463,2.439,2.444,2.470,2.493,2.474,2.491,2.483])

SteinerD4 = Steiner(Datosd4,d4)
MID4 = SteinerD4.MI()

MomentosDisco = np.array([MID1,MID2,MID3,MID4])
Dcuadrado = np.square(np.array([d1,d2,d3,d4])/100)"""

def regresionSimple(x,y):
    """Axusta os datos dos vectore x e y a unha resta dada pola ec. y=a + bx
    Parametros:
    x vector con medidas da magnitud x
    y vector con medidas da magnitud y
    Devolve:
    a coeficiente a
    b coeficiente b
    sa incerteza de a
    sb incerteza de b
    r coeficiente de regresion lineal """
    n=len(x)
    sx=np.sum(x); sy=np.sum(y); xx=np.dot(x,x); yy=np.dot(y,y); xy=np.dot(x,y)
    denom=(n*xx - sx**2)
    b=(n*xy - sx*sy)/denom
    a=(xx*sy - sx*xy)/denom
    s=sqrt(sum((y-a-b*x)**2)/(n-2))
    sa=s*sqrt(xx/(n*xx-sx**2))
    sb=s*sqrt(n/(n*xx-sx**2))
    r=(n*xy-sx*sy)/sqrt((n*xx-sx**2)*(n*yy-sy**2))
    return [a,b, sa, sb, r, s]

"""regSteiner1 = regresionSimple(Dcuadrado,MomentosDisco)

print(regSteiner1)

def recta(a,b):
    x = np.linspace(0,0.015,1000)
    y = a + b*x
    return [x,y]

recta1 = recta(regSteiner1[0],regSteiner1[1])

plot(Dcuadrado,MomentosDisco,'o',color='royalblue',label='Datos experimentales')
plot(recta1[0],recta1[1],'--',color='navy',label='Recta de regresión')
xlabel('d\u00B2 (m\u00B2)')
ylabel('I (kg·m\u00B2)')
grid(True)
legend(loc='lower right')

show()"""


# Barra

#Datos del centro de masas
#cada distancia varía en un cm
longitudbarra=0.657

semiTCM = np.array([1.595,1.596,1.595,1.600,1.595,1.596,1.561])
semiT1 = np.array([1.606,1.606,1.606,1.607])
semiT2 = np.array([1.625,1.633,1.627,1.629,1.632])
semiT3 = np.array([1.649,1.643,1.648,1.651,1.646,1.661])
semiT4 = np.array([1.689,1.686,1.677,1.685,1.671])
semiT5 = np.array([1.681,1.688,1.681,1.682,1.680])
semiT6 = np.array([1.697,1.710,1.703,1.700,1.703])
semiT7 = np.array([1.738,1.732,1.738,1.732,1.729,1.724])
semiT8= np.array([1.772,1.785,1.782,1.781,1.777])
semiT9 = np.array([1.826,1.829,1.833,1.831,1.825])
semiT10 = np.array([1.866,1.871,1.876,1.879,1.870])


## Steiner barra

Barra0 = Steiner(semiTCM,0)
Barra1 = Steiner(semiT1,1)
Barra2 = Steiner(semiT2,2)
Barra3 = Steiner(semiT3,3)
Barra4 = Steiner(semiT4,4)
Barra5 = Steiner(semiT5,5)
Barra6 = Steiner(semiT6,6)
Barra7 = Steiner(semiT7,7)
Barra8 = Steiner(semiT8,8)
Barra9 = Steiner(semiT9,9)
Barra10 = Steiner(semiT10,10)

MIbarra0 = Barra0.MI()
MIbarra1 = Barra1.MI()
MIbarra2 = Barra2.MI()
MIbarra3 = Barra3.MI()
MIbarra4 = Barra4.MI()
MIbarra5 = Barra5.MI()
MIbarra6 = Barra6.MI()
MIbarra7 = Barra7.MI()
MIbarra8 = Barra8.MI()
MIbarra9 = Barra9.MI()
MIbarra10 = Barra10.MI()

datosBarra = np.array([MIbarra0,MIbarra1,MIbarra2,MIbarra3,MIbarra4,MIbarra5,MIbarra6,MIbarra7,MIbarra8,MIbarra9,MIbarra10])

pd.DataFrame(datosBarra).to_csv('datosbarra.csv')
