from operaciones import suma_n, resta_n, multi_n, division_n

def menu():
    print("---CALCULADORA---")
    print("""Elija una función:
    1. suma
    2. resta
    3. multiplicación
    4. division
    5. salir""")
    n = int(input("Escriba: "))
    return n

key = True
while key:
    n = menu()
    if n == 1:
        print("-----SUMA-----")
        n1 = float(input("Digita un numero: "))
        n2 = float(input("Digita otro numero: "))
        suma_n(n1, n2)
    elif n == 2:
        print("----RESTA----")
        n1 = float(input("Digita un numero: "))
        n2 = float(input("Digita otro numero: "))
        resta_n(n1, n2)
    elif n == 3:
        print("---MULTIPLICACIÓN---")
        n1 = float(input("Digita un numero: "))
        n2 = float(input("Digita otro numero: "))
        multi_n(n1, n2)
    elif n == 4:
        print("---DIVISIÓN---")
        n1 = float(input("Digita un numero: "))
        n2 = float(input("Digita otro numero: "))
        division_n(n1, n2)
    elif n == 5:
        key = False
        