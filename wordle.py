palabra_secreta = "limon"
letras_verificadas = []
cantidad_letras = 5

def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []

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

# definir la cantidad de intentos = variable
intentos = 0

while intentos < 6:
    print(f"Te quedan {6 - intentos} intentos")
    intentos = intentos + 1
    palabra_ingresada = input("\nIngrese una palabra: ")
    print(f"\nLa palabra ingresada es: {palabra_ingresada}")
    respuesta = verificador_palabra(palabra_ingresada, palabra_secreta)
    print(respuesta)

    if palabra_ingresada == palabra_secreta:
        print("\nAcertaste la palabra. GANASTE")
        break
    elif intentos == 6:
        print("\nLlegaste al limite de intentos. PERDEDOR")
