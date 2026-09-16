#ESCRIBIR UN PROGRAMA QUE IMPRIMA CADA UNO DE LOS TWRMINOS DE LA SERIE 2,5,7,10,12,15,17,....,1800. ADEMAS, CALCULE E IMPRIMA LA SUMA DE LOS TERMINOSS
# INICIALIZACION DE VARIABLES
# termino = 2
# suma_total = 0
# sumar_tres = True  # CONTROLA SI SUMAMOS 3 O 2

# print("Términos de la serie:")

# EL BUCLE SE EJECUTA MIENTRAS EL TEMRINO NO SUPERE EL NUMERO 1800
# while termino <= 1800:
#     print(termino)          # IMPRIME TEMRINO ACTUAL
#     suma_total += termino   # ACUMULA EN LA SUMA TOTAL
    
#     # Aplicamos el patrón alternado (+3, luego +2)
#     if sumar_tres == True:
#         termino += 3
#     else:
#         termino += 2
#         # CAMBIAMOS EL ESTADO DE LA ITERACION
#         sumar_tres = not sumar_tres

# # CUANDO FINALIZA EL BUCLE IMPRIMIMOS EL RESULTADO DEL BUCLE
# print("\n" + "="*30) #PERMITE *30 MULTIPLICAR Y QUE IMPRIMA EL = (IGUAL) 30 VECES SEGUIDAS
# print(f"La suma total de los términos es: {suma_total}")
# print("="*30)


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
aa
print(f'La suma total es de: {suma}')