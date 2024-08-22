#Fase Complejos

import math

def fase(real,imaginario):
    
    faseR = math.atan2(imaginario,real)
    fase = math.degrees(faseR),

    print("\nLa fase es:",fase)

def main():

    real = int(input("Digite el numero real:"))
    imaginario = int(input("Digite el numero imaginario:"))
    fase(real,imaginario)

main()
