# Bobinas Helmholtz

from numpy import *
from math import *
from matplotlib.pyplot import *

# a = R

R = 0.2

N = 154

d1 = 82.4 #cm, referencia del 0

z1 = array([82.4,81.3,79.5,79.0,77.7,76.7,76.0,75.5,75.1,75.0,74.7,74.0,73.5,73.0,72.4,72.0,71.5,70.9,70.2,69.6,69.0,68.4,67.9,67.46,67.0,66.5,65.9,65.4,64.8,64.0,63.4,62.9,62.4,61.9,61.5,60.9,60.0,59.4,58.9,58.3,57.7,57.0,56.4,55.8,55.0,54.3,53.6,52.9,52.3,51.7,51.0,50.2,49.5,48.0,47.4,46.9,46.2,45.4,44.8,44,83.0,83.8,84.5,85.3,86.2,87.0,87.8,88.5,89.3,90.2,90.9,91.8,92.6,93.7,94.5,95.1,95.6,96.0,96.6,97.2])    #A un lado


z1 = z1-d1


B1 = array([1.95,1.94,1.95,1.95,1.95,1.94,1.94,1.93,1.92,1.91,1.91,1.90,1.88,1.87,1.86,1.83,1.81,1.77,1.76,1.71,1.69,1.64,1.60,1.57,1.55,1.51,1.47,1.43,1.39,1.32,1.27,1.23,1.20,1.17,1.13,1.10,1.02,1.00,0.96,0.92,0.89,0.85,0.81,0.77,0.72,0.69,0.66,0.63,0.60,0.58,0.55,0.52,0.49,0.45,0.43,0.42,0.40,0.38,0.37,0.35,1.94,1.94,1.94,1.94,1.94,1.93,1.93,1.94,1.92,1.91,1.90,1.86,1.84,1.80,1.75,1.72,1.70,1.67,1.64,1.60])  #mt

#print(f'z1: {sort(z1)}, B1: {B1}')


# sb1 = 0.02



####################  mu 0

sI = 0.01


I = array([0.06,0.27,0.50,0.73,0.88,1.03,1.23,1.45,1.65,1.86,2.06,2.23,2.39,2.62,2.81])
B = array([0.06,0.20,0.35,0.51,0.61,0.71,0.85,0.99,1.12,1.26,1.40,1.50,1.60,1.76,1.90])

#print(len(I))

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


"""print('Datos de la regresión de la permeabilidad')
regresion = regresionSimpleSenTermoIndependente(I,B/1000)   # Hay que pasar a teslas

plot(I,B,'o',color='royalblue',label='Valores experimentales')
plot(I,regresion[0]*I*1000,color='navy',label='Recta de regresión')
xlabel('I (A)')
ylabel('B (mT)')
grid(True)
title('Representación gráfica de B en función de I')
legend(loc='lower right')

show()

gamma = 2/((5/4)**(3/2))

mu0 = (2*regresion[0]*R)/(gamma*N)

smu0 = ((2*R)/(gamma*N))*regresion[1]

print(f'mu0 = {mu0}')
print(f'Incertidumbre de la permeabilidad={smu0}')
print('Valor real de la permeabilidad = ',4*pi*10**(-7))"""

# a = R/2

d2 = 78.0

z2 = array([78.0,76.8,77.3,75.6,76.5,75.6,74.6,73.9,73.4,72.7,72.2,71.7,71.0,69.8,69.2,68.5,67.8,67.0,66.6,66.0,65.4,64.9,64.5,63.8,63.3,62.5,62.0,61.1,60.2,58.7,57.5,56.1,54.4,53.3,51.1,50.0,48.8,47.2,45.5,44.0,42.8,41.5,79.3,79.8,80.5,81.2,82.0,82.8,83.5,83.2,84.9,85.6,86.3,87.2,88.0,89.5,90.7,91.4,92.5,94.0,95.5])
B2 = array([2.41,2.40,2.41,2.38,2.39,2.37,2.34,2.32,2.30,2.25,2.22,2.17,2.15,2.06,1.98,1.94,1.87,1.82,1.76,1.71,1.66,1.60,1.54,1.48,1.44,1.37,1.32,1.25,1.18,1.07,0.98,0.89,0.77,0.73,0.62,0.58,0.54,0.48,0.43,0.40,0.37,0.33,2.41,2.40,2.39,2.36,2.32,2.27,2.24,2.21,2.14,2.08,2.03,1.93,1.88,1.74,1.62,1.53,1.45,1.33,1.21])

z2 = z2 - d2

#print('z2: ',z2)


# a = 2R

d3 = 93.0

z3 = array([93.0,92.1,91.2,90.0,89.2,88.5,87.6,87.0,86.5,85.8,85.0,84.5,84.0,83.6,83.0,82.4,81.6,81.1,80.6,79.7,78.9,78.0,77.4,76.8,76.2,75.5,74.8,74.0,73.2,72.5,71.5,70.8,70.2,69.5,69.0,68.3,67.5,66.5,66.0,65.2,64.5,63.5,62.1,61.0,60.9,59.7,58.5,57.8,57.0,56.2,55.4,93.5,94.0,94.5,95.0,95.5,96.0,96.5,97.0,97.5,98.0])
B3 = array([0.95,0.95,0.94,0.95,0.97,1.00,1.01,1.02,1.03,1.06,1.08,1.11,1.12,1.13,1.15,1.19,1.21,1.23,1.26,1.30,1.34,1.37,1.39,1.41,1.43,1.45,1.46,1.48,1.48,1.48,1.47,1.47,1.46,1.42,1.40,1.37,1.34,1.29,1.26,1.22,1.17,1.11,1.03,1.00,0.96,0.89,0.82,0.78,0.74,0.70,0.66,0.95,0.96,0.96,0.97,0.99,1.00,1.01,1.02,1.03,1.04])

z3 = z3 - d3

#print('z3: ',z3)

##### Cálculo de los valores teóricos del campo y la desviación cuadrática media#################


def Bteorico(z,a,I):
    mu0 = 4*pi*(10**(-7))
    R = 0.2
    N = 154 #numero de espiras
    BT = ((mu0*I*N)/(2*R)) * ((1/(1+((z-a/2)/R)**2)**(3/2))    + (1/(1+((z+a/2)/R)**2)**(3/2))  )
    return BT

def DesvCuadratica(Bexp,BT):
    N = 154
    s = (1/N)*(sqrt(sum((Bexp-BT)**2)))
    return s
            
I = 3 ##Intensidad con la que se toman las medidas

Bteorico1 = Bteorico(sort(z1/100),R,I)

Bteorico1tabla= Bteorico(z1/100,R,I) #En la tabla no están ordenados

#print(around(Bteorico1*1000,decimals=2)

#print('Valores de bt para la tabla',around(Bteorico1tabla*1000,decimals=2))


"""plot(z1,B1,'o',color='royalblue',label='Puntos experimentales')
plot(sort(z1),Bteorico1*1000,'--',color='navy', label='Curva teórica') #Hay que poner el sort para que la curva no quede cortada
title('Curva teórica y valores experimentales (a=R)')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

show()

clf()"""

# a=R/2

Bteorico2 = Bteorico(sort(z2/100),R/2,I)

#print('b teorico R/2: ',around(Bteorico2*1000,decimals=2))

Bteorico2tabla= Bteorico(z2/100,R/2,I) #En la tabla no están ordenados

#print('Valores de bt 2 para la tabla: ',around(Bteorico2tabla*1000,decimals=2))

"""plot(z2,B2,'o',color='royalblue',label='Puntos experimentales')
plot(sort(z2),Bteorico2*1000,'--',color='navy', label='Curva teórica') #Hay que poner el sort para que la curva no quede cortada
title('Curva teórica y valores experimentales (a=R/2)')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

show()

clf()"""

# a = 2R

Bteorico3 = Bteorico(sort(z3/100),2*R,I)

Bteorico3tabla = Bteorico(z3/100,2*R,I)

print('Valores de bt3 para la tabla: ', around(Bteorico3tabla*1000, decimals=2))


"""plot(z3,B3,'o',color='royalblue',label='Puntos experimentales')
plot(sort(z3),Bteorico3*1000,'--',color='navy', label='Curva teórica') #Hay que poner el sort para que la curva no quede cortada
title('Curva teórica y valores experimentales (a=2R)')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

show()

clf()"""


##### Vamos a hacer un subplot de las 3 curvas con I=2.8, para que se aprecie que los defectos son por eso

Icorregida = 2.8

BTcorregido1 = Bteorico(sort(z1/100),R,Icorregida)

BTcorregido2 = Bteorico(sort(z2/100),R/2,Icorregida)

BTcorregido3 = Bteorico(sort(z3/100),2*R,Icorregida)

"""figure(figsize=(13,4))

subplot(131)

plot(z1,B1,'o',color='royalblue',ms=3,label='Puntos experimentales')
plot(sort(z1),BTcorregido1*1000,'--',color='red', label='Curva teórica corregida') #Hay que poner el sort para que la curva no quede cortada
plot(sort(z1),Bteorico1*1000,'--',color='navy', label='Curva teórica')
title('a=R')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

subplot(132)

plot(z2,B2,'o',color='royalblue',ms=3,label='Puntos experimentales')
plot(sort(z2),BTcorregido2*1000,'--',color='red', label='Curva teórica corregida') #Hay que poner el sort para que la curva no quede cortada
plot(sort(z2),Bteorico2*1000,'--',color='navy', label='Curva teórica')
title('a=R/2')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

subplot(133)

plot(z3,B3,'o',color='royalblue',ms=3,label='Puntos experimentales')
plot(sort(z3),BTcorregido3*1000,'--',color='red', label='Curva teórica corregida') #Hay que poner el sort para que la curva no quede cortada
plot(sort(z3),Bteorico3*1000,'--',color='navy', label='Curva teórica')
title('a=2R')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='lower right')
grid(True)

suptitle('Correcciones de la curva teórica')

show()"""

## Cálculo de las desviaciones cuadráticas medias

s1 = DesvCuadratica(B1,Bteorico1)

#print('Desviación cuadrática de los valores de a=R: ',s1)

s2 = DesvCuadratica(B2,Bteorico2)

#print('Desviación cuadrática de los valores de a=R/2: ',s2)

s3 = DesvCuadratica(B3,Bteorico3)

print('Desviación cuadrática media de los valores de a=2R: ',s3)


############# Tratamiento del desajuste de las medidas

def cociente(Bexp,Bt):
    k = (Bt*1000)/Bexp
    mediak = mean(k)
    sk = std(k)
    print('Vector k con los cocientes: ',k)
    print('Media de los coeficientes: ',mediak)
    print('Desviación típica de los cocientes: ',sk) 

"""print('Datos para a=R')
cociente(B1,Bteorico1tabla)

print('datos de a=R/2')
cociente(B2,Bteorico2tabla)

print('datos de a=2R')
cociente(B3,Bteorico3tabla)"""


####### Representación de las 3 curvas

plot(z1,B1,'o',ms=3,color='royalblue',label='Puntos experimentales')
plot(sort(z1),Bteorico1*1000,'--',color='navy', label='Curva teórica a=R') #Hay que poner el sort para que la curva no quede cortada
plot(z2,B2,'o',ms=3,color='royalblue')
plot(sort(z2),Bteorico2*1000,'--',color='limegreen', label='Curva teórica a=R/2')
plot(z3,B3,'o',ms=3,color='royalblue')
plot(sort(z3),Bteorico3*1000,'--',color='red', label='Curva teórica a=2R')
title('Representación de los datos experimentales y las tres curvas teóricas')
xlabel('z(cm)')
ylabel('B(mT)')
legend(loc='upper left')
grid(True)

show()

