#Calculadora inductancia
from math import *
from pandas import *
from pylab import *
from numpy import *
from numpy.linalg import *

datos1 = DataFrame({'frecuencias':[300,400,500,600,700,800,900,1000,1100,1200,1350,1400,1500,1700,2000,2400,2900,3500,3750,3999],'vmr':[1.95,2.52,3.04,3.6,4.08,4.56,4.88,5.28,5.52,5.81,6.08,6.16,6.4,6.72,7.12,7.52,7.84,8.0,8.08,8.16],'vmc':[8.40,8.20,8.0,7.8,7.4,7.2,7.0,6.8,6.4,6.2,6.0,5.8,5.4,5.2,4.8,4.4,4.2,3.8,3.6,3.4],'deltaT':[680,520,360,320,240,200,164,152,128,104,88,84,72,60,48,32,28,20,16,12]})
#Los datos de deltaT están en microsegundos(e-06)

[nf,nl] = datos1.shape

R = 10000
C = 12E-09
v=9


Z = []
XC = []
Z2 = []
F1 = [] #Log10 de la frecuencia
F2 = [] #Frecuencias
logXC = []
cociente = []
z = 0 ; xc = 0 ; z2 = 0


for i in range(nf):
    f = datos1.iloc[i,0]
    F1.append(log10(f))
    F2.append(f)
    vr = datos1.iloc[i,1]
    vc = datos1.iloc[i,2]
    z = R*(v/vr)
    Z.append(z)
    xc = 1/(2*pi*f*C)   #Capacitancia reactiva
    XC.append(xc)
    z2 = 20*log10(z)    #Escala logarítmica
    Z2.append(z2)
    logXC.append(20*log10(xc))  #Escala logarítmica
    cociente.append(vr/vc)

   
#print('Inductancias: ',Z)#
#print('Reactancias capacitivas: ',XC)
#print('20logz =', Z2)
#print('vmr/vmc = ',cociente)
#print('20logXc: ',logXC)

x1 = arange(2.5,3.7,0.1)    #Resistencia
y1 = 20*log10(R)


"""plot(F1,Z2,label='Curva RC')
plot(x1,[y1 for i in x1],label='Curva R')
plot(F1,logXC,label='Curva C')
xlabel('log(f)')
ylabel('20logZ')
title('Inductancia frente a frecuencia')
legend(loc='upper right')

grid(True)


show(False)
clf()"""

#Regresión lineal de VmR/VmC respecto a f

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

datosreg = regresionSimpleSenTermoIndependente(array(F2),array(cociente)) #Los datos tienen que estar en formato array
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
    sx=sum(x); sy=sum(y); xx=dot(x,x); yy=dot(y,y); xy=dot(x,y);
    denom=(n*xx - sx**2)
    b=(n*xy - sx*sy)/denom
    a=(xx*sy - sx*xy)/denom
    s=sqrt(sum((y-a-b*x)**2)/(n-2))
    sa=s*sqrt(xx/(n*xx-sx**2))
    sb=s*sqrt(n/(n*xx-sx**2))
    r=(n*xy-sx*sy)/sqrt((n*xx-sx**2)*(n*yy-sy**2))
    print('s = ',s)
    return [a,b, sa, sb, r]

#datosreg2 = regresionSimple(array(F1),array(logXC))
#print('a = ',datosreg2[0],' b = ',datosreg2[1],' sa = ',datosreg2[2],' sb = ',datosreg2[3],'coeficiente = ',datosreg2[4])

y2 = datosreg[0]*array(F2)

"""plot(F2,cociente,'o',label='Vmr/vmc') #Datos sueltos
plot(F2,y2,label='Recta de regresión')
xlabel('Frecuencia(Hz)')
ylabel('Vmr/Vmc')
title('Vmr/Vmc respecto a la frecuencia')
legend(loc='lower right')
grid(True)"""

#print('b = ',datosreg[0],' sb =',datosreg[1],' El coeficiente de regresión es: ',datosreg[2],' s = ',datosreg[3])

#print('Frecuencia de corte = ',1/datosreg[0])

#Desfase entre señales

fase=[]

for i in range(nf):
    deltaT = datos1.iloc[i,3]
    deltaT = deltaT*1e-06
    fase.append(2*pi*F2[i]*deltaT*(180/pi))
    
print('Fases = ',fase)

polinomio = polyfit(F1,fase,3)  #Ajuste de los datos a un polinomio de grado 3
p = polyval(polinomio,F1)

plot(F1,fase,'o',label='Fases en grados')
plot(F1,p,label='Ajuste de los datos a un polinomio')
xlabel('Log(f)')
ylabel('Fase(Grados)')
grid(True)
legend(loc='upper right')

for i in range(3):
    print(polinomio[3-i],' x**',i,'+',end=',')
print(polinomio[0],' x**', 3)