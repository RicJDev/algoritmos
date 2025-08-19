## Estructura condicional `Si-Entonces`

Esta estructura nos permite actuar tomando decisiones.

### Simple

```
Si (<condicion>) Entonces;
  // Esto se ejecuta si la condicion es cierta

  // ...
Fin_Si
```

### Doble

```
Si (<condicion 1>) Entonces;
  // Esto se ejecuta si la condicion 1 es cierta

  Sino
    // Esto se ejecuta si la condicion 1 es falsa

    // ...
Fin_Si
```

### Multiple

```
Si (<condicion 1>) Entonces;
  // Esto se ejecuta si la condicion 1 es cierta

  Sino
    Si (<condicion 2>) Entonces;
    // Esto se ejecuta si la condicion 2 es cierta

    Sino
      Si (<condicion 3>) Entonces;
        // Igual con la condicion 3

        Sino
          Si (<condicion n>) Entonces;
            // Y con la cantidad de condiciones que quieras

            // ...
          Fin_Si
      Fin_Si
  Fin_Si
Fin_Si
```

## Operadores

Estos son simbolos que permiten obtener valores de verdad (verdadero o falso) al aplicarlos a dos elementos. Dicho resultado se obtiene de combinar valores de verdad o de realizar comparaciones entre los elementos

### Logicos

Permiten hacer combinaciones de valores de verdad.

```
  var a, b: Booleano;

  a = 1;
  b = 1;

  Si (a And b) Entonces;
    Mostrar << "a y b son verdaderas";
  Fin_Si

  a = 1;
  b = 0;

  Si (a Or b) Entonces;
    Mostrar << "a o b son verdaderas";
  Fin_Si
```
Estan muy relacionados a la tabla de la verdad:

| a | b | a And b | a Or b |
|---|---|---------|--------|
| 1 | 1 |    1    |   1    |
| 1 | 0 |    0    |   1    |
| 0 | 1 |    0    |   1    |
| 0 | 0 |    0    |   0    |

Donde `1` es verdadero y `0` es falso.

### De comparacion

**Mayor que y menor que**

```
  var a, b: Entero;

  a = 1;
  b = 3;

  Si (a > b) Entonces;
    Mostrar << "a es mayor que b";

    Sino
      Mostrar << "a no es mayor que b";
  Fin_Si

  Si (a < b) Entonces;
    Mostrar << "a es menor que b";

    Sino
      Mostrar << "a no es menor que b";
  Fin_Si
```
**Igualdad y desigualdad**

```
  var a, b, c: Entero;

  a = 2;
  b = 3;
  c = b;

  // Aca usamos `=` aunque es mas usual `==` o `===`
  Si (a = c) Entonces;
    Mostrar << "a es igual a b";
  Fin_Si

  Si (a != b) Entonces;
    Mostrar << "a es desigual a b";
  Fin_Si
```
**Mayor o igual que y menor o igual que**

```
  var a, b: Entero;

  a = 3;
  b = 4;

  Si (a >= b) Entonces;
    Mostrar << "a es mayor o igual que b";

    Sino
      Mostrar << "a no es mayor o igual que b";
  Fin_Si

  Si (a <= b) Entonces;
    Mostrar << "a es menor o igual que b";

    Sino
      Mostrar << "a no es menor o igual que b";
  Fin_Si
```
