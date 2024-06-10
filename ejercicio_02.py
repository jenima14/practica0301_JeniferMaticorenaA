import cProfile

def dni(documento):  
    '''Escribir una función que lea dos ficheros csv con una lista larga
    de datos de personas (50 personas y 1000 personas) y llame a dos
    funciones que pongan su nombre en formato capitalizado y calculen
    la letra de DNI correspondiente. Realiza la comprobación de rendimiento
    con la librería cProfile y muestra los datos. Describe que indica cada
    dato que nos proporciona cProfile.'''
    import csv

    diccionario = {}
    resto = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22
    letras = list('TRWAGMYFPDXBNJZSQVHLCKE')
   
    for i in range(len(resto)):
        diccionario[resto[i]] = letras[i]

    if documento == '50' or documento == '1000':
        with open(documento+".csv") as file:
            lector = csv.reader(file)
            for j in lector:
                id = int(j[1]) % 23
                nombre = j[0].capitalize()
                identificación = j[1]
                letra_id = diccionario[id]
                print('Nombre: '+nombre+' DNI: '+identificación+''+letra_id)
    else:
        print("El documento " +documento+ " no fue encontrado")

# dni('50')
# dni('1000')

cProfile.run("dni('documento')")