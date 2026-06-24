print("______Transformador de Sistemas de Númeración.______")
print(f'-  Menú;  \n 1. Binario -> Decimal \n 2. Decimal -> Binario \n 3. Hexadecimal -> Decimal \n 4. Decimal -> Hexadecimal \n 5. Historial \n 6 Salida')
Prefijo_bin = [128,64,32,16,8,4,2,1]
Historial = {}
prefijo_hexa = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
while True:
    opcion = input('Ingrese una de las opciones enumeradas; ')
 
    if opcion == '1':
        print("______Convertidor de Binario a Decimal.______")
        número10 = 0
        binario = input('Ingrese un número binario: ')
        while len(binario) != 8 or any(caracter not in '01' for caracter in binario):
            print("Debe tener 8 caracteres binarios (1 o 0)")
            binario = input('Ingrese un número binario:')
        for bit, valor in zip(binario, Prefijo_bin):
            if bit == '1':
                número10 += valor
            elif bit == '0':
                número10 += 0
        print(f"Tú número binario {binario}, pasado a decimal es {número10}.")
        
    elif opcion == '2':
        print('_____Convertidor de Decimal a binario._____')         
        try:
            Decimal = int(input('Ingrese un número: '))
            while Decimal < 0 or Decimal > 255:
                print("Debe ser un número entero entre 0 y 255.")
                Decimal = int(input('Ingrese un número: '))
            copia = str(Decimal)
            resultado = ""
            for i in Prefijo_bin:
                if Decimal >= i:
                    resultado += "1"
                    Decimal = Decimal - i 
                elif Decimal < i:
                    resultado += "0"
                    Decimal = Decimal
            print(f"Tú número decimal {copia}, pasado a binario es {resultado}.")
        except:
            print('Prohibido Ingresar letras, Devuelta al Menú...')
    
    elif opcion == '3':
        print('_____Convertidor de Hexadecimal a Decimal._____')
        pos = [3,2,1,0]
        num_hexa = input('Ingrese un Número Hexadecimal: ')
        while len(num_hexa) != 4 or any(caracter not in '0123456789ABCDEFabcdef' for caracter in num_hexa):
            num_hexa = input('Ingrese un Número Hexadecimal: ')
            for j in range(len(pos)):
                if num_hexa[i]  :
                    print('En progreso...')

    elif opcion == '4':
        print('En progreso...')
    elif opcion == '4':
        print('En progreso...')
    elif opcion == '5':    
        print('En progreso...')
    elif opcion == '6':
        print('Adiooos...')
        break
    else:
        print("Opción Invalida")

                
