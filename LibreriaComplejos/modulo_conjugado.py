#Modulo y Conjugado Complejos

import math
def ModComp(real,imaginario):
    
    operacion = math.sqrt(real**2+imaginario**2),

    print("El resultado es:",operacion)

def ConjComp(real,imaginario):

    imag = imaginario * -1
    res = real,imag

    print("El resultado es:",res)

def main():

    real = int(input("Digite el real "))
    imaginario = int(input("Digite el imaginario "))
    n = int(input("Si desea saber el modulo digite 1, si desea saber el conjugado digite 2."))

    if n == 1:
        ModComp(real,imaginario)
    elif n == 2:
        ConjComp(real,imaginario)
    else:
        print("Elija bien :D")
main()
