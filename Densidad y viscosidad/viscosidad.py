#Viscosidad

from numpy import *
from math import *
from matplotlib.pyplot import *

### Datos

tag=array([153.45,156.20,154.89,154.54,153.50,154.06,154.01,154.27,154.64,154.10])
tac=array([69.51,69.99,69.58,69.80,69.85,69.73,69.84,69.67,69.59,69.80])
tah=array([312.88,315.22,314.57,314.47,315.96,315.74,313.51])

### Datos de la viscosidad del agua

visAg = 0.010054 ## Poise
IncVisAg = 0.000054 

def VariasMedidas(x):   
    k = 2 #Factor de cobertura
    
    sb = float(input('Introduce la incertidumbre de tipo B: '))
    
    media1 = mean(x)
    desviacion1 = std(x)
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
            
    media2 = mean(datos)    #Nuevo valor de la media
    
    sa = std(datos)/sqrt(len(datos)) #Incertidumbre de tipo a de la media
    
    sc = sqrt(sa**2 + sb**2)    #Incertidumbre combinada

    print(f'Datos de la muestra:')
    print(f'media inicial: {media1}')
    print(f'Desv tipica inicial: {desviacion1}')
    print(f'sb: {sb}')
    print(f'Datos excluidos: {excluidos}')
    print(f'Datos finales: {datos}')
    print(f'Media final: {media2}')
    print(f'Desv tipica final de la muestra: {std(datos)}')
    print(f'sa de la media {sa}')
    print(f'sc de la muestra: {sc}')
    
    return (sa,sb,sc,media2,excluidos,datos,media1,desviacion1)

datosagua = VariasMedidas(tag)

tK = datosagua[3]

k = visAg /(1*tK) ## Calculamos la constante con vis = k rho t

IncK = sqrt((visAg/datosagua[3]**2)**2*datosagua[2]**2 + (1/datosagua[3]**2)*IncVisAg**2)

print(f'Constante del viscosímetro {k} y su incertidumbre {IncK}')

def viscosidad(t,inct,densidad,incdensidad):
    k = 6.521701526530495e-05
    incK = 3.715773084490752e-07
    visc = t*densidad*k
    incVisc = sqrt((densidad*t)**2*incK**2+ (k*t)**2*incdensidad**2 + (k*densidad)**2*inct**2)
    return [visc,incVisc]

#Acetona

"""densidadAc = 0.79723
incDensAc =  0.00083 

datosacetona = VariasMedidas(tac)

VisAcetona = viscosidad(datosacetona[3],datosacetona[2],densidadAc,incDensAc)

print(f'Viscosidad de la acetona {VisAcetona[0]} con su incertidumbre {VisAcetona[1]}')"""

#Alcohol

densidadAl = 0.8262
incDensAl = 0.00069

datosalcohol = VariasMedidas(tah)

VisAlcohol = viscosidad(datosalcohol[3],datosalcohol[2],densidadAl,incDensAl)

print(f'Viscosidad del alcohol: {VisAlcohol[0]} y su incertidumbre: {VisAlcohol[1]}')




