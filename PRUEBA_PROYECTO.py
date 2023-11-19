import time  
import random
import threading

#estas variables mantienen desactivado el contador hasta que sea True 
tiempo_agotado = False
detener_contador = False

palabras = [
        "dulce", "perdon", "corazon", "hijo", "orar", "tarde", "semanas", "oracion", "edificar", "ayuda", "batalla", "calidad", "vida", "verdad", "caminar", "piadoso", "tiempo", "gracia", "dulzura",
        "señor", "libre", "sueño", "anhelo", "favor", "gracias", "esperar", "palabra", "vision", "muestra", "amor", "gozo", "vivir", "meditar", "feliz", "firme", "leer", "ayuda", "creer", "virtud",
        "amable", "estable", "libro", "hablar", "ejemplo", "obrar", "amigo", "guiar", "mañana", "varon", "mujer", "causa", "pasos", "crecer", "orden", "hombre", "promesa", "mentor", "lider", "pacto",
        "bondad", "decreto", "regreso", "sabio", "sembrar", "salvo", "cumplir", "enseñar", "respeto", "escudo", "refugio", "salud", "ofrenda", "juez", "justo", "camino", "cambio", "aceptar", "belleza",
        "refleja", "etapa", "mayor", "trabajo", "revelar", "edad", "estado", "pasado", "desafio", "nombre", "armonia", "certeza", "fuente", "ideal", "origen", "pensar", "solemne", "milagro", "ayuno",
        "iglesia", "alabare", "aceite", "medidor", "piston", "partes", "filtro", "bateria", "exhosto", "tanque", "aire", "agua", "presion", "chispa", "bobina", "motor", "espejos", "fusible", "asiento",
        "sistema", "alerta", "seguro", "faro", "inicio", "diodo", "rotor", "polea", "correa", "cambio", "unidad", "varilla", "entrada", "sensor", "drenaje", "chasis", "freno", "cilindro", "frio", "etanol", 
        "energia", "fluido", "liquido", "ventaja", "daños", "control", "diseño", "voltaje", "ventana", "luces", "turbina", "carcasa", "hibrido", "recarga", "apio", "perejil", "brocoli", "patata", "tomate", 
        "acelga", "puerro", "cebolla", "lechuga", "maiz", "haba", "pepino", "rabano", "fresa", "limon", "naranja", "pomelo", "melon", "sandia", "coco", "datil", "kiwi", "litchi", "mango", "papaya", "piña", 
        "platano", "cereza", "ciruela", "manzana", "pera", "castaña", "nuez", "sesamo", "arroz", "lenteja", "frijol", "mazorca", "avena", "centeno", "quinoa", "trigo", "azafran", "canela", "comino", "curry", 
        "mostaza", "oregano", "eneldo", "hinojo", "laurel", "menta", "romero", "salvia", "tomillo", "mora", "durazno", "guayaba", "jalapeño", "lulo", "uchuva", "sazonar", "emigrar", "acta", "agil", "viajar", 
        "barco", "avion", "crucero", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "mesa", "silla", "sofa", "cama", "piscina", "oceano", "pais", "nevera", "horno", "fruto", "siembra",
        "viajero", "dias", "semanas", "ciudad", "atun", "salmon", "pulpo", "almeja", "calamar", "camaron", "queso", "leche", "azucar", "miel", "melaza", "risoto", "crema", "ponque", "auto", "hornear", "congelar",
        "enfriar", "calentar", "mezclar", "vaca", "oveja", "gallina", "pavo", "beca", "cena", "onces", "cima", "cocinar", "euro", "dolar", "freir", "hogar", "casa", "cabaña", "oficina", "fabrica", "cocina",
        "alcoba", "sala", "comedor", "garaje", "terraza", "patio", "baño", "bañera", "estudio", "sotano", "granja", "ahumar", "dorar", "monitor", "tostar", "idea", "isla", "archivo", "jalea", "leña", "mapa", "arbol", 
        "arcilla", "arveja", "adobar", "fisica", "industrial", "derecho", "salto", "carrera", "atomico", "auditor", "autobus", "aval", "avance", "axial", "cabina", "piloto", "ahorro", "tren", "ayuda", "azafran", 
        "azul", "verde", "morado", "blanco", "plata", "cafe", "bacalao", "trucha", "balanza", "balance", "bambu", "yate", "velero", "broca", "vinagre", "base", "bebida", "benigno", "craneo", "maxilar", "humero", 
        "cubito", "pelvis", "carpo", "falange", "femur", "correo", "tibia", "perone", "riñon", "neurona", "cerebro", "nariz", "boca", "brazo", "pierna", "pulmon", "mano", "divisas", "banco", "tobillo", "tamizar", 
        "podar", "humano", "aspecto", "bufanda", "abrigo", "morral", "camisa", "zapatos", "chaleco", "blazer", "sueter", "buzo", "medias", "gorra", "cepillo", "cortar", "secador", "tijeras", "salud", "medico", 
        "lesion", "terapia", "tocino", "trapero", "comprendo", "redimido", "sabiduria", "encontrar", "prepararse", "viviendo", "decision", "practicar", "comunion", "fortaleza", "compartir", "voluntad", "honestidad", 
        "proteccion", "perdonar", "libertad", "respuesta", "valiente", "proyecto", "fundamento", "añadidura", "revelacion", "atencion", "confianza", "entereza", "revelacion", "organizar", "escrito", "palabra", "importante",
        "espiritual", "integral", "recordar", "victoria", "redencion", "radiante", "verdadero", "agradecido", "fidelidad", "alimento", "esperanza", "busqueda", "prioridad", "solucion", "identidad", "proveedor", "protector",
        "escogido", "bendecido", "dirigido", "santidad", "enseñanza", "sostiene", "consuelo", "defensor", "testimonio", "aspecto", "diferente", "expresar", "considerar", "escritura", "sensible", "escuchar", "aprender", 
        "adornadas", "completo", "principio", "peticion", "examinar", "original", "abundancia", "enfrentar", "realidad", "bienestar", "reconocer", "orientar", "construir", "constancia", "erradicar", "privilegio", 
        "asombroso", "profundo", "soberano", "direccion", "altisimo", "reflexion", "calendario", "diferencia", "inspirado", "compasion", "perceptivo", "consciente", "necesidad", "transforma", "habilidad", "optimista",
        "comunidad", "consejero", "gratitud", "inyector", "valvulas", "inyeccion", "cilindro", "ingenieria", "gasolina", "termostato", "radiador","indicador", "tacometro", "encendido", "cableado", "generador", 
        "rodamiento", "ensamble", "ensamblaje", "retenedor", "conector", "separador", "negativo", "particion", "conducir", "velocidad", "diferencial", "cigüeñal", "compresion", "acelerador", "mecanismo", "suspension", 
        "procesos", "vehiculo", "combustion", "evolucion", "servicio", "monoxido", "friccion", "lubricante", "centrifuga", "operación", "eficiente", "corrosion", "resistente", "accesorios", "circuito", "lamparas", 
        "automatico", "dinamico", "impulsor", "deposito", "seguridad", "conduccion", "zanahoria", "berenjena", "pimiento", "remolacha", "espinaca", "esparrago", "champiñon", "guisante", "calabacin", "calabaza", 
        "pepinillo", "alcachofa", "coliflor", "arandano", "frambuesa", "zarzamora", "mandarina", "aguacate", "melocoton", "almendra", "avellana", "cacahuate", "pistacho", "maracuya", "garbanzo", "habichuela", 
        "albahaca", "cilantro", "aceituna", "pimienta", "tamarindo", "guanabana", "vainilla", "jengibre", "manzanilla", "cultivar", "agricola", "terminar", "variedad", "sustento", "subsuelo", "producto", "probable", 
        "perfecto", "orquidea", "merendar", "magnolia", "frondoso", "extracto", "estofado", "ensalada", "envuelto", "degustar", "creacion", "cerilla", "barbacoa", "agridulce", "alcaparra", "bocadillo", "cobertura", 
        "confitura", "refrigerar", "aborigen", "acogedor", "apreciar", "aventura", "calcular", "castillo", "catarata", "celebrar", "circular", "codorniz", "conceder", "concepto", "consulta", "contrato", "correcto", 
        "culminar", "creativo", "destello", "degustar", "enfatico", "estudiar", "explorar", "fabricar", "gabinete", "genetica", "impulsar", "imprenta", "perdurar", "precepto", "producto", "repuesto", "simetria", 
        "autoridad", "codificar", "compresor", "ejercicio", "extractor", "hidrogeno", "vinagreta", "astronomia", "arqueologo", "autentico", "autoclave", "autodromo", "automotriz", "autonomia", "autopista", "aviacion", 
        "avicultura", "deposito", "balneario", "barometro", "alcalino", "vertebra", "talonario", "confiteria", "telegrama", "cortadora", "perfumeria", "gimnasio", "equipaje", "esqueleto", "mensajes", "lenceria", 
        "chequera", "cerradura", "biblioteca", "desayuno", "hambriento", "anfitrion", "microondas", "destapador", "abrelatas", "triturador", "escurridor", "espatula", "espumadera", "cucharon", "botiquin", "lavamanos", 
        "suavizante", "enguajar", "detergente", "limpieza", "rastrillo", "protector", "aspersor", "atomizador", "cortadora", "rastrillar", "cosechar", "cultivar", "desyerbar", "herbicida", "hidrante", "portafolio", 
        "sintetico", "pantalon", "camiseta", "cinturon", "billetera", "tablilla", "conmocion", "inyeccion", "patologia", "oncologia", "odontologo", "acupuntura", "homeopatia", "suplemeto", "relajacion", "individual", 
        "vivienda", "ampliacion", "citofono", "edificio", "triangulo", "arrecife", "restitucion", "restauracion", "justificado", "entendimiento", "perspicacia", "transformacion", "preparacion", "inteligente", 
        "transmitir", "capacitarce", "pensamiento", "consciencia", "eternamente", "misericordia", "reconciliacion", "determinado", "mandamiento", "experimentar", "comprension", "oportunidad", "comunicación", 
        "circunstancia", "instrumento", "intercesion", "identificar", "conversacion", "perseverancia", "indulgencia", "avivamiento", "arrepentimiento", "persistente", "maravilloso", "expectativa", "perspectiva", 
        "fervientemente", "agradecimiento", "edificacion", "significativo", "sobrenatural", "convicciones", "recordatorio", "sorprendido", "mansedumbre", "acontecimiento", "transparencia", "manifestacion", "inquebrantable", 
        "responsabilidad", "colaboracion", "conocimiento", "hospitalidad", "incomparable", "personalidad", "salvaguardia", "tranquilidad", "aniversario", "despertarse", "empujadores", "refrigerador", "silenciador", 
        "convertidor", "catalizador", "reguladores", "instrumento", "distribuidor", "temperatura", "velocimetro", "direccional", "componentes", "aparcamiento", "transmision", "combustible", "estructural", "calibrador", 
        "calefaccion", "compartimento", "almacenamiento", "diferencial", "electronico", "construccion", "volatibilidad", "lubricacion", "hidraulico", "generadores", "refrigeracion", "automaticamente", "eliminacion", 
        "presurizado", "iluminacion", "aerodinamico", "resistencia", "suplementos", "evolucionado", "tecnologias", "ordenadores", "estabilidad", "distribucion", "caracteristicas", "programacion", "polipropileno", 
        "poliestireno", "electrostatica", "galvanizado", "electromovilidad", "inflamabilidad", "fotovoltaico", "hidrocarburo", "industrializacion", "albaricoque", "condimentar", "hamburguesa", "vegetariana", "cosechadora", 
        "espantapajaros", "equilibrio", "hidrolavadora", "helicoptero", "apartamento", "archipielago", "climatizador", "departamento", "especialidad", "inteligencia", "instrumental", "originalidad", "rentabilidad", 
        "licenciatura", "aerodeslizador", "aerofotografia", "aerostatico", "alfanumerico", "alimentacion", "alineamiento", "almacenamiento", "amortiguador", "alternativa", "balsamico", "transatlantico", "hipoalergenico",
        "propietario", "contraventana", "dispensador", "descorazonador", "centrifugar", "cortacesped", "transplantar", "salsamentaria", "diccionario", "enciclopedia", "paralelogramo", "circunferencia", "perpendicular", 
        "denominador", "dimensiones", "profundidad", "calculadora", "laboratorio", "microscopio", "portaobjetos", "bibliotecaria", "investigacion", "conservatorio", "papelografo", "presentacion", "presentador", 
        "electricista", "veterinaria", "parqueadero", "parquimetro", "todoterreno", "anticongelante", "motocicleta", "estabilizador", "ultraliviano", "hidrodeslizador", "inmovilizacion", "entrenamiento", "sincronizado", 
        "tablavelista", "paracaidismo", "motociclismo", "estiramiento", "indicaciones", "enciendefuegos", "amplificador", "exposimetro", "sobreexpuesto", "desenfocado", "rompecabezas", "carboncillo", "constelacion", 
        "trasbordador", "binoculares", "rinoceronte", "estructuras", "farmaceutico", "autoservicio", "pantorrilla", "comprobantes", "transferencia", "informacion", "recepcionista", "restaurante", "iluminacion", 
        "dispensario", "medicamento", "cuentagotas", "supermercado", "impermeable", "esparadrapo"

]

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

#funcion para generar una cuenta regresiva
def tiempo():
    #se llaman las variables globales
    global tiempo_agotado, detener_contador
    #se establece el tiempo inicial
    tiempo_restante = 45
    #mientras el tiempo no se agote y no se solicite apagar el contador este funcionara
    while tiempo_restante > 0 and not detener_contador:
        #imprime el tiempo restante para la cuenta regresiva
        print(f"Tiempo restante: {tiempo_restante} segundos", end='\r')
        #espera 1 segundo
        time.sleep(1)
        #resta 1 al contador para generar el efecto de cuenta regresiva
        tiempo_restante -= 1
    #apaga el contador    
    if tiempo_restante <= 0:
        tiempo_agotado = True

#funciones de texto graficos para hacerlo mas atractivo visualmente (hecho con ASCII art)
#TODOS FUNCIONAN DE LA MISMA MANERA
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




def easteregg():
    pokemon = [

"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
" ⠀⠀⠀⠀⢀⡀⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⢀⣀⠀⠀⠈⠉⠀⠀⣀⣀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⣀⣶⣿⣿⣿⣾⣇⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣼⡏⠀⠀⠀⣀⣀⣉⠉⠩⠭⠭⠭⠥⠤⢀⣀⣀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀",
"⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣶⣤⣄⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀",
"⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀",
"⠀⠀⣀⠀⢸⡿⠿⣿⡿⠋⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠻⠿⠟⠉⢙⣿⣿⣿⣿⣿⣿⡇",
"⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢿⡿⣿⠳⠀",
"⠀⠀⡞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⡀⠀⠀",
"⢀⣸⣀⡀⠀⠀⠀⠀⣠⣴⣾⣿⣷⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢿⣿⠿⠃⠀",
"⠘⢿⡿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⡸⠁⠀⠀⠀",
"⠀⠀⠳⣄⠀⠀⠀⠹⣿⣿⣿⡿⠛⣠⠾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠳⣄⠙⠛⠿⠿⠛⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀",
"⠀⠀⠀⠈⠑⠢⠤⠤⠬⠭⠥⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠤⠤⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀",
     ]

    for linea5 in pokemon:
        print(linea5) 


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
    print("Bienvenido al juego de ahorcados\n")

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
            print("\n")
            #mensaje de derrota y la palabra que habia que adivinar
            print("\nLa palabra era: " + palabra_a_adivinar)
            perdiste()
            #imprime el temporizador
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
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
            print("\nHas adivinado la palabra: " + palabra_a_adivinar)
            felicitaciones()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
            break

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

    print("Bienvenido al juego de ahorcados\n")

    while True:
        ahorcado_medio(intentos)
        print("".join(palabra_adivinada))

        if intentos == 7:
            ahorcado_medio(7)
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("\nPerdiste! La palabra era: " + palabra_a_adivinar)
            perdiste()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
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
            print("\nHas adivinado la palabra: " + palabra_a_adivinar)
            felicitaciones()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
            break


    while True:
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI / NO):\n ").lower()
        if jugar_de_nuevo == "no": 
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":
            dificultad = input("Elige la dificultad (facil, medio, dificil): \n").lower()
            if dificultad == "facil":
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
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

    print("Bienvenido al juego de ahorcados\n")


    
    while True:
        ahorcado_dificil(intentos)
        print("".join(palabra_adivinada))

        if intentos == 4:
            ahorcado_dificil(4) 
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time

            print("\nPerdiste La palabra era: " + palabra_a_adivinar)
            perdiste()

            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
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
            print("\nHas adivinado la palabra: " + palabra_a_adivinar)
            felicitaciones()

            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos\n")
            break
        

    while True:
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (SI / NO):\n ").lower()
        if jugar_de_nuevo == "no": 
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":

            dificultad = input("Elige la dificultad (facil, medio, dificil):\n ").lower()

            if dificultad == "facil":
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                jugar_ahorcado_dificil()  
        else:
            print("Opcion no valida. Elige entre 'SI / NO'")




def ahorcado_extremo(intentos):
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
        

    while True:
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (SI / NO):\n ").lower()
        if jugar_de_nuevo == "no": 
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":
            dificultad = input("Elige la dificultad (facil, medio, dificil):\n ").lower()
            if dificultad == "facil":
                jugar_ahorcado_facil()

            elif dificultad == "medio":
                jugar_ahorcado_medio()

            elif dificultad == "dificil":
                jugar_ahorcado_dificil()  
            
            #al igual toca llamar la variables globales para poder utilizarlo otra vez
            elif dificultad == "extremo":
                detener_contador = False
                tiempo_agotado = False
                jugar_ahorcado_extremo()
        else:
            print("\nOpcion no valida. Elige entre SI / NO\n ")




def ahorcado_2_jugadores(intentos):
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

        letra = input("\nAdivina una letra: ").lower()

        if letra in palabra_jugador1:
            for i in range(len(palabra_jugador1)):
                if palabra_jugador1[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos += 1

        if "".join(palabra_adivinada) == palabra_jugador1:
            ahorcado_2_jugadores(intentos)
            end_time = time.time() 
            tiempo_transcurrido = end_time - start_time
            print("\nHas adivinado la palabra: " + palabra_jugador1)
            print("\nFelicidades El Jugador 2 ha adivinado la palabra.\n")
            felicitaciones()
            print(f"\nTiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
            break
    #se pide que si quiere jugar de nuevo en 2    
    while True:
        jugar_de_nuevo = input("\n¿Quieren jugar de nuevo? SI / NO: \n").lower()
        if jugar_de_nuevo == "no": 
            fin_del_juego()
            break
        elif jugar_de_nuevo == "si":
            jugar_2_jugadores()
        else:
            print("\nOpcion no valida. Elige entre SI / NO\n")

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


    

