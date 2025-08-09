# habi_prueba_tecnica_2 JOAN SEBASTIAN DIAZ GOMEZ 
## Lo que necesito hacer:
--
Tengo un arreglo con números del 1 al 9 y algunos ceros. Los ceros actúan como separadores que dividen el arreglo en "bloques". Cada bloque necesita ser ordenado de menor a mayor, y luego todos los bloques se juntan separados por espacios.
### Mi estrategia va a ser:
Implementaré una clase principal llamada BlockProcessor que va a manejar todo el procesamiento. Esta clase será el núcleo de mi solución porque encapsula toda la lógica de manera organizada.
Dentro de BlockProcessor voy a crear estos métodos:

__init__() - Para inicializar con el arreglo de entrada

process_blocks() - El método principal que coordina todo y devuelve el resultado final

_split_into_blocks() - Un método privado que se encarga específicamente de dividir el arreglo en bloques usando los ceros como separadores

_sort_block() - Otro método privado que toma un bloque individual y lo ordena, además maneja el caso especial de bloques vacíos convirtiéndolos en "X"

### ¿Por qué esta estructura?
Es simple pero bien organizada. Cada método tiene una responsabilidad específica, lo que hace el código fácil de entender y mantener. La clase BlockProcessor actúa como una caja que recibe un arreglo desordenado y produce el resultado formateado.

Para asegurarme de que todo funciona bien, también implementaré una clase TestBlockProcessor usando unittest. Esta clase tendrá varios métodos de test para probar diferentes escenarios: el ejemplo básico, bloques vacíos, arreglos sin ceros, solo ceros, etc.

La idea es mantener todo simple pero funcional, sin complicaciones innecesarias.