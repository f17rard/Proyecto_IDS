#aqui se definen las 4 funciones principales de la calculadora

def suma_n(num1 = float, num2 = float):
    """Funcion de suma que ocupa dos numeros"""
    resultado = num1+num2
    print(f"el resultado de la operación es: {resultado}")

def resta_n(num1 = float, num2 = float):
    """Funcion de resta que ocupa dos numeros"""
    resultado = num1-num2
    print(f"el resultado de la operación es: {resultado}")

def multi_n(num1 = float, num2 = float):
    """Funcion de multiplicación que ocupa dos numeros"""
    resultado = num1*num2
    print(f"el resultado de la operación es: {resultado}")

def division_n(num1 = float, num2 = float):
    """Funcion de división que ocupa dos numeros"""
    resultado = num1/num2
    print(f"el resultado de la operación es: {resultado}")
