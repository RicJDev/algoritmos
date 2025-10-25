## Ejercicio

Diseña un algoritmo para cargar un vector de `n` posiciones. Luego de que esté cargado dicho vector con valores enteros positivos, con la ayuda de un menú de opciones, desarrolle los siguientes procesos:

- Operaciones aritméticas (suma, resta, multiplicación y división de todos los elementos del vector)
- Copia de todos los elementos del vector en otro vector (backup)
- Cantidad de números pares e impares
- Ordenar elementos de menor a mayor
- Búsqueda de un elemento dentro de un vector
- Mayor valor contenido en el vector
- Mostrar todas las operaciones
- Borrar elementos del vector
- Salir del sistema

Utilice sub algoritmos para la elaboración de los procesos solicitados y habilite para que los usuarios puedan volver a cargar el vector

## Auitoría 

Se han cambiado los nombres de las variables `s`, `e` y `r` para evitar una colisión de nombres: 

- `s` ahora se llama `suma`. Evitando que se parezca a la palabra reservada para indicar variables de salida.
- `e` ahora se llama `t`. Evitando que se parezca a la palabra reservada para indicar variables de entrada.
- `r` ahora se llama `res`. Para distinguirla de otra variable declarada como `r`.

Se ha modificado el uso de un procedimiento par obtener el numero mayor y usado una función en su lugar. Esto ahorra pasar una variable por parámetro, lo que ayuda a la legibilidad y mantenibilidad. Y tiene más sentido al tratarse de un único valor a calcular.

Se ha desarrollado una versión propia del algoritmo de ordenamiento con método de burbuja que evita acceder a índices fuera del arreglo.

## Árbol de archivos de mi solución

```
.
├── README.md
└── src
    ├── backend
    │   ├── aritmetica.gabo.txt
    │   ├── busqueda.gabo.txt
    │   ├── mayor.gabo.txt
    │   ├── ordenado.gabo.txt
    │   ├── par_impar.gabo.txt
    │   └── respaldo.gabo.txt
    ├── frontend
    │   ├── borrar.gabo.txt
    │   ├── datos.gabo.txt
    │   ├── elemento_busqueda.gabo.txt
    │   ├── impresiones
    │   │   ├── impresion_aritmetica.gabo.txt
    │   │   ├── impresion_busqueda.gabo.txt
    │   │   ├── impresion_mayor.gabo.txt
    │   │   ├── impresion_ordenado.gabo.txt
    │   │   ├── impresion_par_impar.gabo.txt
    │   │   └── impresion_respaldo.gabo.txt
    │   └── pantalla.gabo.txt
    └── principal.gabo.txt
```
