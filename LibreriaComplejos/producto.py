#Producto de Complejos

def ProdComp(real1,real2,imag1,imag2):

    a = (real1 + real2)-(imag1 + imag2)
    b = (real1 + imag2)+(real2 + imag1)
    res = a,b

    print("El resultado de la multiplicacion es:",res)

def main():
    real1 = int(input("Digite el primer real "))
    real2 = int(input("Digite el segundo real "))
    imag1 = int(input("Digite el primer imaginario "))
    imag2 = int(input("Digite el segundo imaginario "))

    ProdComp(real1,real2,imag1,imag2)
main()
