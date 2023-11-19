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

````python
#funcion pa escoger una palabra de la lista de forma aleatoria
def seleccionar_palabra_facil():
    palabras_facil = [palabra for palabra in palabras if len(palabra) < 5]
    return random.choice(palabras_facil)

def seleccionar_palabra_medio():
    palabras_medio = [palabra for palabra in palabras if len(palabra) >= 5 and len(palabra) <= 8]
    return random.choice(palabras_medio)

def seleccionar_palabra_dificil():
    palabras_dificil = [palabra for palabra in palabras if len(palabra) >= 9]
    return random.choice(palabras_dificil)
````

## AHORCADO: 

Para generar el dibujo El Ahorcado toma en cuenta los consejos del profesor el cual expresó que la mejor idea para generar un dibujo era usando texto por lo cual me base en un proyecto de github sobre doom para generar un dibujo de un ahorcado con código ASCII, para esto investigué Cómo hacer arte en python e imprimirlo línea por línea, después de ya tenido el dibujo base que era el árbol pasé a poner El Ahorcado donde se utilizó la variable intentos para ir generándolo según los intentos del jugador, la cantidad de intentos que requiere dibujar El Ahorcado completo depende de la dificultad. 

````python
#funcion para mostar el ahorcado en modo facil
def ahorcado_facil(intentos):
    ahorcado = [
#arbol en ASCII art     
"░░░░█░░▄▌░░░░▌░░░█░░░▄▄░░░░░░          ",
"░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄ ░░░░░░         ",
"░░░░░▐█░░░░░░░▌░▄█▀░░░▀█▄▄▄▄▄       ",
"░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░░▐░░░       ",
"░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░░▐░░░     ",
"▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░░▐░░░        ",
"█░░░▐░░░██░░░░░█░░▄░█▀░░░▐░░░        ",
"▐░░░█░░░▐█░░░░░░░░▌▀░░░░░▐░░░        ",
f"░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░{'▐██░░' if intentos > 1 else ' '}", #aca se separa con corchetes para 
f"▄▄▀▄█░░░░██░▄█▀░█▄▄░▐░░░ {'█▀░░' if intentos > 2 else ' '}", #hacer que con cada intento fallido  
f"░░░░▀█▄░▄███░░░░░░░░░░░░{'███░░' if intentos > 3 else ' '}", #añada una parte nueva del dibujo del
f"░░░░░░█████░░░░░░░░░░░░{'▄███▄░' if intentos > 4 else ' '}", #ahorcado al dibujo del arbol
f"░░░░░░░▐███░░░░░░░░░░░░░{'▐█▌░░' if intentos > 5 else ' '}",
f"░░░░░░░▐███░░░░░░░░░░░░ {'█▀█░░' if intentos > 6 else ' '}",
f"░░░░░░░▐████░░░░░░░░░░░ {'█░█▄░' if intentos > 7 else ' '}",
f"░░▒▒▒▒▒█████▒▒░░░░░░░░░ {'▀▀░░░ Has muerto' if intentos > 8 else ' '}",
"▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒░░░░░        ",
"▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒░░░░░        ",
"█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒░░░░░        ",

    ]
    #imprime el texto grafico linea por linea
    for linea in ahorcado:
        print(linea)   
````

## PALABRA POR ADIVINAR: 

Para jugar El Ahorcado hice una función dónde se utiliza el selector de palabras aleatorias, se imprime la palabra siendo "_", se genera una variable de intentos y se le empieza a correr el temporizador (dicho temporizador solo es para mostrar el tiempo Qué tomo en resolverlo y empieza desde este punto ya que es cuando empieza el juego). 

````python
def jugar_ahorcado_facil():
    #selecciona una palabra
    palabra_a_adivinar = seleccionar_palabra_facil()
    #imprime (_) para mostrar la logitud
    palabra_adivinada = ["_"] * len(palabra_a_adivinar)
    #contados de intentos empezando en 1
    intentos = 1
    #temporizador
    start_time = time.time()

    #bienvenida
    print("Bienvenido al juego de ahorcados\n")
````

## INTENTO DE ADIVINAR: 

Se utiliza un input con la variable letra Donde se compara si la letra está en la palabra que toca adivinar, donde se recorre la palabra y se analiza que si la letra se encuentra en esta reemplaza el espacio en blanco con dicha letra, sino sumar a uno a los intentos y esto provocará que dibuje una parte de el ahorcado.

````python
#imput de las letras adivinadas, con lower case siempre
letra = input("\nAdivina una letra: ").lower()

    #si la letra se encuentra en la palabra se coloca en la cadena 
    if letra in palabra_a_adivinar:
        for i in range(len(palabra_a_adivinar)):
            if palabra_a_adivinar[i] == letra:
                palabra_adivinada[i] = letra
    #sino se añade 1 a la cantidad de intentos
    else:
        intentos += 1
````

## GANAR: 

Acá también se encuentra la condición si la letra que se escribe se encuentra en la palabra para adivinar de ser así se reemplaza si no se suma un intento fallido, si la palabra que se escribió coincide con la palabra adivinar se detiene el tiempo, se muestra Cuál era la palabra y un mensaje de felicitaciones junto cuánto tomó resolverlo

````python
#si se adivina la palbra sin llegar a los maximos intentos
if "".join(palabra_adivinada) == palabra_a_adivinar: #se compara para saber que se adivino
    ahorcado_facil(intentos)
    #se detiene el temporizador
    end_time = time.time() 
    tiempo_transcurrido = end_time - start_time
    #mensaje de felicitaciones ademas del temporizador
    print("\nHas adivinado la palabra: " + palabra_a_adivinar)
    felicitaciones()
    print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
    break
````

## PERDER: 

si los intentos llegan al máximo se imprime el Ahorcado completo, se detiene el temporizador se imprime la palabra que tocaba adivinar y un mensaje de derrota Además del tiempo que se demoró. 

````python
#si se alcanza la maxima cantida de intentos
if intentos == 9:
    #imprime al ahorcado completo
    ahorcado_facil(9) 
    #detiene el temporizador
    end_time = time.time() 
    tiempo_transcurrido = end_time - start_time
    print("\n")
    #mensaje de derrota y la palabra que habia que adivinar
    print("\nLa palabra era: " + palabra_a_adivinar)
    perdiste()
    #imprime el temporizador
    print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
    break
````

## JUGAR DE NUEVO 

Para jugar de nuevo dentro de la misma función de jugar (se crea uno para cada dificultad) El Ahorcado se genera una variable donde se pregunta si quiere jugar de nuevo en en lowercase, sí sé que no imprime un mensaje de buen juego y termina el programa. Sí La respuesta es sí te pide que ingreses otra vez la dificultad, si la respuesta no coincide con un sí o un no te pide que ingreses una opción válida 

````python
    #al perder o ganar siempre se activara la funcion para jugar de nuevo
    while True:
        #pide escoger entre si y no, convierte el mensaje en lower case
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI / NO): \n").lower()
        #si se escoge "no" sale el mensaje y se finaliza el programa
        if jugar_de_nuevo == "no": 
            fin_del_juego()
            break
        #si se escoge "si" pide escoger la dificultad para jugar de nuevo y ejecuta
        elif jugar_de_nuevo == "si":
            dificultad = input("\nElige la dificultad (facil, medio, dificil):\n ").lower()
            if dificultad == "facil":
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                jugar_ahorcado_dificil()  
        #en caso de se ingrese otro valor pedira que se ingrese otra vez un "si" o "no"
        else:
            print("Opcion no valida. Elige entre 'SI / NO'")
````

## MAIN: 

Para correr primero el juego se pide la dificultad ademas de que imprime una breve idea de cada dificultad, se toma el dato ingresado lowercase y según esta se asigna una variable con la cantidad de intentos y se pasa a comparar las dificultades para saber cuál ahorcado correr.

````python
#programa principal para correr el juego
if __name__ == "__main__":
 while True:
    jugadores = input("Escoja cuantos jugadores (1 / 2): ")
    if jugadores == "2":
        intentos = 6
        break

    elif jugadores == "1":
        print("\nfacil 8 intentos\n")
        print("medio 6 intentos\n")
        print("dificil 3 intentos\n")
        print("extremo 3 intentos contra reloj\n")
        #se pide la dificultad y la convierte el lowercase
        dificultad = input("Elige la dificultad (facil, medio, dificil o extremo): ").lower()
        print()
        #se asigna la cantidad de intentos
        if dificultad == "facil":
            intentos = 8
            break
        elif dificultad == "medio":
            intentos = 6
            break
        elif dificultad == "dificil":
            intentos = 3
            break
        elif dificultad == "extremo":
            intentos = 3
            break
        elif dificultad == "snorlax":
            easteregg()
        #si no llega a coincidir pide que lo ingrese bien
        else:
            print("Dificultad no valida. Elige entre facil, medio o dificil.")
    else:
        print("Escoja entre (1 / 2) jugadores")

    #imprime el ahorcado solicitado segun la dificultad y corre el juego
if jugadores == "2":
   jugar_2_jugadores() 

elif dificultad == "facil":
    print(f"\nTienes {intentos} intentos para adivinar la palabra.\n")
    jugar_ahorcado_facil()

elif dificultad == "medio":
    print(f"\nTienes {intentos} intentos para adivinar la palabra.\n")
    jugar_ahorcado_medio()
    
elif dificultad == "dificil":
    print(f"\nTienes {intentos} intentos para adivinar la palabra.\n")
    jugar_ahorcado_dificil()

elif dificultad == "extremo":
    print(f"\nTienes 45 segundos y {intentos} intentos para adivinar la palabra.\n")
    jugar_ahorcado_extremo()
````

## GRAFICOS Y DECORACION: 

Para mejorar este apartado decidí usar el mismo principio del ahorcado, usando ASCII art para escribir texto un poco más vistoso y generar los mensajes de Victoria, derrota y de Buen juego, esto no solo para generar un mayor atractivo visual sino también para que el usuario tenga más claro que está sucediendo.

````python
def felicitaciones():
    feli = [
     
"█▀▀ █▀▀ █░░ ░▀░ █▀▀ ░▀░ ▀▀█▀▀ █▀▀█ █▀▀ ░▀░ █▀▀█ █▀▀▄ █▀▀ █▀▀    ",
"█▀▀ █▀▀ █░░ ▀█▀ █░░ ▀█▀ ░░█░░ █▄▄█ █░░ ▀█▀ █░░█ █░░█ █▀▀ ▀▀█    ",
"▀░░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀    ",                                                                                                   

    ]
    for linea2 in feli:
        print(linea2) 

def perdiste():
    perdi = [

"▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▄ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀  ",
"▒█▄▄█ ▒█▀▀▀ ▒█▄▄▀ ▒█░▒█ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀  ",
"▒█░░░ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▀ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄  ",

    ]
    for linea3 in perdi:
        print(linea3) 

def fin_del_juego():
    GG = [

"▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▄░▒█ ░█▀▀█ 　 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▄ ░█▀▀█", 
"▒█▀▀▄ ▒█░▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█▄▄█ 　 　 ▒█▄▄█ ▒█▄▄█ ▒█▄▄▀ ░▒█░░ ▒█░ ▒█░▒█ ▒█▄▄█", 
"▒█▄▄█ ░▀▄▄▀ ▒█▄▄▄ ▒█░░▀█ ▒█░▒█ 　 　 ▒█░░░ ▒█░▒█ ▒█░▒█ ░▒█░░ ▄█▄ ▒█▄▄▀ ▒█░▒█",

    ]
    #imprime el texto grafico linea por linea
    for linea4 in GG:
        print(linea4) 
````

# CARACTERISTICAS AÑADIDAS POSTERIORMENTE 

## ASCII ART 

Para generar una interfaz gráfica más agradable para la vista, además de generar una mejor guía para el usuario sobre lo que está sucediendo se utilizo el mismo concepto que con el Ahorcado usando ascii, con ayuda de la página https://fsymbols.com/es/arte-de-texto/#aftercats  se escribieron mensajes en consola para lograr el resultado que vemos, simplemente se escribe el mensaje y la página lo convierte en la caligrafía requerida.

### Dibujo el ahorcado:
![ascii_art_pagina](https://github.com/CJxCJ/proyecto_final_camilo_sanchez/assets/115903431/28b2b392-f1e8-401a-9b2b-8cdf4db1ff7e)

### Mensajes de consola: 
![texto_ascii](https://github.com/CJxCJ/proyecto_final_camilo_sanchez/assets/115903431/39caabd9-228c-49c8-82c3-f1a20232cdfc)




## 2 JUGADORES: 

Para el modo dos jugadores al principio planteé que los dos se enfrentaran y que ganara el que menor tiempo tuvo pero decidí hacerlo un poco más sencillo permitiendo que el primer jugador ingrese una palabra y el segundo tenga que adivinarla. Para esto simplemente tomé el código de un arcano nivel medio y en vez de seleccionar una palabra aleatoria tomaría la que ingrese el primer jugador, la donde si el segundo jugador Adivina la palabra gana y si no gana el primero.

````python
#se pide que se ingrese una palabra
def jugar_2_jugadores():
    print("\nJugador 1, ingresar una palabra:\n ")
    palabra_jugador1 = input("Palabra: ").lower()

    #contador de intentos, la palbra oculta y el temporizador iniciado
    intentos = 1  
    palabra_adivinada = ["_"] * len(palabra_jugador1)
    start_time = time.time() 

    #espacios en blanco para "limpiar la consola"
    print("\n" * 50)

    #aca se realiza lo mismo solo que en vez de usar una de las palabras de la lista se juega con la escrita por el jugador 1
    print("Turno del Jugador 2:")
    while True:
        ahorcado_2_jugadores(intentos)
        print("".join(palabra_adivinada))
        
        if intentos == 7:
            ahorcado_2_jugadores(7)
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("\nJugador 1 perdio La palabra era: " + palabra_jugador1)
            perdiste()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break
````

## MODO EXTREMO (CONTRARELOJ): 

Para el modo contrarreloj investigué Cómo hacer una cuenta regresiva donde utiliza la librería "THREADIND" dónde basándome en programas de internet cree dos variables globales dónde se mantiene desactivado por defecto el contador. Luego se creó una función que llame tiempo que servirá para determinar si el tiempo se agotó y detener el contador, donde su tiempo inicial será de 45 mientras el tiempo restante sea mayor a cero y no se llame a la variable de tener contador este se irá imprimiendo cada segundo y se irá restando uno al tiempo restante si llega a cero la variable de tiempo agotado se convierte en "True". 

Ya cuando esto está definido en la función para jugar este modo se llaman y definen las variables iniciales y se pone a funcionar la cuenta regresiva [threading.Thread(target=tiempo)]. El código es el mismo que en el modo difícil simplemente que al momento de ganar o perder se detiene la cuenta regresiva.

````python
#el concepto de juego es el mismo con una pequeña diferencia
def jugar_ahorcado_extremo():
    #se llama la variable del contador
    global tiempo_agotado, detener_contador
    palabra_a_adivinar = seleccionar_palabra_dificil()
    palabra_adivinada = ["_"] * len(palabra_a_adivinar)
    intentos = 1
    start_time = time.time()

    #aca tenemos un contador en pantalla que funciona mediante la extencion (threading.Thread) importada de "threading"
    tiempo_transcurrido = threading.Thread(target=tiempo)
    tiempo_transcurrido.start()

    print("Bienvenido al juego de ahorcados\n")
 
    while True:
        ahorcado_extremo(intentos)
        print("".join(palabra_adivinada))
        #si el contador se detiene imprime la pantalla de derrota
        if tiempo_agotado:
            print("\n¡Tiempo agotado! Has excedido los 60 segundos.")
            perdiste()
            print("\nLa palabra era: " + palabra_a_adivinar)
            detener_contador = True
            break
        #al igual con los intentos 
        if intentos == 4:
            ahorcado_extremo(4) 
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("\nPerdiste! La palabra era: " + palabra_a_adivinar)
            perdiste()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")

            detener_contador = True
            break

        letra = input("\nAdivina una letra: ").lower()

        if letra in palabra_a_adivinar:
            for i in range(len(palabra_a_adivinar)):
                if palabra_a_adivinar[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1

        if "".join(palabra_adivinada) == palabra_a_adivinar:
            ahorcado_extremo(intentos)
            end_time = time.time()
            tiempo_transcurrido = end_time - start_time
            print("\nHas adivinado la palabra: " + palabra_a_adivinar)
            felicitaciones()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            #siempre hay que detener el contador siempre o sino muestra pantalla de derrota incluso si se gana
            detener_contador = True
            break
````


