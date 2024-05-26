def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, low, high):
    pivot_index = low  # El pivote es el primer elemento
    pivot = array[pivot_index]
    
    left = low + 1
    right = high

    while True:
        # Buscar desde el final hacia el inicio hasta encontrar un elemento menor que el pivote
        while right >= left and array[right] >= pivot:
            right -= 1

        if right < left:
            break

        # Intercambiar el pivote con el elemento menor encontrado
        swap(array, pivot_index, right)
        pivot_index = right

        # Buscar desde el inicio hacia el final hasta encontrar un elemento mayor que el pivote
        while left <= right and array[left] <= pivot:
            left += 1

        if left > right:
            break

        # Intercambiar el pivote con el elemento mayor encontrado
        swap(array, pivot_index, left)
        pivot_index = left
    
    return pivot_index

def qsort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        qsort(array, low, pivot - 1)
        qsort(array, pivot + 1, high)

# Ejemplo de uso
array = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6,1,5,5,123,51,566,141,42,51,25,1,231,23415,51,5,1,23,32,1,5,7,8,2]
print(f"Array inicial: {array}")

low = 0
high = len(array) - 1

qsort(array, low, high)
print(f"Array ordenado: {array}")
