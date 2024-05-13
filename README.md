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


## Introducción. <a name="introducción"></a>

- El siguiente proyecto proporcionará información acerca de los algoritmos de ordenamiento trabajados en clase. Se analizará en profundidad el funcionamiento del "Quick Sort". Por otro lado, se desarrollará el algoritmo visto en el video y se presentarán sus ventajas, desventajas...


## :1234: Algoritmo QuickSort<a name="quicksort"></a>

### ¿Cómo funciona el algoritmo de ordenamiento Quick Sort?

- Quick Sort es un método que suele ser más rápido que los demás a la hora de ordenar elementos de un vector. 
- Implica tomar de un vector el ultimo de sus elementos para tomarlo con "pivot". De esta manera, el pivot divide el array entre los elementos iguales o menores que este, y los elementos iguales o mayores que este.

    ![QuickSortExample](https://blog.shahadmahmud.com/quicksort/qs3/)

- Una vez dividido el array en "subarrays", se volverá a repetir este procedimiento: cada "pedacito" de la lista tomará como pivot el último de sus elementos y hará la comparación formando nuevos subarrays, hasta que el vector no tenga más elementos con los cuales compararse. 

#### :scroll: Explicación paso a paso del código.

- Luego de definir un vector con elementos sin órden alguno, se llamará a la función quick_sort, la cual recibe tres parametros. Estos son: 
    - "array", siendo la lista en sí.
    - "low", como el primer elemento de la lista.
    - "high", como el último elemento de la lista. 
- Mientras haya un primer elemento diferente a un último elemento (que low sea menor que high) se ejecutará el sorteamiento.
    ##### Función "quick_sort"
~~~ Python 
    def quick_sort(array, low, high):
    if low < high:
        pi = particionar(array, low, high) 
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
~~~

- Lo primero que hace esta función es llamar a otra: particionar, la cual recibe los mismos tres parámetros. Ésta es la encargada de realizar, como bien su nombre lo dice, particionar el array a través de un pivot.
