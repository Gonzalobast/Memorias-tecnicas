#Densidad y viscosidad

from numpy import *
from math import *
from matplotlib.pyplot import *

da = 1

mp = 19.12 # Masa del picnómetro vacío
sp = 0.01

mpe = 9.61  #Masa de los perdigones

mplaca = 44.22  #Masa de la placa con la que pesamos los perdigones

mpag = array([45.74,45.73,45.76,45.75,45.78,45.67,45.66,45.80,45.78,45.74]) #Medidas del picnometro con agua (g)
mpac = array([40.38,40.43,40.39,40.34,40.34,40.35,40.33,40.30,40.28,40.29]) #Medidas del picnómetro con acetona
mpal = array([41.12,41.13,41.13,41.12,41.13,41.11,41.02,41.07,41.11,41.11]) #Medidas del picnómetro con alcohol
mppe = array([54.42,54.43,54.49,54.44,54.49,54.51,54.40,54.40,54.46,54.46]) #Medidas del picnometro con agua+perdigones


indice=arange(1,11)

masaAgua = array([indice,mpag],dtype='U')
masaAgua = masaAgua.T


savetxt('masaAgua.txt',masaAgua,delimiter=',')

masaAcetona = array([indice,mpac])
masaAcetona = masaAcetona.T

savetxt('masaAcetona.txt',masaAcetona,delimiter=',')


masaAlcohol = array([indice,mpal])
masaAlcohol = masaAlcohol.T

savetxt('masaAlcohol.txt',masaAlcohol,delimiter=',')


masaPerdigones = array([indice,mppe])
masaPerdigones = masaPerdigones.T

savetxt('masaPerdigones.txt',masaPerdigones,delimiter=',')

####### Cálculo del volumen del picnómetro ######

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
    
    return (sa,sb,sc,media2,excluidos,datos)


INCpag = VariasMedidas(mpag)

print('Incertidumbres relativas a las medidas del picnómetro con agua')
print('sa = ',INCpag[0])
print('sb = ',INCpag[1])
print('sc = ',INCpag[2]); scag = INCpag[2]
print('media = ',INCpag[3]); mag=INCpag[3]
print('datos excluidos: ',INCpag[4])
print('datos buenos: ',INCpag[5])

Vp = mag - mp
print('Volumen del picnometro: ',Vp)   #Volumen del picnometro

# Calculo de la incertidumbre del volumen del picnometro

sv = sqrt(INCpag[2]**2+sp**2) # Inc de la masa del pic+agua y inc de la masa del pic

print('Incertidumbre del volumen del picnometro',sv)


#### Calculo de la densidad de la acetona y del agua ####

####Acetona
INCpac = array(VariasMedidas(mpac))    #Incertidumbres de la medida del pic+acetona

print('Incertidumbres relativas a las medidas del picnómetro con acetona')
print('sa = ',INCpac[0])
print('sb = ',INCpac[1])
print('sc = ',INCpac[2]); scac = INCpac[2]
print('media = ',INCpac[3]); mac = INCpac[3]
print('datos excluidos: ',INCpac[4])
print('datos buenos: ',INCpac[5])

DensidadAcetona = (mac-mp)/(mag-mp) #Cálculo de la densidad de la acetona

print('Densidad de la acetona: ',DensidadAcetona)

#Hay que calcular la incertidumbre de la densidad de la acetona

spAc = sqrt(((1/(mag-mp))*scac)**2+(((mac-mag)/(mag-mp)**2)*sp)**2+(((mp-mac)/(mag-mp)**2)*scag)**2)

print('Incertidumbre de la densidad de la acetona = ',spAc)

####Alcohol

INCpal = VariasMedidas(mpal)    #Incertidumbres de la medida del pic+acetona

print('Incertidumbres relativas a las medidas del picnómetro con alcohol')
print('sa = ',INCpal[0])
print('sb = ',INCpal[1])
print('sc = ',INCpal[2]); scal = INCpal[2]
print('media = ',INCpal[3]); mal = INCpal[3]
print('datos excluidos: ',INCpal[4])
print('datos buenos: ',INCpal[5])

DensidadAlcohol = (mal-mp)/(mag-mp) #Cálculo de la densidad del alcohol

print('Densidad del alcohol: ',DensidadAlcohol)

#Cálculo de la incertidumbre de la densidad del alcohol

spAl = sqrt(((1/(mag-mp))*scal)**2+((mal-mag)/(mag-mp)**2*sp)**2+((mp-mal)/(mag-mp)**2*scag)**2)

print('Incertidumbre de la densidad del alcohol = ',spAl)


##### Cálculo de la densidad de un sólido(plomo) ######

INCppe = VariasMedidas(mppe)    #Incertidumbres de la medida del pic+perdigones

print('Incertidumbres relativas a las medidas del picnómetro con perdigones+agua')
print('sa = ',INCppe[0])
print('sb = ',INCppe[1])
print('sc = ',INCppe[2]); scpe = INCppe[2]
print('media = ',INCppe[3]); mTotal = INCppe[3]
print('datos excluidos: ',INCppe[4])
print('datos buenos: ',INCppe[5])

DensidadPlomo = mpe/(mpe+mag-mTotal)

print('Densidad del plomo = ',DensidadPlomo)

# Cálculo de la incertidumbre de la densidad del plomo

spPb = sqrt((((mag-mTotal)/(mp+mag-mTotal)**2)*sp)**2+(((-mp)/(mp+mag-mTotal)**2)*scag)**2+(((mp)/(mp+mag-mTotal)**2)*scag)**2)

print('Incertidumbre de la densidad del plomo = ',spPb)



