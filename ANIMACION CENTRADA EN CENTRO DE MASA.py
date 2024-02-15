# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


fig= plt.figure()
ax = plt.axes(projection= '3d')

data = pd.read_csv('MDES_Data_Inp_0_body_system.DAT', header = 1, delim_whitespace=True)
data2 = pd.read_csv('MDES_Data_Inp_1_body_system.DAT',header = 1, delim_whitespace = True)
data3 = pd.read_csv('MDES_Data_Inp_2_body_system.DAT',header = 1, delim_whitespace = True)
data4 = pd.read_csv('MDES_Data_Inp_3_body_system.DAT',header = 1, delim_whitespace = True)
data5 = pd.read_csv('MDES_Data_Inp_4_body_system.DAT',header = 1, delim_whitespace = True)
#constantes
G = 6.67**(-20)#constante universal de gravitacion universal en (km^3)/(segundos*kg)^2
contador  = 0
VA = 30 #VELOCIDAD ASTRONOMICA ES 30KM/S
DA = 150*(10**5)
T = 315600 # cantidad de segundos por dato 


densidadsol = 1411 #kg/m^3
densidadgiant = 1336 #use la densidad de jupiter como ejemplo de una gigante gaseosa kg/m3
densidadrocoso = 3.933 #densidad media de marte com ejemplo de planeta rocoso kg/m3
densidadagua = 997 #densidad para cometa pues esta hecho de agua en m
#datos de primer planeta

tiemp1= list(data.iloc[:,1])
x1 = list(data.iloc[:,2])
y1 =list(data.iloc[:,3])
z1 = list(data.iloc[:,4])
vx1  =list(data.iloc[:,5])
vy1 = list(data.iloc[:,6])
vz1  = list(data.iloc[:,7])

#segunda estrella
x2 = list(data2.iloc[:,2])
y2 =list(data2.iloc[:,3])
z2 = list(data2.iloc[:,4])
vx2  =list(data2.iloc[:,5])
vy2 = list(data2.iloc[:,6])
vz2  = list(data2.iloc[:,7])

#primer planeta, tercer cuerpo dado 
x3 = list(data3.iloc[:,2])
y3 =list(data3.iloc[:,3])
z3 = list(data3.iloc[:,4])
vx3  =list(data3.iloc[:,5])
vy3 = list(data3.iloc[:,6])
vz3 = list(data3.iloc[:,7])

# segundo planeta, cuarto cuerpo dado 
x4 = list(data4.iloc[:,2])
y4 = list(data4.iloc[:,3])
z4 = list(data4.iloc[:,4])
vx4  =list(data4.iloc[:,5])
vy4 = list(data4.iloc[:,6])
vz4  = list(data4.iloc[:,7])

#cometa, quinto cuespo dado
x5 = list(data5.iloc[:,2])
y5 = list(data5.iloc[:,3])
z5 = list(data5.iloc[:,4])
vx5  =list(data5.iloc[:,5])
vy5 = list(data5.iloc[:,6])
vz5  = list(data5.iloc[:,7])
#calculo de masas y radios
def MasaYRadio (psx, psx2, psy1, psy2,psz1, psz2,velx, vely, velz, velx2, vely2, velz2,densidad):#funcion que muestra masas y radios
    suma = 0
    suma1 =0
    suma2 = 0
    for i in range (1,409,1):
        vel = np.sqrt(((velx[i])**2+(vely[i])**2+ (velz[i])**2)*VA**2)#velocidad estrella en km/s
        vel2= np.sqrt(((velx2[i])**2+(vely2[i])**2+ (velz2[i])**2)*VA**2) # velovidad estrella 2 en km/s
        
        distancia = np.sqrt(((psx[i]-psx2[i])**2 + (psy1[i]-psy2[i])**2 + (psz1[i]-psz2[i])**2)*DA**2)#Distancia en km entre ambos vectores
        tiempo = T*i 
        masa1 = (vel*distancia**2)/(tiempo*G)
        masa2 = (vel2*distancia**2)/(tiempo*G)
        suma1 += masa2
        suma += masa1
        promedioMasa = suma/i #promedio para masa asociada a vx2 y velocidad 2
    for i in range (1,400,1) :
        vel = np.sqrt(((velx[i])**2+(vely[i])**2+ (velz[i])**2)*VA**2)#velocidad estrella en km/s
        vel2= np.sqrt(((velx2[i])**2+(vely2[i])**2+ (velz2[i])**2)*VA**2) # velovidad estrella 2 en km/s
        
        distancia = np.sqrt(((psx[i]-psx2[i])**2 + (psy1[i]-psy2[i])**2 + (psz1[i]-psz2[i])**2)*DA**2)#Distancia en km entre ambos vectores
        tiempo = T*i 
        masa1 = (vel*distancia**2)/(tiempo*G)
        
        rad1 = np.cbrt((3*(masa1)/(4*densidad*np.pi)))    #radio de masa1 
        suma2 +=rad1
        promrad1 = suma2/i
    return promedioMasa, promrad1

MasaEstrella1, radioEstrella1 = MasaYRadio(x1,x2,y1,y2,z1,z2,vx2,vy2,vz2, vx1,vy1,vz1,densidadsol)
print("masa estrella 1 es en promedio ", MasaEstrella1, " en kg",
      "\n","  su radio es ", radioEstrella1 , "en m")

MasaEstrella2, radioEstrella2= MasaYRadio(x1,x2,y1,y2,z1,z2,vx1,vy1,vz1,vx2,vy2,vz2,densidadsol)
print("masa estrella 2 es en promedio ", MasaEstrella2, " en kg",
      "\n","  su radio es ", radioEstrella2 , "en m")

masaPlaneta1, radioPlaneta1 = MasaYRadio(x1,x3,y1,y3,z1,z3,vx1,vy1,vz1,vx3,vy3,vz3, densidadgiant)
print("masa estrella gaseosa es en promedio ", masaPlaneta1 , " en kg",
      "\n","  su radio es ", radioPlaneta1 , "en m", "\n")

masaPlaneta2, radioplaneta2=  MasaYRadio(x1,x4,y1,y4,z1,z4,vx1,vy1,vz1,vx4,vy4,vz4, densidadrocoso)
print("masa planeta rocoso es en promedio ", masaPlaneta2 , " en kg",
      "\n","  su radio es ", radioplaneta2 , "en m")

MasaCometa, radiocometa =  MasaYRadio(x1,x5,y1,y5,z1,z5,vx1,vy1,vz1,vx5,vy5,vz5,densidadagua)
print("masa del cometa es ", MasaCometa, "en kg", "\n", 
      " su radio es ", radiocometa)
#Centro de masa en el sistema



def concometa(i):
    #centros de masa 
    centroMasaX = (MasaEstrella1*x1[i] + MasaEstrella2*x2[i] + masaPlaneta1*x3[i]+ masaPlaneta2*x4[i] + MasaCometa*x5[i])/(MasaEstrella1 + MasaEstrella2
                                                                                                   + masaPlaneta1 + masaPlaneta2)
    centroMasaY = (MasaEstrella1*y1[i] + MasaEstrella2*y2[i] + masaPlaneta1*y3[i]+ masaPlaneta2*y4[i] + MasaCometa*y5[i])/(MasaEstrella1 + MasaEstrella2
                                                                                                   + masaPlaneta1 + masaPlaneta2)
    centroMasaZ = (MasaEstrella1*z1[i] + MasaEstrella2*z2[i] + masaPlaneta1*z3[i]+ masaPlaneta2*z4[i]+ MasaCometa*x5[i])/(MasaEstrella1 + MasaEstrella2
                                                                                                   + masaPlaneta1 + masaPlaneta2 )
    ax.clear()
    x = (centroMasaX + x1[:3*i])*DA  
    y = (centroMasaY + y1[:3*i])*DA  
    z = (centroMasaZ + z1[:3*i])*DA  

    xx = (centroMasaX + x2[:3*i])*DA
    yy = (centroMasaY + y2[:3*i])*DA
    zz = (centroMasaZ + z2[:3*i])*DA

    xxx = (centroMasaX+ x3[3*i])*DA
    yyy = (centroMasaY + y3[:3*i])*DA
    zzz = (centroMasaZ + z3[:3*i])*DA
    
    xxxx = (centroMasaX + x4[:3*i])*DA
    yyyy = (centroMasaY + y4[:3*i])*DA
    zzzz = (centroMasaZ + z4[:3*i])*DA
    ax.set_xlim3d(-10**9 +centroMasaX,centroMasaX + 10**9)
    ax.set_ylim3d(-10**9 +centroMasaY,centroMasaY + 10**9)
    ax.set_zlim3d(-10**9 +centroMasaZ,centroMasaZ + 10**9)

    
    if (i == 2999):         #decirle donde acaba
        anim.event_source.stop()
    plt.xlabel("coordenada en x, en km")
    plt.ylabel("coordenada en y , en km")
    plt.title("Animacion de la solucion numerica de 5 cuerpos en tiempo T " )
    ax.scatter3D(x,y,z, s = 3, marker= 'o', color = 'Yellow', label = "primera estrella") #estrella 1
    ax.scatter3D(xx,yy,zz, s = 3, marker = 'o',color = 'Red', label = "segunda estrella") #estrella 1
    ax.scatter3D(xxx,yyy,zzz ,s = 5,color = 'Blue', label = "estrella gaseosa") #planeta 1
    ax.scatter3D(xxxx,yyyy,zzzz,s = 5,color = 'Green', label = "planeta rocoso ") #planeta 2

    plt.legend(loc='best',shadow=False,fontsize='small')



anim = animation.FuncAnimation(fig, concometa , 
                                  interval=1, repeat = False)#velocidad






