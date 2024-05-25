# Hungarian folk dance  (QuickSort)


array = [3,0,1,8,7,2,5,4,9,6]

def swap(a: int, b: int):
    return b,a

def partition(array, low, high):
    pivot = array[low] #pivot es el primer elemento de la lista
    i = low + 1
    
    for j in range (high, low, -1): #Desde el último elemento, hasta el anteúltimo (desde mayor a menor)
        flag_swap = False
        if array[j] <= pivot:
            i -= 1
            print(array[j])
            print(array[i])
            array[j], array[i] = swap(array[j], array[i])
            flag_swap = True
            if flag_swap:
                pivot = array[low + 1]
            print(array)
    
    array[i - 1], array[low] = swap(array[i - 1], array[low])

    return i - 1

def qsort(array, low, high) -> list:

    if low < high:
        p = partition(array, low, high)
        qsort(array, low, p - 1)
        qsort(array, p + 1, high)


qsort(array, 0, len(array) - 1)

print(array)
