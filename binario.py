print("______Convertidor a sistemas Númericos.______")
prefijo_bin = [128,64,32,16,8,4,2,1]
binario = input('Ingrese un número binario: ')
while len(binario) != 8 and ('0' or '1') not in binario:
    print("Debe tener 8 caracteres(números decimales del 0 al 255), y los números mayores a 1 se consideran 0")
    binario = input('Ingrese un número binario:')
número10 = 0
for bit, valor in zip(binario, prefijo_bin):
    if bit == '1':
        número10 += valor
    elif bit == '0':
        número10 += 0
print(f"Tú número binario {binario}, pasado a decimal es {número10}.")

                
