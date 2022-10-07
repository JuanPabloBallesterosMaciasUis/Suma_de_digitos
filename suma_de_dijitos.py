# Ejercicio de suma de los dijitos

print("________________________________________")
print("|         La suma de los digitos        |")
print("|_______________________________________|")
print("")

#input
n = int(input("Digite un numero positivo: "))
suma = 0
n0 = n


if n>= 0:
    while n > 0 :
        n1 = n%10
        suma = suma + n1
        n = n//10
        
    print("La suma de los digitos del numero",n0,"es",suma)
else:
    print("Numero no valido")
