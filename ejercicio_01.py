#CÓDIGO DE EJERCICIO RECURSIVO:
import datetime

comienzo = datetime.datetime.now()
def Fibonacci_Recursiva(n):
    '''una función que reciba un número entero positivo n y calcule el
        número de fibonacci asociado a ese número de manera recursiva
        Parámetro:
            Escribir un número entero positivo'''
    
    if n <= 1:
        return 1
    else:
        return Fibonacci_Recursiva(n-1) + Fibonacci_Recursiva(n-2)
   
usuario = int(input("Escriba un número entero: "))
print(Fibonacci_Recursiva(usuario))

final = datetime.datetime.now()
print(final - comienzo)

#CÓDIGO DE EJERCICIO BUCLE:
import datetime

Comienzo = datetime.datetime.now()
def Fibonacci_Bucle(n):
    '''Escribir dos funciones, una función que reciba un número entero 
    positivo n y calcule el número de fibonacci asociado a ese número 
    de manera recursiva y otra función que haga la misma operación pero 
    con bucles.
    Con ambas funciones, calcular y comparar el tiempo de ejecución para 
    n = (1, 10, 20, 30 y 40) por fuerza bruta.'''

    primero = 0
    segundo = 1
    tercero = 0
    lista = [0,1]
    for j in range(n):
        tercero = primero + segundo
        lista.append(tercero)
        primero = segundo
        segundo = tercero
    return lista[-1]

print(Fibonacci_Bucle(1))
#print(Fibonacci_Bucle(10))
#print(Fibonacci_Bucle(20))
#print(Fibonacci_Bucle(30))
#print(Fibonacci_Bucle(40))
Fin = datetime.datetime.now()
print(f"{Fin} - {Comienzo} = {Fin - Comienzo}")