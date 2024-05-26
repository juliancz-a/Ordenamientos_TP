# Hungarian folk dance  (QuickSort)

contador = 0
def swap(a: int, b: int):
    return b,a

def partition(array, low, high):
    pivot = array[low]  # El pivote es el primer elemento
    izq = low + 1
    der = high

    while True:
        # Encontrar el primer elemento menor que el pivote desde el final
        while der >= izq and array[der] >= pivot:
            der -= 1
        
        if der >= izq:
            # Intercambiar el pivote con el elemento menor encontrado
            array[low], array[der] = swap(array[low], array[der])
            pivot = array[der]
        
        # Encontrar el primer elemento mayor que el pivote desde el inicio
        while izq <= der and array[izq] <= pivot:
            izq += 1

        if izq <= der:
            # Intercambiar el pivote con el elemento mayor encontrado
            array[izq], array[der] = swap(array[izq], array[der])

        else:
        # Si los índices se cruzan, romper el bucle
            break

    # Intercambiar el pivote con el elemento en la posición de 'right'
    array[low], array[der] = swap(array[low], array[der])

    print(array)
    return der


        
def qsort(array, low, high) -> list:

    if low < high:
        pivot = partition(array, low, high)
        print(pivot)
        qsort(array, low, pivot - 1)
        qsort(array, pivot + 1, high)

array = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(f"Array inicial : {array}")

qsort(array, 0, len(array)- 1)

print(array)
