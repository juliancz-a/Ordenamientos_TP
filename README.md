# Trabajo Práctico: Algoritmos de Ordenamiento.
 <center><img src="https://assets-global.website-files.com/606a802fcaa89bc357508cad/6123c034286044167618b263_7.png" width="800" height="500"></center>

## Integrantes :raising_hand:
- Julián Caceres

## Índice
- [Introducción.](#introducción)
- [Parte 1. Algoritmo Quick Sort.](#quicksort)
    - ¿Cómo funciona?
    - ¿Como emplear Quick Sort sin recursividad?
    - Diferencias entre Quick Sort con y sin recursividad.
- [Parte 2. Algoritmo Quick Sort Actvidad.](quicksort2)


## 0. Introducción. <a name="introducción"></a>

- El siguiente proyecto proporcionará información acerca de los algoritmos de ordenamiento trabajados en clase. Se analizará en profundidad el funcionamiento del "Quick Sort". Por otro lado, se desarrollará el algoritmo visto en el video y se presentarán sus ventajas, desventajas...


## 1. Algoritmo QuickSort. :1234:<a name="quicksort"></a>

### ¿Cómo funciona el algoritmo de ordenamiento Quick Sort?

- Quick Sort es un método que suele ser más rápido que los demás a la hora de ordenar elementos de un vector. 
- Implica tomar de un vector el ultimo de sus elementos para tomarlo con "pivot". De esta manera, el pivot divide el array entre los elementos iguales o menores que este, y los elementos mayores que este.

    ![QuickSortExample](https://blog.shahadmahmud.com/quicksort/qs3/)

- Una vez dividido el array en "subarrays", se volverá a repetir este procedimiento: cada "pedacito" de la lista tomará como pivot el último de sus elementos y hará la comparación formando nuevos subarrays, hasta que el vector no tenga más elementos con los cuales compararse. 

#### :scroll: Explicación paso a paso del código.

- Luego de definir un vector con elementos sin órden alguno, se llamará a la función quick_sort, la cual recibe tres parametros. Estos son: 
    - "array", siendo la lista en sí.
    - "low", como el primer elemento de la lista.
    - "high", como el último elemento de la lista. 
- Mientras haya un primer elemento diferente a un último elemento (que low sea menor que high) se ejecutará el sorteamiento.
    ##### :hash:Función "quick_sort":
~~~ Python 
    def quick_sort(array, low, high):
    if low < high:
        pi = particionar(array, low, high) 
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
~~~
- Lo primero que hace esta función es llamar a otra: particionar, la cual recibe los mismos tres parámetros. Ésta es la encargada de realizar, como bien su nombre lo dice, las particiones al array a través de un pivot.
    ##### :hash:Función "particionar":
- El primer paso será establecer el último elemento del array como el pivote.
- Luego se creará una nueva variable "i", que será utilizada para realizar el swap. Esta misma toma el valor del primer elemento menos una unidad. 
    - Se denominará swap al intercambio entre dos elementos de un vector.
- Lo siguiente que se realizará será un "recorrido" del vector, este será desde el primer elemento hasta el anteúltimo elemento, ya que el búcle "for" itera excluyendo el último valor asigando. Excluye, entonces, el pivot, ya que no necesitamos que se compare a sí mismo.
- Comparamos si los elementos son iguales o más pequeños que el pivot. Si se da la condición:
    -   A "i" se le suma 1 unidad.
    -   Se realizará el swap, a través de la función "swap":
        -   Del elemento en posición "i", con el elemento en posición "j" (el elemento recorrido que puede variar desde el primer elemento del vector hasta el anteúltimo).

- Pongamos en un ejemplo esto:
    - Tenemos la siguiente lista : [5,2,1,7,9,3]. El vector será [3].
    - i, sin entrar en la condicion del for, vale: "-1" (puesto a que el primer elemento se encuentra en posición "0").
    - Los elementos recorridos serán: [5,2,1,7,9].
    - [5] es más grande que el vector, no ingresa. Sin embargo, [2], el siguiente elemento, es más pequeño o igual que el vector. Se procede a hacer el swap.
    - Se intercambia el primer elemento [5] (porque i+1 = 0) con [2]. Quedará esto: [2,5,1,7,9,3].
    - Se encuentra otro número menor o igual que el vector: [1]. La variable "i" se le suma 1 y se realiza el swap de [5] con [1], porque ahora [5] se vuelve a encontrar en la posición "i" (1). Quedará: [2,1,5,7,9,3]. 
    
    - Ahora falta corregir la posición del pivot, que se encuentra en una posición incorrecta. La anteúltima línea intercambia la posición del elemento en posición "i" +  1, que es el elemento más grande que el pivot, siendo el [5], ya que "i" pasa a valer 2. Ahora el pivot queda en el "medio": [2,1,3,7,9,5].

~~~ Python
    def particionar(array, low, high):
    pivote = array[high] #
    i = low - 1 
        
    for j in range(low, high):
        if array[j] <= pivote: 
            i += 1 
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] ) 
    
    return i + 1
~~~

- La función "particionar" devuelve la posición del pivot (i+1). A partir de esta posición se llama de manera recursiva a la funcíon quick_sort para los subarrays menores o iguales al pivot y para los que son mayores a este:

~~~ Python
    quick_sort(array, low, pi - 1)
~~~
- En esta llamada se calcula el ordenamiento de los elementos menores o iguales al pivot, puesto a que el elemento máximo del subarray será la posición del pivot - 1.
- Se utilizamos el ejemplo anterior, la posición máxima será [1].

~~~ Python
    quick_sort(array, pi + 1, high)
~~~
- En esta llamada se calcula el ordenamiento de los elementos mayores, puesto a que la posición mínima del subarray será la posición del pivot + 1. Se excluirá al pivot y se ordenará hasta el último elemento, que será el nuevo pivot.
- En el ejemplo visto, la posición mínima será el [7], y la máxima el [5], siendo este último el nuevo pivot del subarray.


    
