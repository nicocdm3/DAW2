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
    