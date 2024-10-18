# Verificar si un número es positivo, negativo o cero
# Descripción: Crea un programa que pida al usuario un número y verifique si es positivo, negativo o cero.

numero = int(input("Ingresa un número: "))
if numero > 0:
    print('Número Positivo')
elif(numero < 0):
    print('Número negativo')
else:
    print('Es cero')

# Determinar si un estudiante aprobó o no
#Descripción: Crea un programa que pida la calificación de un estudiante y determine si ha aprobado (60 o más) o no.

calificacion = int(input("Ingresa una calificación: "))
if calificacion >= 60:
    print('Aprobado')
else:
    print('Reprobado')

# Comprobar si un número es par o impar
# Descripción: Crea un programa que pida al usuario un número y determine si es par o impar.

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print('Número par')
else:
    print('Número impar')

# Verificar si un número está dentro de un rango
# Descripción: Crea un programa que pida al usuario un número y verifique si está en el rango de 1 a 10 (inclusive). 

numero = int(input("Ingresa un número: "))
if numero >=1 and numero <= 10:
    print('Esta en el rango 1 a 10')
else:
    print('Fuera de rango')

# Clasificación de Números
# Descripción: Crea una función que reciba una lista de números enteros y clasifique cada número como "positivo", "negativo" o "cero". La función debe devolver un diccionario que contenga el conteo de cada categoría.

numeros = [1, -2, 0, 3, -4, 0, 5]

def clasificar_numeros(numeros):
    clasificacion = {
        'positivos': 0,
        'negativos': 0,
        'ceros': 0
    }
    
    for numero in numeros:
        if numero > 0:
            clasificacion['positivos'] += 1
        elif numero < 0:
            clasificacion['negativos'] += 1
        else:
            clasificacion['ceros'] += 1
            
    return clasificacion

print (str(clasificar_numeros(numeros)))

# Cálculo de Tarifas de Envío
# Descripción: Diseña una función que calcule la tarifa de envío basada en el peso del paquete y el destino. La tarifa debe ser calculada usando las siguientes reglas:

"""
    Menos de 1 kg: $5
    De 1 a 5 kg: $10
    Más de 5 kg: $20
    Si el destino es internacional, sumar un recargo del 50% al costo total.
    Requisitos:
"""

peso = int(input("Ingresa el peso del paquete en kg:"))
destino = input("Indique si es Nacional o Internacional:")

def calcula_tarifa(peso, destino):
    costo = 0.0
    
    if peso < 1:
        costo = 5.0
    elif peso > 5:
        costo = 20.0
    else:
        costo = 10.0

    if destino == "Internacional":
        costo = costo + (costo*0.5) 
            
    return costo

print (str(calcula_tarifa(peso, destino)))