#Fecha de entrega: 31/07/24

#Ejercicio 1: Lista de números pares.
#Escribe un programa que solicite al usuario ingresar 10 números
#y luego imprima una lista con los números pares ingresados.

numeros_pares = []

for i in range(10):
    num = int(input("ingrese un numero: "))
    if num % 2 == 0:
        numeros_pares.append(num)
print(f"los numeros pares son {numeros_pares}")


