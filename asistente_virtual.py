import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio 
        audio = r.listen(origen)

        try:
            # Buscar en Google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-col")

            # Prueba de que pudo ingresa
            print("Dijiste: " + pedido)

            # Devolver pedio 
            return pedido
        
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # Prueba quye no comprendiói el audio
            print("Ups!, no entendí")

            #Devolver error
            return "Sigo esperando"
        
        # En caso de no resolver el pedido
        except sr.RequestError:

            # Prueba quye no comprendiói el audio
            print("Ups!, no hay servicio")

            #Devolver error
            return "Sigo esperando"
        
        # Error inesperado
        except:
            # Prueba quye no comprendiói el audio
            print("Ups!, algo salió mal")

            #Devolver error
            return "Sigo esperando"
        
# Función para que el asistente pueda ser escuchado
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar el día de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variable para el día de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombre de días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # Decir el día de la semana 
    hablar(f'Hoy es {calendario[dia_semana]} {dia.day}/{dia.month}/{dia.year}')

# Informar que hora es
def pedir_hora():

    # Crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    
    # Decir la hora
    hablar(hora)


# Función saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'

    elif 6 <= hora.hour < 13:
        momento = 'Buen día'

    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy Andromeda, tú asistente personal. Por favor, dime en qué te puedo ayudar')


# Función central del asistente
def pedir_cosas():

    # Activar saludo inicial:
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido: 
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https//www.google.com')
            continue

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue

        elif 'qué hora es' in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue

        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado: ')

        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue

        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue

        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break



pedir_cosas()