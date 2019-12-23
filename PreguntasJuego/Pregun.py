import random as rn
print("Juego de preguntas")
print(".------------------.")
c=0
i=0
r=0
archi=open ("PreguntasJuego.csv","r")
t=rn.randint(1,87)
for datos in archi.readlines():
    
    reg=datos.replace("\n","").split(";")

    juego=rn.randint(1,87)
    

    if t<=juego and i<3 and c<5:
        b=int(reg[5])
        print(reg[0])
        print("Opcion 1: "+ reg[1])
        print("Opcion 2: "+ reg[2])
        print("Opcion 3: "+ reg[3])
        print("Opcion 4: "+ reg[4])
        a=int(input("Ingrese una opción:"))
        
        if a==b:
            print("Correcto\n")
            t=rn.randint(1,87)
            c=c+1
            r=r+1
        else:
            t=rn.randint(1,87)
            i=i+1
            r=r+1
            print(f"Incorrecto\nLa respuesta correcta es {reg[b]}\n")
            
if i==3:
    print(f"\nHas perdido en el round nro. {r}\nGAME OVER")
elif c==5:
    print(f"\nHas ganado en el round nro. {r}\nGAME OVER")

archi.close()

            





