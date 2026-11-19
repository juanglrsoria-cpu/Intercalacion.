# Metodo de ordenamiento: Intercalacion
# Ejercicio: Combinar dos listas de numeros ordenadas.


def intercalacion(lista1, lista2):
    resultado = []
    i = 0
    j = 0

    # Compara elementos de ambas listas y agrega el menor.
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agrega los elementos que quedaron pendientes.
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado


if __name__ == "__main__":
    lista1 = [2, 8, 15, 23, 40]
    lista2 = [5, 10, 18, 30, 45]


    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Resultado de la intercalacion:", intercalacion(lista1, lista2))
