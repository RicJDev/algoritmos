## Trabajando con condicionales

Usaremos el mismo enunciado para mostrar dos enfoques a la hora de validar con condicionales.

**ENUNCIADO:**

> Cree un algoritmo que solicite dos numeros y calcule la raiz con el primer numero como indice y el segundo numero como radicando. Tome en cuenta que no se admiten numeros negativos para el calculo

Y ahora veremos como seria nuestro `Algoritmo Calculadora`. Notese que hay operadores que son ideales segun se use uno u otro enfoque

### Camino Feliz :D

Te enfocas en lo que quieres que sea verdadero, bueno o valido

```
  var indice: Entero;
  var radicando, resultado: Real;

  Mostrar << "Ingrese el indice de la raiz";
  Leer >> indice;
  Mostrar << "Ingrese el radicando de la raiz";
  Leer >> radicando;

  Si (indice >= 1 And radicando >= 0) Entonces;
    resultado = radicando ^ (1 / indice);

    Mostrar << "La raiz es igual a ", resultado;

    Sino
      Mostrar << "Datos no validos para la operacion";
  Fin_Si
```

### Camino Triste :(

Te enfocas en lo que puede que sea falso, malo o invalido

```
  var indice: Entero;
  var radicando, resultado: Real;

  Mostrar << "Ingrese el indice de la raiz";
  Leer >> indice;
  Mostrar << "Ingrese el radicando de la raiz";
  Leer >> radicando;

  Si (indice < 1 Or radicando < 0) Entonces;
    Mostrar << "Datos no validos para la operacion";

    Sino
      resultado = radicando ^ (1 / indice);

      Mostrar << "La raiz es igual a ", resultado;
  Fin_Si
```

### Ejercicio de los dados

> Se necesita un algoritmo que solicite los numeros de tres dados y muestre un mensaje dependiendo de la cantidad de 6 obtenidos:
>    - 6 en los tres dados: "Excelente"
>    - 6 en dos dados: "Muy bien"
>    - 6 en un solo dado: "Regular"
>    - Ningun 6: "Pesimo"
>
> Esto solo debe realizarse con datos previamente validados. En caso de haber datos invalidos, notificar al usuario y finalizar el programa

[Ver solucion](./dados.txt) 

### Ejercicio del carnet

>   Desarrolle un algoritmo que aplique un 10% de descuento en la compra de un usuario, en caso de poseer carnet de membresia. No olvide solicitar el nombre del mismo y validar el monto de la compra

[Ver solucion](./carnet.txt) 

