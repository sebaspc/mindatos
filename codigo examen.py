import numpy as np
depart=np.zeros([10,4],dtype=object)
rut2=np.zeros([10,4],dtype=object)
costo=np.zeros([10,4],dtype=object)
lista=['10','9','8','7','6','5','4','3','2','1']
lista2=['A','B','C','D']
listaP=[3800,3000,2800,3500]
#Alejandro 
def reservar():
    while 1:
        i=input("�Que piso desea?\n")
        while not(i in lista):
            i=input("tipo de parametro invalido, ingrese valor de 1 a 10\n")
        i=int(i)-1
        j=(input("�Que departamento?\n"))
        while not(j in lista2):
            j=input("""tipo de parametro invalido.
                     Favor ingrese digito correcto (A, B, C O D)\n""")
        j=lista2.index(j)
        if depart[i][j]!=0:
            print("Departamento ocupado")
        else:
            nombre=input("�Cu�l es su nombre?\n")
            rut=input("�Cu�l es su rut?. Favor ingresar RUT sin guion verificador\n")
            depart[i][j]=nombre
            rut2[i][j]=str(rut)
            valor=listaP[j]
            costo[i][j]=int(valor+max(0,100*(i-1)))
            print("reservado exitosamente")
            break
#Sebastian Carrasco
def ordenL():
    rutList=[]
    i=0
    j=0
    while i<10:
        while j<4:
            if rut2[i][j]!=0:
                rutList.append(rut2[i][j])
                
            j+=1
        j=0
        i+=1
    rutList.sort()
    for r in rutList:
        i=0
        j=0
        while i<10:
            while j<4:
                if rut2[i][j]==r:
                    print("Rut: "+str(r)+", nombre: "+depart[i][j])
                j+=1
            j=0
            i+=1
#Alejandro 
def reasignar():
    rut=input("ingresar rut\n=>")
    i=0
    j=0  
    while i<10:
        while j<4:
            if rut2[i][j]==str(rut):
                depart[i][j]=0
                rut2[i][j]=0
                costo[i][j]=0
                print("departamento modificado")
                reservar()
                return 
            j+=1
        j=0
        i+=1
    print("departamento desocupado")
#Sebastian Painen
def buscarC():
    rut=input("ingresar rut\n=>")
    i=0
    j=0
    
    while i<10:
        while j<4:
            if rut2[i][j]==str(rut):
                print("comprador: "+depart[i][j])
                return 
            j+=1
        j=0
        i+=1
    print("RUT inexistente")
        
#Sebastian Painen
def printearMatriz():
    print (""" \t TIPO
PISO\t A  B  C  D""")
    i=9
    j=0
    s = ""
    while i>=0:
        s=str(i+1)+"\t"
        while j<4:
            if depart[i][j]==0:
                s=s+"   "
            else:
                s=s+" x "
            j=j+1
        print (s)
        j=0
        #Aca se le agrega el 10
        i=i-1
#Sebastian Carrasco
def ganancia():
    print("Tipo de Departamento    Cantidad        Total          Recargo por piso")
    j=0
    tc=0
    tp=0
    trc=0
    while j<4:
        s="Tipo "+lista2[j]+"\t"+str(listaP[j])+" UF"
        cantidad=0
        total=0
        i=0
        while i < 10:
            if depart[i][j] !=0:
                cantidad+=1
                total+=costo[i,j]
            i+=1
        s=s+"\t"+"\t"+str(cantidad)+"\t\t"+str(cantidad*listaP[j])+" UF" +"\t\t"+str(total-cantidad*listaP[j])+" UF"
        tc+=cantidad
        tp+=cantidad*listaP[j]
        trc+=total-cantidad*listaP[j]
        print(s)
        j+=1
    print("TOTAL" + "\t\t\t"+str(tc) + "\t\t" +str(tp)+" UF" + "\t  +     "+ str(trc)+" UF"+ "\t"+"=", str(trc+tp)+"UF")
        
        

while 1:
    print("seleccione una opcion")
    print("1)\tcomprar departamento")
    print("2)\tMostrar departamentos disponibles")
    print("3)\tver listado de compradores")
    print("4)\tBuscar comprador")
    print("5)\treasignar")
    print("6)\tganancia")
    print("7)\tsalir")
    opcion=input(">>")
    while opcion<str(0) or opcion >=str(8):
        (opcion)=input("opcion fuera de rango,>>")
    if(opcion==str(1)):
        reservar()
    if(opcion==str(2)):
        printearMatriz()
    if(opcion==str(3)):
        ordenL()
    if(opcion==str(4)):
        buscarC()
    if(opcion==str(5)):
        reasignar()
    if(opcion==str(6)):
        ganancia()
    if(opcion==str(7)):
        break