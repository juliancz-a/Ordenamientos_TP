def swap(a: int, b: int):
    return b, a

def partition(array, low, high):
    pivot = array[low]  # El pivote es el primer elemento
    left = low + 1
    right = high

    while left <= right:
        # Encontrar el primer elemento menor que el pivote desde el final
        while right >= left and array[right] >= pivot:
            right -= 1
        
        if right >= left:
            # Intercambiar el pivote con el elemento menor encontrado
            array[low], array[right] = swap(array[low], array[right])
            pivot = array[right]
        
        # Encontrar el primer elemento mayor que el pivote desde el inicio
        while left <= right and array[left] <= pivot:
            left += 1

        if left <= right:
            # Intercambiar el pivote con el elemento mayor encontrado
            array[left], array[right] = swap(array[left], array[right])

    # Colocar el pivote en su posición correcta
    array[low], array[right] = swap(array[low], array[right])

    return right

# Ejemplo de uso
array = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(f"Array inicial: {array}")

low = 0
high = len(array) - 1


def qsort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        qsort(array, low, pivot - 1)
        qsort(array, pivot + 1, high)

#jemplo de uso
qsort(array,low,high)
print(array)