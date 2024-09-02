class OperacionAritmeticas:

    def ingresoNumeros(self):
        numero01 = int(input("Ingrese primer número: "))
        numero02 = int(input("Ingrese segundo número: "))
        return numero01, numero02

    def suma(self, numero01, numero02):
        return numero01 + numero02


if __name__ == '_main_':
    operacion = OperacionAritmeticas()
    num1, num2 = operacion.ingresoNumeros()  # Llamada correcta al método
    print(f"{num1} + {num2} = {operacion.suma(num1, num2)}")