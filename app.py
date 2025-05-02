import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# ----------------------------------------
# Configuración de la página
# ----------------------------------------
st.set_page_config(
    page_title="Informe Scouting: Ismael Ruesca Godino",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Sidebar con navegación estilizada
# ----------------------------------------
st.sidebar.markdown("## 🎯 **Menú de Secciones**")
sections = [
    "1. Datos Generales",
    "2. Resumen de Partidos",
    "3. Perfil & Liderazgo",
    "4. Análisis Técnico",
    "5. Análisis Táctico",
    "6. Análisis Físico",
    "7. Conclusiones",
    "8. Presentación"
]
choice = st.sidebar.radio(
    label="Selecciona 👉",
    options=sections,
    format_func=lambda x: {
        "1. Datos Generales": "🏷️  Datos Generales",
        "2. Resumen de Partidos": "📊  Resumen de Partidos",
        "3. Perfil & Liderazgo": "🧠  Perfil & Liderazgo",
        "4. Análisis Técnico": "⚙️  Análisis Técnico",
        "5. Análisis Táctico": "🗺️  Análisis Táctico",
        "6. Análisis Físico": "💪  Análisis Físico",
        "7. Conclusiones": "✅  Conclusiones",
        "8. Presentación": "📣  Presentación"
    }[x],
    key="menu_radio"
)
st.sidebar.markdown("---")

# ----------------------------------------
# Datos Base
# ----------------------------------------
player_info = {
    "Nombre": "Ismael Ruesca Godino",
    "Equipo": "Atlético Marbella Paraíso",
    "Categoría": "División de Honor Infantil",
    "Valoración": "⭐⭐⭐⭐ (4/5)",
    "Posición": "Defensa central / Mediocentro Defensivo (Pivote)"
}
# URL directa de la foto
photo_url = "ismael-2.jpg"

videos = [
    "https://youtu.be/4298-i9oUz0",
    "https://youtu.be/46sYpmyH0Gw",
    "https://youtu.be/D6uTUhOmMmo",
    "https://youtu.be/EFAMg3fL8SU",
    "https://youtube.com/shorts/rN6Isayo0BY"
]

matches = pd.DataFrame([
    {"Partido": "Granada CF vs Atl. Marbella Paraíso", "Resultado": "1 – 1", "Rol": "Pivote defensivo (3-5-2)", "Valoración": 4},
    {"Partido": "Atl. Marbella vs Real Betis",         "Resultado": "1 – 2", "Rol": "Defensa central → pivote",       "Valoración": 4},
    {"Partido": "La Cañada vs Atl. Marbella Paraíso", "Resultado": "0 – 1", "Rol": "Defensa central / pivote",     "Valoración": 3.5},
    {"Partido": "Mar. Atl. Paraíso vs CD Tiropichón", "Resultado": "2 – 2", "Rol": "Defensa central iniciador",   "Valoración": 4},
])

# Radar: categorías y valores 0–10
categories = ["Ritmo", "Físico", "Defensa", "Regate", "Pase", "Tiro"]
values     = [7, 7, 8, 8, 8, 5]

def plot_radar(categories, values, title):
    angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
    vals   = values + values[:1]
    angs   = angles + angles[:1]
    fig, ax = plt.subplots(subplot_kw={'polar': True})
    ax.plot(angs, vals, 'o-', linewidth=2)
    ax.fill(angs, vals, alpha=0.3)
    ax.set_thetagrids(np.degrees(angles), categories)
    ax.set_ylim(0, 10)
    ax.set_title(title, y=1.1, fontweight='bold')
    return fig

# ----------------------------------------
# Renderizado de secciones
# ----------------------------------------
if choice.startswith("1."):
    # ----------------------------------------
    # Sección 1: Datos Generales con tarjeta estilo FIFA
    # ----------------------------------------

    # Añadimos estilos CSS inline
    st.markdown(
        """
        <style>
        .fifa-card {
            display: flex;
            max-width: 900px;
            margin: 24px auto;
            border-radius: 16px;
            overflow: hidden;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        }
        .fifa-card__left {
            position: relative;
            width: 260px;
            background: linear-gradient(135deg, #1f4e78 0%, #133b5c 100%);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .fifa-card__left img {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            border: 4px solid #ffffff;
        }
        .fifa-card__left .overall {
            position: absolute;
            top: 16px;
            left: 16px;
            font-size: 48px;
            font-weight: bold;
            line-height: 1;
        }
        .fifa-card__left .position {
            position: absolute;
            bottom: 16px;
            left: 16px;
            font-size: 18px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .fifa-card__right {
            flex: 1;
            background: #f4f4f4;
            padding: 24px 32px;
            position: relative;
        }
        .fifa-card__right img.team-badge {
            position: absolute;
            top: 24px;
            right: 24px;
            width: 80px;
            height: 80px;
            object-fit: contain;
        }
        .fifa-card__right h2 {
            margin: 0 0 4px;
            font-size: 28px;
            color: #333;
        }
        .fifa-card__right .info {
            margin: 8px 0;
            font-size: 16px;
            color: #555;
        }
        .fifa-card__right .videos {
            margin-top: 16px;
        }
        .fifa-card__right .videos li {
            margin-bottom: 4px;
        }
        .fifa-card__right .videos a {
            color: #1f4e78;
            text-decoration: none;
        }
        .fifa-card__right .videos a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Datos y URLs
    logo_url = "https://cdn.resfu.com/img_data/escudos/medium/25597.jpg?size=120x&lossy=1"
    overall = 4  # Valoración global 4/5
    position = "DF / MCD"
    
    # Construcción de la card
    card_html = f"""
    <div class="fifa-card">
        <div class="fifa-card__left">
            <div class="overall">14</div>
            <img src="{photo_url}" alt="Foto de jugador"/>
            <div class="position">{position}</div>
        </div>
        <div class="fifa-card__right">
            <img class="team-badge" src="{logo_url}" alt="Escudo Atlético Marbella"/>
            <h2>{player_info['Nombre']}</h2>
            <div class="info"><strong>Equipo:</strong> {player_info['Equipo']}</div>
            <div class="info"><strong>Categoría:</strong> {player_info['Categoría']}</div>
            <div class="info"><strong>Valoración:</strong> {player_info['Valoración']}</div>
            <hr style="border:none; border-top:1px solid #ddd; margin:16px 0;">
            <h4 style="margin:0 0 8px; color:#1f4e78;">📹 Vídeos de Análisis</h4>
            <ul class="videos">
                {"".join(f'<li><a href="{u}" target="_blank">{u}</a></li>' for u in videos)}
            </ul>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)





elif choice.startswith("2."):
    st.title("2. 📊 Resumen de Partidos")
    st.dataframe(matches, use_container_width=True)

elif choice.startswith("3."):
    st.title("3. 🧠 Perfil & Liderazgo")
    st.markdown("""
- **Inteligencia Posicional:**  
  Ismael se desenvuelve como un veterano leyendo la jugada antes de que suceda.  
  Su ubicación en el bloque bajo es casi milimétrica, tapando líneas de pase y forzando al rival a desequilibrarse.  
  En fase de construcción, se mete entre centrales o en la zona de tres cuartos para triangular y ofrecer salida limpia.  
  Es un “peón táctico” que no se descoloca ni un segundo del despliegue colectivo.

- **Iniciación de Juego:**  
  Cuando el equipo atrapa el balón, él “coge la batuta”: el timing de sus recepciones es sobresaliente,  
  siempre orientado para romper las líneas rivales. Su pase al primer toque lleva dirección, peso y tempo,  
  alternando envíos al pie con salidas en conducción con gran facilidad e incluso regate en salidas.

- **Comunicación y Mando:**  
  Aunque posee temple y carácter de líder silencioso, todavía debe soltar la voz más allá de los gestos.  
  En momentos de apuro, un grito suyo para coordinar la salida o pedir coberturas marcaría la diferencia.  
  Tiene capacidad de líder para ser el “general” que ordene la zaga y avise de las coberturas, pero necesita dar un  
  paso adelante en "arrojo verbal".

- **Versatilidad Táctica:**  
  Se adapta al rol de “líbero avanzado” cuando el bloque está en 5-4-1, subiendo a iniciar desde atrás;  
  y retrocede a pivote en el 3-5-2 para darle pausa al juego. Cambia de posición con naturalidad, da  
  equilibrio en las transiciones y apunta a convertirse en un “todocampista” que cubre zonas críticas  
  sin perder ni un ápice de eficacia. Su polivalencia le permite ser comodín: último hombre o ancla  
  posicional.
    """)

elif choice.startswith("4."):
    st.title("4. ⚙️ Análisis Técnico")
    st.markdown("""
#### Manejo de Balón & Salida Limpia
- Posee una exquisita cadencia al tocar el balón, moviéndolo con temple y solvencia.  
  Control orientado al primer toque, deja la pelota siempre perfilada para progresar o cambiar el juego.  
- Sabe proteger el cuero bajo presión, usando el cuerpo como escudo y saliendo en carrera con soltura.  
- Es un defensa central/ Medicentro pivote con mucha calidad en salida de balón. Sabe sortear de forma que parece fácil a los rivales. Tiene capacidad para sortear la presión con pausa y decidir con criterio.

#### Pases & Distribución
- Genera ruptura de líneas con pases entre defensas: filtra balones interiores al mediocentro y encuentra receptores en la zona de tres cuartos.  
- No obstante, le falta potencia en el envío largo: los pases en profundidad carecen de pegada para superar líneas defensivas muy cerradas.  
- En situaciones de transición posee gran temple: busca siempre la opción más segura antes de arriesgar.

#### Anticipación & Duelos
- Se anticipa con inteligencia a los movimientos del rival, cortando líneas de pase antes del balón llegar al pie contrario.   
- En el uno contra uno, su colocación y timing son excelentes, pero debe mejorar la contundencia física para imponerse siempre. No es un jugador de ir al suelo.
- En el juego aéreo es fiable defensivamente: gana saltos en segunda línea, aunque en el área rival apenas disputa remates ni se muestra como amenaza en acciones a balón parado.

#### Control de Ritmo & Salida desde atrás
- Cuando recibe bajo presión, frena el ritmo de la jugada con un toque suave y luego acelera el balón, marcando el tempo para el equipo.  
- Su golpeo al primer toque es limpio, con ángulo de pase y velocidad adecuada para romper una línea rival o iniciar contraataque.  
- Debe trabajar la proyección de golpeo en largo (40+ metros) para conectar con los carrileros y abrir el campo en bloque alto.
    """)
    st.markdown("**Radar: Perfil de Fortalezas y Debilidades**")
    radar_fig = plot_radar(categories, values, "Radar Técnico")
    st.pyplot(radar_fig)

elif choice.startswith("5."):
    st.title("5. 🗺️ Análisis Táctico")
    st.markdown("""
**Sistema predominante:**  
Se basa en un 5-4-1 con laterales carrileros que liberan espacios en las bandas y pivote de contención. También ha alternado con un 5-4-1 para reforzar el bloque bajo y un 5-3-3 cuando busca mayor amplitud ofensiva.

**Funciones estrella:**  
- **Pivote en 5 4 1:** Actúa como equilibrio del equipo. Tácticamente impecable, distribuye en corto para sostener la posesión y dirige la salida limpia desde zona de creación.  
- **Último hombre en 5-4-1 / 4-3-3:** Su rol de defensa central más libre permite que los carrileros asciendan sin desprotección. Hace de referencia con los centrales y filtra balones de seguridad para iniciar transiciones.

**Lectura de juego & Coberturas:**  
- Se desplaza con timing para tapar pasillos interiores y cerrar líneas de pase de mediapuntas rivales.  
- En repliegues ofensivos por parte del equipo rival cuando Ismael juega de ultimo hombre observamos que le cuesta mas replegar por una falta de velocidad.

**Ruptura de presión:**  
- Cuando el rival presiona en bloque medio, baja entre los centrales para triangular y romper la primera línea.  
- Posee suficiente temple para girarse con balón y cambiar el flanco con pases de 10-15 metros.

**Áreas de mejora:**  
- **Presión al balón:** Falta contundencia en campo contrario y robar por alto, nos ha faltado ver más ahí.  
- **Comunicación táctica:** Debe elevar la voz para coordinar los cambios de marca y cubrir los huecos cuando se descoloca el bloque.  
- **Transiciones defensivas:** Hay ocasiones en que tarda en reasumir su posición tras pérdida; trabajar velocidad de reacción para impedir contragolpes.

**Mapa de Posiciones:**  
""")
    pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
    fig, ax = pitch.draw(figsize=(8, 6))
    # Posición como central
    ax.scatter(30, 50, color='white', edgecolors='black', s=200, label='Defensa Central')
    # Posición como pivote
    ax.scatter(50, 50, color='white', edgecolors='blue', s=200, label='Pivote')
    ax.legend(loc='upper right')
    st.pyplot(fig)


elif choice.startswith("6."):
    st.title("6. 💪 Análisis Físico")
    st.markdown("""
- **Resistencia Aeróbica**  
  Exhibe un fondo físico sobresaliente durante la primera hora de juego, manteniendo el ritmo de presión y cobertura en bloque bajo. No obstante, a partir del minuto 35 del segundo tiempo se aprecia un ligero descenso en el nivel de intensidad, traduciéndose en una menor agresividad en las ayudas defensivas y en la velocidad de desplazamiento.

- **Velocidad y Reactividad**  
  Demuestra explosividad en aceleraciones cortas para cerrar espacios y salir al corte. Sin embargo, adolece de velocidad mantenida en situaciones de balón a las espaldas.

- **Fuerza y Duelo Corporal**  
  Presenta una complexión adecuada para imponerse en acciones de 1 vs 1, con un centro de gravedad que le permite absorber cargas y proteger el balón. Aun así, debería ganar algo de masa muscular en tren superior para imponerse con mayor contundencia en los duelos cuerpo a cuerpo y en los apoyos para giro bajo presión.

- **Agilidad y Equilibrio**  
  Muestra soltura para girarse y reorientarse tras presión rival, manteniendo la estabilidad en recepciones de balón en zonas comprometidas. Un trabajo específico en pliometría y estabilidad de core mejoraría su capacidad para recuperar posición en caso de pérdida.

- **Capacidad de Recuperación**  
  Tras esfuerzos intensos recupera el ritmo de juego con rapidez, pero la acumulación de metros a alta intensidad le pasa factura en la recta final. Tiene mucha mejora en todos esos aspectos físicos.
    """)


elif choice.startswith("7."):
    st.title("7. ✅ Conclusiones & Recomendaciones")
    st.markdown("""
**🔍 Conclusiones**  
Ismael Ruesca Godino se perfila como un futbolista con un instinto defensivo muy afinado y una capacidad de lectura táctica que le permite anticiparse a las acciones del rival. Su manejo de balón en espacios reducidos y la precisión en la circulación convierten al ‘central-pivote’ en un recurso valioso para romper la presión alta adversaria y lanzar transiciones rápidas.

- **Visión de Juego y Anticipación:**  
  Su colocación en zona media y defensiva es precisa; detecta líneas de pase antes de que se abran y lee la carrera de los delanteros con solvencia, cortando el juego rival en la génesis de la jugada.  

- **Calidad Técnica en Posesión:**  
  Buen dominio de ambos perfiles para recibir y girar bajo presión, combinando con apoyos en corto y salida en rombo. La ejecución de pases frontales y diagonales demuestra criterio y temple, clave para iniciar ataques desde campo propio.  

- **Polivalencia Táctica:**  
  Se adapta sin fisuras a jugar tanto de defensa central como de pivote defensivo, tanto en fase defensiva como en la de construcción. Puede asumir la primera línea de pase como pivote o retrasarse como central con autoridad, liberando carrileros y gestionando espacios.

---

**🛠️ Áreas de Mejora**  

1. **Pases Largos y Cambio de Ritmo + Velocidad continuada:**  
   Mejorar la potencia y precisión en lanzamientos en largo (más allá de 30 metros) para buscar extremos o romper líneas defensivas en campo contrario. Y mejora en velocidad continuadad para hacer frente a cuando juegue en posicion de Defensa central, poder suplir esos problemas detectados.  
2. **Comunicación y Liderazgo:**  
   Fomentar la asunción de mando en defensa, elevando el volumen de voz para organizar la línea de cuatro y coordinar coberturas.  


---


    """)


elif choice.startswith("8."):
    st.title("8. 📣 Presentación a Agencia")
    st.markdown("""
**🏅 Valoración de Incorporación**  
Después de analizar a fondo el perfil de Ismael Ruesca Godino, podemos afirmar que es **un jugador sumamente atractivo** para incorporar a la agencia, por las siguientes razones:

1. **Adaptabilidad Táctica**  
   - Domina tanto el rol de **central** como el de **pivote iniciador**.  
   - Se ajusta perfectamente a sistemas de **5-4-1**, **4-5-1** o **4-3-3**, permitiendo al cuerpo técnico variar el dibujo sin perder fluidez en la construcción.

2. **Lectura de Juego y Anticipación**  
   - Su capacidad para **cortar líneas de pase** y anticipar el movimiento de los delanteros rivales le da un plus en defensas zonales y en transición.  
   - Es capaz de **cerrar carriles de penetración** y neutralizar combinaciones rivales en zona media.

3. **Salida de Balón**  
   - Presenta temple y criterio en la **primera línea de pase**, ofreciendo soluciones limpias en presión alta.  
   - La combinación en corto y el pase vertical lo convierten en un nexo fiable entre defensa y mediocampo.

4. **Potencial de Desarrollo**  
   - Con 13 años en **División de Honor Infantil**, su potencial de crecimiento es elevado.  
   - Mejora aún el **pase en largo**, la **comunicación en campo** y la **resistencia de alta intensidad**, áreas que pueden trabajarse rápido con un buen cuerpo técnico.

5. **Característica de Liderazgo**  
   - Aunque callado en el campo, su presencia física y táctica inspira confianza.  



---

**🎯 Conclusión**  
Ismael Ruesca Godino supone una **oportunidad de inversión** de alto potencial. Reúne **características técnicas, tácticas y físicas** de un futbolista llamado a vivir un salto de calidad en próximas categorías de futbol base venideras y tiene todo para poder llegar al fútbol de élite bajo mi scotuing.  


> """)

