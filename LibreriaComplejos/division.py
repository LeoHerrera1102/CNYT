#Division Complejos

#Suma Complejos

def DivComp(real1,real2,imag1,imag2):
    
    a = (real1*real2)+(imag1*imag2)
    b = (real1*imag1)+(real2*imag2)
    c = (real2**2+imag2**2)
    d = a/c
    e = b/c
    res = d,e
    
    print("El resultado de la suma es:",res)

def main():
    real1 = int(input("Digite el primer real "))
    real2 = int(input("Digite el segundo real "))
    imag1 = int(input("Digite el primer imaginario "))
    imag2 = int(input("Digite el segundo imaginario "))

    DivComp(real1,real2,imag1,imag2)
main()
