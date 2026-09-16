
def inicio():

    str : miCadena = "Daniel Perez"


    print('BIENVENIDO A TU EXAMEN');


    # Pedimos el número y lo transformamos a entero con int()
    numero = int(input("Introduce un número entero: "))

    # Ya puedes operar con él
    resultado = numero * 2

    if numero >= 5 :
        print("Has Aprobado :)")
    else:
        print("Has Desaprobado")

def ejercicio9():
    termino: int = 2
    suma: int = 2
    i: int = 1
    while termino < 1800:
        if i % 2 == 1:
            termino +=3
        else:
            termino +=2
        i+=1
        print(f'{i} : Valor -> {termino}')
        suma += termino

    print(f'La suma total es de: {suma}')

def ejercicio10():
# Ejercicio 10
# HACER UN PROGRAMA QUE LEA POR TECLADO EL NUMERO N E IMPRIMA UN TRIANGULO RECTANGULO DE N FILAS. EJ: N=5, SE PINTARA LO SIGUIENTE:
# 1
# 12
# 123
# 1234
# 12345

    numero: int = 1
    filas: int = 5
    estrella = '*'

    for i in range(filas):
        print(estrella)
        estrella += '*'

def ejercicio11():
    # MODIFICA 
    # 1
    # 12
    # 123
    # 1234
    # 12345

    numero: int = 1
    filas: int = 5
    estrella = ''

    for i in range(1,5):
        estrella += f'{i}'
        print(estrella)
    
    
    
    

if __name__ == '__main__':
    ejercicio11()

