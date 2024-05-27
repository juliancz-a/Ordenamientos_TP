# Hungarian folk dance  (QuickSort)
import time
contador = 0
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, low, high):
    pivot_index = low  # El pivote es el primer elemento
    pivot = array[pivot_index]
    
    izq = low + 1
    der = high

    while True:
        # Buscar desde el final hacia el inicio hasta encontrar un elemento menor que el pivot
        while der >= izq and array[der] >= pivot:
            der -= 1

        if der < izq:
            break

        # Intercambiar el pivot con el elemento menor encontrado
        swap(array, pivot_index, der)
        pivot_index = der # 

        # Buscar desde el inicio hacia el final hasta encontrar un elemento mayor que el pivote
        while izq <= der and array[izq] <= pivot:
            izq += 1

        if izq > der:
            break

        # Intercambiar el pivote con el elemento mayor encontrado
        swap(array, pivot_index, izq)
        pivot_index = izq
    
    return pivot_index

def qsort(array, low, high):
    global contador
    contador += 1
    if low < high:
        pivot_index = partition(array, low, high)
        qsort(array, low, pivot_index - 1)
        qsort(array, pivot_index + 1, high)

array = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
print(f"Array inicial : {array}")
start = time.time()

qsort(array, 0, len(array)- 1)

end = time.time()
print(f"Tiempo: {(end - start)*1000}")
print(f"Repeticiones: {contador}")

print(f"Array ordenado : {array}")

