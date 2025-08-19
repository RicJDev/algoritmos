## Ciclos repetitivos

Antes de ver los ciclos como tal, es importante ver un par de conceptos relacionados

### Acumuladores y contadores

Estas son variables que utilizamos para manejar el incremento o el decremento de cantidades. Esto es posible gracias a que podemos escribir instrucciones como las siguientes:

```
mi_variable = mi_variable + 1; // cambia de uno a uno
mi_variable = mi_variable - 1;

mi_variable = mi_variable + mi_otra_variable; // desconocemos el valor almacenado en `mi_otra_variable`
mi_variable = mi_variable - mi_otra_variable;
```

Aumentando o disminuyendo la cantidad almacenada en `mi_variable`.

Los **contadores** hacen esto incrementando o decrementando en intervalos regulares, generalmente de uno a uno. Esto permite, precisamente, contar elementos.

Los **acumuladores**, por otro lado, incrementan o decrementan en cantidades que pueden variar. Esto permite acumularlas y obtener un total.

### Ciclo `Repetir-Hasta`

Este ejecuta una accion (o serie de acciones) y luego evalua si una condicion es cierta. En caso de ser cierta, deja de ejecutarse la accion (o acciones) y vuelve al flujo normal del programa. Su caracteristica principal es que el bloque de codigo que contiene se ejecuta al menos una vez.

Esta es su sintaxis:
```
Repetir
  <instrucciones>
  ...

  Hasta (<condicion>); // Deja de ejecutar las instrucciones cuando esta condicion es verdadera
Fin_Repetir
```

Y este un ejemplo de su uso:
```
var respuesta: Booleano;
var numero: Entero;

numero = 1;

Repetir
  Mostrar << "El numero esta ahorita en ", numero;

  Mostrar << "Quiere aumentar el numero actual? (0: no, 1: si)";
  Leer >> respuesta;

  numero = numero + 1;

  Hasta (respuesta = 0);
Fin_Repetir

Mostrar << "El numero al final quedo en ", numero;
```

### Ciclo `Mientras-Hacer`

Este tambien ejecuta una serie de acciones, pero a diferencia del `Repetir-Hasta` primero evalua la condicion, y si esta es cierta, ejecuta sus instrucciones. Repetira esto hasta que la condicion sea falsa, momento en el que volvera al flujo normal del programa.

Es especialmente util para hacer validaciones. Pero hay que tener cuidado y asegurar que en algun momento la condicion sera falsa, ya que de lo contrario no podra salir del ciclo, ejecutandose infinitamente.

Su sintaxis:
```
Mientras (<condicion>) Hacer;
  <instrucciones>
Fin_Mientras
```

Ejemplo de uso:
```
var cantidad: Entero;

Mostrar << "Ingrese la cantidad de veces que quiere lanzar los dados"
Leer >> cantidad;

Mientras (cantidad < 0 Or cantidad > 10) Hacer;
  Mostrar << "Cantidad de veces no valida. Ingrese nuevamente";
  Leer >> cantidad;
Fin_Mientras

Mostrar << "Bien. Hora de lanzar los dados..."
```
### Variables de iteracion

Iterar es repetir hasta obtener un resultado o hasta llegar al final de algo. Una **variable de iteracion** es una variable auxiliar que nos permite hacer repeticiones a lo largo de un ciclo.

Por ejemplo, podemos mostrar los numeros del 1 al 100 con un `Mientras-Hacer` utilizando una variable a la que llamaremos `i`.

```
var i: Entero;

i = 1;

Mientras (i <= 100) Hacer;
  Mostrar << i;
  i = i + 1;
Fin_Mientras
```

Como `i` va cambiando a lo largo del ciclo, podemos hacer repeticiones para cada uno de sus valores. En este caso, cada uno de los numeros del 1 al 100.

Este tipo de variables estan especialmente relacionadas a el siguiente ciclo a estudiar.

### Ciclo `Para-Hacer`

Su sintaxis seria:
```
Para (<varible> = <estado inicial> Hasta <varible> = <estado final>) Hacer; // La variable `i` aumenta en pasos de 1
  <instrucciones>
Fin_Para
```

Ejemplo de uso, mostrando los numeros del 1 al 100
```
var i: Entero;

Para (i = 1 Hasta i = 100) Hacer;
  Mostrar << i;
Fin_Para
```
