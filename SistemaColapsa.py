# -*- coding: utf-8 -*-
"""
primer planeta lectura
fig = go.Figure(data=[go.Mesh3d(R1=R1,tet=tet,alf=alf, color='lightpink', opacity=0.50)])
fig.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



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

fi, ax = plt.subplots()
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
def MasaYRadio (psx, psx2, psy1, psy2,psz1, psz2,velx, vely, velz, velx2, vely2, velz2):#funcion que muestra masas y radios
    suma = 0
    suma1 =0
    suma2 = 0
    for i in range (1,299,1):
        vel = np.sqrt(((velx[i])**2+(vely[i])**2+ (velz[i])**2)*VA**2)#velocidad estrella en km/s
        vel2= np.sqrt(((velx2[i])**2+(vely2[i])**2+ (velz2[i])**2)*VA**2) # velovidad estrella 2 en km/s
        
        distancia = np.sqrt(((psx[i]-psx2[i])**2 + (psy1[i]-psy2[i])**2 + (psz1[i]-psz2[i])**2)*DA**2)#Distancia en km entre ambos vectores
        tiempo = T*i 
        a = tiemp1[i]
        masa1 = (vel*distancia**2)/(tiempo*G)
        masa2 = (vel2*distancia**2)/(tiempo*G)
        suma1 += masa2
        suma += masa1
        promedioMasa = suma/i #promedio para masa asociada a vx2 y velocidad 2
        promedioMasa2 = suma1/i
        ax.scatter(a,masa1)
        
    

    return promedioMasa

masaPlaneta1  = MasaYRadio(x1,x3,y1,y3,z1,z3,vx1,vy1,vz1,vx3,vy3,vz3)
plt.show()
'''como se observa en la figura la masa no es constante, por lo tanto el sistema colapsa en tiempo aproximado 5 años'''




