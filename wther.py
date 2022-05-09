import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'weatherAUS.csv')
#cantidad de datos filas x columns
print(df.size)

#transformando el campo fecha a un desgloce de los datos como son año, mes y dia
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#cantidad de valores nulos x columnas
print(df.isnull().sum())

#Eliminando datos nulos
df = df.dropna(subset=['RainToday'])
print('Identifica datos nulos')
print(df.isnull().sum())
#
# 12 horas diarias trabajan en las mineras

#array ciudades
citys = list()
indices = list()

#ciudades
ciudadess = df.groupby(by = "Location").sum()


count = 0
for i in ciudadess.index:
    count = count + 1
    citys.append(str(i))
    indices.append(count)


localidades = { 'indice': indices, 'citys' : citys}


df02 = pd.DataFrame(data = localidades)
df02.rename(columns={'indice': 'id', 'citys': 'ciudad'})
print('aplicamos un groupby con sum a ciudades, luego lo iteramos y lo transformamos a un DataFrame solo las columnas de indice (creada) y ciudad\n para ver si esta melbourne y perth y en que posicion')
print(df02)
cxd = np.array(df02, dtype=object)
cdsID = np.array(df02['indice'])
cds = np.array(df02['citys'])
print (""" \t DataFrame
ID\t Ciudades""")
print(cxd)
minera = [19,32]

#busqueda = int(input("Ingrese id a buscar: "))
for mn in minera:
    if mn in cdsID:
        found = str(cds[mn-1])
        local = df[df['Location'] == found]
        #local = df.loc[df['Location'] == found]
        print ('Ciudad: '+found)
        df4 = local.groupby(['Year'])['Pressure9am'].mean().reset_index(name='Promedio presipitación') #.sort_values(by='Cantidad', ascending=False)
        print(df4)