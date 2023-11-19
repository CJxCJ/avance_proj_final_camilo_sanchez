# Proyecto final - Code house

![logo_codehouse](https://github.com/CJxCJ/proyecto_final_camilo_sanchez/assets/115903431/68571d21-36d3-4969-b173-b861dfbba744)

## Camilo Jose Sanchez Vilamar

# Proyecto final seleccionado juego de ahorcado 

## - Para empezar el proyecto se realizó un desglose de las características que quería que tuviera el juego, la mayoría de Estas ideas se implementaron en el desarrollo del programa aunque con diferente enfoque ya que se fue cambiando durante el proceso el funcionamiento y el flujo del programa.
 
1. Primero un listado con mil palabras de diferente cantidad de caracteres. Como característica extra u opcional soporte para diferentes idiomas 

2. Selector de dificultad, acá al principio se deseaba que según la dificultad que se escogiera se tomara una palabra más larga del listado

3. Seleccionar la cantidad de intentos, el cual diría relacionado también con la dificultad 

4. Mostrar la cantidad de caracteres que tiene la palabra además de imprimir los espacios con un "_" para mostrar la longitud de la palabra.7 

5. Pedir al usuario que ingrese una letra y comparar si está en la palabra o no 

6. Si la letra se encuentra en la palabra reemplazarla en el espacio y si no descontar un intento en El Ahorcado, como característica opcional dar la opción de pedir pista

7. Si el usuario encuentra la palabra Mostrar un mensaje felicitaciones y si pierde uno de derrota 

8. Preguntar al usuario si quiere jugar de nuevo, donde un sí reinicia el programa y un no lo termina 

9. CARACTERISTICAS EXTRA: Un temporizador, dibujo de un ahorcado, modo para dos personas, cuenta regresiva y un easter-egg.

## LISTADO DE PALABRAS:

El primer paso fue las palabras, donde al principio Pensé en generarlas automáticamente con python pero al final la idea fue descartada debido a problemas de generación de palabras, luego opté porque una IA las escribiera pero al igual que python tuvo error de generaciones además de repetir palabras y distintos problemas gramaticales, pensé en usar una biblioteca descargada de internet pero al final me fue más sencillo y para cortar tiempo escribir Las mil palabras (800 ya que 200 las saco una IA) y usarlas como un listado 

## ESCOGER UNA PALABRA ALEATORIA:

Para esto importa la librería random e investiga en internet cómo utilizarla al principio simplemente selecciona una palabra aleatoria con la función seleccionar palabra y la dificultad, ya cuando el proyecto estaba casi terminando investigué un poco más para poder hacer la selección de palabra según su cantidad de caracteres dejándonos una función donde se analiza si la palabra es igual o mayor según la cantidad de caracteres que escogí y así la toma aleatoriamente del listado 

## AHORCADO: 

Para generar el dibujo El Ahorcado toma en cuenta los consejos del profesor el cual expresó que la mejor idea para generar un dibujo era usando texto por lo cual me base en un proyecto de github sobre doom para generar un dibujo de un ahorcado con código ASCII, para esto investigué Cómo hacer arte en python e imprimirlo línea por línea, después de ya tenido el dibujo base que era el árbol pasé a poner El Ahorcado donde se utilizó la variable intentos para ir generándolo según los intentos del jugador, la cantidad de intentos que requiere dibujar El Ahorcado completo depende de la dificultad. 

## PALABRA POR ADIVINAR: 

Para jugar El Ahorcado hice una función dónde se utiliza el selector de palabras aleatorias, se imprime la palabra siendo "_", se genera una variable de intentos y se le empieza a correr el temporizador (dicho temporizador solo es para mostrar el tiempo Qué tomo en resolverlo y empieza desde este punto ya que es cuando empieza el juego). 

## GANAR: 

Acá también se encuentra la condición si la letra que se escribe se encuentra en la palabra para adivinar de ser así se reemplaza si no se suma un intento fallido, si la palabra que se escribió coincide con la palabra adivinar se detiene el tiempo, se muestra Cuál era la palabra y un mensaje de felicitaciones junto cuánto tomó resolverlo


## PERDER: 

si los intentos llegan al máximo se imprime el Ahorcado completo, se detiene el temporizador se imprime la palabra que tocaba adivinar y un mensaje de derrota Además del tiempo que se demoró. 

## JUGAR DE NUEVO 

Para jugar de nuevo dentro de la misma función de jugar El Ahorcado se genera una variable donde se pregunta si quiere jugar de nuevo en en lowercase, sí sé que no imprime un mensaje de buen juego y termina el programa. Sí La respuesta es sí te pide que ingreses otra vez la dificultad, si la respuesta no coincide con un sí o un no te pide que ingreses una opción válida 

## MAIN: 

Para correr el juego se pide la dificultad en lowercase y según esta se asigna una variable con la cantidad de intentos y se pasa a comparar las dificultades para saber cuál ahorcado correr 

## GRAFICOS Y DECORACION: 

Para mejorar este apartado decidí usar el mismo principio del ahorcado, usando ASCII art para escribir texto un poco más vistoso y generar los mensajes de Victoria, derrota y de Buen juego, esto no solo para generar un mayor atractivo visual sino también para que el usuario tenga más claro que está sucediendo 

# CARACTERISTICAS AÑADIDAS POSTERIORMENTE 

## 2 JUGADORES: 

Para el modo dos jugadores al principio planteé que los dos se enfrentaran y que ganara el que menor tiempo tuvo pero decidí hacerlo un poco más sencillo permitiendo que el primer jugador ingrese una palabra y el segundo tenga que adivinarla. Para esto simplemente tomé el código de un arcano nivel medio y en vez de seleccionar una palabra aleatoria tomaría la que ingrese el primer jugador, la donde si el segundo jugador Adivina la palabra gana y si no gana el primero 

## MODO EXTREMO (CONTRARELOJ): 

Para el modo contrarreloj investigué Cómo hacer una cuenta regresiva donde utiliza la librería "THREADIND" dónde basándome en programas de internet cree dos variables globales dónde se mantiene desactivado por defecto el contador. Luego se creó una función que llame tiempo que servirá para determinar si el tiempo se agotó y detener el contador, donde su tiempo inicial será de 45 mientras el tiempo restante sea mayor a cero y no se llame a la variable de tener contador este se irá imprimiendo cada segundo y se irá restando uno al tiempo restante si llega a cero la variable de tiempo agotado se convierte en "True" 

Ya cuando esto está definido en la función para jugar este modo se llaman y definen las variables iniciales y se pone a funcionar la cuenta regresiva [threading.Thread(target=tiempo)]. El código es el mismo que en el modo difícil simplemente que al momento de ganar o perder se detiene la cuenta regresiva
