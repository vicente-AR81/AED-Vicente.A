n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
c = []
if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

for i in range(menor + 1, mayor):
    if i % 2 != 0:
        c.append(i)

print("Los numeros impares comprendidios entre sus numeros son:", c)
print("Descendente:", c[::-1])