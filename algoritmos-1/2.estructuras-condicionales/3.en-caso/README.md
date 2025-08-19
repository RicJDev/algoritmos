## Estructura `En_Caso`

Esta estructura sirve para evaluar múltiples valores para una variable. Pero dado a que estamos trabando con una sintaxis diseñada por el profesor, hay algunas consideraciones de las que me gustaría hablar, ya que su sintaxis no se ajusta por completo a cómo funciona esta estructura en la mayoría de lenguajes

### El `En_Caso` típico

Esta sería una sintaxis más real.

```
  En_Caso (<variable>) Sea;
    Caso(<valor 1>);
      // Instrucciones para el valor 1

    Caso(<valor 2>);
      // Instrucciones para el valor 2

    Caso(<valor 3>);
      // Instrucciones para el valor 3

    ...

    Caso(<valor n>);
      // Instrucciones para el valor n

    Otro_Caso
      // Instrucciones por defecto
      // Se ejecuta si el valor de la variable no coincide con ninguno de valores anteriores
  Fin_Caso
```

Puesto en un ejemplo, sería así:

```
  var a: Entero;
  a = 3;

  En_Caso (a) Sea;
    Caso(5);
      Mostrar << "a es un cinco";
    Caso(3);
      Mostrar << "a es un tres";
    Caso(8);
      Mostrar << "a es un ocho";
    Otro_Caso
      Mostrar << "No entiendo qué es a";
  Fin_Caso
```

### El `En_Caso` exótico

Y esta es la sintaxis que manejaremos:

```
  En_Caso (<condicion>) Sea;
    Caso(<comparacion 1>);
      // Instrucciones para la comparacion 1

    Caso(<comparacion 2>);
      // Instrucciones para la comparacion 2

    Caso(<comparacion 3>);
      // Instrucciones para la comparacion 3

    ...

    Caso(<comparacion n>);
      // Instrucciones para la comparacion n

    Otro_Caso
      // Instrucciones por defecto
      // Se ejecuta si ninguna de las comparaciones anteriores es verdadera
  Fin_Caso
```

La cual parece hecha con la intención de combinar las estructuras condicionales con la del `En_Caso`. Esto queda más claro en el ejemplo:

```
  var a: Entero;
  a = 8;

  // Dicho sea de paso, <condicion> debe ser verdadera para ejecutar el `En_Caso`
  En_Caso (a > 0) Sea;
    Caso(a = 5);
      Mostrar << "a es un cinco";
    Caso(a = 3);
      Mostrar << "a es un tres";
    Caso(a = 8);
      Mostrar << "a es un ocho";
    Otro_Caso
      Mostrar << "No entiendo qué es a";
  Fin_Caso
```

## En conclusión...

Esto sigue siendo pseudo código. La sintaxis puedes ajustarla cómo necesites si te la creas tú mismo. Sin embargo considero importante dejar este tema claro debido a que me generó mucha confusión en su momento y no quisiera que a otros les pase.

## Dados exóticos

Recordemos el ejercicio de los Dados.

> Se necesita un algoritmo que solicite los numeros de tres dados y muestre un mensaje dependiendo de la cantidad de 6 obtenidos:
>    - 6 en los tres dados: "Excelente"
>    - 6 en dos dados: "Muy bien"
>    - 6 en un solo dado: "Regular"
>    - Ningun 6: "Pesimo"
>
> Esto solo debe realizarse con datos previamente validados. En caso de haber datos invalidos, notificar al usuario y finalizar el programa

[Aquí está su solución usando el `En_Caso`](./dados-exotico.txt) 
