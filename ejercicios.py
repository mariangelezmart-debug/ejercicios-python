def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    
    for caracter in texto:
        if caracter in vocales:
            contador += 1
            
    return contador

# Prueba del programa
frase = "Programacion en Python"
resultado = contar_vocales(frase)
print(f"La frase '{frase}' tiene {resultado} vocales.")
