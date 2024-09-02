def ingreseNumero():

    numero01=float(input("Ingrese sumandp 01: "))
    numero02=float(input("Ingrese sumandp 02: "))
    return numero01,numero02

def suma(numero01,numero02):
    return numero01 + numero02

if __name__ == "__main__":
    num1,num2 = ingreseNumero()
    print(f"{num1} + {num2} = {suma(num1,num2)}")