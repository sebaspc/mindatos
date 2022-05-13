import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import train_test_split


df = pd.read_csv(r'weatherAUS.csv')
#cantidad de datos filas x columns
#print(df.size)

#transformando el campo fecha a un desgloce de los datos como son año, mes y dia
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#canidad de valores nulos x columnas
print(df.isnull().sum())
print(df.info())
#transformando dato nulos de raintoday a Null
df = df.dropna(subset=['RainToday'])

#borrando filas en null
#df = df.dropna(subset=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine' ])
#print(df.isnull().sum())

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
cxd = np.array(df02, dtype=object)
cdsID = np.array(df02['indice'])
cds = np.array(df02['citys'])
print (""" \t DataFrame
ID\t Ciudad""")
print(cxd)
busqueda = int(input("Ingrese id a buscar: "))
if busqueda in cdsID:
    found = str(cds[busqueda-1])
    local = df[df['Location'] == found]
    
    df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad') #.sort_values(by='Cantidad', ascending=False)
    anxs = list()
    cnty = list()
    cntn = list()
    for i, fila in df4.iterrows():
        if fila['RainToday'] == 'Yes':
            anxs.append(fila['Year'])
            cnty.append(fila['Cantidad'])
            print(fila['Year'], fila['Cantidad'])
        else:
            print('Hay otros datos')
    for i, fila in df4.iterrows():
        if fila['RainToday'] == 'No':
            if fila['Year'] not in anxs:
                anxs.append(fila['Year'])
                cntn.append(fila['Cantidad'])
            else:
                cntn.append(fila['Cantidad']) 
    rain = {'Year': anxs, 'Yes': cnty, 'No': cntn}
    dfRain = pd.DataFrame (data = rain)
    dfRain.rename(columns={'Year': 'Años', 'Yes': 'Lluvio', 'No':'NoLluvio'})
    
    print('Ciudad '+found)
    print(dfRain)
    
    
    ax = dfRain.plot(kind='line', x = 'Year', y='Yes', color='DarkBlue')
    ax2= dfRain.plot(kind='line', x='Year', y='No', secondary_y=True,color='Red', ax=ax)
    

    ax.set_ylabel('Cantidad de SI')
    ax2.set_ylabel('Cantidad de NO')
    plt.title('Cantidades de veces que ha y no llovido por año según ciudad '+found+'.')
    plt.grid()
    plt.tight_layout()
    plt.show()
    
    
        #separo los datos logisticamente
    df4yes = df4[df4['RainToday'] == 'Yes']
    df4no = df4[df4['RainToday'] == 'No']
    
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
        
    #ax = df4yes.plot(kind='line', x = 'Year', y='Cantidad', color='DarkBlue')
    #ax2= df4no.plot(kind='line', x='Year', y='Cantidad', secondary_y=True,color='Red', ax=ax)
    

    #ax.set_ylabel('Height')
    #ax2.set_ylabel('Weight')
    #plt.title('Cantidad de veces que ha llovido por año en: '+found)
    #plt.grid()
    #plt.legend(loc=4)
    #plt.tight_layout()
    #plt.show()
    
    print ('Ciudad: '+found)
    print(str(df4)+'\nEl promedio total de lluvia es:\t'+str(prom)+'\nEl promedio total de sin lluvia es:\t'+str(promno))
        #elimino las columnas innecesarias para mi analisis
    df4yes.drop(['RainToday'], axis = 1, inplace=True)
    df4no.drop(['RainToday'], axis = 1, inplace=True)
    print(df4yes)
        # Le doy valor a mi vector x e y
    x = np.array(df4yes['Year'])
    y = np.array(df4yes['Cantidad'])
    
        # cantidad de datos en x 
    n = len(x)
    
    #print('aqui va n\n')
    #print(n)
    
        #variables necesarios para mi ecuacion algoritmica de regresión lineal (ecuacion de la recta)
    sumx = sum(x)
    sumy = sum(y)
    sumx2 = sum(x*x)
    sumy2 = sum(y*y)
    sumxy = sum(x*y)
    promx = sumx/n
    promy = sumy/n
    
        # sacando el pendiente de la recta (b)
    
    m = (sumx*sumy - n * sumxy) / (sumx ** 2 - n*sumx2)
    
    b = promy - m*promx
    
    #   
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
    print(lx)
    print(ly)
    lx = np.array(lx)
    ly = np.array(ly)
    
    print('el valor de m es: '+str(m))
    print('el valor de b es: '+str(b))
    print(x.shape)
    print(y.shape)

    plt.plot(lx,ly, 'o', label= 'Datos')
    plt.plot(lx, m*lx +b, label='Ajuste')
    plt.scatter(lx,ly)
    plt.title('Cantidad de veces que ha llovido por año en: '+found + '. \nMas Predicción de los años 2018-19')
    plt.xlabel('Años')
    plt.ylabel('Cantidad ')
    plt.grid()
    plt.legend(loc=4)
    plt.show()
    



else:
    print("Digitalice el id correspondiente, estos pueden ser\n"+str(cxd))
    print (""" \t TIPO
ID\t Ciudad""")