# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:33:18 2019

@author: Alumno
"""

#Una empresa cuenta con un sistema que le permite calcular los sueldos de sus empleados.
#El sistema cuenta con un archivo que almacena:
#el número de legajo del empleado, el nombre completo, la descripción de la categoría, 
#fecha de ingreso, años de ingreso, años de antigüedad y sueldo básico. 

"""def orden1():
    
    import random as rn
    archi=open("Datos-TP6.csv","r")
    for datos in archi.readlines():
        registro=datos.replace("\n","").split(";")
        antiguedad=registro[6]*registro[5]*1.2/100
        presente=(registro[6]+antiguedad)*8.35/100
        sueldo=registro[6]+antiguedad+presente
    print (registro[1].ljust(25,"-"),registro[2]-ljust(25,"-"),antiguedad,presente,sueldo)
           
orden1()"""

def orden1():
    
    archi=open("Datos-TP6.csv","r")
    for datos in archi.readlines():
        reg=datos.replace("\n","").split(";")
        
        basico=float(reg[6].replace(",","."))
        ant= float (reg[5].replace(",","."))
        
        antiguedad=round(basico*ant*1.2/100,1)
        presente=round((basico+antiguedad)*8.35/100,1)
        sueldo=round(basico+antiguedad+presente,1)
        
        print (reg[1].ljust(20, " ")+reg[2].ljust(23, " ")+"$"+str(antiguedad).ljust(10, " ")+"$"+str(presente).ljust(10, " ")+"$"+str(sueldo).ljust(10, " ")  )
    
    archi.close
    print("--------------------")       


def orden2():
    
    anti=int(input("Ingrese minimo de antiguedad requerida: "))
    archi=open("Datos-TP6.csv","r")
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        anti_emp=int(reg[5])
        basico=float(reg[6].replace(",","."))
        
        if anti<anti_emp:
            print("\n"+reg[1].ljust(20," ")+reg[2].ljust(20," ")+"$"+str(basico).ljust(20," ")+"\n")
            
    archi.close
    print("--------------------")    


        
def orden3():
    
    archi_read=open("Datos-TP6.csv","r")
    archi_write=open("Import.csv","w")
    for datos in archi_read.readlines():
        reg=datos.replace("\n","").split(";")
        
        basico=float(reg[6].replace(",","."))
        ant=float(reg[5])
        
        antiguedad=round(basico*ant*1.2/100,1)
        presente=round((basico+antiguedad)*8.35/100,1)
        sueldo=round(basico+antiguedad+presente,1)
        
        archi_write.write(reg[1]+";"+reg[2]+";"+str(basico).replace(".",",")+";"+str(antiguedad).replace(".",",")+";"+str(presente).replace(".",",")+";"+str(sueldo).replace(".",",")+"\n")
        print ("\n"+reg[1]+";"+reg[2]+";"+str(basico).replace(".",",")+";"+str(antiguedad).replace(".",",")+";"+str(presente).replace(".",",")+";"+str(sueldo).replace(".",",")+"\n")
    archi_read.close
    archi_write.close
    print("Se guardaron los datos")
    

    

def orden4():
    
    cat=str(input("\nMaestranza \nAdministrativo \nPersonal Auxiliar \nVendedor \nCajero \nIngrese categoria requerida: "))
    archi=open("Datos-TP6.csv","r")
    
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        basico=float(reg[6].replace(",","."))
        
        if cat.upper()==reg[2].upper():
            print("--------------------")  
            print(reg[1].ljust(20," ")+reg[2].ljust(20," ")+"$"+str(basico).ljust(20," ")+"\n")
            
    archi.close
    print("--------------------")   
    

def orden5():
    
    anti=int(input("Ingrese minimo de antiguedad requerida: "))
    archi=open("Datos-TP6.csv","r")
    arch=open("orden5.csv","w")
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        anti_emp=int(reg[5])
        basico=float(reg[6].replace(",","."))
        
        if anti<anti_emp:
            arch.write("\n"+reg[1].ljust(20," ")+reg[2].ljust(20," ")+"$"+str(basico).ljust(20," ")+"\n")
            
    archi.close
    arch.close
    print("Se guardaron los datos")
    
def orden6():
    
    leg=int(input("Ingrese numero de legajo: "))
    archi=open("Datos-TP6.csv","r")
    for data in archireadlines():
        reg=data.replace("\n","").split(";")
        basico=float(reg[6].replace(",","."))
        antiguedad=round(basico*ant*1.2/100,1)
        presente=round((basico+antiguedad)*8.35/100,1)
        sueldo=round(basico+antiguedad+presente,1)
        
        if leg==reg[0]:
            print ("\n"+reg[1]+";"+reg[2]+";"+str(basico).replace(".",",")+";"+str(antiguedad).replace(".",",")+";"+str(presente).replace(".",",")+";"+str(sueldo).replace(".",",")+"\n")        
    archi.close
    print ("---------------------")
    
def orden7():
    
    archi=open("Datos-TP6.csv","r")
    total=0
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        basico=float(reg[6].replace(",","."))
        total=total+basico
            
    print (f"Suma sueldos: ${total}")
    archi.close
    

def orden8():
    archi=open("Datos-TP6.csv","r")
    total=0
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        basico=float(reg[6].replace(",","."))
        if basico>total:
            total=basico
            
    print (f"El mayor sueldo es de ${total}")
    archi.close
    print("----------------------")
    
def orden9():
    
    total=0
    archi=open("Datos-TP6.csv","r")
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        
        ant=float(reg[5])
        basico=float(reg[6].replace(",","."))
        
        antiguedad=round(basico*ant*1.2/100,1)
        if antiguedad:
            total=total+antiguedad
        
    print (f"El monto a pagar poradicionales es ${total}")
    archi.close
    print("----------------------")
        
def orden10():
    
    promedio=0
    total=0
    archi=open("Datos-TP6.csv","r")
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        
        ant=float(reg[5])
        basico=float(reg[6].replace(",","."))
        
        antiguedad=round(basico*ant*1.2/100,1)
        if antiguedad:
            total=total+antiguedad
            promedio=promedio+1
        
    x=total/promedio    
    print (f"El promedio a pagar por adicionales es ${x}")
    archi.close
    print("----------------------")


def orden11():
    
    total=0
    archi=open("Datos-TP6.csv","r")

    for datos in archi.readlines():
        reg=datos.replace("\n","").split(";")
        
        basico=float(reg[6].replace(",","."))
        ant=float(reg[5])
        
        antiguedad=round(basico*ant*1.2/100,1)
        presente=round((basico+antiguedad)*8.35/100,1)
        if presente:
            total=total+presente
    
    print (f"El monto a pagar por presentismos es ${total}")
    archi.close
    print("----------------------") 
    
        
def orden12():
    
    promedio=0
    total=0
    archi=open("Datos-TP6.csv","r")
    for data in archi.readlines():
        reg=data.replace("\n","").split(";")
        
        ant=float(reg[5])
        basico=float(reg[6].replace(",","."))
        antiguedad=round(basico*ant*1.2/100,1)
        presente=round((basico+antiguedad)*8.35/100,1)        

        if presente:
            total=total+presente
            promedio=promedio+1
        
    x=round(total/promedio,1)  
    print (f"El promedio a pagar por presentismos es ${x}")
    archi.close
    print("----------------------")
    
orden12()