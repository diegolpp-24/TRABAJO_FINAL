# Importamos la libreria
import streamlit as st

# Creamos cada uno de los apartados de la página, con un inicio y una sección de cada juego.
paginas = ['INICIO', 'JAN KEN PO', 'AHORCADOS','TRES EN RAYA', 'TUTTI FRUTTI', 'PASAPALABRAS' ]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Comenzamos a dividir cada apartado con if, elif y else
if pagina_seleccionada == 'INICIO':
    # colocamos el titulo principal
    st.markdown("<h1 style='text-align: center;'>ZONA GAMER</h1>", unsafe_allow_html=True)
    
    #Colocamos el texto en variables para luego imprimirlos en la página
    texto_1_1 = """
    Bienvenido a una plataforma creada para revivir la emoción de los juegos de siempre. 
    Aquí encontrarás una selección de juegos simples pero entretenidos, pensados para disfrutar en cualquier momento, desde cualquier dispositivo y sin complicaciones.
    En un mundo cada vez más conectado, los juegos tradicionales siguen ocupando un lugar especial en la memoria y el entretenimiento de muchas generaciones. 
    Lejos de desaparecer, han encontrado una nueva forma de vivir: adaptándose al entorno digital y conectando con la cultura juvenil actual.
    """
    texto_1_2 = """
    Todo en una sola página, completamente gratuita y optimizada para que puedas retar a tus amigos desde cualquier dispositivo. 
    Nuestra misión es simple: ofrecerte partidas rápidas, entretenidas y llenas de nostalgia, con una interfaz limpia y sin distracciones.
    Solo abre tu juego favorito, ¡y que comience la diversión!"""
    
    # Llamamos el primer apartado de los textos
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_1_1}", unsafe_allow_html=True)
    
    # Usamos codigos vistos en videos para ordenar mejor el texto por puntos.
    st.subheader("Juegos clásicos como:")
    st.markdown("#### ✊ Jan Ken Po (Piedra, papel o tijera)")
    st.markdown("""
    - Juego clásico de manos basado en la lógica y el azar.  
    - Dos jugadores eligen simultáneamente entre piedra, papel o tijera.  
    - La piedra vence a la tijera, la tijera al papel y el papel a la piedra.  
    - Rápido, divertido y perfecto para resolver cualquier reto entre amigos.
    """)
    st.markdown("#### 🔤 Ahorcado")
    st.markdown("""
    - Juego de adivinanzas para descubrir una palabra secreta, letra por letra.  
    - Cada error dibuja una parte del ahorcado.  
    - El reto es completar la palabra antes de que el dibujo se termine.  
    - Ideal para poner a prueba tu vocabulario y agilidad mental.
    """)
    st.markdown("#### ❌⭕ Tic Tac Toe (Tres en raya)")
    st.markdown("""
    - Dos jugadores compiten por alinear tres símbolos (X o O) en una cuadrícula de 3x3.  
    - Gana quien forme una línea recta: horizontal, vertical o diagonal.  
    - Un juego sencillo pero estratégico, que nunca pasa de moda.
    """)
    st.markdown("#### 🍓 Tutti Frutti")
    st.markdown("""
    - Juego de agilidad mental y rapidez verbal.  
    - Se elige una letra al azar y se deben completar distintas categorías (nombre, fruta, país, etc.) con esa letra.  
    - ¡Divertido, competitivo y educativo!
    """)
    st.markdown("#### 🔠 Pasapalabra")
    st.markdown("""
    - Inspirado en el concurso televisivo, este juego pone a prueba tus conocimientos y memoria.  
    - Cada letra del abecedario tiene una definición, tú debes adivinar la palabra.  
    - Puedes decir “pasapalabra” si no sabes… ¡pero vuelve pronto a ella!
    """)
    
    # Volvemos a llamar al texto 2
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_1_2}</div>", unsafe_allow_html=True)
    
    # Colocamos el logo principal de la página
    st.image("logo.jpg", caption='', width=700)

elif  pagina_seleccionada == 'JAN KEN PO':
    ############################# TITULO #########################################
    st.markdown("<h1 style='text-align: center;'>JAN KEN PO</h1>", unsafe_allow_html=True)
    ############################## ORIGEN #######################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Origen e historia del juego</h2>", unsafe_allow_html=True)

    #colocamos el texto
    texto_2_1 = """
    Jan Ken Po, conocido globalmente como “Piedra, papel o tijera”, es un juego milenario que tiene sus raíces en la antigua China, alrededor del siglo II a.C., donde se practicaba un juego llamado shoushiling. 
    Posteriormente, se popularizó en Japón con el nombre de Jan-Ken, adoptando las formas modernas de “piedra” (puño cerrado), “papel” (mano extendida) y “tijera” (dedos en V).
    En su versión japonesa, el juego no solo era una forma de entretenimiento, sino también un modo simbólico de resolver disputas o tomar decisiones sin conflictos. 
    Su simplicidad y rapidez lo hicieron fácil de transmitir de generación en generación, cruzando continentes y culturas. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2_1}</div>", unsafe_allow_html=True)
    
    # colocamos una imagen representativa
    st.image("yan ken po 4.jpg", caption='', width=300)
    
    ############################ VALOR LATINO ##########################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Llegada y valor cultural en Latinoamérica</h2>", unsafe_allow_html=True)

    #colocamos el texto
    texto_2_2 = """
    A lo largo del siglo XX, Jan Ken Po llegó a Latinoamérica a través del intercambio cultural global, especialmente por la influencia japonesa en países como Brasil y Perú. 
    En su versión hispanohablante, el nombre más común pasó a ser “Piedra, papel o tijera”, aunque el término “Jan Ken Po” también se conserva en algunas zonas y versiones escolares del juego.
    En el contexto latinoamericano, este juego se ha convertido en un ritual lúdico universal, presente en patios escolares, recreos, juegos entre hermanos, y decisiones cotidianas (“¿quién va primero?”, “¿quién lava los platos?”). 
    Su valor cultural radica en su carácter inclusivo y espontáneo, ya que no requiere materiales ni preparación, y todos conocen las reglas.
    Más allá de un simple juego, Jan Ken Po representa la creatividad, improvisación y resolución pacífica de conflictos dentro de las culturas juveniles, mostrando cómo lo tradicional puede mantenerse vivo en contextos modernos. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2_2}</div>", unsafe_allow_html=True)
    
    # colocamos una imagen representativa
    st.image("yan ken po 5.png", caption='', width=500)

    ############################ POPULARIDAD ##########################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Tabla de popularidad respecto al país</h2>", unsafe_allow_html=True)

    #importamos la libreria pandas, para los diccionarios
    import pandas as pd

    #Creamos los diccionarios
    data = {
        "País": [
            "Perú, Brasil",
            "México",
            "Chile",
            "Colombia, Argentina, Ecuador, Uruguay, Venezuela",
            "Paraguay",
        ],
        "Nombre local": [
            "Jan Ken Po / Jankenpon",
            "Piedra, papel o tijera (también “chin chan pú”)",
            "Ca‑chi‑pún",
            "Piedra, papel o tijera",
            "Hakembó / Ha Ken Bo",
        ],
        "Grado de popularidad": [
            "Muy alta (uso común, variante original)",
            "Muy alta, juguete universal",
            "Alta, variante local",
            "Muy alta, nombre estándar",
            "Alta, variante regional",
        ],
    }

    df = pd.DataFrame(data)

    # Mostramos la tabla
    st.dataframe(df, use_container_width=True) 

    ############################ ANTES VS. DESPUES ##########################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Comparativa: antes vs. después de la digitalización</h2>", unsafe_allow_html=True)
    
    # colocamos variables con los textos respectivos
    texto_3_1 = """
    Antes (tradicional):
    Se jugaba en patios, recreos, calles; sin materiales pero con reglas simples 
    """
    texto_3_2 = """
    Después (era digital):
    Ha llegado a plataformas online y apps educativas, manteniendo su uso lúdico y pedagógico 
    Se han organizado torneos profesionales, campeonatos universitarios y mundiales con premios como el de la WRPSA o en la UK, incluso transmitidos en redes y TV 
    En redes sociales, aparece como fenómeno viral (como simuladores en TikTok con millones de interacciones) .
    """
    texto_3_3 = """
    Impacto:
    Antes: juego espontáneo, social y omnipresente.
    Ahora: convive con su versión online, ha ganado visibilidad global en medios, redes y deporte competitivo.
    """
    
    # llamamos a imprimir los textos
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_2}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_3}</div>", unsafe_allow_html=True)

    ############################ VIDEO ##########################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Video intuitivo</h2>", unsafe_allow_html=True)
    
    # colocamos el link del video en el codigo respectivo
    st.video("https://www.youtube.com/watch?v=gJJ-SHJgNnY")

    ############################ JUEGO ##########################################
    # Colocamos un subtitulo
    st.markdown("<h2 style='text-align: center;'>Prueba el juego</h2>", unsafe_allow_html=True)

    # Este juego fue mejorado con la IA
    # Importamos la libreria random para la variable aleatoria
    import random

    # Creamos las opciones existentes
    st.set_page_config(page_title="Piedra • Papel • Tijeras",
                    page_icon="✊",
                    layout="centered")

    OPCIONES = ("Piedra", "Papel", "Tijeras")

    # Iniciar / mantener el marcador en la sesión
    if "jugador" not in st.session_state:
        st.session_state.update(jugador=0, maquina=0, empates=0)

    # Creamos los titulos que se mostraran en pantalla
    st.title("✊🖐️✌️  Piedra • Papel • Tijeras")
    st.caption("Juega contra la computadora directamente en tu navegador.")

    # Creamos los botones en dos columnas, en una la opcion que elige el jugador y en la otra el boton de empezar el juego.
    col1, col2 = st.columns([2, 1])
    with col1:
        # se crean las opciones que aparecen en pantalla
        jugada_usuario = st.radio(
            "Elige tu jugada:",
            OPCIONES,
            index=0,
            key="eleccion_usuario"
        )
    with col2:
        # se crea el boton de jugar
        jugar = st.button("¡Jugar!")

    # creamos la logica del juego a base de if, elif y else para las condiciones
    def ganador(jugador: str, maquina: str) -> str:
        if jugador == maquina:
            return "empate"
        gana_jugador = (
            (jugador == "Piedra" and maquina == "Tijeras") or
            (jugador == "Papel"  and maquina == "Piedra")  or
            (jugador == "Tijeras" and maquina == "Papel")
        )
        return "jugador" if gana_jugador else "maquina"

    if jugar:
        # colocamos los codigos de la libreria random para que la maquina elija aleatoriamente una opción
        jugada_pc = random.choice(OPCIONES)
        resultado = ganador(jugada_usuario, jugada_pc)

        # Mostrar resultados dependiendo las elecciones de ambos jugadores
        st.subheader("Resultado de la ronda")
        # se muestra las elecciones de ambos en pantalla
        st.write(f"**Tú:** {jugada_usuario}  \n**Computadora:** {jugada_pc}")

        # se dan las condiciones para cada caso
        if resultado == "empate":
            st.info("🟰 ¡Empate!")
            # se coloca contador para las tabla del marcador
            st.session_state.empates += 1
        elif resultado == "jugador":
            st.success("🎉 ¡Ganaste esta ronda!")
            # se coloca contador para las tabla del marcador
            st.session_state.jugador += 1
        else:
            st.error("💻 La computadora gana esta ronda.")
            # se coloca contador para las tabla del marcador
            st.session_state.maquina += 1

    # llamamos los codigos para la tabla de marcador, esto tomado de la IA como apoyo
    # en cada uno de ellas tienen contadores, los cuales van cambiando y aumentando dependiendo de los resultados de cada partida
    st.markdown("---")
    st.subheader("📊 Marcador")
    st.write(f"- Tú: **{st.session_state.jugador}**")
    st.write(f"- Computadora: **{st.session_state.maquina}**")
    st.write(f"- Empates: **{st.session_state.empates}**")

    # Este codigo reinicia el contador, aunque no esta bien estructurado para una pagina, otro metodo es la actualización de la página
    if st.button("Reiniciar marcador"):
        st.session_state.update(jugador=0, maquina=0, empates=0)
        st.experimental_rerun()

    ############################ LINKS ##########################################
    # se coloca subtitulos
    st.markdown("<h2 style='text-align: center;'>Juego oficial</h2>", unsafe_allow_html=True)
    # se coloca imagen de la pagina que elegimos como juego oficial
    st.image("juego1.jpeg", caption='', width=700)
    # se coloca el link de la otra pagina de juegos
    st.markdown(f"<div style='text-align: center;'><a href='https://www.fr9.es/juegosdiarios/juegos/piedra-papel-o-tijera.html' target='_blank'><button>Yan Ken Po</button></a></div>", unsafe_allow_html=True) 
    
    ############################ DATOS Y CURIOSIDADES ##########################################
    # se llama a subtitulos
    st.markdown("<h2 style='text-align: center;'>Datos y curiosidades</h2>", unsafe_allow_html=True)
    # el apartado de las curiosidades elegidas, se crea un diccionario con titulos, emojis y el contenido
    curiosidades = [
        {
            "titulo": "📜 1. Es más antiguo de lo que imaginas",
            "contenido": "El juego tiene más de 2000 años de antigüedad. Nació en la antigua China como 'shoushiling' y luego se popularizó en Japón como 'Jan-Ken', con las formas actuales: piedra, papel y tijera."
        },
        {
            "titulo": "🌍 2. Tiene nombres distintos según el país",
            "contenido": "Dependiendo del país, cambia de nombre: 'Jan Ken Po' (Perú, Japón), 'Ca-chi-pún' (Chile), 'Chin Chan Pú' (México), y 'Piedra, papel o tijera' en la mayoría de Latinoamérica."
        },
        {
            "titulo": "🧠 3. No es completamente azaroso",
            "contenido": "Aunque parece de azar, los humanos siguen patrones. Por ejemplo, quien gana suele repetir su gesto. ¡Hay estrategias para ganar más veces!"
        },
        {
            "titulo": "🏆 4. Tiene torneos internacionales",
            "contenido": "Existen campeonatos oficiales como el World Rock Paper Scissors Championship, con premios reales y participantes de todo el mundo."
        },
        {
            "titulo": "🤖 5. Existen versiones con más elementos",
            "contenido": "Hay versiones extendidas como 'Piedra, papel, tijera, lagarto, Spock' (de The Big Bang Theory), y otras que incluyen caracol, serpiente y más."
        },
        {
            "titulo": "🎮 6. Aparece en videojuegos y series",
            "contenido": "Jan Ken Po se ha usado en videojuegos como Pokémon y Final Fantasy, y también en animes como Naruto o Dragon Ball."
        },
        {
            "titulo": "📲 7. En la era digital, sigue creciendo",
            "contenido": "Hoy en día, hay miles de apps, minijuegos y bots que usan este juego como mecánica rápida de decisión. ¡Incluso tiene versiones educativas!"
        },
    ]

    # Mostrar curiosidades en bloques expandibles sacado de la IA
    for item in curiosidades:
        with st.expander(item["titulo"]):
            st.write(item["contenido"])

    ############################ COMENTARIOS ##########################################
    # llamamos a las librerias datetime y os, estos ayudan con los comentarios
    from datetime import datetime
    import os
    # ponemos los titulos que contendran los comentarios
    st.markdown("---")
    st.header("💬 Comparte tu opinión")

    COMMENTS_FILE = "comentarios_ppt.csv"

    @st.cache_data(show_spinner=False)
    def load_comments(path: str) -> pd.DataFrame:
        """Carga los comentarios existentes (o crea el archivo si no existe)."""
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            empty = pd.DataFrame(columns=["timestamp", "nombre", "comentario"])
            empty.to_csv(path, index=False)
            return empty

    def add_comment(path: str, nombre: str, comentario: str) -> None:
        """Añade un nuevo comentario al archivo."""
        df = load_comments(path)
        nuevo = pd.DataFrame({
            "timestamp": [datetime.now().isoformat(timespec="seconds")],
            "nombre": [nombre if nombre else "Anónimo"],
            "comentario": [comentario.strip()],
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(path, index=False)

    # En este apartado se pide que el usuario comente
    with st.form("comment_form", clear_on_submit=True, border=True):
        nombre = st.text_input("Tu nombre (opcional)")
        comentario = st.text_area("Escribe tu comentario aquí 👇")
        enviado = st.form_submit_button("Enviar")

################################################################################################
################################################################################################

elif  pagina_seleccionada == 'AHORCADOS':
    ############################# TITULO #########################################
    # se coloca el titulo principal
    st.markdown("<h1 style='text-align: center;'>AHORCADOS</h1>", unsafe_allow_html=True)
    ############################## ORIGEN #######################################
    # se coloca los subtitulos
    st.markdown("<h2 style='text-align: center;'>Origen e historia del juego</h2>", unsafe_allow_html=True)
    # se coloca las variables de texto con su contenido para luego llamarlas en código
    texto_3_1 = """
    La versión más popular sobre el origen del juego del ahorcado, aunque no cuenta con documentación oficial, relata que entre los siglos XVII y XVIII existía un supuesto “Rito de palabra o vida”, en el que los condenados a muerte podían salvarse adivinando una palabra elegida por el verdugo; cada error implicaba romper una pata de la mesa de cinco patas sobre la que estaban parados, y al fallar cinco veces eran ahorcados, pero si acertaban, eran liberados. 
    La primera referencia histórica real aparece en el libro The Traditional Games of England, Scotland, and Ireland (1894) de Alice Bertha Gomme, donde se describe un juego similar, aunque sin la figura del ahorcado, usando en su lugar un sistema de puntuación. 
    Otra leyenda sugiere un origen más simbólico: la historia de un hombre que se suicidó tras escuchar de su esposa que ya no lo amaba, reforzando así la idea de que las palabras equivocadas pueden causar daño mortal, lo que da al juego una advertencia sobre el poder del lenguaje. 
    """
    # se llama la variable de texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_1}</div>", unsafe_allow_html=True)
    #Se coloca una imagen representativa
    st.image("ahorcado2.webp", caption='', width=700)
    
    ############################ VALOR LATINO ##########################################
    # se coloca un subtitulo
    st.markdown("<h2 style='text-align: center;'>Llegada y valor cultural en Latinoamérica</h2>", unsafe_allow_html=True)

    texto_3_2 = """
    Escoge bien tu siguiente letra, o podría ser la última. 
    Ahorcados es un juego que invita al jugador a que adivine una palabra, normalmente dentro de una categoría, basándose en la cantidad de espacio vacíos que existen para completar la palabra.
    Si es que el concursante se equivoca, se empezara a dibujar a un hombre colgado, pero de manera creciente: primero su eje central, luego sus extremidades, luego su cabeza y ya, si el participante supera esta fase, el hombre terminará colgado y el juego habrá llegado a su fin. 
    Este juego se volvió popular en salones de clase de los 80‑90, en cuadernos y pizarras como método lúdico de aprender ortografía y vocabulario. Durante los procesos de modernización educativa, fue un aliado de maestros para hacer más dinámicas las lecciones y reforzar la alfabetización en países en transición democrática. 
    """
    # se coloca las variables de texto con su contenido para luego llamarlas en código
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_2}</div>", unsafe_allow_html=True)
    #Se coloca una imagen representativa
    st.image("ahorcado.webp", caption='', width=500)

    ############################ POPULARIDAD ##########################################
    # se coloca subtitulo
    st.markdown("<h2 style='text-align: center;'>Tabla de popularidad respecto al país</h2>", unsafe_allow_html=True)

    # se importa las librerias correspondientes
    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os
    # se crea una data con un diccionario con los datos
    data = {
        "País": [
            "México",
            "Perú",
            "Colombia",
            "Argentina",
            "Chile",
            "Venezuela",
            "Bolivia",
            "Paraguay",
        ],
        "Nombre local": [
            "El ahorcado",
            "El ahorcado",
            "Juego del ahorcado",
            "El juego del ahorcado",
            "Ahorcado / El juego de letras",
            "Ahorcado",
            "Ahorcado",
            "Juego del colgado / Ahorcado",
        ],
        "Grado de popularidad": [
            "Alta, se juega en escuelas y hogares",
            "Muy alta, conocido en todo el país",
            "Media, más común en el pasado",
            "Alta, usado en educación",
            "Alta, sobre todo entre niños",
            "Media, conocido pero poco jugado hoy",
            "Media-baja, en desuso reciente",
            "Media, variante con dibujo local",
        ],
    }
    df_pop = pd.DataFrame(data)
    # se llama a la tabla de popularidad
    st.dataframe(df_pop, use_container_width=True)


    ############################ ANTES VS. DESPUES ##########################################
    # se llama a un subtitulo
    st.markdown("<h2 style='text-align: center;'>Comparativa: antes vs. después de la digitalización</h2>", unsafe_allow_html=True)
    # se coloca las variables de texto con su contenido
    texto_3_4 = """
    Antes de la digitalización, el juego del ahorcado se jugaba de forma presencial, usando papel, pizarra o incluso de manera oral, con una interacción directa entre los participantes. 
    El diseño era simple y manual, con líneas y dibujos que representaban al ahorcado, y el objetivo principal era entretener mientras se reforzaba la ortografía y el vocabulario. 
    La experiencia era espontánea, social y no quedaba ningún registro del juego. 
    """
    texto_3_5 = """
    Después (era digital):
    Con la digitalización, el ahorcado se transformó en una experiencia interactiva accesible desde computadoras, móviles o tabletas, con gráficos, sonidos y opciones personalizables como categorías temáticas o niveles de dificultad. 
    Además, permite jugar en solitario o en línea, guardar progresos, competir con otros usuarios y convertirse en una herramienta lúdica y educativa más sofisticada, aunque a veces con menos contacto humano directo.
    """
    texto_3_6 = """
    Impacto:
    Antes: juego espontáneo, social y omnipresente.
    Ahora: convive con su versión online, ha ganado visibilidad global en medios, redes y deporte competitivo.
    """
    
    # se llama a cada uno de las variables de texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_4}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_5}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3_6}</div>", unsafe_allow_html=True)

    ############################ VIDEO ##########################################
    # se coloca el subtitulo
    st.markdown("<h2 style='text-align: center;'>Video intuitivo</h2>", unsafe_allow_html=True)
    # se coloca el link de uno de los videos intuitivos 
    st.video("https://www.youtube.com/watch?v=bZUqvTQN8q4")

    ############################ JUEGO ##########################################
    # se coloca un subtitulo
    st.markdown("<h2 style='text-align: center;'>Prueba el juego</h2>", unsafe_allow_html=True)
    # se llama la libreria random para una elección aleatoria
    import random
    # Palabras posibles 
    PALABRAS = ['juego', 'apruebenos', 'comunicación', 'zona gamer', 'pelota', 'programa', 'fiesta']

    # Inicializar el juego en la sesión si es la primera vez
    if 'palabra' not in st.session_state:
        st.session_state.palabra = random.choice(PALABRAS)
        st.session_state.letras_adivinadas = []
        st.session_state.intentos = 6
        st.session_state.juego_terminado = False

    # Mostrar la palabra con guiones y letras adivinadas
    palabra_mostrada = ''
    for letra in st.session_state.palabra:
        if letra in st.session_state.letras_adivinadas:
            palabra_mostrada += letra + ' '
        else:
            palabra_mostrada += '_ '

    st.write(f"**Palabra:** {palabra_mostrada.strip()}")

    # Mostrar letras adivinadas e intentos restantes
    st.write(f"**Letras adivinadas:** {' '.join(st.session_state.letras_adivinadas)}")
    st.write(f"**Intentos restantes:** {st.session_state.intentos}")

    # Campo para ingresar una letra
    if not st.session_state.juego_terminado:
        letra = st.text_input("Adivina una letra:", max_chars=1).lower()

        if st.button("Intentar"):
            if letra and letra.isalpha():
                if letra in st.session_state.letras_adivinadas:
                    st.warning("Ya intentaste con esa letra.")
                else:
                    st.session_state.letras_adivinadas.append(letra)
                    if letra not in st.session_state.palabra:
                        st.session_state.intentos -= 1
                        st.error("¡Letra incorrecta!")

            # Verificar si el juego terminó
            if all(l in st.session_state.letras_adivinadas for l in st.session_state.palabra):
                st.success(f"🎉 ¡Ganaste! La palabra era **{st.session_state.palabra}**.")
                st.session_state.juego_terminado = True
            elif st.session_state.intentos == 0:
                st.error(f"💀 ¡Perdiste! La palabra era **{st.session_state.palabra}**.")
                st.session_state.juego_terminado = True

    # Botón para reiniciar el juego
    if st.button("🔄 Reiniciar juego"):
        st.session_state.palabra = random.choice(PALABRAS)
        st.session_state.letras_adivinadas = []
        st.session_state.intentos = 6
        st.session_state.juego_terminado = False

    ############################ LINKS ##########################################
    st.markdown("<h2 style='text-align: center;'>Juego oficial</h2>", unsafe_allow_html=True)
    # se coloca una imagen referencial de la página
    st.image("ahorcado3.png", caption='', width=500)
    # un codigo que coloque un boton con el link de la página
    st.markdown(f"<div style='text-align: center;'><a href='https://www.epasatiempos.es/movil/ahorcado.php' target='_blank'><button>Diviertete</button></a></div>", unsafe_allow_html=True) 
    
    ############################ DATOS Y CURIOSIDADES ##########################################
    st.markdown("<h2 style='text-align: center;'>Datos y curiosidades</h2>", unsafe_allow_html=True)

    # se llaman a las librerias necesarias
    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    # se crea un diccionario con todos los datos
    curiosidades = [
        "🔤 El Ahorcado es uno de los juegos más antiguos de adivinanza de palabras. Se jugaba ya en el siglo XIX.",
        "📚 Fue mencionado por primera vez en un libro de juegos de 1894, titulado *Traditional Games* por Alice Gomme.",
        "👨‍🏫 En muchas escuelas se usa para enseñar vocabulario, ortografía y lógica.",
        "🌐 En inglés se llama *Hangman*, y en francés *Pendu* (el colgado).",
        "🖍️ En su versión tradicional, cada error dibuja una parte del cuerpo del personaje (cabeza, torso, brazos, etc.).",
        "⚖️ En algunos países se ha cuestionado su temática (el 'ahorcamiento') por razones pedagógicas y simbólicas.",
        "🧠 Hay versiones modernas que reemplazan al ahorcado por un robot, frutas, naves o piezas de rompecabezas.",
        "📱 Existen cientos de versiones del juego en aplicaciones móviles y páginas web educativas.",
    ]

    # Mostrar curiosidad
    for curiosidad in curiosidades:
        st.markdown(f"- {curiosidad}")

    ############################ COMENTARIOS ##########################################
    
    from datetime import datetime
    import os
    # los comentarios para cada juego son iguales
    st.markdown("---")
    st.header("💬 Comparte tu opinión")

    COMMENTS_FILE = "comentarios_ppt.csv"

    @st.cache_data(show_spinner=False)
    def load_comments(path: str) -> pd.DataFrame:
        """Carga los comentarios existentes (o crea el archivo si no existe)."""
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            empty = pd.DataFrame(columns=["timestamp", "nombre", "comentario"])
            empty.to_csv(path, index=False)
            return empty

    def add_comment(path: str, nombre: str, comentario: str) -> None:
        """Añade un nuevo comentario al archivo."""
        df = load_comments(path)
        nuevo = pd.DataFrame({
            "timestamp": [datetime.now().isoformat(timespec="seconds")],
            "nombre": [nombre if nombre else "Anónimo"],
            "comentario": [comentario.strip()],
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(path, index=False)

    with st.form("comment_form", clear_on_submit=True, border=True):
        nombre = st.text_input("Tu nombre (opcional)")
        comentario = st.text_area("Escribe tu comentario aquí 👇")
        enviado = st.form_submit_button("Enviar")
################################################################################################

elif  pagina_seleccionada == 'TRES EN RAYA':
    ############################# TITULO #########################################
    st.markdown("<h1 style='text-align: center;'>TRES EN RAYA</h1>", unsafe_allow_html=True)
    ############################## ORIGEN #######################################
    st.markdown("<h2 style='text-align: center;'>Origen e historia del juego</h2>", unsafe_allow_html=True)

    texto_2_1 = """
    Los juegos de mesa surgieron en el Neolítico y fueron evolucionando en la Edad de Bronce.
    La historia del tres en raya tal y como conocemos se remonta a la lejana Persia, hace casi mil años, desde donde mercaderes italianos lo exportaron a sus tierras y lo extendieron. 
    En poco tiempo se convirtió en uno de los juegos más populares de las clases bajas en la Edad Media. 
    En España se conservan numerosas pruebas de lo extendido que estaba este juego.
    El juego que todos conocemos es muy fácil de recrear y eso fue vital a la hora de su pronta expansión. 
    Tuvo un periodo negro, entre los siglos X y XI debido a su asociación con rituales paganos y su descalificación por parte de las clases altas de la sociedad. 
    Tal fue su importancia y fama que el Papa Bonifacio VI creó una bula papal que prohibía su práctica para todos los cristianos, arrinconando así el juego como un elemento de la magia negra o pagana.
    La práctica de las tres en raya fue poco a poco resurgiendo en las universidades, siendo muy popular en Salamanca y Bolonia. Verdaderamente hasta el Renacimiento no fue cuando este juego volvió a formar parte de la cultura popular y se extendió como nunca antes, pero esto no significa que no se siguiera jugando en el medievo.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2_1}</div>", unsafe_allow_html=True)
    st.image("3rayas.png", caption='', width=400)
    
    ############################ VALOR LATINO ##########################################
    st.markdown("<h2 style='text-align: center;'>Llegada y valor cultural en Latinoamérica</h2>", unsafe_allow_html=True)

    texto_2_2 = """
    Tic Tac Toe, logra colocar tres elementos similares en la misma línea y habrás ganado! 
    No importa así sea vertical, horizontal o diagonal, el objetivo sigue siendo el mismo, así que evita que tu enemigo se atraviese en tu camino. 
    Rescatado de la antigüedad romana, tomó fuerza en los 70s-90s en escuelas y periódicos. En periodos de incertidumbre política y crisis económicas (como los 80s), ofrecía entretenimiento barato y universal que rompía clases sociales: un juego de café, bus, escuela o parque, uniendo a todos por igual. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2_2}</div>", unsafe_allow_html=True)
    st.image("3rayas2.png", caption='', width=400)

    ############################ POPULARIDAD ##########################################
    st.markdown("<h2 style='text-align: center;'>Tabla de popularidad respecto al país</h2>", unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    data = {
        "País": [
            "México",
            "Perú",
            "Colombia",
            "Argentina",
            "Chile",
            "Venezuela, Ecuador, Bolivia",
            "Paraguay",
            "Uruguay",
        ],
        "Nombre local": [
            "Gato / Tres en raya",
            "Tres en raya / Gato",
            "Triqui / Triki",
            "Tatetí",
            "Gato",
            "Gato",
            "Tres en línea / Gato",
            "Tatetí",
        ],
        "Grado de popularidad": [
            "Muy alta, común entre niños y en papel",
            "Muy alta, juego clásico escolar",
            "Muy alta, tradicional en recreos",
            "Alta, jugado en papel y digital",
            "Alta, asociado a infancia y escuela",
            "Alta, aún vigente en juegos informales",
            "Media, se juega en zonas escolares",
            "Alta, juego de papel muy difundido",
        ]
    }

    df_pop = pd.DataFrame(data)

    st.dataframe(df_pop, use_container_width=True)


    ############################ ANTES VS. DESPUES ##########################################
    st.markdown("<h2 style='text-align: center;'>Comparativa: antes vs. después de la digitalización</h2>", unsafe_allow_html=True)
    texto_4_1 = """
    La jugabilidad no ha cambiado mucho en la versión actual, lo que convierte a Tic Tac Toe en el juego perfecto para perder el tiempo. El juego se puede jugar literalmente en cualquier superficie, siempre que los jugadores tengan algo para escribir o marcar sus espacios.
    Strategic Tic Tac Toe es una versión derivada del juego con un giro complicado. 
    Los jugadores deben conectar tres X u O en varias cuadrículas más pequeñas. El ganador de cada juego luego coloca una X o una O más grande en una cuadrícula de 3x3 más grande. Esta versión permite a los jugadores pensar un poco más en cómo están jugando. Tienen que diseñar una estrategia para sus victorias de modo que se alinean tres tableros más pequeños.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4_1}</div>", unsafe_allow_html=True)


    ############################ VIDEO ##########################################
    st.markdown("<h2 style='text-align: center;'>Video intuitivo</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=u5RFayoUqOU")

    ############################ JUEGO ##########################################
    st.markdown("<h2 style='text-align: center;'>Prueba el juego</h2>", unsafe_allow_html=True)

    import streamlit as st
    import random

    # Inicializar estado del juego
    if 'tablero' not in st.session_state:
        st.session_state.tablero = ['' for _ in range(9)]
        st.session_state.jugador = 'X'
        st.session_state.ia = 'O'
        st.session_state.ganador = None
        st.session_state.turno = 'jugador'

    # Función para verificar ganador
    def verificar_ganador(tablero):
        combinaciones = [
            [0,1,2],[3,4,5],[6,7,8], 
            [0,3,6],[1,4,7],[2,5,8], 
            [0,4,8],[2,4,6]          
        ]
        for c in combinaciones:
            if tablero[c[0]] != '' and tablero[c[0]] == tablero[c[1]] == tablero[c[2]]:
                return tablero[c[0]]
        return None

    # Turno de la computadora
    def turno_ia():
        libres = [i for i, v in enumerate(st.session_state.tablero) if v == '']
        if libres:
            eleccion = random.choice(libres)
            st.session_state.tablero[eleccion] = st.session_state.ia
            st.session_state.ganador = verificar_ganador(st.session_state.tablero)
            st.session_state.turno = 'jugador'

    # Reiniciar juego
    def reiniciar():
        st.session_state.tablero = ['' for _ in range(9)]
        st.session_state.ganador = None
        st.session_state.turno = 'jugador'

    # Mostrar tablero
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = i*3 + j
            with cols[j]:
                if st.button(st.session_state.tablero[idx] or " ", key=idx, use_container_width=True):
                    if st.session_state.tablero[idx] == '' and not st.session_state.ganador and st.session_state.turno == 'jugador':
                        st.session_state.tablero[idx] = st.session_state.jugador
                        st.session_state.ganador = verificar_ganador(st.session_state.tablero)
                        if not st.session_state.ganador and '' in st.session_state.tablero:
                            st.session_state.turno = 'ia'
                            turno_ia()

    # Mensajes de estado
    if st.session_state.ganador:
        st.success(f"🏆 ¡Ganó {'Tú' if st.session_state.ganador == st.session_state.jugador else 'la computadora'}!")
    elif '' not in st.session_state.tablero:
        st.info("🤝 ¡Empate!")
    else:
        st.write(f"Turno: {'Tu turno' if st.session_state.turno == 'jugador' else 'Turno de la computadora'}")

    # Botón de reinicio
    st.button("🔄 Reiniciar Juego", on_click=reiniciar)


    ############################ LINKS ##########################################
    st.markdown("<h2 style='text-align: center;'>Juego oficial</h2>", unsafe_allow_html=True)
    st.image("3rayas3.png", caption='', width=700)
    st.markdown(f"<div style='text-align: center;'><a href='https://papergames.io/es/r/lm9spR2zvE' target='_blank'><button>JUEGA</button></a></div>", unsafe_allow_html=True) 
    
    ############################ DATOS Y CURIOSIDADES ##########################################
    st.markdown("<h2 style='text-align: center;'>Datos y curiosidades</h2>", unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    curiosidades = [
        "🧠 Es uno de los primeros juegos de estrategia que aprenden los niños en todo el mundo.",
        "🏛️ Su origen se remonta al antiguo Egipto y al Imperio Romano, donde se jugaban variantes similares.",
        "✍️ El nombre *tatetí* proviene de la simplificación fonética del patrón de juego 'ta-te-ti'.",
        "📐 Aunque parece simple, hay estrategias para empatar siempre si juegas perfectamente.",
        "🎮 Ha sido adaptado a videojuegos, apps móviles y hasta inteligencia artificial.",
        "👶 Muchos lo aprenden dibujando el tablero con lápiz y papel durante clases o recreos.",
        "📊 Solo existen 255.168 partidas posibles, y de ellas, 46.080 terminan en victoria.",
        "🔁 En algunos lugares se juega con tablero de 4x4 o 5x5 como versiones más avanzadas.",
    ]
    for dato in curiosidades:
        st.markdown(f"- {dato}")

    ############################ COMENTARIOS ##########################################
    
    from datetime import datetime
    import os

    st.markdown("---")
    st.header("💬 Comparte tu opinión")

    COMMENTS_FILE = "comentarios_ppt.csv"

    @st.cache_data(show_spinner=False)
    def load_comments(path: str) -> pd.DataFrame:
        """Carga los comentarios existentes (o crea el archivo si no existe)."""
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            empty = pd.DataFrame(columns=["timestamp", "nombre", "comentario"])
            empty.to_csv(path, index=False)
            return empty

    def add_comment(path: str, nombre: str, comentario: str) -> None:
        """Añade un nuevo comentario al archivo."""
        df = load_comments(path)
        nuevo = pd.DataFrame({
            "timestamp": [datetime.now().isoformat(timespec="seconds")],
            "nombre": [nombre if nombre else "Anónimo"],
            "comentario": [comentario.strip()],
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(path, index=False)

    with st.form("comment_form", clear_on_submit=True, border=True):
        nombre = st.text_input("Tu nombre (opcional)")
        comentario = st.text_area("Escribe tu comentario aquí 👇")
        enviado = st.form_submit_button("Enviar")
################################################################################################

elif  pagina_seleccionada == 'TUTTI FRUTTI':
    ############################# TITULO #########################################
    st.markdown("<h1 style='text-align: center;'>TUTTI FRUTTI</h1>", unsafe_allow_html=True)
    ############################## ORIGEN #######################################
    st.markdown("<h2 style='text-align: center;'>Origen e historia del juego</h2>", unsafe_allow_html=True)

    texto_5_1 = """
    No se sabe exactamente cuándo se inventó el juego, en qué época o en qué lugar en particular, pero ciertamente nació entre los pupitres de la escuela. 
    Es en esa área donde tiene más éxito y en poco tiempo se vuelve popular también en varias partes del mundo porque es simple, divertido y requiere poco material para usar.
    Pero sin dudas su nombre le da el toque ítalo-argentino. 
    Su nombre tutti frutti se puede interpretar como un dicho argentino “mándale fruta” quizás por la rapidez y el apuro en el que hay que escribir la palabra en cada categoría para poder sacar la máxima cantidad de puntos. 
    En Italia este juego se lo conoce como:  Nomi, cose, città (Nombres, cosas, ciudades) diverso que la Argentina.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5_1}</div>", unsafe_allow_html=True)
    st.image("tuti.jpg", caption='', width=700)
    
    ############################ VALOR LATINO ##########################################
    st.markdown("<h2 style='text-align: center;'>Llegada y valor cultural en Latinoamérica</h2>", unsafe_allow_html=True)

    texto_5_2 = """
    Una letra, diversas categorías para elegir, un solo objetivo: ser quien tenga todas estas completas en base a que, sea lo que sea se te pida, comience con la letra indicada y que, obviamente, tenga un sentido común para los concursantes. 
    Tutti Fruti o también conocido como "Basta" se hizo popular en reuniones familiares y escuelas durante los 80–90, en tiempos donde convivir era esencial por la ausencia de internet. 
    Era un puente de integración entre generaciones, incluso en países divididos políticamente, promoviendo la cultura general a través del juego.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5_2}</div>", unsafe_allow_html=True)
    st.image("tuti2.jpg", caption='', width=500)

    ############################ POPULARIDAD ##########################################
    st.markdown("<h2 style='text-align: center;'>Tabla de popularidad respecto al país</h2>", unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    data = {
        "País": [
            "Perú",
            "México",
            "Argentina",
            "Colombia",
            "Chile",
            "Venezuela",
            "Bolivia",
            "Paraguay",
            "Uruguay",
            "Ecuador"
        ],
        "Nombre local": [
            "Tutti Frutti / Basta",
            "Basta / Stop",
            "Tutti Frutti",
            "Stop / Basta",
            "Tutti Frutti",
            "Stop / Basta",
            "Mercadito / Stop",
            "Tutti Frutti",
            "Tutti Frutti",
            "Basta / Stop"
        ],
        "Grado de popularidad": [
            "Muy alta, tradicional en colegios",
            "Muy alta, ampliamente jugado en primaria y secundaria",
            "Muy alta, muy común en juegos familiares",
            "Alta, sobre todo en edad escolar",
            "Muy alta, conocido por generaciones",
            "Alta, presente en contextos escolares",
            "Media, en zonas escolares y rurales",
            "Media-alta, conocido entre jóvenes",
            "Alta, juego clásico en papel",
            "Media, ha perdido presencia con lo digital"
        ]
    }

    df_pop = pd.DataFrame(data)

    st.dataframe(df_pop, use_container_width=True)

    ############################ ANTES VS. DESPUES ##########################################
    st.markdown("<h2 style='text-align: center;'>Comparativa: antes vs. después de la digitalización</h2>", unsafe_allow_html=True)
    texto_5_1 = """
    Antes (tradicional):
    Antes de la digitalización, el juego de Tutti Frutti se jugaba de manera manual, con lápiz, papel y entre varios participantes que se reunían físicamente. 
    Cada jugador dibuja una tabla con categorías como nombre, ciudad, comida, etc., y se elegía una letra al azar para comenzar. 
    El juego requería rapidez mental y escritura ágil, y su encanto radica en la interacción directa, las risas compartidas y los debates sobre respuestas dudosas. 
    """
    texto_5_2 = """
    Después (era digital):
    Con la digitalización, Tutti Frutti se trasladó a plataformas en línea y aplicaciones móviles, permitiendo jugar con personas de todo el mundo, guardar puntuaciones automáticamente y elegir entre muchas más categorías. 
    Ahora incluye cronómetros automáticos, diseño visual llamativo y opciones de juego en solitario o competitivo. 
    Aunque se ha ganado en accesibilidad, dinamismo y variedad, se ha perdido en parte la calidez y espontaneidad del juego tradicional entre amigos cara a cara.
    """
    texto_5_3 = """
    Impacto:
    Antes: juego espontáneo, social y omnipresente.
    Ahora: convive con su versión online, ha ganado visibilidad global en medios, redes y deporte competitivo.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5_1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5_2}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5_3}</div>", unsafe_allow_html=True)

    ############################ VIDEO ##########################################
    st.markdown("<h2 style='text-align: center;'>Video intuitivo</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=_t6YT61c600")

    ############################ JUEGO ##########################################
    st.markdown("<h2 style='text-align: center;'>Prueba el juego</h2>", unsafe_allow_html=True)

    import streamlit as st
    import random
    import string

    # Categorías que se pueden usar
    CATEGORIAS = ['Nombre', 'Apellido', 'Ciudad', 'Animal', 'Fruta', 'Color', 'Cosa']

    # Inicializar el juego en la sesión
    if 'letra_actual' not in st.session_state:
        st.session_state.letra_actual = random.choice(string.ascii_uppercase)
        st.session_state.respuestas = {cat: '' for cat in CATEGORIAS}
        st.session_state.mostrando_resultados = False

    # Función para reiniciar el juego
    def nuevo_juego():
        st.session_state.letra_actual = random.choice(string.ascii_uppercase)
        st.session_state.respuestas = {cat: '' for cat in CATEGORIAS}
        st.session_state.mostrando_resultados = False

    # Mostrar letra
    st.header(f"Letra: {st.session_state.letra_actual}")

    # Formulario para respuestas
    with st.form("tutti_frutti_form"):
        for categoria in CATEGORIAS:
            st.session_state.respuestas[categoria] = st.text_input(f"{categoria}:", value=st.session_state.respuestas[categoria])
        
        enviado = st.form_submit_button("✋ ¡STOP!")

    # Mostrar resultados si se presiona STOP
    if enviado:
        st.session_state.mostrando_resultados = True

    if st.session_state.mostrando_resultados:
        st.subheader("📋 Tus respuestas:")
        puntos_totales = 0
        for categoria, respuesta in st.session_state.respuestas.items():
            if respuesta.strip().lower().startswith(st.session_state.letra_actual.lower()):
                puntos = 10
                st.success(f"{categoria}: {respuesta} ✅ (+{puntos} puntos)")
            elif respuesta.strip() == '':
                puntos = 0
                st.warning(f"{categoria}: (vacío) ⚠️ (+{puntos} puntos)")
            else:
                puntos = 5
                st.info(f"{categoria}: {respuesta} ❌ (+{puntos} puntos, no empieza con la letra)")
            puntos_totales += puntos

        st.markdown(f"### 🎯 **Puntaje total: {puntos_totales} puntos**")

    # Botón para nuevo juego
    st.button("🔄 Nueva letra / Juego", on_click=nuevo_juego)



    ############################ LINKS ##########################################
    st.markdown("<h2 style='text-align: center;'>Juego oficial</h2>", unsafe_allow_html=True)
    st.image("tuti4.png", caption='', width=700)
    st.markdown(f"<div style='text-align: center;'><a href='https://stopots.com/es/' target='_blank'><button>JUEGA</button></a></div>", unsafe_allow_html=True) 
    
    ############################ DATOS Y CURIOSIDADES ##########################################
    st.markdown("<h2 style='text-align: center;'>Datos y curiosidades</h2>", unsafe_allow_html=True)

    curiosidades = [
        "🧠 Es un excelente ejercicio mental para ampliar vocabulario y agilidad verbal.",
        "📋 El nombre 'Tutti Frutti' proviene de la idea de juntar muchas categorías mezcladas, como una ensalada de frutas.",
        "✋ En muchos países se grita '¡Basta!' o '¡Stop!' para frenar la ronda cuando alguien termina.",
        "📚 Se utiliza en aulas para reforzar temas como letras, nombres propios, animales, alimentos y más.",
        "🌎 Es conocido en casi toda América Latina, aunque con diferentes nombres según el país.",
        "🧒 Se juega desde primaria hasta adultos, tanto en papel como en apps móviles.",
        "🖊️ Antes de las versiones digitales, se jugaba con hojas de cuaderno y lápiz, trazando columnas a mano.",
        "📱 Actualmente hay versiones en línea, videojuegos y hasta integraciones educativas.",
    ]

    for dato in curiosidades:
        st.markdown(f"- {dato}")

    ############################ COMENTARIOS ##########################################
    
    from datetime import datetime
    import os

    st.markdown("---")
    st.header("💬 Comparte tu opinión")

    COMMENTS_FILE = "comentarios_ppt.csv"

    @st.cache_data(show_spinner=False)
    def load_comments(path: str) -> pd.DataFrame:
        """Carga los comentarios existentes (o crea el archivo si no existe)."""
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            empty = pd.DataFrame(columns=["timestamp", "nombre", "comentario"])
            empty.to_csv(path, index=False)
            return empty

    def add_comment(path: str, nombre: str, comentario: str) -> None:
        """Añade un nuevo comentario al archivo."""
        df = load_comments(path)
        nuevo = pd.DataFrame({
            "timestamp": [datetime.now().isoformat(timespec="seconds")],
            "nombre": [nombre if nombre else "Anónimo"],
            "comentario": [comentario.strip()],
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(path, index=False)

    with st.form("comment_form", clear_on_submit=True, border=True):
        nombre = st.text_input("Tu nombre (opcional)")
        comentario = st.text_area("Escribe tu comentario aquí 👇")
        enviado = st.form_submit_button("Enviar")
################################################################################################


else:
    ############################# PASAPALABRA #########################################
    st.markdown("<h1 style='text-align: center;'>PASAPALABRA</h1>", unsafe_allow_html=True)
    ############################## ORIGEN #######################################
    st.markdown("<h2 style='text-align: center;'>Origen e historia del juego</h2>", unsafe_allow_html=True)

    texto_6_1 = """
    Creado por Rebecca Thornhill, Mark Maxwell-Smith y Andrew O'Connor, se produjo en Inglaterra, de la mano de Objetive Productions y la cadena BBC North, una división de la BBC. 
    Aunque era algo mancomunado, O'Connor (58) fue el que llevó la voz cantante del proyecto, ya que era el presidente y cofundador de Objetive Productions. 
    De hecho, hasta se puso al frente como presentador, ya que tenía experiencia previa delante de la cámara; había conducido otros programas de entretenimiento en Inglaterra y también había hecho sus pinitos como actor y cómico, aunque su obra más prolija estaba detrás de cámara, como productor.
    El 5 de agosto de 1996, ve la luz en la BBC The Alphabet Game, el programa que un día se convertiría en Pasapalabra. Su funcionamiento era bastante similar. 
    Dos concursantes se enfrentaban en varias pruebas relacionadas con el alfabeto y, para ayudarles, cada uno contaba con dos famosos.
    A pesar del desfile de rostros conocidos, lo curioso de las pruebas y la chispa que aportaba O'Connor, el programa no fue capaz de enganchar. 
    Se emite por última vez el 27 de marzo de 1997. Adiós al sueño de O'Connor.
    Sin embargo, el que la sigue la consigue y este decide comercializar el formato con la productora ITV estudios, una de las empresas audiovisuales más importantes a nivel mundial. 
    Los términos del contrato solo los saben ellos, pero parece que O'Connor y cía debieron vender todos los derechos, ya que en el litigio que mantuvo ITV con Mediaset recalcaron que el programa "está basado en The Alphabet Game" y que ellos son "los únicos dueños de los derechos".
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6_1}</div>", unsafe_allow_html=True)
    st.image("pasapalabra.webp", caption='', width=700)
    
    ############################ VALOR LATINO ##########################################
    st.markdown("<h2 style='text-align: center;'>Llegada y valor cultural en Latinoamérica</h2>", unsafe_allow_html=True)

    texto_6_2 = """
    Un rosco con todo el abecedario y un participante en contra del tiempo. 
    Pasapalabra es un juego familiar en el que un concursante trata de responder correctamente a la pregunta que se le hace, en base a que esta hace referencia a una palabra en específico. 
    El jugador, con ello en mente, debe de aplicar sus conocimientos y adivinar la palabra, teniendo en cuenta que la palabra incógnita comienza con la letra del abecedario que toca en el rosco. 
    Ojo que, se puede saltar la palabra, dando tiempo a que si se está jugando en grupo, el siguiente concursante comience su turno, pero si se equivoca, se habrá perdido el turno y la oportunidad de ganarla. 
    Gana quien tenga cero errores o, en todo caso, quién tenga menos errores. Este juego llegó en los 2000 con programas en TV argentina (2002), chilena y española. Durante la estabilización democrática y boom de TV de concurso, ofrecía cultura, lectoescritura y entretenimiento familiar. 
    En medio de crisis económicas, fue un símbolo de cultura accesible y aspiracional.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6_2}</div>", unsafe_allow_html=True)
    st.image("pasapalabra2.jpg", caption='', width=500)

    ############################ POPULARIDAD ##########################################
    st.markdown("<h2 style='text-align: center;'>Tabla de popularidad respecto al país</h2>", unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os
    
    data = {
        "País": [
            "España",
            "Argentina",
            "Chile",
            "México",
            "Perú",
            "Colombia",
            "Uruguay",
            "Ecuador",
            "Venezuela",
            "Bolivia"
        ],
        "Nombre local": [
            "Pasapalabra",
            "Pasapalabra (TV y juegos de mesa)",
            "Pasapalabra (versión TV y educativa)",
            "Pasapalabra (inspirado en TV)",
            "Juego del abecedario / Pasapalabra",
            "Pasapalabra escolar / Rosco",
            "Pasapalabra",
            "Juego del abecedario",
            "Juego tipo Pasapalabra",
            "Rosco de letras"
        ],
        "Grado de popularidad": [
            "Muy alta, versión original televisiva",
            "Muy alta, éxito televisivo y recreativo",
            "Alta, visto en TV y usado en educación",
            "Media-alta, adaptado por docentes",
            "Media, conocido por estudiantes y docentes",
            "Media, usado como recurso escolar",
            "Media, más conocido en formato digital",
            "Media-baja, aparece en actividades escolares",
            "Media, conocido en contextos educativos",
            "Baja, más reciente su introducción"
        ]
    }

    df_pop = pd.DataFrame(data)

    st.dataframe(df_pop, use_container_width=True)

    ############################ ANTES VS. DESPUES ##########################################
    st.markdown("<h2 style='text-align: center;'>Comparativa: antes vs. después de la digitalización</h2>", unsafe_allow_html=True)
    texto_6_1 = """
    Antes (tradicional):
    Antes de que lo digital invadiera nuestras vidas, Pasapalabra era un programa que vivía en el mundo analógico: cámaras tradicionales, cintas, y una buena dosis de logística física. 
    Sin embargo, con la llegada de la digitalización, el show se subió al tren tecnológico y no ha mirado atrás.  
    """
    texto_6_2 = """
    Después (era digital):
    Hoy en día, emplea un arsenal de herramientas digitales tanto para producir como para difundir y promocionar el contenido. 
    Esta transformación no solo agilizó sus procesos detrás de cámaras, sino que también potenció la experiencia del público, haciendo el entretenimiento más dinámico, accesible y eficiente.
    """
    texto_6_3 = """
    Impacto:
    Antes: juego espontáneo, social y omnipresente.
    Ahora: convive con su versión online, ha ganado visibilidad global en medios, redes y deporte competitivo.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6_1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6_2}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6_3}</div>", unsafe_allow_html=True)

    ############################ VIDEO ##########################################
    st.markdown("<h2 style='text-align: center;'>Video intuitivo</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=cuq8h-RQMIY")

    ############################ JUEGO ##########################################
    st.markdown("<h2 style='text-align: center;'>Prueba el juego</h2>", unsafe_allow_html=True)

    import streamlit as st
    import random

    # Preguntas elegidas
    PREGUNTAS = {
        'A': ('Empieza con A: Capital de Grecia.', 'atenas'),
        'B': ('Empieza con B: Lo opuesto a malo.', 'bueno'), 
        'C': ('Empieza con C: Animal que da leche.', 'cabra'), 
        'D': ('Empieza con D: Día después del sabado.', 'domingo'), 
        'E': ('Empieza con E: Mamifero terrestre mas grande.', 'elefante'), 
        'F': ('Empieza con F: Fruta roja y dulce.', 'fresa'),
        'G': ('Empieza con G: Menestra.', 'garbanzo'), 
        'H': ('Empieza con H: Lugar donde se duerme.', 'habitación'),
        'I': ('Empieza con I: Contrario de exterior.', 'interior'),
    }

    # Inicializar sesión
    if 'letras' not in st.session_state:
        st.session_state.letras = list(PREGUNTAS.keys())
        st.session_state.preguntas = PREGUNTAS.copy()
        st.session_state.respuestas = {}
        st.session_state.pasadas = []
        st.session_state.actual = st.session_state.letras[0]
        st.session_state.terminado = False
        st.session_state.puntos = 0

    def siguiente_letra():
        if st.session_state.pasadas:
            st.session_state.actual = st.session_state.pasadas.pop(0)
        elif st.session_state.letras:
            st.session_state.actual = st.session_state.letras.pop(0)
        else:
            st.session_state.terminado = True

    def procesar_respuesta(resp):
        correcta = st.session_state.preguntas[st.session_state.actual][1].lower()
        if resp.lower() == correcta:
            st.success(f"✅ ¡Correcto! Era: {correcta}")
            st.session_state.puntos += 1
        elif resp.lower() == 'pasapalabra':
            st.info("⏭️ Pasaste esta palabra. Volverás luego.")
            st.session_state.pasadas.append(st.session_state.actual)
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta era: {correcta}")
        siguiente_letra()

    # Juego activo
    if not st.session_state.terminado:
        letra = st.session_state.actual
        pregunta, _ = st.session_state.preguntas[letra]
        st.subheader(f"Letra {letra}")
        st.write(pregunta)

        with st.form("formulario"):
            respuesta = st.text_input("Tu respuesta (o escribe 'pasapalabra')", key=letra)
            enviado = st.form_submit_button("Enviar")

        if enviado and respuesta:
            procesar_respuesta(respuesta)

    # Final del juego
    if st.session_state.terminado:
        st.balloons()
        st.success(f"🎉 ¡Juego terminado! Puntaje total: {st.session_state.puntos} / {len(PREGUNTAS)}")
        if st.button("🔄 Jugar de nuevo"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]

    ############################ LINKS ##########################################
    st.markdown("<h2 style='text-align: center;'>Juego oficial</h2>", unsafe_allow_html=True)
    st.image("pasa.png", caption='', width=700)
    st.markdown(f"<div style='text-align: center;'><a href='https://www.cokitos.com/juegos/pasapalabra--ninos/' target='_blank'><button>JUEGA</button></a></div>", unsafe_allow_html=True) 
    
    ############################ DATOS Y CURIOSIDADES ##########################################
    st.markdown("<h2 style='text-align: center;'>Datos y curiosidades</h2>", unsafe_allow_html=True)

    import streamlit as st
    import pandas as pd
    from datetime import datetime
    import os

    curiosidades = [
        "📺 El juego se popularizó gracias al programa de televisión español *Pasapalabra*, estrenado en 2000.",
        "🔤 El rosco del abecedario es su elemento central: los jugadores deben acertar una palabra por cada letra del alfabeto.",
        "🌎 El formato fue adaptado en países como Argentina, Chile, Reino Unido, Italia y más.",
        "🧠 Es un juego que estimula la memoria, el vocabulario y la cultura general.",
        "🎓 Muchas escuelas lo usan como recurso educativo para reforzar áreas como lengua, historia o ciencia.",
        "📱 Existen apps y versiones web donde se puede jugar en solitario o en grupo.",
        "🔁 Si no sabes la palabra, puedes decir 'pasapalabra' y volver a ella después, lo que le da nombre al juego.",
        "🏆 En televisión, algunos participantes llegaron a ganar premios millonarios tras completar el rosco final.",
    ]

    for dato in curiosidades:
        st.markdown(f"- {dato}")

    ############################ COMENTARIOS ##########################################
    
    from datetime import datetime
    import os
    
    st.markdown("---")
    st.header("💬 Comparte tu opinión")

    COMMENTS_FILE = "comentarios_ppt.csv"

    @st.cache_data(show_spinner=False)
    def load_comments(path: str) -> pd.DataFrame:
        """Carga los comentarios existentes (o crea el archivo si no existe)."""
        if os.path.exists(path):
            return pd.read_csv(path)
        else:
            empty = pd.DataFrame(columns=["timestamp", "nombre", "comentario"])
            empty.to_csv(path, index=False)
            return empty

    def add_comment(path: str, nombre: str, comentario: str) -> None:
        """Añade un nuevo comentario al archivo."""
        df = load_comments(path)
        nuevo = pd.DataFrame({
            "timestamp": [datetime.now().isoformat(timespec="seconds")],
            "nombre": [nombre if nombre else "Anónimo"],
            "comentario": [comentario.strip()],
        })
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv(path, index=False)

    with st.form("comment_form", clear_on_submit=True, border=True):
        nombre = st.text_input("Tu nombre (opcional)")
        comentario = st.text_area("Escribe tu comentario aquí 👇")
        enviado = st.form_submit_button("Enviar")
################################################################################################
################################################################################################