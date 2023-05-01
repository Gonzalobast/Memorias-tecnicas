##masa picnometro con agua(mpa)
##media picnometro con agua (meanmpa)
##masa picnometro con acetona (mpac)
##vp=v volumen del picnómetro
##masa picnometro (mp)
##densidad agua (da) (g/ml)
##volumen del picnometro (vp)
##masa perdigones (mpe)
##masa picnometro con agua y perdigones (mppe)
##media del picnometro con agua y perdigones (meanmppe)
#tag tiempo del agua
#tac tiempo acetona

\\densidad de los perdigones (dpe)
da=1
mp=19.12
\\incertidumbre +- 0.01
mpag=c(45.74,45.73,45.76,45.75,45.78,45.67,45.66,45.80,45.78,45.74)
meanmpa=mean(mpag)
mpac=c(40.38,40.43,40.39,40.34,40.34,40.35,40.33,40.30,40.28,40.29)
mpah=c(41.12,41.13,41.13,41.12,41.13,41.11,41.02,41.07,41.11,41.11)
vp=(meanmpa-mp)/da
###############solidos###################
mpe=9.61
mplaca=44.22
mppe=c(54.42,54.43,54.49,54.44,54.49,54.51,54.40,54.40,54.46,54.46)
meanmppe=mean(mppe)
Tag=19.5
dpe=((mpe)/(mpe+meanmpa-meanmppe))*da


tag=c(153.45,156.20,154.89,154.54,153.50,154.06,154.01,154.27,154.64,154.10)
tac=c(69.51,69.99,69.58,69.80,69.85,69.73,69.84,69.67,69.59,69.80)
tah=c(312.88,315.22,314.57,314.47,315.96,315.74,313.51)
