#Se necesita un programa que genere un listado de todos los mozos con los siguientes datos: 
#nombre del mozo, categoría, importe a cobrar por la comisión de la venta.


def e1():
    
    archi=open("DatosMozos.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        comision="$"+str((float(registro[3].replace(",","."))*float(registro[4]))/100)


        print(registro[1].ljust(25," ")+registro[2].ljust(10," ")+str(comision).rjust(12," "))
    archi.close()
  
  
def e2():
    categoria=input("-Juniors \n-Master \n-Experto \nIngrese la categoria: ")
    archi=open("DatosMozos.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        if registro[2].upper()==categoria.upper():
            print(registro[1])
    archi.close()
         

def e3():
    
    archi_lectura=open("DatosMozos.csv","r")
    archi_escritura=open("DatosExport.csv","w")
    for datos in archi_lectura.readlines():
        registro=datos.replace("\n" , "").split(";")
        comision="$"+str((float(registro[3].replace(",","."))*float(registro[4]))/100)


        archi_escritura.write(registro[1]+";"+registro[2]+";"+str(comision).replace(".",",")+"\n")
        
    archi_lectura.close()
    archi_escritura.close()
    print ("Los datos han sido exportado en el archivo DatosExport")

    
def e4():
    categoria=input("-Juniors \n-Master \n-Experto \nIngrese la categoria: ")
    archi_lectura=open("DatosMozos.csv","r")
    archi_escritura=open("DatosExporta.csv","w")
    for datos in archi_lectura.readlines():
        registro=datos.replace("\n" , "").split(";")
        if registro[2].upper()==categoria.upper():    
            archi_escritura.write(registro[1].replace(".",";")+"\n")
            
    archi_lectura.close()
    archi_escritura.close()
    print ("Los datos han sido exportado en el archivo DatosExporta")
    


def e5():

   archi=open("DatosMozos.csv","r")  
   total=0 
   for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        total=total+int(registro[4])
   print(f"Ventas totales: $ {total}")
            
   archi.close()
    

   
def e6():

   archi=open("DatosMozos.csv","r")  
   total=0 

   for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        total=total+int(registro[4])
   prom=round(total/len(datos),3)
   print (f"Promedio de ventas: $ {prom}")
            
   archi.close()



def e7():

   archi=open("DatosMozos.csv","r")  
   vendedor=0 
   maxx=0
   for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        if int(registro[4])>maxx:
            maxx=int(registro[4])
            vendedor=registro[1]
            
   archi.close()
   print(f"El mozo que logró la mayor venta es {vendedor}")
    


def e8():
    total=0
    archi=open("DatosMozos.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n" , "").split(";")
        comision=(float(registro[3].replace(",","."))*float(registro[4]))/100
        total+=comision

    print (f"Total de comisiones: ${total}")
    archi.close()



def e9():
    num=0
    total=0
    archi=open("DatosMozos.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n","").split(";")
        comision=(float(registro[3].replace(",","."))*float(registro[4]))/100
        total+=comision
        num+=1
        promedio=round(total/num,)
    print(f"La comision por venta promedio es de: ${promedio}")
    archi.close()


def e10():
    maxx=0
    archi=open("DatosMozos.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n","").split(";")
        comision=float(registro[3].replace(",","."))*float(registro[4])/100
        if comision>maxx:
            maxx=comision
        archi.close()
    print(f"La mayor comisión a pagar es de $ {maxx}")

print("1- genere un listado de todos los mozos con los siguientes datos: nombre del mozo, categoría, importe a cobrar por la comisión de la venta. ")
print("2- genere un listado de los mozos que correspondan a una categoría en particular, indicada por el usuario.")
print("3- genere un archivo con extensión CSV de todos los mozos con los siguientes datos: nombre del mozo, categoría, importe a cobrar por la comisión de la venta.")
print("4- genere un archivo con extensión CSV de los mozos que correspondan a una categoría en particular, indicada por el usuario.")
print("5- muestre el total de las ventas.")
print("6- muestre el promedio de las ventas.")
print("7- muestre el nombre del mozo que logró la mayor venta.")
print("8- muestre el total a pagar por comisiones de ventas.")
print("9- muestre el promedio a pagar por comisiones de ventas.")
print("10-muestre el mayor importe a pagar por comisiones de ventas.")

ok=input("Ingrese una opcion del 1 al 10: ")

if ok =="1":
    e1()
    
elif ok =="2":
    e2()
    
elif ok =="3":
    e3()
    
elif ok =="4":
    e4()
    
elif ok =="5":
    e5()
    
elif ok =="6":
    e6()
    
elif ok =="7":
    e7()
    
elif ok =="8":
    e8()
    
elif ok =="9":
    e9()
    
elif ok =="10":
    e10()
