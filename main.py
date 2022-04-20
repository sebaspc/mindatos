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
df['RainToday'].replace(['NA'], [0], inplace=True)

#borrando filas en null
#df = df.dropna(subset=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine' ])
#print(df.isnull().sum())

# viendo si haa llovido según ubicacion y año
#locationYes = df.loc[df["RainToday"] == 'Yes', ["Location", "Year"]]
#locationNo = df.loc[df["RainToday"] == 'No', ["Location", "Year"]]

#lluviaYes = df[df['RainToday'] == 'Yes' ]
#lluviaNO = df[df['RainToday'] == 'No']
#lNO = lluviaNO.groupby(['Year', 'RainToday'])['RainToday'].count()
#lou = lluviaYes['RainToday']
#print(lou)


#cantidad de lluvia por año según ciudad

#df3 = lluviaYes.groupby(['Year','Location'])['RainToday'].count().reset_index(name='LLuviaCOUNT')
#print(df3)



    #elimino las columnas innecesarias para mi analisis
    #df4yes.drop(['RainToday'], axis = 1, inplace=True)
    #df4no.drop(['RainToday'], axis = 1, inplace=True)
    
    #yrs = np.array(df4yes['Year']).reshape((1, -1))
    #cntidad = np.array(df4yes['Cantidad'])


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
    print ('Ciudad: '+found)
    df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad') #.sort_values(by='Cantidad', ascending=False)

    #separo los datos logisticamente
    df4yes = df4[df4['RainToday'] == 'Yes']
    df4no = df4[df4['RainToday'] == 'No']
    
        #elimino las columnas innecesarias para mi analisis
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
    plt.title('Cantidad de veces que ha llovido por año en: '+found)
    plt.xlabel('Años')
    plt.ylabel('Cantidad ')
    plt.grid()
    plt.legend(loc=4)
    plt.show()
    


    
    # PROMEDIO SEGÚN SI LLUVIO O NO





    #elimino las columnas innecesarias para mi analisis
    #df4yes.drop(['RainToday'], axis = 1, inplace=True)
    #df4no.drop(['RainToday'], axis = 1, inplace=True)
    
    #yrs = np.array(df4yes['Year']).reshape((1, -1))
    #cntidad = np.array(df4yes['Cantidad'])

    #X = yrs
    #X = X.transpose()
    #y = cntidad
    #print(X.shape)
    #print(y.shape)
    #plt.scatter(X,y)
    #plt.title('Cantidad de veces que ha llovido por año en: '+found)
    #plt.xlabel('Años')
    #plt.ylabel('Cantidad ')
    #plt.show()


else:
    print("Digitalice el id correspondiente, estos pueden ser\n"+str(cxd))
    print (""" \t TIPO
ID\t Ciudad""")

#print('Datos 2017 si ha llovido o no en adelaide')

#anoNO = 0
#anoYES = 0
#anius = int(input('Ingrese el año: '))
#for i in local.index:
    #v2017 = v2017
#    if local['Year'][i] == anius:
        
#        if local['RainToday'][i] == 'No':
#            anoNO = anoNO+1
#        else:
#            if local['RainToday'][i] == 'Yes':
#                anoYES = anoYES+1
#    else:
#        print('ingrese un valor valido')
#        break
            #print('Año: '+str(local['Year'][i])+' '+'lluvio: '+ str(local['RainToday'][i]))


#print('Cantidad de veces que no lluvio en Adelaide: '+ str(anoNO))
#print('Cantidad de veces que lluvio en Adelaide: '+ str(anoYES))

#for i in range(cds)

# ciudad adelaide
#local = df[df['Location'] == 'Adelaide']

# cantidad de veces y las que no ha llovido en adelaide según groupby de años y lluvia (yes or no)
#df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count().reset_index(name='Cantidad')#.sort_values(by='Cantidad', ascending=False)





#print('Datos anuales si ha llovido o no en adelaide')
#print(df4)
#cantidad de veces que lluvio o no lluvio según ciudad
#local = df[df['Location'] == 'Canberra']
#df4 = local.groupby(['Year', 'RainToday'])['RainToday'].count()

    

    
#→ DataFrame de frecuencia
#for cate in a:
#    frecuency = df[cate].value_counts()
#    df_frequency = pd.DataFrame({
#        cate: frecuency.index.tolist(), 
#        'Cantidad': frecuency.tolist()
#    })
#    sns.barplot(x=cate, y='Cantidad', data=df_frequency)
#    plt.show()

#df['Date'] = pd.to_datetime(df['Date'])
#df['Year'] = df['Date'].dt.year
#df['Month'] = df['Date'].dt.month
#df['Day'] = df['Date'].dt.day


#descripcion = df.describe()
#print(descripcion)

#estadistica cualitativa
categorical_var = ['Location','RainToday','RainTomorrow','Year', 'Month','WindGustDir']
categorical_hours_var = ['WindDir9am','WindDir3pm']
#estadistica cuantitativa
numerical_clima_var = ['MinTemp','MaxTemp', 'Evaporation', 'RISK_MM','Evaporation','Sunshine','WindGustSpeed']
numerical_clima_hours_var = ['WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm']
#lluviano = df[df['RainToday'] == 'Yes']
#
#locationYes = df.loc[df["RainToday"] == 'Yes', ["Location", "Year"]]
#locationNo = df.loc[df["RainToday"] == 'No', ["Location", "Year"]]
#location = df[['Location','Year', 'RainToday']]
