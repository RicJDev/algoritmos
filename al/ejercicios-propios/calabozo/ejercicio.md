### EL CALABOZO DE LAS MATRICES

Tenemos este calabozo:

```
...#......
........#.
.#........
.....#....
.........#
....#.....
#.........
.....^.#..
..#.......
........#.
```

El `^` representa a nuestro héroe, quien debe escapar de este terrible calabozo. Para ello debe moverse siguiendo unas reglas (o morirá). Empieza moviéndose hacia arriba siguiendo los puntos (`.`) y al chocar con un obstáculo (representado por un `#`) gira noventa grados a su derecha, cambiando su dirección. Hará esto hasta quedar fuera del calabozo.

Ahora nuestro héroe necesita ayuda extra de nuestra parte. Al salir le espera un troll armado con un mazo, que le preguntará por cuántas casillas ha pasado en su trayecto. La pregunta tiene truco, pues hay que contar _las casillas_ no _los pasos_. Es decir, los puntos (`.`) por las cuales se ha pasado, sin importar si se ha pasado por ellos más de una vez. Hay que asegurarse de responder bien.

Desarrolla un algoritmo que permita realizar este conteo y de ser posible prográmalo para dar respuesta con este calabozo en particular.
