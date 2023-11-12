import random
import time  


#listado de palabras provicional segun la dificultad elegida
palabras_facil = ["python", "programacion", "desarrollo", "computadora", "teclado", ]

palabras_medio = ["carrito", "rascacielos", "aretes", "lapiz"]

palabras_dificil = ["inteligencia", "artificial", "algoritmo", "aplicacion", "tecnologia"]


#funcion pa escoger una palabra de la lista de forma aleatoria
def seleccionar_palabra_facil():
    return random.choice(palabras_facil)

def seleccionar_palabra_medio():
    return random.choice(palabras_medio)

def seleccionar_palabra_dificil():
    return random.choice(palabras_dificil)

#funciones de texto graficos para hacerlo mas atractivo visualmente (hecho con ASCII art)
#TODOS FUNCIONAN DE LA MISMA MANERA
def fin_del_juego():
    GG = [

"▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▄░▒█ ░█▀▀█ 　 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▄ ░█▀▀█", 
"▒█▀▀▄ ▒█░▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█▄▄█ 　 　 ▒█▄▄█ ▒█▄▄█ ▒█▄▄▀ ░▒█░░ ▒█░ ▒█░▒█ ▒█▄▄█", 
"▒█▄▄█ ░▀▄▄▀ ▒█▄▄▄ ▒█░░▀█ ▒█░▒█ 　 　 ▒█░░░ ▒█░▒█ ▒█░▒█ ░▒█░░ ▄█▄ ▒█▄▄▀ ▒█░▒█",

    ]
    #imprime el texto grafico linea por linea
    for linea4 in GG:
        print(linea4) 




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


#funcion para jugar al ahorcado, todos funcionan con el mismo pricipio salvo la cantidad de intentos
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
    print("Bienvenido al juego de ahorcados!")
    print("   ")

    #empieza el juego
    while True:
        #imprime el arbol del ahorcado y la cadena de "_" para la palabra
        ahorcado_facil(intentos)
        print("".join(palabra_adivinada))
        #si se alcanza la maxima cantida de intentos
        if intentos == 9:
            #imprime al ahorcado completo
            ahorcado_facil(9) 
            #detiene el temporizador
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("   ")
            #mensaje de derrota y la palabra que habia que adivinar
            print("La palabra era: " + palabra_a_adivinar)
            print("   ")
            perdiste()
            print("   ")
            #imprime el temporizador
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            print("   ")
            break

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

        #si se adivina la palbra sin llegar a los maximos intentos
        if "".join(palabra_adivinada) == palabra_a_adivinar: #se compara para saber que se adivino
            ahorcado_facil(intentos)
            #se detiene el temporizador
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            #mensaje de felicitaciones ademas del temporizador
            print("  ")
            print("Has adivinado la palabra: " + palabra_a_adivinar)
            print("  ")
            felicitaciones()
            print("  ")
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            print("   ")
            break

    #al perder o ganar siempre se activara la funcion para jugar de nuevo
    while True:
        #pide escoger entre si y no, convierte el mensaje en lower case
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI / NO): ").lower()
        #si se escoge "no" sale el mensaje y se finaliza el programa
        if jugar_de_nuevo == "no": 
            print("   ")
            fin_del_juego()
            break
        #si se escoge "si" pide escoger la dificultad para jugar de nuevo y ejecuta
        elif jugar_de_nuevo == "si":
            dificultad = input("Elige la dificultad (facil, medio, dificil): ").lower()
            if dificultad == "facil":
                print("   ")
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                print("   ")
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                print("   ")
                jugar_ahorcado_dificil()  
        #en caso de se ingrese otro valor pedira que se ingrese otra vez un "si" o "no"
        else:
            print("Opcion no valida. Elige entre 'SI / NO'")


#aca en adelante todo funciona de la misma manera con la unica diferencia estando en los intentos
def ahorcado_medio(intentos):
    ahorcado = [
        
"░░░░█░░▄▌░░░░▌░░░█░░░▄▄░░░░░░          ",
"░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄ ░░░░░░         ",
"░░░░░▐█░░░░░░░▌░▄█▀░░░▀█▄▄▄▄▄       ",
"░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░░▐░░░       ",
"░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░░▐░░░     ",
"▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░░▐░░░        ",
"█░░░▐░░░██░░░░░█░░▄░█▀░░░▐░░░        ",
"▐░░░█░░░▐█░░░░░░░░▌▀░░░░░▐░░░        ",
f"░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░{'▐██░░' if intentos > 1 else ' '}", #como podemos ver aca se permiten
f"▄▄▀▄█░░░░██░▄█▀░█▄▄░▐░░░ {'█▀░░' if intentos > 1 else ' '}", #menos intentos aumentando la dificultad 
f"░░░░▀█▄░▄███░░░░░░░░░░░░{'███░░' if intentos > 2 else ' '}", #para ganar el juego, ademas se escogen 
f"░░░░░░█████░░░░░░░░░░░░{'▄███▄░' if intentos > 3 else ' '}", #palabras mas complicadas para adivinar
f"░░░░░░░▐███░░░░░░░░░░░░░{'▐█▌░░' if intentos > 3 else ' '}",
f"░░░░░░░▐███░░░░░░░░░░░░ {'█▀█░░' if intentos > 4 else ' '}",
f"░░░░░░░▐████░░░░░░░░░░░ {'█░█▄░' if intentos > 5 else ' '}",
f"░░▒▒▒▒▒█████▒▒░░░░░░░░░ {'▀▀░░░ Has muerto' if intentos > 6 else ' '}",
"▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒░░░░░        ",
"▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒░░░░░        ",
"█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒░░░░░        ",

    ]
    for linea in ahorcado:
        print(linea)   

def jugar_ahorcado_medio():
    palabra_a_adivinar = seleccionar_palabra_medio() #se escogen palabras de otra lista de mayor dificultad
    palabra_adivinada = ["_"] * len(palabra_a_adivinar)
    intentos = 1 
    start_time = time.time()

    print("Bienvenido al juego de ahorcados!")
    print("   ")
    while True:
        ahorcado_medio(intentos)
        print("".join(palabra_adivinada))

        if intentos == 7:
            ahorcado_medio(7)
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("   ")
            print("¡Perdiste! La palabra era: " + palabra_a_adivinar)
            print("   ")
            perdiste()
            print("   ")
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break

        letra = input("\nAdivina una letra: ").lower()

        if letra in palabra_a_adivinar:
            for i in range(len(palabra_a_adivinar)):
                if palabra_a_adivinar[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1

        if "".join(palabra_adivinada) == palabra_a_adivinar:
            ahorcado_medio(intentos)
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("  ")
            print("Has adivinado la palabra: " + palabra_a_adivinar)
            print("  ")
            felicitaciones()
            print("  ")
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break


    while True:
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI / NO): ").lower()
        if jugar_de_nuevo == "no": 
            print("   ")
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":
            dificultad = input("Elige la dificultad (facil, medio, dificil): ").lower()
            if dificultad == "facil":
                print("   ")
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                print("   ")
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                print("   ")
                jugar_ahorcado_dificil()  
        else:
            print("Opcion no valida. Elige entre 'SI / NO'")




def ahorcado_dificil(intentos):
    ahorcado = [
        
"░░░░█░░▄▌░░░░▌░░░█░░░▄▄░░░░░░          ",
"░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄ ░░░░░░         ",
"░░░░░▐█░░░░░░░▌░▄█▀░░░▀█▄▄▄▄▄       ",
"░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░░▐░░░       ",
"░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░░▐░░░     ",
"▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░░▐░░░        ",
"█░░░▐░░░██░░░░░█░░▄░█▀░░░▐░░░        ",
"▐░░░█░░░▐█░░░░░░░░▌▀░░░░░▐░░░        ",
f"░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░{'▐██░░' if intentos > 1 else ' '}",
f"▄▄▀▄█░░░░██░▄█▀░█▄▄░▐░░░ {'█▀░░' if intentos > 1 else ' '}",
f"░░░░▀█▄░▄███░░░░░░░░░░░░{'███░░' if intentos > 1 else ' '}",
f"░░░░░░█████░░░░░░░░░░░░{'▄███▄░' if intentos > 2 else ' '}",
f"░░░░░░░▐███░░░░░░░░░░░░░{'▐█▌░░' if intentos > 2 else ' '}",
f"░░░░░░░▐███░░░░░░░░░░░░ {'█▀█░░' if intentos > 2 else ' '}",
f"░░░░░░░▐████░░░░░░░░░░░ {'█░█▄░' if intentos > 3 else ' '}",
f"░░▒▒▒▒▒█████▒▒░░░░░░░░░ {'▀▀░░░ Has muerto' if intentos > 3 else ' '}",
"▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒░░░░░        ",
"▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒░░░░░        ",
"█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒░░░░░        ",

    ]
    for linea in ahorcado:
        print(linea)   

def jugar_ahorcado_dificil():
    palabra_a_adivinar = seleccionar_palabra_dificil()
    palabra_adivinada = ["_"] * len(palabra_a_adivinar)
    intentos = 1
    start_time = time.time()

    print("Bienvenido al juego de ahorcados!")
    print("   ")

    
    while True:
        ahorcado_dificil(intentos)
        print("".join(palabra_adivinada))

        if intentos == 4:
            ahorcado_dificil(4) 
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("   ")
            print("¡Perdiste! La palabra era: " + palabra_a_adivinar)
            print("   ")
            perdiste()
            print("   ")
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break

        letra = input("\nAdivina una letra: ").lower()

        if letra in palabra_a_adivinar:
            for i in range(len(palabra_a_adivinar)):
                if palabra_a_adivinar[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1

        if "".join(palabra_adivinada) == palabra_a_adivinar:
            ahorcado_dificil(intentos)
            end_time = time.time()
            tiempo_transcurrido = end_time - start_time
            print("  ")
            print("Has adivinado la palabra: " + palabra_a_adivinar)
            print("  ")
            felicitaciones()
            print("  ")
            print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break
        

    while True:
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI / NO): ").lower()
        if jugar_de_nuevo == "no": 
            print("   ")
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":
            dificultad = input("Elige la dificultad (facil, medio, dificil): ").lower()
            if dificultad == "facil":
                print("   ")
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                print("   ")
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                print("   ")
                jugar_ahorcado_dificil()  
        else:
            print("Opcion no valida. Elige entre 'SI / NO'")


#programa principal para correr el juego
while True:
    #se pide la dificultad y la convierte el lowercase
    dificultad = input("Elige la dificultad (facil, medio, dificil): ").lower()
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
    #si no llega a coincidir pide que lo ingrese bien
    else:
        print("Dificultad no valida. Elige entre facil, medio o dificil.")

#imprime el ahorcado solicitado segun la dificultad y corre el juego
if dificultad == "facil":
   print(f"Tienes {intentos} intentos para adivinar la palabra.")
   jugar_ahorcado_facil()

elif dificultad == "medio":
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    jugar_ahorcado_medio()
    
elif dificultad == "dificil":
    print(f"Tienes {intentos} intentos para adivinar la palabra.")
    jugar_ahorcado_dificil()

    

