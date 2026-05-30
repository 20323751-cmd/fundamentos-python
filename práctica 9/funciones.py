# pre-definidas print(), type(), range(), input()

def saludar(nombre):
    print("Hola" , nombre)

    #Cesius a fahrenheit: (c * 1.8) + 32
    def convertir_a_fahreneit(c):
        #ingrese un valor
        return (c * 1.8) + 32
    
    #saludar("pedro")
    #saludar("juan")
   # saludar("sergio")

   print(convertir_a_fahrenheit(10))
print(convertir_a_fahrenheit(30))
print(convertir_a_fahrenheit(80))
