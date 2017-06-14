import turtle
import math
from tkinter import*

ventana=Tk() 
ventana.title("MENU")
frame=Frame(ventana)
frame.grid(column=0,row=4,padx=(100,100),pady=(100,100))
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)
ventana.configure(width=640,height=480)
opcion="" 
opcion=StringVar()
b1=Button(frame,text='OPCION 1')
b1.grid(column=10,row=2)


t=turtle.Pen()

def area_cuadrado(L):
    area=L**2
    return  print("EL area del cuadrado es:",area)

def peri_cuadrado(L):
    peri=L*4
    return  print("EL  perimetro es:",peri)

def area_triangulo(b,h):
    area=b*h
    return  print("El area del triangulo es:",area)

def peri_triangulo(b):
    peri=b*3
    return  print("EL  perimetro es:",peri)

def peri_pent(L):
    peri=L*5
    return print("EL  perimetro es:",peri)

def area_pent(L,ap):
    area=(5*L*ap)/2
    return print("El area del pentagono:",area)

num=int(input("Ingrese el numero de lados de la figura que desea calcular el area y el perimetro:"))
if (num==4):
    print("SU FIGURA ES UN CUADRADO")
    L=int(input("Ingrese el tamaño del lado:"))
    
    area_cuadrado(L)
    peri_cuadrado(L)
    
elif (num==3):
    print("SU FIGURA ES UN TRIANGULO")
    b=int(input("Ingrese la base:"))
    h=int(input("Ingrese la altura:"))
    area_triangulo(b,h)
    peri_triangulo(b)
elif (num==5):
    print("SU FIGURA ES UN PENTAGONO")
    L=int(input("Ingrese la longuitud de los lados:"))
    ap=int(input("Ingrese el apotema:"))
    area_pent(L,ap)
    peri_pent(L)
    


def figura(lado,num):
    if(num<=5):
      
        for i in range(num):
           t.forward(lado)
           t.left(360/num)
    else:
        print("El numero de lados debe ser menor o igual a 5")

lado=int(input("Ingrese el tamaño de la figura:"))
figura(lado,num)



ventana.mainloop()







