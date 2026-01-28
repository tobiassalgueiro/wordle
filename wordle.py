letras_verificadas = []
cantidad_letras = 5
palabra_secreta = "holas"
palabra_ingresada = input("ingresa una palabra ")
intentos = 0


def verificador_palabra(palabra_ingresada, palabra_secreta):
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] # True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            letras_verificadas.append(palabra_ingresada[i])
    
    return letras_verificadas

while intentos < 6:
    print(f"te quedan {6 - intentos} intentos")
    intentos = intentos + 1
    palabra_ingresada = input("Ingrese una palabra")
    print(f"la palabra ingresada es: {palabra_ingresada}")

