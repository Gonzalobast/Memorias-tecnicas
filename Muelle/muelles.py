# Muelles

from numpy import *
from math import *
from matplotlib.pyplot import *

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
    return [b, sb, r, s]

masas = array([10.20,30.25,50.27,70.24,80.20,90.22,100.01,105.04,110.07,115.15])   #gramos
print(len(masas))


sregla = 0.5 #milimetros
speriodo = 0.25 #segundos

g=9.8

htotal = 732

x = 560


"""peso = (masas/1000)*g


x2 = array([527,461,397,333,300,269,238,220,205,188]) 

deltax = sort(x - x2)

regresion1 = regresionSimpleSenTermoIndependente(deltax/1000,peso) #Hay que pasar a SI

plot(deltax/1000,peso,'o',color='royalblue',label='Datos experimentales')
plot(deltax/1000,regresion1[0]*(deltax/1000),'--',color='navy',label='Recta de regresión')
xlabel(r'$\Delta x$ (m)')
ylabel('F (N)')
grid(True)
legend(loc='lower right')

show()"""

periodo10 = array([4.24,7.07,8.47,9.97,10.56,11.22,11.72,12.07,12.19,12.62]) 

periodo = periodo10/10
Tcuadrado = periodo**2

IncTcuadrado = 0.05*periodo

datosDinamico = array([periodo10,periodo,Tcuadrado]).T
print(datosDinamico)
print('Incertidumbre T^2 : ',IncTcuadrado)

####Regresión lineal simple del método dinámico

regresion2 = regresionSimpleSenTermoIndependente(4*(pi**2)*(masas/1000),Tcuadrado)


plot(4*pi**2*(masas/1000),Tcuadrado,'o',color='royalblue',label='Datos experimentales')
plot((4*pi**2*(masas/1000)),((4*(pi**2)*(masas/1000))*regresion2[0]),'--',color='navy',label='Recta de regresión')
xlabel(r'4$\pi^2$m (kg)')
ylabel('T\u00B2 (s\u00B2)')
grid(True)
legend(loc='lower right')


show()

print(f'Valor de k: {1/regresion2[0]} y su incertidumbre {regresion2[1]/(regresion2[0]**2)}')

"""plateadoligero = 49.26  #gramos
DxPL = x - 400 #o 400 o 360x2 #Deformacion del plateado ligero
DxPLA = x - 458 #deformacion del plateado ligero en el agua


plateadopesado = 137.87
DxPP = x - 115 #deformacion del plateado pesado
DxPPA = x - 168 #deformacion del plateado pesado en el agua

dorado = 147.43
DxD = x - 84 #deformacion del dorado
DxDA = x - 135 #deformacion del dorado en el agua

def densidad(delta,deltaagua):
    densidad = delta/(delta-deltaagua)
    return densidad

def incDensSolido(delta,deltaagua,IncDelta,IncDeltaagua):
    delta = delta/1000
    deltaagua = deltaagua/1000
    partialDelta = deltaagua/(delta-deltaagua)**2
    partialDeltaagua = delta/(delta-deltaagua)**2
    incRhoS = 1000*sqrt((partialDelta**2)*(IncDelta**2) + (partialDeltaagua**2)*(IncDeltaagua**2)) #Multiplicamos por 1000 por el factor de la densidad del agua (Trabajamos en SI(kg/m^3))
    return incRhoS/1000 #Pasamos a g/cm^3

IncDelta = 0.0028 #incertidumbre de las deformaciones en m


rhoPP = densidad(DxPP,DxPPA) #Densidad del plateado pesado
rhoPL = densidad(DxPL,DxPLA) #densidad del plateaado ligero
rhoD = densidad(DxD,DxDA) #densidad del dorado

IncRhoPP = incDensSolido(DxPP,DxPPA,IncDelta,IncDelta)
IncRhoPL = incDensSolido(DxPL,DxPLA,IncDelta,IncDelta)
IncRhoD = incDensSolido(DxD,DxDA,IncDelta,IncDelta)

print(f'Densidad del PP: {rhoPP} con su incertidumbre: {IncRhoPP}')
print(f'Densidad del Pl: {rhoPL} con su incertidumbre: {IncRhoPL}')
print(f'Densidad del D: {rhoD} con su incertidumbre: {IncRhoD}')

DxPLalc = x - 430


DxPPalc = x - 162


DxDalc = x - 120

def densidadliquido(densidadsolido,deltaxsinagua,deltaxconalcohol):
    densidadalcohol = densidadsolido * ((deltaxsinagua-deltaxconalcohol)/deltaxsinagua)
    return densidadalcohol

def incDensLiq(delta,deltaxalcohol,IncDelta,Incdeltaalcohol,rho_S,IncRho_s):
    partialDelta = (rho_S*deltaxalcohol)/(delta**2)
    partialDeltaalcohol = rho_S/delta
    partialRho_S = (delta-deltaxalcohol)/delta
    IncRho_L = sqrt((partialDelta**2)*(IncDelta**2) + (partialDeltaalcohol**2)*(Incdeltaalcohol**2) + (partialRho_S**2)*(IncRho_s**2))
    return IncRho_L

rhoAlPP = densidadliquido(rhoPP,DxPP,DxPPalc)

rhoAlPL = densidadliquido(rhoPL,DxPL,DxPLalc)

rhoAlD = densidadliquido(rhoD,DxD,DxDalc)


print(rhoAlD)
print(rhoAlPL)
print(rhoAlPP)"""

#recta que pasa por el origen y la pendiente es g
#a  la altura hay que restarle 1cm
#incertidumbre del tiempo de caida es 0.00001 segundos

altura = array([0.58,0.56,0.54,0.52,0.50,0.48,0.46,0.42,0.40,0.38])
tiempo = array([0.34094,0.33338,0.32952,0.31880,0.31177,0.30416,0.29593,0.29176,0.28261,0.27488])

altura2 = altura*2
TiempoCuadrado = tiempo**2

regresion3 = regresionSimpleSenTermoIndependente(TiempoCuadrado,altura2)

plot(TiempoCuadrado,altura2,'o',color='royalblue',label='Datos experimentales')
plot(TiempoCuadrado,TiempoCuadrado*regresion3[0],'--',color='navy',label='Recta de regresión')
xlabel('t\u00B2 (s\u00B2)')
ylabel('2h (m)')
grid(True)
legend(loc='lower right')

show()


