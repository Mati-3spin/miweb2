print("Convertidor de binario a decimal")
prefijo = [128,64,32,16,8,4,2,1]
binario = input('Ingrese un número binario:')
while len(binario) != 8 and ('0' or '1') not in binario:
    print("Debe tener 8 prefijos (solo transforma a numeros decimales del 0 al 255)")
    binario = input('Ingrese un número binario:')
número = 0
for dato, valor in zip(binario, prefijo):
    if dato == '1':
        número += valor
    elif dato == '0':
        número += 0
print(número)
            

                
