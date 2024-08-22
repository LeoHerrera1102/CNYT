#Coordenadas Cartesianas y Polares

import math

def Cart_Pol(real,imaginario):

    modulo = math.sqrt(real**2 + imaginario**2)
    anguloR = math.atan2(imaginario,real)
    anguloG = math.degrees(anguloR)
    res = modulo,anguloG

    print("Las coordenadas polares son:",res)

def Pol_Cart(modulo,angulo):

    x = modulo*math.cos(angulo)
    y = modulo*math.sin(angulo)
    res = x,y

    print("Las coordenadas cartesianas en radianes son:",res)

def main():

    n = int(input("Digite 1 si desea convertir de cartesianas a polares o 2 si lo desea al contrario."))
    if n == 1:
        real = int(input("Digite el numero real:"))
        imaginario = int(input("Digite el numero imaginario:"))
        Cart_Pol(real,imaginario)
    elif n == 2:
        modulo = int(input("Digite el modulo:"))
        angulo = float(input("Digite el angulo en radianes:"))
        Pol_Cart(modulo,angulo)
    else:
        print("Elija bien :D")
main()
