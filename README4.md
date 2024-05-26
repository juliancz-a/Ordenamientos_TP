## 4.
# Eficiencia en el caso promedio:

### QuickSort: Tiene una complejidad de tiempo promedio de O(n log n), es decir, grandes conjuntos de datos de manera muy eficiente en comparación con otros algoritmos de ordenamiento. Lo que lo hace mucho más eficiente que Burbujeo y Selección para conjuntos de datos grandes.

### Burbujeo: Tiene una complejidad de tiempo promedio de O(n^2) o mejor dicho, que tiene una complejidad de tiempo de ejecución que crece de forma cuadrática con respecto al tamaño del conjunto de datos. Lo que lo hace menos eficiente que QuickSort, especialmente para conjuntos de datos grandes.

### Selección: También tiene una complejidad de tiempo promedio de O(n^2), por lo que es menos eficiente que QuickSort en términos de tiempo de ejecución en conjuntos de datos grandes.

# Eficiencia en el peor caso:

### QuickSort: Puede degradarse a O(n^2) en el peor caso si el pivote elegido divide la lista de manera desigual. Sin embargo, esto es poco probable en la práctica si se elige un pivote adecuado.

### Burbujeo: Siempre tiene una complejidad de tiempo de O(n^2), ya que realiza un número cuadrático de comparaciones e intercambios.

### Selección: También siempre tiene una complejidad de tiempo de O(n^2), ya que realiza un número cuadrático de comparaciones y movimientos.

# Estabilidad:

### QuickSort: No es estable, lo que significa que no necesariamente preserva el orden relativo de los elementos con valores iguales.

### Burbujeo: Es estable, ya que solo intercambia elementos adyacentes si son inversos.

### Selección: No es estable, ya que puede cambiar el orden relativo de los elementos con valores iguales.

# Uso de memoria:

### QuickSort: Puede ser implementado in-place, lo que significa que no requiere memoria adicional más allá de la lista que está siendo ordenada. Esto lo hace eficiente en términos de uso de memoria.

### Burbujeo: Requiere memoria adicional para realizar intercambios entre elementos.

### Selección: Requiere memoria adicional para realizar intercambios entre elementos.

## En resumen, QuickSort es generalmente más eficiente que Burbujeo y Selección en términos de tiempo de ejecución y es especialmente eficiente para conjuntos de datos grandes. Sin embargo, los algoritmos de Burbujeo y Selección son más simples de implementar y pueden ser útiles para conjuntos de datos pequeños o en situaciones donde la eficiencia no es crítica.
