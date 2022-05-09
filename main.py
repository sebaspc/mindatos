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

# toda informacion
print(df.info())

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
        df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad') #.sort_values(by='Cantidad', ascending=False)

        #separo los datos logisticamente
        df4yes = df4[df4['RainToday'] == 'Yes']
        df4no = df4[df4['RainToday'] == 'No']
        
            # sacando el promedio de las cantidades
        var = 0
        cont = 0
        for i in df4yes.index:
            cont = cont + 1
            var = var + df4yes['Cantidad'][i]
            prom = var / cont
            
        varno = 0
        contno = 0
        for n in df4no.index:
            contno = contno + 1
            varno = varno + df4no['Cantidad'][n]
            promno = varno / contno
        print(str(df4)+'\nEl promedio total de lluvia es:\t'+str(prom)+'\nEl promedio total de sin lluvia es:\t'+str(promno))
        
        #elimino las columnas innecesarias para mi analisis
        df4yes.drop(['RainToday'], axis = 1, inplace=True)
        print(df4yes)

            # Le doy valor a mi vector x e y
        x = np.array(df4yes['Year'])
        y = np.array(df4yes['Cantidad'])
        print('Años y cantidades SIN predicción en la ciudad de '+found)
        print(x)
        print(y)

        n = len(x)
        
        #print('aqui va n\n')
        #print(n)
        
            #variables necesarios para mi ecuacion algoritmica de regresión lineal (ecuacion de la recta)
        #si
        sumx = sum(x)
        sumy = sum(y)
        sumx2 = sum(x*x)
        sumy2 = sum(y*y)
        sumxy = sum(x*y)
        promx = sumx/n
        promy = sumy/n

        
            # sacando el pendiente de la recta (b)
        #SI
        m = (sumx*sumy - n * sumxy) / (sumx ** 2 - n*sumx2)
        b = promy - m*promx

            #SI
        lx = list()
        ly = list()
        for i in df4yes['Year']:
            lx.append(i)
            
        for c in df4yes['Cantidad']:
            ly.append(c)
            
            # Imprimo un ejemplo de pronostico 2018-2019
            
        anios = [2018, 2019]
        
        for i in anios:
            if i not in lx:
                pred = int((m*i)+b)
                lx.append(i)
                ly.append(pred)
            else:
                print('Item ya agregado')
        print('Predicción de los años años 2018 y 2019 en la Ciudades de '+found)
        print(lx)
        print(ly)
        lx = np.array(lx)
        ly = np.array(ly)
        
        print('el valor de m es: '+str(m))
        print('el valor de b es: '+str(b))

        plt.plot(lx,ly, 'o', label= 'Datos')
        plt.plot(lx, m*lx +b, label='Declive')
        plt.scatter(lx,ly)
        plt.title('Cantidad de veces que ha llovido por año en: '+found)
        plt.xlabel('Años')
        plt.ylabel('Cantidad ')
        plt.grid()
        plt.legend(loc=4)
        plt.show()