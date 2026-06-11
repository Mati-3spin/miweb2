print("Bienvenido a mi despensa simple")

print("\nMenú:""\n1 Añadir a despensa""\n2 Mirar la despensa""\n3 Sacar total de objetos""\n4 Vaciar despensa""\n5+ Salir")
Despensa = []
while True:
    opción = input("¿Tú opción? ")    
    if opción == "1":
        cosa = input("Añade un elemento; ")
        Despensa.append(cosa)
    elif opción == "2":
        if len(Despensa) == 0:
            print("No hay elementos en la despensa")
        else:
            print("Tú Despensa:")
            for i,valor in enumerate(Despensa):
                print(f"En índice; {i} , Esta el objeto; {valor}")
    elif opción == "3":
        if len(Despensa) == 0:
            print("No hay elementos en la despensa")
        else:
            average = len(Despensa)
            print(f"Total: {average}")
    elif opción == "4":
        Despensa = []
        print("La despensa se ha vaciado.")
    else:
        print("Saliendo del programa...")
        break
    