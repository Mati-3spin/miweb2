'''lista_productos = {'clavos':50,'martillos':100,'pala': 4}
print("Menú")
producto = input("Ingrese su producto")
if producto in lista_productos:
    print(lista_productos[producto])
else:
    print("No se encuentra este producto")'''

notas = {'pin':20,'pong':56}
estudiante = input()
nota = int(input())
notas[estudiante] = nota
print(notas)
promedio = sum(notas.values()) / len(notas)
print(promedio)