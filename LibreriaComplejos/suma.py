#Suma Complejos

def sumaComp(real1,real2,imag1,imag2):
    
    real = real1 + real2
    imag = imag1 + imag2
    res = real,imag
    
    print("El resultado de la suma es:",res)

def main():
    real1 = int(input("Digite el primer real"))
    real2 = int(input("Digite el segundo real"))
    imag1 = int(input("Digite el primer imaginario"))
    imag2 = int(input("Digite el segundo imaginario"))

    sumaComp(real1,real2,imag1,imag2)
main()
