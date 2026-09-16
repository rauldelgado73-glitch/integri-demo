# VERSION INTEGRID-LN: CABECERA_SIN_MENU_DUPLICADO - 16/09/2026
import base64
import html
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="INTEGRID-LN | Asistente de Integridad Institucional",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def imagen_en_base64(nombre: str) -> str:
    """Convierte una imagen local en una fuente que el navegador puede mostrar."""
    ruta = Path(__file__).parent / "assets" / nombre
    if not ruta.exists():
        return ""
    return base64.b64encode(ruta.read_bytes()).decode("utf-8")


robot = imagen_en_base64("integri_robot.png")
robot_html = (
    f'<img class="robot" src="data:image/png;base64,{robot}" alt="Mascota INTEGRID-LN">'
    if robot
    else '<div class="robot-fallback">🤖</div>'
)

# Icono propio para RVL construido con HTML y CSS. Streamlit puede filtrar los
# elementos SVG incrustados; esta versión no depende de SVG, emojis ni archivos.
icono_rvl_html = """
<span class="rvl-badge" role="img" aria-label="Credencial de visitante">
    <span class="rvl-person"></span><span class="rvl-lines"></span>
</span>
"""


def respuesta_guiada(texto: str) -> str:
    """Respuestas demostrativas sin API, organizadas por intención temática."""
    consulta = texto.lower().strip()

    if any(p in consulta for p in ("dni", "teléfono", "telefono", "dirección", "direccion", "nombre completo", "prueba", "evidencia adjunta")):
        return (
            "Por seguridad, no compartas datos personales, nombres de involucrados ni evidencias en este chat. "
            "Puedo brindarte orientación general o indicarte el canal institucional correspondiente."
        )
    if consulta in ("hola", "buenos días", "buenos dias", "buenas tardes", "ayuda", "qué puedes hacer", "que puedes hacer"):
        return (
            "¡Hola! Soy INTEGRID-LN. Puedo explicarte los nueve componentes del Modelo de Integridad, ética pública, "
            "declaraciones juradas, denuncias, transparencia y PTE, neutralidad electoral, visitas y agendas, guías y derivación a la UFII."
        )
    if any(p in consulta for p in ("portal de transparencia", "transparencia estándar", "transparencia estandar", "pte", "acceso a la información", "acceso a la informacion", "datos abiertos", "rendición de cuentas", "rendicion de cuentas")):
        return (
            "El Portal de Transparencia Estándar de DIRIS Lima Norte reúne información institucional pública. "
            "La tarea 4.1 de la Directiva N.° 001-2026-PCM/SIP contempla verificar su actualización. "
            "Abre «Transparencia y PTE» para acceder al portal oficial y conocer la ruta de verificación; "
            "la UFII coordina el seguimiento, mientras la publicación corresponde al funcionario responsable del PTE."
        )
    if any(p in consulta for p in ("neutralidad", "integridad electoral", "proselitismo", "propaganda electoral", "publicidad estatal", "campaña electoral", "campana electoral")):
        return (
            "Durante el proceso electoral, los servidores deben respetar las reglas de neutralidad y publicidad estatal. "
            "Abre «Neutralidad electoral 2026» para ver ejemplos preventivos y las normas oficiales del JNE y la PCM. "
            "No escribas nombres, partidos, hechos de un caso ni evidencias en este chat. La entidad debe confirmar "
            "quién ocupa actualmente el cargo de Oficial de Integridad Institucional y el canal de consulta aplicable."
        )
    if any(p in consulta for p in ("alta dirección", "alta direccion", "gestión de riesgos", "gestion de riesgos", "control interno", "auditoría", "auditoria", "capacitación", "capacitacion", "supervisión", "supervision", "programa de integridad", "icp")):
        return (
            "Es un tema de uno de los nueve componentes del Modelo de Integridad. En «Modelo de Integridad» "
            "puedes abrir cada componente para ver acciones, responsables y ejemplos de medios de verificación. "
            "Los reportes y evidencias institucionales deben ser validados por las unidades competentes."
        )
    if any(p in consulta for p in ("denuncia", "denunciar", "corrupción", "corrupcion", "represalia", "protección", "proteccion")):
        return (
            "No coloques en este chat nombres, hechos sensibles ni evidencias. La Plataforma Digital Única de Denuncias permite "
            "presentar una denuncia de forma anónima o identificada y entrega un código de seguimiento. Abre el botón «Canal de Denuncias» "
            "para revisar la ruta y el acceso oficial."
        )
    if any(p in consulta for p in (
        "conflicto de interés", "conflicto de interes", "ética", "etica", "regalo", "favorecimiento", "conducta",
        "principio", "deber", "prohibición", "prohibicion", "proselitismo", "bien del estado",
        "bienes del estado", "información privilegiada", "informacion privilegiada",
    )):
        return (
            "Si tienes una duda ética, describe únicamente el tipo de situación, sin mencionar personas ni datos sensibles. "
            "La Ley N.° 27815 establece principios, deberes y prohibiciones para la función pública. Puedes revisar la guía práctica "
            "desde el botón «Consultas de Ética». INTEGRID-LN brinda orientación preventiva, pero no califica infracciones ni determina sanciones."
        )
    if any(p in consulta for p in ("declaración jurada", "declaracion jurada", "declaraciones juradas", "dji")):
        return (
            "Existen diferentes declaraciones, como la Declaración Jurada de Intereses y la de Ingresos, Bienes y Rentas. "
            "La obligación, oportunidad y sistema dependen del cargo y del tipo de declaración. Revisa el botón «Declaraciones Juradas» "
            "y confirma tu condición de obligado con el área responsable, sin proporcionar aquí datos personales."
        )
    if any(p in consulta for p in ("rvl", "registro de visitas", "visita", "agenda oficial")):
        return (
            "El Registro de Visitas en Línea publica información sobre las visitas que reciben funcionarios y servidores públicos y el motivo "
            "de estas. El botón «Registro de Visitas RVL» contiene una ruta rápida y la Directiva N.° 003-2026-PCM/SIP vigente."
        )
    if any(p in consulta for p in ("modelo de integridad", "componentes", "integridad institucional", "cultura de integridad")):
        return (
            "El Modelo de Integridad fortalece la capacidad preventiva y defensiva de las entidades públicas frente a la corrupción "
            "y las prácticas contrarias a la ética. Está organizado en 9 componentes. Puedes conocerlos desde el botón "
            "«Modelo de Integridad vigente», ubicado debajo de mi imagen."
        )
    if any(p in consulta for p in ("checklist", "guía", "guia", "formato", "material")):
        return (
            "El módulo «Checklists y Guías» reúne verificaciones rápidas para consultas éticas, declaraciones juradas, denuncias, visitas "
            "y derivaciones. Son ayudas preventivas y no sustituyen los formatos ni instrucciones oficiales."
        )
    if any(p in consulta for p in ("contacto", "correo", "anexo", "derivar", "ufii")):
        return (
            "Puedes revisar el botón «Derivar a UFII» para saber cuándo corresponde solicitar orientación. En el prototipo figuran "
            "integridad@dirisln.gob.pe y el Anexo 2005; ambos datos deben ser confirmados por la UFII antes de la presentación oficial."
        )
    return (
        "Aún no tengo una respuesta guiada para esa consulta. Puedes reformularla usando uno de estos temas: "
        "ética, Modelo de Integridad, neutralidad electoral, transparencia/PTE, declaraciones juradas, denuncias, RVL, guías o derivación a la UFII."
    )


if "historial_chat" not in st.session_state:
    st.session_state.historial_chat = []
if "ultima_consulta" not in st.session_state:
    st.session_state.ultima_consulta = ""

mensajes = []
for autor, mensaje in st.session_state.historial_chat:
    clase = "user" if autor == "usuario" else "bot"
    etiqueta = "Tú" if autor == "usuario" else "INTEGRID-LN"
    texto_seguro = html.escape(mensaje).replace("\n", "<br>")
    mensajes.append(
        f'<div class="chat-message {clase}"><div class="chat-label">{etiqueta}</div>'
        f'<div class="chat-bubble">{texto_seguro}</div></div>'
    )

historial_html = "".join(mensajes)
historial_invertido_html = "".join(reversed(mensajes))


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;600;700&family=Roboto:wght@400;500;700;900&display=swap');

:root {
    --azul-900: #08265e;
    --azul-800: #063b82;
    --azul-700: #0753a8;
    --azul-500: #168fe4;
    --azul-100: #eaf3ff;
    --borde: #c7daf5;
    --texto: #0a2459;
    --verde: #198d50;
    --rojo: #d84a32;
}

* { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: "Roboto Condensed", "Arial Narrow", Arial, sans-serif;
}

.stApp {
    color: var(--texto);
    background:
        radial-gradient(circle at 50% -10%, rgba(255,255,255,.98) 0 18%, rgba(235,242,255,.96) 48%, rgba(225,235,252,.98) 100%);
}

.block-container {
    width: min(1100px, 100%);
    max-width: 1100px;
    padding: 2.1rem 1.5rem 2rem !important;
}

#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

.integri-shell { width: 100%; margin: 0 auto; }

.brand {
    text-align: center;
    padding: 0 1rem 1.2rem;
}

.brand h1 {
    margin: 0;
    color: #063a86;
    font-family: Roboto, Arial, sans-serif;
    font-size: clamp(2rem, 5.5vw, 5.3rem);
    font-weight: 900;
    line-height: .94;
    letter-spacing: .02em;
    text-shadow: 0 2px 0 #fff, 0 5px 12px rgba(2,46,119,.18);
}

.brand-line {
    height: 1px;
    margin: 1.05rem auto .85rem;
    background: linear-gradient(90deg, transparent, #b7cef0 14%, #b7cef0 86%, transparent);
}

.brand h2 {
    margin: 0;
    font-family: Roboto, Arial, sans-serif;
    font-size: clamp(1.45rem, 3vw, 2.25rem);
    color: var(--azul-900);
    font-weight: 800;
}

.brand p {
    margin: .34rem 0 0;
    font-family: Roboto, Arial, sans-serif;
    font-size: clamp(1rem, 2vw, 1.48rem);
    color: var(--azul-900);
    font-weight: 600;
}

.topic-bar {
    margin: .25rem 0 1.55rem;
    padding: .88rem 1rem;
    color: white;
    text-align: center;
    font-size: clamp(1.12rem, 2.3vw, 1.55rem);
    font-weight: 700;
    background: linear-gradient(135deg, #073b85, #0664b7 58%, #063c87);
    border: 1px solid #042f72;
    border-radius: 9px;
    box-shadow: 0 7px 14px rgba(1,52,125,.18), inset 0 1px rgba(255,255,255,.25);
}


.panel {
    background: rgba(255,255,255,.6);
    border: 1px solid var(--borde);
    border-radius: 16px;
    box-shadow: 0 6px 14px rgba(21,65,135,.12), inset 0 1px rgba(255,255,255,.95);
}

.hero {
    position: relative;
    min-height: 305px;
    overflow: hidden;
    display: grid;
    grid-template-columns: 31% 69%;
    align-items: stretch;
    background: linear-gradient(115deg, rgba(248,251,255,.94), rgba(239,245,255,.92));
}

.mascot-wrap { position: relative; min-height: 305px; }
.robot {
    position: absolute;
    z-index: 2;
    left: 1.2rem;
    bottom: -2px;
    width: min(290px, 100%);
    height: auto;
    mix-blend-mode: multiply;
}
.robot-fallback { font-size: 9rem; display:flex; align-items:center; justify-content:center; height:100%; }

.hero-copy {
    position: relative;
    z-index: 3;
    padding: 2.05rem 1.45rem 1.65rem .25rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 1.2rem;
}

.speech {
    position: relative;
    background: rgba(255,255,255,.95);
    border: 2px solid #b7ceed;
    border-radius: 14px;
    padding: 1.15rem 1.45rem;
    color: #091f50;
    font-family: Roboto, Arial, sans-serif;
    font-size: clamp(1.35rem, 3vw, 2.15rem);
    font-weight: 800;
    box-shadow: 0 6px 12px rgba(17,59,123,.12);
}
.speech:before {
    content: "";
    position: absolute;
    left: -27px;
    bottom: 25%;
    width: 48px;
    height: 48px;
    background: white;
    border-left: 2px solid #b7ceed;
    border-bottom: 2px solid #b7ceed;
    transform: rotate(45deg);
    z-index: -1;
}

.quick-chat {
    display:grid;
    grid-template-columns:1fr auto;
    gap:.65rem;
    width:100%;
}
.quick-chat input {
    min-width:0;
    padding:.82rem 1rem;
    color:#0a2459;
    background:white;
    border:2px solid #b7ceed;
    border-radius:10px;
    font:500 1rem Roboto,Arial,sans-serif;
    outline:none;
}
.quick-chat input:focus { border-color:#0b66ba; box-shadow:0 0 0 3px rgba(11,102,186,.12); }
.quick-chat button {
    padding:.78rem 1.1rem;
    color:white;
    background:#0755a8;
    border:0;
    border-radius:10px;
    font:700 1rem Roboto,Arial,sans-serif;
    cursor:pointer;
    box-shadow:0 4px 9px rgba(7,65,139,.2);
}
.quick-chat button:hover { background:#063d83; }
.chat-hint { margin-top:-.65rem; font:500 .76rem/1.2 Roboto,Arial,sans-serif; color:#506889; }

.hero-link {
    display: block;
    width: min(520px, 90%);
    margin-left: auto;
    color: inherit;
    text-decoration: none;
}

.hero-feature-card {
    position: relative;
    margin-left: 0;
    width: 100%;
    min-height: 116px;
    display: grid;
    grid-template-columns: 74px 1fr 30px;
    align-items: center;
    gap: .8rem;
    padding: 1.05rem 1.25rem;
    color: #fff;
    background: linear-gradient(145deg, #1680cf, #0755a8 62%, #073c83);
    border: 9px solid #edf4ff;
    outline: 2px solid #bdd3f1;
    border-radius: 13px;
    box-shadow: 0 7px 10px rgba(7,48,111,.19), inset 0 1px rgba(255,255,255,.35);
}
.badge {
    position: absolute;
    right: 15%;
    top: -27px;
    padding: .48rem 1.2rem;
    color: #173263;
    background: linear-gradient(#fff1a7, #ffd96d);
    border: 1px solid #efc246;
    border-radius: 10px;
    font-family: Roboto, Arial, sans-serif;
    font-size: .92rem;
    font-weight: 900;
    white-space: nowrap;
}
.shield { font-size: 3.7rem; filter: drop-shadow(0 3px 2px rgba(0,0,0,.22)); }
.hero-feature-card strong { display:block; font: 800 clamp(1.35rem,3vw,2.15rem)/1 Roboto,Arial,sans-serif; text-shadow:0 2px 2px rgba(0,0,0,.28); }
.hero-feature-card small { display:block; margin-top:.3rem; font: 500 clamp(.9rem,2vw,1.35rem)/1 Roboto,Arial,sans-serif; }
.arrow { font-size: 3.1rem; font-family: Arial,sans-serif; }

.notice {
    margin: 1.25rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    padding: .9rem 1rem;
    font: 800 clamp(1.05rem,2.3vw,1.45rem)/1.2 Roboto,Arial,sans-serif;
    text-align: center;
}
.notice-i {
    flex: 0 0 auto;
    display:grid;
    place-items:center;
    width:38px;
    height:38px;
    color:white;
    background:#0c58a7;
    border-radius:50%;
    font:900 1.5rem Georgia,serif;
}

.chat-panel { margin:1.25rem 0; padding:1rem 1.15rem 1.1rem; }
.chat-heading { display:flex; justify-content:space-between; gap:1rem; align-items:center; padding:.2rem .2rem .8rem; border-bottom:1px solid #ceddf1; }
.chat-heading strong { font:800 1.15rem Roboto,Arial,sans-serif; }
.chat-heading span { color:#4c6588; font:600 .78rem Roboto,Arial,sans-serif; }
.chat-history { display:flex; flex-direction:column; gap:.8rem; padding:1rem 0 .35rem; }
.chat-message { max-width:82%; }
.chat-message.user { align-self:flex-end; }
.chat-message.bot { align-self:flex-start; }
.chat-label { margin:0 .35rem .2rem; color:#546c8d; font:700 .75rem Roboto,Arial,sans-serif; }
.chat-message.user .chat-label { text-align:right; }
.chat-bubble { padding:.8rem 1rem; border-radius:14px; font:500 .95rem/1.45 Roboto,Arial,sans-serif; }
.chat-message.user .chat-bubble { color:white; background:#0755a8; border-bottom-right-radius:4px; }
.chat-message.bot .chat-bubble { color:#0a2459; background:#eef5ff; border:1px solid #c5d9f3; border-bottom-left-radius:4px; }
.chat-actions { text-align:right; }
.chat-actions a { color:#0755a8; font:700 .8rem Roboto,Arial,sans-serif; text-decoration:none; }

.embedded-chat-box {
    height:390px;
    padding:1rem;
    display:flex;
    flex-direction:column;
    overflow:hidden;
    color:#102a56;
    background:linear-gradient(160deg,#edf5ff,#e3eefc);
    border:1px solid #bdd3ee;
    border-radius:16px;
    box-shadow:0 6px 14px rgba(18,64,126,.11);
}
.embedded-chat-heading {
    display:flex;
    align-items:center;
    gap:.75rem;
    margin:-1rem -1rem 1rem;
    padding:.85rem 1rem;
    color:white;
    background:linear-gradient(135deg,#0755a8,#086ac7);
    border-radius:15px 15px 0 0;
}
.embedded-chat-heading .mini-avatar { display:grid; place-items:center; width:40px; height:40px; background:white; border-radius:50%; font-size:1.55rem; }
.embedded-chat-heading strong { display:block; font:800 1rem Roboto,Arial,sans-serif; }
.embedded-chat-heading small { display:block; margin-top:.15rem; font:500 .72rem Roboto,Arial,sans-serif; opacity:.9; }
.embedded-chat-box .chat-history {
    flex:1;
    min-height:0;
    overflow-y:auto;
    overflow-x:hidden;
    flex-direction:column-reverse;
    justify-content:flex-start;
    padding-right:.55rem;
    scrollbar-width:thin;
    scrollbar-color:#74a7dc #dceafb;
}
.embedded-chat-box .chat-history::-webkit-scrollbar { width:9px; }
.embedded-chat-box .chat-history::-webkit-scrollbar-track { background:#dceafb; border-radius:10px; }
.embedded-chat-box .chat-history::-webkit-scrollbar-thumb { background:#74a7dc; border-radius:10px; border:2px solid #dceafb; }
.embedded-chat-box .chat-history::-webkit-scrollbar-thumb:hover { background:#477fb8; }
.embedded-chat-box .chat-message { width:fit-content; max-width:82%; }
.embedded-chat-box .chat-message.user { margin-left:auto; }
.embedded-chat-box .chat-message.bot { margin-right:auto; }
.embedded-chat-box .chat-message.user .chat-bubble { color:#fff !important; background:linear-gradient(135deg,#0866ff,#0752b7); }
.embedded-chat-box .chat-message.bot .chat-bubble { color:#102a56 !important; background:#fff; }
[data-testid="stForm"] {
    margin-top:.65rem;
    padding:.65rem !important;
    background:#ffffff !important;
    border:1px solid #bdd3ee !important;
    border-radius:14px !important;
    box-shadow:0 5px 12px rgba(18,64,126,.09) !important;
}
[data-testid="stTextInput"] input {
    color:#102a56 !important;
    -webkit-text-fill-color:#102a56 !important;
    background:#f8fbff !important;
    border:2px solid #9bbfe8 !important;
}
[data-testid="stTextInput"] input::placeholder {
    color:#5c718f !important;
    -webkit-text-fill-color:#5c718f !important;
    opacity:1 !important;
}
[data-testid="stFormSubmitButton"] button {
    height:42px !important;
    color:#ffffff !important;
    background:#0866ff !important;
    border:1px solid #0752b7 !important;
    border-radius:10px !important;
    font-weight:700 !important;
}

.section { padding: 1.1rem 1.35rem 1.3rem; margin-bottom: 1.25rem; }
.section-title {
    display:flex;
    align-items:center;
    gap:1.2rem;
    margin:0 0 1.05rem;
    font:800 clamp(1.35rem,2.5vw,1.75rem)/1 Roboto,Arial,sans-serif;
    text-align:center;
}
.section-title:before, .section-title:after { content:""; flex:1; height:2px; background:#afc9ed; }

.menu-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; }
.menu-link { display:block; color:inherit; text-decoration:none; }
.menu-card {
    min-height: 178px;
    padding: 1rem .65rem .9rem;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:.7rem;
    color:var(--texto);
    background:linear-gradient(145deg,rgba(255,255,255,.98),rgba(242,247,255,.82));
    border:1px solid #c3d7f2;
    border-radius:11px;
    box-shadow:0 5px 10px rgba(18,56,116,.13), inset 0 1px white;
    text-align:center;
    transition:.18s ease;
    cursor:pointer;
}
.menu-card:hover { transform:translateY(-3px); border-color:#7eaddf; box-shadow:0 9px 17px rgba(18,56,116,.17); }
.election-link {
    display:flex; align-items:center; gap:1rem; margin-top:1rem;
    padding:1rem 1.2rem; color:#08346a !important; text-decoration:none !important;
    background:#f1f7ff; border:2px solid #79a9db; border-radius:11px;
    box-shadow:0 5px 10px rgba(18,56,116,.11);
}
.election-link:hover, .election-link:focus-visible { border-color:#0753a8; background:#e5f1ff; }
.election-link .election-icon { font-size:2.1rem; line-height:1; }
.election-link strong { display:block; font:700 1.25rem Roboto,Arial,sans-serif; }
.election-link small { display:block; font:400 .95rem Roboto,Arial,sans-serif; margin-top:.22rem; }
.election-link .election-arrow { margin-left:auto; font-size:1.8rem; font-weight:800; }
.menu-icon { font-size:3.7rem; line-height:1; filter:drop-shadow(0 2px 1px rgba(10,55,115,.16)); }
.menu-icon.rvl-menu-icon { display:block; padding-top:.45rem; }
.rvl-badge {
    position:relative;
    display:inline-block;
    width:66px;
    height:52px;
    background:#eaf4ff;
    border:4px solid #0755a8;
    border-radius:8px;
    box-shadow:0 3px 0 rgba(6,59,130,.16);
}
.rvl-badge:before {
    content:"";
    position:absolute;
    left:20px;
    top:-11px;
    width:20px;
    height:10px;
    background:#063b82;
    border-radius:4px 4px 2px 2px;
}
.rvl-person {
    position:absolute;
    left:7px;
    top:9px;
    width:25px;
    height:33px;
}
.rvl-person:before {
    content:"";
    position:absolute;
    left:7px;
    top:0;
    width:12px;
    height:12px;
    background:#0755a8;
    border-radius:50%;
}
.rvl-person:after {
    content:"";
    position:absolute;
    left:1px;
    bottom:0;
    width:24px;
    height:17px;
    background:#168fe4;
    border-radius:14px 14px 3px 3px;
}
.rvl-lines {
    position:absolute;
    right:7px;
    top:11px;
    width:20px;
    height:27px;
    background:repeating-linear-gradient(to bottom,#0755a8 0 3px,transparent 3px 9px);
}
.menu-card strong { font:700 clamp(1rem,2.2vw,1.35rem)/1.12 "Roboto Condensed",Arial,sans-serif; }

.metrics-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.9rem; }
.demo-caption { margin:-.5rem 0 .9rem; color:#5b7090; text-align:center; font:600 .78rem/1.3 Roboto,Arial,sans-serif; }
.demo-disclaimer {
    margin:1rem 0 0;
    padding:.78rem 1rem;
    color:#65501d;
    background:#fff8e7;
    border:1px solid #efd58d;
    border-left:5px solid #e3a717;
    border-radius:9px;
    text-align:center;
    font:600 .8rem/1.4 Roboto,Arial,sans-serif;
}
.metric {
    min-height:168px;
    padding:1rem .75rem;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:space-between;
    text-align:center;
    background:linear-gradient(145deg,#edf5ff,#dae8fb);
    border:1px solid #d2def0;
    border-radius:10px;
    box-shadow:0 5px 10px rgba(21,58,118,.11);
}
.metric.warn { background:linear-gradient(145deg,#fff7ed,#f5e5d6); }
.metric.folder { background:linear-gradient(145deg,#f5f6fb,#e3e5ee); }
.metric-icon { font-size:3.2rem; line-height:1; }
.metric-title { min-height:44px; display:flex; align-items:center; font:700 1rem/1.05 Roboto,Arial,sans-serif; }
.metric-rule { width:100%; height:1px; background:#b8cbe3; }
.metric-value { font:800 1.8rem/1 Roboto,Arial,sans-serif; color:#174999; }
.metric.warn .metric-value { color:#d24b36; }
.metric-value small { font-size:.8rem; font-weight:600; color:var(--texto); }
.metric-text { font:600 .83rem/1.15 Roboto,Arial,sans-serif; }
.metric-link { color:var(--texto) !important; text-decoration:none !important; transition:transform .16s ease, box-shadow .16s ease; }
.metric-link:hover { transform:translateY(-3px); border-color:#78a9dc; box-shadow:0 9px 17px rgba(18,56,116,.17); }
.evidence-entry { display:block; margin:.95rem 0 .2rem; padding:.9rem 1.1rem; color:#0755a8 !important; background:#fff; border:1px solid #a6c6ee; border-radius:10px; text-decoration:none !important; font:800 .92rem/1.35 Roboto,Arial,sans-serif; }
.evidence-entry:hover { background:#eef6ff; }
.panel-detail { margin-top:1rem; padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; box-shadow:0 4px 10px rgba(18,61,121,.08); }
.panel-detail h3 { margin:0 0 .35rem; color:#092b66; font:800 1.15rem/1.2 Roboto,Arial,sans-serif; }
.panel-detail > p { margin:.2rem 0 .8rem; color:#546c8d; font:500 .84rem/1.4 Roboto,Arial,sans-serif; }
.demo-flow { display:grid; grid-template-columns:repeat(4,1fr); gap:.65rem; }
.demo-flow-step { position:relative; min-height:105px; padding:.8rem; color:#24476f; background:#edf5ff; border:1px solid #c2d9f2; border-radius:10px; font:600 .8rem/1.35 Roboto,Arial,sans-serif; }
.demo-flow-step b { display:grid; place-items:center; width:27px; height:27px; margin-bottom:.45rem; color:#fff; background:#0755a8; border-radius:50%; }
.focus-panel { max-width:1000px; margin:1.5rem auto; padding:1.35rem; }
.focus-header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:1rem;
    padding:1rem 1.15rem;
    color:#fff;
    background:linear-gradient(135deg,#073b82,#0873c7);
    border-radius:12px;
}
.focus-header strong { display:block; font:800 clamp(1.25rem,3vw,1.8rem)/1.1 Roboto,Arial,sans-serif; }
.focus-header small { display:block; margin-top:.25rem; color:#dceeff; font:600 .78rem Roboto,Arial,sans-serif; }
.focus-badge { padding:.4rem .7rem; color:#704f00; background:#fff0b8; border-radius:999px; white-space:nowrap; font:800 .72rem Roboto,Arial,sans-serif; }
.focus-panel .panel-detail { margin-top:1rem; }
.focus-actions { display:flex; justify-content:center; margin-top:1rem; }
.focus-actions .back-button { margin-top:0; }

.footer-nav {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:2rem;
    padding: .65rem 8% 0;
    border-top:2px solid #d2e0f4;
    font:700 1rem/1.2 Roboto,Arial,sans-serif;
}
.footer-nav div, .footer-nav a { color:#0a2459; text-align:center; text-decoration:none; }
.footer-nav a:hover { color:#0755a8; text-decoration:underline; }

/* Panel administrativo demostrativo */
.admin-page { padding:1.45rem; }
.admin-header {
    display:flex;
    justify-content:space-between;
    gap:1rem;
    align-items:center;
    padding:1.15rem 1.3rem;
    color:#fff;
    background:linear-gradient(135deg,#073b82,#0873c7);
    border-radius:14px;
}
.admin-header h2 { margin:0 0 .2rem; font:800 clamp(1.45rem,3vw,2.2rem)/1.1 Roboto,Arial,sans-serif; }
.admin-header p { margin:0; color:#dceeff; font:500 .9rem/1.35 Roboto,Arial,sans-serif; }
.admin-lock { display:grid; place-items:center; min-width:58px; height:58px; background:#fff; border-radius:50%; font-size:2rem; }
.admin-demo-badge { padding:.45rem .75rem; color:#714f00; background:#fff0b8; border-radius:999px; white-space:nowrap; font:800 .75rem Roboto,Arial,sans-serif; }
.admin-tabs { display:flex; flex-wrap:wrap; gap:.5rem; margin:1rem 0; }
.admin-tabs a { padding:.65rem .9rem; color:#0755a8; background:#edf5ff; border:1px solid #bfd6f1; border-radius:9px; text-decoration:none; font:700 .84rem Roboto,Arial,sans-serif; }
.admin-tabs a.active, .admin-tabs a:hover { color:#fff; background:#0755a8; }
.admin-kpis { display:grid; grid-template-columns:repeat(4,1fr); gap:.8rem; }
.admin-kpi { min-height:145px; padding:1rem; color:#0a2459 !important; background:#fff; border:1px solid #c5d9f2; border-radius:12px; text-decoration:none !important; box-shadow:0 4px 11px rgba(18,61,121,.10); transition:.16s ease; }
.admin-kpi:hover { transform:translateY(-3px); border-color:#6fa5dc; box-shadow:0 8px 16px rgba(18,61,121,.16); }
.admin-kpi span { display:block; font-size:2rem; }
.admin-kpi strong { display:block; margin:.45rem 0 .35rem; font:800 1rem/1.2 Roboto,Arial,sans-serif; }
.admin-kpi b { display:block; color:#0755a8; font:900 1.9rem/1 Roboto,Arial,sans-serif; }
.admin-kpi small { display:block; margin-top:.35rem; color:#617592; font:600 .75rem/1.3 Roboto,Arial,sans-serif; }
.admin-section { margin-top:1.15rem; padding:1rem; background:#fff; border:1px solid #c9dbf2; border-radius:12px; }
.admin-section h3 { margin:0 0 .75rem; color:#092b66; font:800 1.2rem Roboto,Arial,sans-serif; }
.admin-table-wrap { overflow-x:auto; }
.admin-table { width:100%; border-collapse:collapse; font:500 .8rem/1.35 Roboto,Arial,sans-serif; }
.admin-table th { padding:.65rem; color:#fff; background:#0755a8; text-align:left; white-space:nowrap; }
.admin-table td { padding:.65rem; color:#29476e; border-bottom:1px solid #dce7f5; }
.admin-table tr:nth-child(even) td { background:#f5f9ff; }
.status-pill { display:inline-block; padding:.25rem .55rem; border-radius:999px; font-weight:800; font-size:.7rem; }
.status-pill.ok { color:#17613f; background:#e6f7ee; }
.status-pill.wait { color:#795400; background:#fff2c9; }
.status-pill.sent { color:#174875; background:#e5f2ff; }
.topic-bars { display:grid; gap:.65rem; }
.topic-row { display:grid; grid-template-columns:165px 1fr 42px; gap:.65rem; align-items:center; color:#29476e; font:700 .8rem Roboto,Arial,sans-serif; }
.topic-track { height:13px; overflow:hidden; background:#e7effa; border-radius:999px; }
.topic-fill { height:100%; background:linear-gradient(90deg,#0870c0,#20a0e8); border-radius:999px; }
.source-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.75rem; }
.source-card { padding:1rem; background:#f5f9ff; border:1px solid #c9ddf4; border-radius:10px; }
.source-card strong { display:block; margin-bottom:.35rem; color:#092b66; }
.source-card p { margin:0; color:#4b6486; font:500 .8rem/1.4 Roboto,Arial,sans-serif; }

.module-page {
    min-height: 520px;
    padding: 2.2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.module-symbol { font-size: 5rem; line-height: 1; }
.module-page h2 { margin:1rem 0 .5rem; font:800 clamp(2rem,5vw,3rem)/1.05 Roboto,Arial,sans-serif; }
.module-page p { max-width:650px; margin:.4rem auto; font:500 1.2rem/1.5 Roboto,Arial,sans-serif; }
.status-chip { margin:1.2rem 0; padding:.55rem 1rem; color:#0754a4; background:#e8f3ff; border:1px solid #b9d5f2; border-radius:999px; font-weight:700; }
.back-button { display:inline-block; margin-top:1rem; padding:.8rem 1.25rem; color:white; background:#0754a4; border-radius:9px; text-decoration:none; font:700 1rem Roboto,Arial,sans-serif; box-shadow:0 5px 10px rgba(7,64,134,.18); }
.back-button:hover { background:#063d83; }

.model-access {
    display:grid;
    grid-template-columns:46px 1fr 22px;
    align-items:center;
    gap:.7rem;
    width:100%;
    margin:.85rem 0 .1rem;
    padding:.8rem .9rem;
    color:#fff !important;
    text-decoration:none !important;
    background:linear-gradient(135deg,#0878ca,#084b9e);
    border:1px solid #063c83;
    border-radius:13px;
    box-shadow:0 6px 12px rgba(8,67,139,.20);
    transition:transform .16s ease, box-shadow .16s ease;
}
.model-access:hover { transform:translateY(-2px); box-shadow:0 9px 16px rgba(8,67,139,.26); }
.model-access .model-shield { font-size:2.1rem; line-height:1; }
.model-access strong { display:block; color:#fff !important; font:800 .98rem/1.15 Roboto,Arial,sans-serif; }
.model-access small { display:block; margin-top:.18rem; color:#dbeeff !important; font:600 .72rem/1.2 Roboto,Arial,sans-serif; }
.model-access .model-arrow { color:#fff; font:800 1.75rem/1 Roboto,Arial,sans-serif; }

.model-page { padding:1.65rem; text-align:left; }
.model-intro {
    display:grid;
    grid-template-columns:86px 1fr;
    gap:1.1rem;
    align-items:center;
    padding:1.35rem;
    color:#fff;
    background:linear-gradient(135deg,#073b82,#0873c7);
    border-radius:14px;
}
.model-intro .model-big-shield { display:grid; place-items:center; width:76px; height:76px; font-size:3.3rem; background:#fff; border-radius:50%; }
.model-intro h2 { margin:0 0 .35rem; font:800 clamp(1.7rem,4vw,2.6rem)/1.05 Roboto,Arial,sans-serif; }
.model-intro p { max-width:880px; margin:0; font:500 1rem/1.45 Roboto,Arial,sans-serif; }
.model-section { margin-top:1.4rem; }
.model-section h3 { margin:0 0 .8rem; color:#092b66; font:800 1.35rem/1.2 Roboto,Arial,sans-serif; }
.model-section-lead { margin:-.35rem 0 1rem; color:#4d6586; font:500 .92rem/1.4 Roboto,Arial,sans-serif; }
.component-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.75rem; }
.component-card { min-height:155px; padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; box-shadow:0 4px 10px rgba(18,61,121,.08); }
.component-number { display:inline-grid; place-items:center; width:29px; height:29px; margin-bottom:.55rem; color:#fff; background:#0870c0; border-radius:50%; font:800 .85rem Roboto,Arial,sans-serif; }
.component-card strong { display:block; margin-bottom:.35rem; color:#092b66; font:800 .96rem/1.2 Roboto,Arial,sans-serif; }
.component-card p { margin:0; color:#405a7d; font:500 .82rem/1.4 Roboto,Arial,sans-serif; }
.component-link { display:block; color:inherit !important; text-decoration:none !important; border-radius:12px; }
.component-link .component-card { height:100%; transition:transform .16s ease,box-shadow .16s ease; }
.component-link:hover .component-card, .component-link:focus-visible .component-card { transform:translateY(-3px); border-color:#65a0de; box-shadow:0 9px 18px rgba(18,61,121,.17); }
.component-link small { display:block; margin-top:.6rem; color:#0755a8; font:800 .76rem Roboto,Arial,sans-serif; }
.legal-cards { display:grid; grid-template-columns:repeat(2,1fr); gap:.75rem; }
.legal-card { padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; }
.legal-card strong { display:block; color:#092b66; font:800 1rem Roboto,Arial,sans-serif; }
.legal-card p { color:#405a7d; font:500 .86rem/1.45 Roboto,Arial,sans-serif; }
.legal-card a { color:#0755a8; font:800 .86rem Roboto,Arial,sans-serif; }
.evidence-strip { margin:1rem 0; padding:.9rem 1rem; background:#edf5ff; border-left:5px solid #0755a8; border-radius:9px; color:#183b6d; font:600 .88rem/1.45 Roboto,Arial,sans-serif; }
.stage-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.75rem; }
.stage-grid.five { grid-template-columns:repeat(auto-fit,minmax(145px,1fr)); }
.stage { padding:1rem; text-align:center; background:#eaf4ff; border:1px solid #bcd6f1; border-radius:12px; }
.stage span { display:block; margin-bottom:.3rem; color:#0870c0; font:800 .75rem Roboto,Arial,sans-serif; text-transform:uppercase; letter-spacing:.04em; }
.stage strong { color:#092b66; font:800 1rem Roboto,Arial,sans-serif; }
.diris-box { padding:1.1rem 1.2rem; background:#fff8e7; border:1px solid #efcf7d; border-left:6px solid #e3a717; border-radius:12px; }
.diris-box strong { display:block; margin-bottom:.35rem; color:#774e00; font:800 1.05rem Roboto,Arial,sans-serif; }
.diris-box p { margin:0; color:#694e18; font:500 .9rem/1.45 Roboto,Arial,sans-serif; }
.model-actions { display:flex; flex-wrap:wrap; justify-content:center; gap:.75rem; margin-top:1.35rem; }
.source-button { display:inline-block; margin-top:1rem; padding:.8rem 1.25rem; color:#0754a4 !important; background:#fff; border:1px solid #7faee0; border-radius:9px; text-decoration:none !important; font:700 1rem Roboto,Arial,sans-serif; }
.source-button:hover { background:#edf6ff; }

.ethics-page { padding:1.65rem; text-align:left; }
.ethics-intro {
    display:grid;
    grid-template-columns:86px 1fr;
    gap:1.1rem;
    align-items:center;
    padding:1.35rem;
    color:#fff;
    background:linear-gradient(135deg,#073b82,#0869b6);
    border-radius:14px;
}
.ethics-intro .ethics-icon { display:grid; place-items:center; width:76px; height:76px; font-size:3.2rem; background:#fff; border-radius:50%; }
.ethics-intro h2 { margin:0 0 .35rem; font:800 clamp(1.7rem,4vw,2.6rem)/1.05 Roboto,Arial,sans-serif; }
.ethics-intro p { max-width:900px; margin:0; font:500 1rem/1.45 Roboto,Arial,sans-serif; }
.ethics-section { margin-top:1.4rem; }
.ethics-section h3 { margin:0 0 .4rem; color:#092b66; font:800 1.35rem/1.2 Roboto,Arial,sans-serif; }
.ethics-lead { margin:0 0 1rem; color:#4d6586; font:500 .92rem/1.4 Roboto,Arial,sans-serif; }
.situation-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.75rem; }
.situation-card { min-height:150px; padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; box-shadow:0 4px 10px rgba(18,61,121,.08); }
.situation-icon { display:block; margin-bottom:.55rem; font-size:2rem; line-height:1; }
.situation-card strong { display:block; margin-bottom:.35rem; color:#092b66; font:800 .98rem/1.2 Roboto,Arial,sans-serif; }
.situation-card p { margin:0; color:#405a7d; font:500 .82rem/1.4 Roboto,Arial,sans-serif; }
.ethics-columns { display:grid; grid-template-columns:1.25fr 1fr 1fr; gap:.8rem; }
.ethics-column { padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; }
.ethics-column.principles { border-top:5px solid #0870c0; }
.ethics-column.duties { border-top:5px solid #158a56; }
.ethics-column.bans { border-top:5px solid #d4553d; }
.ethics-column h4 { margin:0 0 .7rem; color:#092b66; font:800 1.05rem Roboto,Arial,sans-serif; }
.ethics-tags { display:flex; flex-wrap:wrap; gap:.42rem; }
.ethics-tag { padding:.38rem .58rem; color:#183b6d; background:#edf5ff; border:1px solid #c9dcf3; border-radius:999px; font:700 .76rem/1.2 Roboto,Arial,sans-serif; }
.duties .ethics-tag { color:#17613f; background:#eaf8f1; border-color:#bde3ce; }
.bans .ethics-tag { color:#8d3022; background:#fff0ed; border-color:#efc8c0; }
.decision-route { display:grid; grid-template-columns:repeat(4,1fr); gap:.65rem; counter-reset:ethics-step; }
.route-step { position:relative; min-height:132px; padding:2.65rem .9rem .9rem; color:#15355f; background:#eaf4ff; border:1px solid #bcd6f1; border-radius:12px; font:600 .84rem/1.4 Roboto,Arial,sans-serif; }
.route-step:before { counter-increment:ethics-step; content:counter(ethics-step); position:absolute; top:.75rem; left:.85rem; display:grid; place-items:center; width:28px; height:28px; color:#fff; background:#0870c0; border-radius:50%; font:800 .82rem Roboto,Arial,sans-serif; }
.ethics-alert { padding:1.05rem 1.15rem; background:#fff8e7; border:1px solid #efcf7d; border-left:6px solid #e3a717; border-radius:12px; color:#694e18; font:500 .9rem/1.45 Roboto,Arial,sans-serif; }
.ethics-alert strong { color:#774e00; }

/* Pantallas informativas de los demás módulos */
.info-page { padding:1.65rem; text-align:left; }
.info-intro {
    display:grid;
    grid-template-columns:86px 1fr;
    gap:1.1rem;
    align-items:center;
    padding:1.35rem;
    color:#fff;
    background:linear-gradient(135deg,#073b82,#0873c7);
    border-radius:14px;
}
.info-intro .info-icon { display:grid; place-items:center; width:76px; height:76px; font-size:3.1rem; background:#fff; border-radius:50%; }
.info-intro .info-icon .rvl-badge { transform:scale(.82); }
.info-intro h2 { margin:0 0 .35rem; font:800 clamp(1.7rem,4vw,2.6rem)/1.05 Roboto,Arial,sans-serif; }
.info-intro p { max-width:900px; margin:0; font:500 1rem/1.45 Roboto,Arial,sans-serif; }
.info-section { margin-top:1.4rem; }
.info-section h3 { margin:0 0 .4rem; color:#092b66; font:800 1.35rem/1.2 Roboto,Arial,sans-serif; }
.info-lead { margin:0 0 1rem; color:#4d6586; font:500 .92rem/1.45 Roboto,Arial,sans-serif; }
.info-grid { display:grid; gap:.75rem; }
.info-grid.cols-2 { grid-template-columns:repeat(2,1fr); }
.info-grid.cols-3 { grid-template-columns:repeat(3,1fr); }
.info-grid.cols-4 { grid-template-columns:repeat(4,1fr); }
.info-card { min-height:145px; padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; box-shadow:0 4px 10px rgba(18,61,121,.08); }
.info-card .info-card-icon { display:block; margin-bottom:.55rem; font-size:2rem; line-height:1; }
.info-card strong { display:block; margin-bottom:.35rem; color:#092b66; font:800 .98rem/1.2 Roboto,Arial,sans-serif; }
.info-card p { margin:0; color:#405a7d; font:500 .84rem/1.42 Roboto,Arial,sans-serif; }
.process-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.65rem; }
.process-step { min-height:140px; padding:.85rem; color:#15355f; background:#eaf4ff; border:1px solid #bcd6f1; border-radius:12px; font:600 .84rem/1.4 Roboto,Arial,sans-serif; }
.process-step span { display:grid; place-items:center; width:29px; height:29px; margin-bottom:.55rem; color:#fff; background:#0870c0; border-radius:50%; font:800 .82rem Roboto,Arial,sans-serif; }
.info-note { padding:1.05rem 1.15rem; border-radius:12px; font:500 .9rem/1.45 Roboto,Arial,sans-serif; }
.info-note strong { font-weight:800; }
.info-note.blue { color:#174875; background:#edf6ff; border:1px solid #b9d7f3; border-left:6px solid #1681d0; }
.info-note.yellow { color:#694e18; background:#fff8e7; border:1px solid #efcf7d; border-left:6px solid #e3a717; }
.info-note.red { color:#7b3025; background:#fff1ee; border:1px solid #efc5bd; border-left:6px solid #d8543e; }
.info-note.green { color:#17613f; background:#edf9f2; border:1px solid #bfe2ce; border-left:6px solid #198d50; }
.info-list { margin:.35rem 0 0; padding-left:1.15rem; color:#405a7d; font:500 .86rem/1.5 Roboto,Arial,sans-serif; }
.info-list li + li { margin-top:.3rem; }
.guide-link { display:block; min-height:155px; padding:1rem; color:#092b66 !important; background:#fff; border:1px solid #c6daf3; border-radius:12px; text-decoration:none !important; box-shadow:0 4px 10px rgba(18,61,121,.08); transition:transform .16s ease, box-shadow .16s ease; }
.guide-link:hover { transform:translateY(-2px); box-shadow:0 8px 15px rgba(18,61,121,.14); }
.guide-link span { display:block; margin-bottom:.55rem; font-size:2rem; }
.guide-link .guide-rvl-icon .rvl-badge { transform:scale(.68); transform-origin:left top; margin-bottom:-13px; }
.guide-link strong { display:block; margin-bottom:.35rem; font:800 .98rem/1.2 Roboto,Arial,sans-serif; }
.guide-link small { color:#4d6586; font:500 .82rem/1.4 Roboto,Arial,sans-serif; }
.contact-box { display:grid; grid-template-columns:1fr 1fr; gap:.75rem; }
.contact-item { padding:1rem; background:#fff; border:1px solid #c6daf3; border-radius:12px; }
.contact-item span { display:block; color:#567091; font:700 .75rem Roboto,Arial,sans-serif; text-transform:uppercase; }
.contact-item strong { display:block; margin-top:.35rem; color:#092b66; font:800 1rem/1.3 Roboto,Arial,sans-serif; }

.chat-app {
    min-height:620px;
    display:flex;
    flex-direction:column;
    overflow:hidden;
    background:rgba(255,255,255,.78);
}
.chat-app-header {
    display:flex;
    align-items:center;
    gap:.9rem;
    padding:1rem 1.2rem;
    color:white;
    background:linear-gradient(135deg,#063b82,#0764b7);
}
.chat-avatar { display:grid; place-items:center; width:52px; height:52px; flex:0 0 auto; font-size:2rem; background:white; border-radius:50%; box-shadow:0 2px 6px rgba(0,0,0,.2); }
.chat-identity { flex:1; }
.chat-identity strong { display:block; font:800 1.2rem Roboto,Arial,sans-serif; }
.chat-identity small { display:block; margin-top:.2rem; font:500 .8rem Roboto,Arial,sans-serif; opacity:.9; }
.chat-home-link { color:white; text-decoration:none; font:700 .85rem Roboto,Arial,sans-serif; }
.chat-window {
    flex:1;
    min-height:400px;
    padding:1.25rem;
    display:flex;
    flex-direction:column;
    justify-content:flex-end;
    gap:.85rem;
    background:linear-gradient(rgba(241,247,255,.93),rgba(233,242,255,.96));
}
.welcome-bubble { align-self:flex-start; max-width:75%; padding:.9rem 1rem; color:#0a2459; background:white; border:1px solid #c5d9f3; border-radius:15px 15px 15px 4px; font:500 .95rem/1.45 Roboto,Arial,sans-serif; box-shadow:0 3px 8px rgba(17,65,129,.08); }
.chat-app .chat-message { max-width:76%; }
.chat-composer { display:grid; grid-template-columns:1fr auto; gap:.7rem; padding:1rem; background:white; border-top:1px solid #cbdcf1; }
.chat-composer input { min-width:0; padding:.9rem 1rem; color:#0a2459; background:#f8fbff; border:2px solid #bed3ee; border-radius:12px; font:500 1rem Roboto,Arial,sans-serif; outline:none; }
.chat-composer input:focus { border-color:#0b66ba; box-shadow:0 0 0 3px rgba(11,102,186,.12); }
.chat-composer button { padding:.85rem 1.25rem; color:white; background:#0755a8; border:0; border-radius:12px; font:700 1rem Roboto,Arial,sans-serif; cursor:pointer; }
.chat-footer { display:flex; justify-content:space-between; gap:1rem; padding:.7rem 1rem; color:#506889; background:white; font:600 .72rem Roboto,Arial,sans-serif; }
.chat-footer a { color:#0755a8; text-decoration:none; font-weight:700; }

/* Chat nativo de Streamlit: contraste tipo Messenger */
[data-testid="stChatMessage"] {
    width:fit-content !important;
    max-width:78% !important;
    margin:.4rem auto .4rem 0 !important;
    padding:.8rem 1rem !important;
    color:#102a56 !important;
    background:#ffffff !important;
    border:1px solid #bfd5f0 !important;
    border-radius:18px 18px 18px 5px !important;
    box-shadow:0 4px 10px rgba(16,58,116,.10) !important;
}
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"],
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] span,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] strong {
    color:#102a56 !important;
    opacity:1 !important;
}
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] a {
    color:#075fc0 !important;
    font-weight:700 !important;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    margin-left:auto !important;
    margin-right:0 !important;
    color:#ffffff !important;
    background:linear-gradient(135deg,#0866ff,#0752b7) !important;
    border-color:#0752b7 !important;
    border-radius:18px 18px 5px 18px !important;
    box-shadow:0 5px 12px rgba(8,88,204,.22) !important;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"],
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] p,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] span,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stMarkdownContainer"] strong {
    color:#ffffff !important;
    opacity:1 !important;
}
[data-testid="stChatMessageAvatarAssistant"] {
    background:#e8f2ff !important;
    border:1px solid #b9d4f2 !important;
}
[data-testid="stChatMessageAvatarUser"] {
    background:#ffffff !important;
    border:1px solid rgba(255,255,255,.8) !important;
}
[data-testid="stBottomBlockContainer"],
[data-testid="stBottom"] > div {
    background:#eaf2ff !important;
    border-top:1px solid #bfd3ed !important;
}
[data-testid="stChatInput"] {
    color:#102a56 !important;
    background:#ffffff !important;
    border:2px solid #8eb8e8 !important;
    border-radius:15px !important;
    box-shadow:0 5px 14px rgba(14,64,131,.13) !important;
}
[data-testid="stChatInput"] textarea {
    color:#102a56 !important;
    -webkit-text-fill-color:#102a56 !important;
    caret-color:#0866ff !important;
    background:#ffffff !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color:#5f718d !important;
    -webkit-text-fill-color:#5f718d !important;
    opacity:1 !important;
}
[data-testid="stChatInputSubmitButton"] {
    color:#ffffff !important;
    background:#0866ff !important;
    border-radius:50% !important;
}
div.stButton > button {
    color:#0755a8 !important;
    background:#ffffff !important;
    border:1px solid #8eb8e8 !important;
}

@media (max-width: 760px) {
    .block-container { padding: 1.2rem .75rem 1.6rem !important; }
    .brand { padding-bottom:.8rem; }
    .topic-bar { line-height:1.25; padding:.7rem .5rem; }
    .hero { grid-template-columns:1fr; min-height:500px; }
    .mascot-wrap { position:absolute; inset:auto auto 0 0; width:43%; height:250px; min-height:0; }
    .robot { left:-.4rem; width:100%; }
    .hero-copy { min-height:500px; padding:1.5rem 1rem 1.2rem; }
    .speech { margin-left:16%; font-size:1.35rem; }
    .quick-chat { margin-left:16%; width:84%; grid-template-columns:1fr; }
    .chat-hint { margin-left:16%; }
    .hero-feature-card { width:72%; margin:0 0 0 auto; grid-template-columns:50px 1fr 20px; padding:.8rem; border-width:6px; }
    .shield { font-size:2.8rem; }
    .badge { right:8%; font-size:.72rem; padding:.38rem .65rem; }
    .menu-grid { grid-template-columns:repeat(2,1fr); }
    .menu-card { min-height:145px; }
    .menu-icon { font-size:2.9rem; }
    .metrics-grid { grid-template-columns:repeat(2,1fr); }
    .admin-kpis { grid-template-columns:repeat(2,1fr); }
    .demo-flow { grid-template-columns:repeat(2,1fr); }
    .source-grid { grid-template-columns:1fr; }
    .admin-header { align-items:flex-start; }
    .focus-header { align-items:flex-start; }
    .chat-message { max-width:94%; }
    .chat-app { min-height:560px; }
    .chat-window { min-height:350px; padding:.85rem; }
    .chat-app .chat-message, .welcome-bubble { max-width:92%; }
    [data-testid="stChatMessage"] { max-width:92% !important; }
    .chat-composer { grid-template-columns:1fr auto; padding:.75rem; }
    .chat-composer button { padding:.8rem .9rem; }
    .chat-home-link { font-size:0; }
    .chat-home-link:after { content:"← Inicio"; font-size:.8rem; }
    .component-grid { grid-template-columns:1fr; }
    .legal-cards { grid-template-columns:1fr; }
    .stage-grid { grid-template-columns:1fr; }
    .model-page { padding:1rem; }
    .model-intro { grid-template-columns:1fr; text-align:center; }
    .model-intro .model-big-shield { margin:auto; }
    .ethics-page { padding:1rem; }
    .ethics-intro { grid-template-columns:1fr; text-align:center; }
    .ethics-intro .ethics-icon { margin:auto; }
    .situation-grid, .decision-route { grid-template-columns:1fr 1fr; }
    .ethics-columns { grid-template-columns:1fr; }
    .info-page { padding:1rem; }
    .info-intro { grid-template-columns:1fr; text-align:center; }
    .info-intro .info-icon { margin:auto; }
    .info-grid.cols-3, .info-grid.cols-4, .process-grid { grid-template-columns:1fr 1fr; }
}

@media (max-width: 420px) {
    .menu-grid, .metrics-grid { grid-template-columns:1fr 1fr; gap:.65rem; }
    .menu-card { min-height:128px; padding:.75rem .3rem; }
    .menu-card strong { font-size:.92rem; }
    .metric { min-height:155px; }
    .footer-nav { grid-template-columns:1fr; padding:.6rem 0 0; gap:.8rem; }
    .admin-kpis { grid-template-columns:1fr 1fr; }
    .topic-row { grid-template-columns:110px 1fr 35px; }
    .demo-flow { grid-template-columns:1fr; }
    .focus-header { flex-direction:column; }
    .situation-grid, .decision-route { grid-template-columns:1fr; }
    .info-grid.cols-2, .info-grid.cols-3, .info-grid.cols-4, .process-grid, .contact-box { grid-template-columns:1fr; }
}
</style>
""",
    unsafe_allow_html=True,
)


def detalle_panel_demostrativo(vista: str) -> str:
    """Detalle interactivo del panel principal con información ficticia."""
    if vista == "consultas":
        return """
        <div class="panel-detail">
            <h3>💬 Detalle de consultas recibidas</h3>
            <p>Muestra de cómo se presentarían los registros generados por el chat y otros canales.</p>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Código</th><th>Fecha</th><th>Canal</th><th>Tema</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>INT-001</td><td>03/07/2026</td><td>Chat INTEGRID-LN</td><td>Conflicto de intereses</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-002</td><td>05/07/2026</td><td>Chat INTEGRID-LN</td><td>Declaración jurada</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-003</td><td>08/07/2026</td><td>Correo</td><td>Modelo de Integridad</td><td><span class="status-pill sent">Derivada</span></td></tr>
                    <tr><td>INT-004</td><td>11/07/2026</td><td>Anexo</td><td>Registro de Visitas</td><td><span class="status-pill wait">Seguimiento</span></td></tr>
                </tbody>
            </table></div>
        </div>
        """
    if vista == "orientaciones":
        return """
        <div class="panel-detail">
            <h3>✅ Orientaciones brindadas</h3>
            <p>Ejemplo de clasificación de las respuestas preventivas proporcionadas durante el periodo.</p>
            <div class="topic-bars">
                <div class="topic-row"><span>Ética pública</span><div class="topic-track"><div class="topic-fill" style="width:78%"></div></div><b>14</b></div>
                <div class="topic-row"><span>Declaraciones juradas</span><div class="topic-track"><div class="topic-fill" style="width:55%"></div></div><b>10</b></div>
                <div class="topic-row"><span>Registro de Visitas</span><div class="topic-track"><div class="topic-fill" style="width:38%"></div></div><b>7</b></div>
                <div class="topic-row"><span>Canal de denuncias</span><div class="topic-track"><div class="topic-fill" style="width:28%"></div></div><b>5</b></div>
            </div>
        </div>
        """
    if vista == "alertas":
        return """
        <div class="panel-detail">
            <h3>⚠️ Alertas preventivas identificadas</h3>
            <p>Situaciones ficticias detectadas durante una orientación, sin mostrar nombres ni información sensible.</p>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Alerta</th><th>Situación general</th><th>Acción preventiva</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>AL-001</td><td>Posible conflicto de intereses</td><td>Orientación previa a la decisión</td><td><span class="status-pill ok">Atendida</span></td></tr>
                    <tr><td>AL-002</td><td>Ofrecimiento de obsequio</td><td>Información sobre prohibiciones</td><td><span class="status-pill ok">Atendida</span></td></tr>
                    <tr><td>AL-003</td><td>Registro RVL incompleto</td><td>Verificación y regularización</td><td><span class="status-pill wait">Seguimiento</span></td></tr>
                </tbody>
            </table></div>
        </div>
        """
    if vista == "derivaciones":
        return """
        <div class="panel-detail">
            <h3>🗂️ Seguimiento de derivaciones</h3>
            <p>Ejemplo de trazabilidad desde la orientación inicial hasta la atención o cierre por la UFII.</p>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Código</th><th>Tema</th><th>Derivación</th><th>Responsable</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>DER-001</td><td>Asistencia sobre Modelo de Integridad</td><td>08/07/2026</td><td>UFII</td><td><span class="status-pill ok">Cerrada</span></td></tr>
                    <tr><td>DER-002</td><td>Orientación ética especializada</td><td>12/07/2026</td><td>UFII</td><td><span class="status-pill wait">En revisión</span></td></tr>
                    <tr><td>DER-003</td><td>Incidencia operativa RVL</td><td>18/07/2026</td><td>UFII / RVL</td><td><span class="status-pill sent">Derivada</span></td></tr>
                </tbody>
            </table></div>
        </div>
        """
    if vista == "evidencias":
        return """
        <div class="panel-detail">
            <h3>📎 Tareas y medios de verificación del Modelo</h3>
            <p>Ejemplo de seguimiento transversal: cada fila indica qué se revisó, qué área debe sustentar la tarea y cuál sería la fuente comprobable.</p>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Componente / tarea</th><th>Periodo</th><th>Responsable de la tarea</th><th>Medio de verificación esperado</th><th>Estado demo</th></tr></thead>
                <tbody>
                    <tr><td>1 · Programa anual</td><td>2026</td><td>Alta Dirección / UFII</td><td>Resolución y matriz aprobada</td><td><span class="status-pill ok">Verificada</span></td></tr>
                    <tr><td>4 · Tarea 4.1 PTE</td><td>Julio</td><td>Responsable del PTE / UFII</td><td>URL, ficha fechada y respuesta a observaciones</td><td><span class="status-pill wait">En revisión</span></td></tr>
                    <tr><td>4 · Tareas 4.3 y 4.4</td><td>Julio</td><td>Responsables RVL y agendas</td><td>Reporte oficial, fecha y verificación</td><td><span class="status-pill sent">Coordinación</span></td></tr>
                    <tr><td>6 · Capacitación</td><td>Agosto</td><td>UFII / áreas de apoyo</td><td>Programa, asistencia y material aprobado</td><td><span class="status-pill ok">Verificada</span></td></tr>
                    <tr><td>8 · Seguimiento</td><td>Trimestre</td><td>UFII / áreas involucradas</td><td>Matriz e informe periódico dirigido a autoridades</td><td><span class="status-pill wait">Pendiente</span></td></tr>
                </tbody>
            </table></div>
            <div class="evidence-strip">Indicadores posibles, una vez conectados a registros validados: tareas verificadas / tareas programadas; hallazgos subsanados / hallazgos comunicados; actividades sustentadas / actividades ejecutadas. Ningún indicador se calcula hoy con datos reales.</div>
        </div>
        """
    return """
    <div class="panel-detail">
        <h3>🔄 Así funcionaría el seguimiento</h3>
        <p>Los registros se actualizarían desde el chat, formularios y controles internos autorizados.</p>
        <div class="demo-flow">
            <div class="demo-flow-step"><b>1</b>INTEGRID-LN asigna un código y registra fecha, canal y tema.</div>
            <div class="demo-flow-step"><b>2</b>La consulta se clasifica como orientación, alerta o posible derivación.</div>
            <div class="demo-flow-step"><b>3</b>La UFII actualiza el estado cuando corresponde una atención especializada.</div>
            <div class="demo-flow-step"><b>4</b>El panel consolida cifras, temas y estados sin exhibir datos personales.</div>
        </div>
    </div>
    """


def pagina_panel_enfocado(vista: str) -> str:
    """Muestra solamente el reporte seleccionado, sin repetir la portada."""
    titulos = {
        "consultas": "Consultas recibidas",
        "orientaciones": "Orientaciones brindadas",
        "alertas": "Alertas preventivas",
        "derivaciones": "Derivaciones a la UFII",
        "evidencias": "Tareas y evidencias del Modelo",
    }
    titulo = titulos.get(vista, "Panel de seguimiento")
    detalle = detalle_panel_demostrativo(vista)
    return f"""
    <main class="integri-shell">
        <section class="focus-panel panel">
            <header class="focus-header">
                <div><strong>INTEGRID-LN · {titulo}</strong><small>Vista demostrativa del seguimiento institucional</small></div>
                <span class="focus-badge">DATOS SIMULADOS</span>
            </header>
            {detalle}
            <p class="demo-disclaimer"><strong>Información ficticia:</strong> los códigos, fechas, cifras y situaciones se utilizan exclusivamente para mostrar cómo funcionaría este reporte. No corresponden a casos ni resultados reales de la UFII.</p>
            <div class="focus-actions"><a class="back-button" href="?" target="_self">← Volver al panel principal</a></div>
        </section>
    </main>
    """


panel_vista_inicio = st.query_params.get("panel", "resumen")
detalle_panel_inicio = detalle_panel_demostrativo(panel_vista_inicio)


pagina = f"""
<main class="integri-shell">
    <header class="brand">
        <h1>INTEGRID-LN</h1>
        <div class="brand-line"></div>
        <h2>Asistente de Integridad Institucional</h2>
        <p>Unidad Funcional de Integridad Institucional (UFII)</p>
    </header>

    <div class="topic-bar" role="heading" aria-level="1">INTEGRID-LN · Plataforma de Integridad Institucional</div>

    <section class="hero panel">
        <div class="mascot-wrap">{robot_html}</div>
        <div class="hero-copy">
            <div class="speech">¡Hola! ¿En qué puedo ayudarte?</div>
            <form class="quick-chat" method="get" action="">
                <input name="chat" type="hidden" value="1">
                <input name="consulta" type="text" maxlength="500" autocomplete="off" placeholder="Escribe tu consulta sobre integridad..." required>
                <button type="submit">Enviar</button>
            </form>
            <div class="chat-hint">No ingreses nombres, DNI, datos personales ni detalles sensibles de una denuncia.</div>
            <a class="hero-link" href="?modulo=modelo" target="_self">
                <div class="hero-feature-card">
                    <div class="shield">🛡️</div>
                    <div><strong>Modelo de Integridad</strong><small>Orientación preventiva</small></div>
                    <div class="arrow">›</div>
                </div>
            </a>
        </div>
    </section>

    <aside class="notice panel">
        <span class="notice-i">i</span><span>INTEGRID-LN orienta, no decide ni sanciona</span>
    </aside>

    <section class="section panel">
        <h2 class="section-title">Menú</h2>
        <div class="menu-grid">
            <a class="menu-link" href="?modulo=etica" target="_self"><div class="menu-card"><span class="menu-icon">⚖️</span><strong>Consultas de Ética</strong></div></a>
            <a class="menu-link" href="?modulo=declaraciones" target="_self"><div class="menu-card"><span class="menu-icon">📄</span><strong>Declaraciones Juradas</strong></div></a>
            <a class="menu-link" href="?modulo=denuncias" target="_self"><div class="menu-card"><span class="menu-icon">📣</span><strong>Canal de Denuncias</strong></div></a>
            <a class="menu-link" href="?modulo=rvl" target="_self"><div class="menu-card"><span class="menu-icon rvl-menu-icon">{icono_rvl_html}</span><strong>Registro de Visitas RVL</strong></div></a>
            <a class="menu-link" href="?modulo=guias" target="_self"><div class="menu-card"><span class="menu-icon">✅</span><strong>Checklists y Guías</strong></div></a>
            <a class="menu-link" href="?modulo=derivacion" target="_self"><div class="menu-card"><span class="menu-icon">💼</span><strong>Derivar a UFII</strong></div></a>
            <a class="menu-link" href="?modulo=transparencia" target="_self"><div class="menu-card"><span class="menu-icon">🔎</span><strong>Transparencia y PTE</strong></div></a>
            <a class="menu-link" href="?modulo=marco" target="_self"><div class="menu-card"><span class="menu-icon">📚</span><strong>Base legal y procesos</strong></div></a>
            <a class="menu-link" href="?modulo=seguimiento" target="_self"><div class="menu-card"><span class="menu-icon">📊</span><strong>Seguimiento del Modelo</strong></div></a>
        </div>
        <a class="election-link" href="?modulo=neutralidad" target="_self"><span class="election-icon">🗳️</span><span><strong>Neutralidad electoral 2026</strong><small>Guía preventiva · Elecciones regionales y municipales del 4 de octubre</small></span><span class="election-arrow">›</span></a>
    </section>

    <section id="panel-seguimiento" class="section panel">
        <h2 class="section-title">Panel de seguimiento · demostración UFII</h2>
        <p class="demo-caption">Selecciona una tarjeta para visualizar cómo se presentarían los registros y el proceso de seguimiento. Esta maqueta es pública y contiene únicamente ejemplos ficticios.</p>
        <div class="metrics-grid">
            <a class="metric metric-link" href="?panel=consultas#panel-seguimiento" target="_self">
                <span class="metric-icon">💬</span><div class="metric-title">Consultas recibidas</div><div class="metric-rule"></div>
                <div class="metric-value">42 <small>durante el mes</small></div>
            </a>
            <a class="metric metric-link" href="?panel=orientaciones#panel-seguimiento" target="_self">
                <span class="metric-icon">✅</span><div class="metric-title">Orientaciones brindadas</div><div class="metric-rule"></div>
                <div class="metric-value">36 <small>respuestas registradas</small></div>
            </a>
            <a class="metric metric-link warn" href="?panel=alertas#panel-seguimiento" target="_self">
                <span class="metric-icon">⚠️</span><div class="metric-title">Alertas preventivas identificadas</div><div class="metric-rule"></div>
                <div class="metric-value">7 <small>situaciones orientadas</small></div>
            </a>
            <a class="metric metric-link folder" href="?panel=derivaciones#panel-seguimiento" target="_self">
                <span class="metric-icon">🗂️</span><div class="metric-title">Derivaciones a UFII</div><div class="metric-rule"></div>
                <div class="metric-value">6 <small>solicitudes derivadas</small></div>
            </a>
        </div>
        <a class="evidence-entry" href="?panel=evidencias" target="_self">📎 Ver cómo se seguirían las tareas, responsables, indicadores y medios de verificación del Modelo →</a>
        {detalle_panel_inicio}
        <p class="demo-disclaimer"><strong>Datos simulados para la maqueta:</strong> todas las cifras, códigos y situaciones son ficticias. Se muestran únicamente para demostrar cómo funcionaría el seguimiento; no representan carga laboral ni resultados oficiales de la UFII.</p>
    </section>

    <footer class="footer-nav">
        <a href="?modulo=guias" target="_self">💬 &nbsp; Guías preventivas</a>
        <a href="?modulo=seguimiento" target="_self">🔎 &nbsp; Seguimiento del Modelo (demo)</a>
    </footer>
</main>
"""

pagina_inicio = pagina

# El Modelo y las rutas de esta maqueta se fundamentan en el D. S. 148-2024-PCM
# y la Directiva 001-2026-PCM/SIP. Las evidencias indicadas son ejemplos de
# presentación: no equivalen a acreditación ante la SIP ni a registros reales.
NORMA_MODELO = "https://www.gob.pe/institucion/rree/normas-legales/6332599-148-2024-pcm"
DIRECTIVA_MODELO = "https://www.gob.pe/institucion/pcm/normas-legales/7644478-002-2026-pcm-sip"
NORMA_EVALUACION = "https://www.gob.pe/institucion/pcm/normas-legales/7192485-009-2025-pcm-sip"
MODIFICACION_EVALUACION = "https://www.gob.pe/institucion/pcm/normas-legales/8166933-007-2026-pcm-sip"
PTE_DIRIS = "https://www.transparencia.gob.pe/enlaces/pte_transparencia_enlaces.aspx?id_entidad=18791"
LINEAMIENTO_PTE = "https://www.gob.pe/institucion/antaip/normas-legales/7244059-066-2025-jus-dgtaipd"
PROGRAMA_DIRIS_2026 = "https://www.gob.pe/institucion/dirislimanorte/normas-legales/7946922-d000352-2026-dg-diris-ln"
NORMA_NEUTRALIDAD_PCM = "https://www.gob.pe/institucion/pcm/normas-legales/7677427-003-2026-pcm-sip"
LINEAMIENTOS_JNE = "https://www.gob.pe/institucion/jne/normas-legales/7908823-000021-2026-p-jne"
ELECCIONES_2026 = "https://erm2026.onpe.gob.pe/"
RESOLUCIONES_DIRIS = "https://www.gob.pe/institucion/dirislimanorte/normas-legales/tipos/26-resolucion-directoral?filter%5Border%5D=publication_desc&sheet=26"

COMPONENTES = {
    1: {
        "titulo": "Compromiso de la Alta Dirección",
        "resumen": "Liderazgo institucional, compromiso suscrito y condiciones para ejercer la función de integridad.",
        "acciones": ("Gestionar el Compromiso de Integridad Institucional y su difusión.", "Preparar el Programa de Integridad anual y coordinar su aprobación.", "Identificar brechas, responsables y necesidades de recursos."),
        "roles": "El titular respalda y aprueba; la UFII propone, coordina y hace seguimiento. El compromiso se renueva si cambia el titular de la entidad.",
        "ejemplo": "Compromiso firmado, resolución que aprueba el Programa, matriz de acciones y constancias de difusión.",
        "ruta": "marco",
    },
    2: {
        "titulo": "Gestión de riesgos",
        "resumen": "Identificar, analizar y tratar riesgos que afectan la integridad en procesos institucionales.",
        "acciones": ("Seleccionar procesos expuestos y coordinar con las áreas dueñas del proceso.", "Registrar riesgos, medidas de tratamiento y responsables.", "Revisar avances y actualizar los controles acordados."),
        "roles": "Las áreas responsables describen y gestionan sus procesos; la UFII orienta y coordina el seguimiento de riesgos de integridad.",
        "ejemplo": "Matriz de riesgos, actas de coordinación, plan de tratamiento y seguimiento fechado.",
        "ruta": "guias",
    },
    3: {
        "titulo": "Políticas de integridad",
        "resumen": "Normas de conducta, prevención de conflictos de intereses y prácticas de debida diligencia.",
        "acciones": ("Orientar sobre principios, deberes y prohibiciones éticas.", "Explicar qué declaración jurada corresponde y cómo llegar al sistema oficial.", "Canalizar dudas sobre conflictos de intereses y restricciones aplicables."),
        "roles": "La UFII brinda orientación preventiva; cada área competente verifica obligaciones concretas y aplica las medidas que le corresponden.",
        "ejemplo": "Material aprobado, constancias de orientación sin datos sensibles y documentación oficial de las áreas competentes.",
        "ruta": "etica",
    },
    4: {
        "titulo": "Transparencia, datos abiertos y rendición de cuentas",
        "resumen": "Acceso público oportuno, PTE, solicitudes de información, RVL, agendas oficiales y datos abiertos.",
        "acciones": ("Verificar la actualización periódica del PTE y coordinar observaciones (tarea 4.1).", "Dar seguimiento institucional a solicitudes de información, RVL y agendas oficiales (tareas 4.2 a 4.4).", "Coordinar apertura de datos y mecanismos de rendición de cuentas (tareas 4.5 y 4.6)."),
        "roles": "El responsable del PTE publica la información; la UFII verifica, coordina y monitorea sin asumir la función de publicación.",
        "ejemplo": "Ficha por rubro y periodo con URL, fecha de revisión, hallazgo, respuesta del responsable y enlace o constancia verificable.",
        "ruta": "transparencia",
    },
    5: {
        "titulo": "Controles y auditoría",
        "resumen": "Articulación de controles, atención de recomendaciones y prevención en decisiones institucionales.",
        "acciones": ("Ubicar controles relevantes en los procesos identificados.", "Coordinar con los órganos y áreas competentes la información de seguimiento.", "Registrar medidas correctivas y fechas de verificación."),
        "roles": "Los órganos de control y las áreas responsables mantienen sus competencias; la UFII articula el componente desde el enfoque preventivo.",
        "ejemplo": "Matriz de recomendaciones y acciones, informes de las áreas competentes y seguimiento de medidas.",
        "ruta": "guias",
    },
    6: {
        "titulo": "Comunicación y capacitación",
        "resumen": "Inducción, difusión interna y externa, formación y materiales de consulta preventiva.",
        "acciones": ("Planificar temas, destinatarios y canales de difusión.", "Realizar acciones formativas y recoger constancias.", "Evaluar alcance y ajustar contenidos de acuerdo con necesidades detectadas."),
        "roles": "La UFII coordina contenidos de integridad con las áreas de comunicaciones y capacitación responsables de su ejecución.",
        "ejemplo": "Cronograma, piezas aprobadas, enlaces de publicaciones, listas de asistencia e informes de resultados.",
        "ruta": "guias",
    },
    7: {
        "titulo": "Canal de denuncia",
        "resumen": "Ruta segura de denuncias por presunta corrupción y medidas de protección del denunciante.",
        "acciones": ("Difundir el canal oficial y distinguir una denuncia de una consulta.", "Proteger la confidencialidad y remitir los hechos solo por canales competentes.", "Monitorear mejoras del canal sin exhibir identidades ni detalles de casos."),
        "roles": "La unidad competente gestiona las denuncias y solicitudes de protección; el asistente únicamente informa y deriva.",
        "ejemplo": "Constancia de difusión y estadísticas agregadas autorizadas, sin identidad ni contenido específico de denuncias.",
        "ruta": "denuncias",
    },
    8: {
        "titulo": "Supervisión y monitoreo",
        "resumen": "Seguimiento del Programa de Integridad, verificación de tareas y reporte de brechas.",
        "acciones": ("Relacionar cada actividad del Programa con su responsable, periodo y medio de verificación.", "Registrar avances y observaciones con fecha y fuente institucional.", "Informar periódicamente al titular y a la máxima autoridad administrativa."),
        "roles": "La UFII consolida y custodia los medios de verificación; las otras unidades ejecutan las tareas y entregan la documentación.",
        "ejemplo": "Matriz de seguimiento anual, informe periódico, documento de sustento y acciones para cerrar brechas.",
        "ruta": "seguimiento",
    },
    9: {
        "titulo": "Encargado del Modelo de Integridad",
        "resumen": "Función de integridad formalizada, competencias especializadas y red de coordinación para sostener el Modelo.",
        "acciones": ("Verificar la modalidad y el documento que formaliza la función de integridad.", "Coordinar la certificación especializada cuando la SIP establezca sus condiciones y plazos.", "Desarrollar la red de integridad y documentar la cooperación interinstitucional."),
        "roles": "La unidad designada para la función de integridad coordina el Modelo; su denominación y responsabilidades concretas deben constar en documentos institucionales.",
        "ejemplo": "Documento de formalización, constancias de certificación cuando correspondan y registro de reuniones de la red.",
        "ruta": "derivacion",
    },
}

modulos = {
    "modelo": ("🛡️", "Modelo de Integridad", "Espacio para orientar sobre los componentes y acciones preventivas del Modelo de Integridad."),
    "etica": ("⚖️", "Consultas de Ética", "Espacio para brindar orientación preventiva ante dudas y dilemas éticos."),
    "declaraciones": ("📄", "Declaraciones Juradas", "Espacio para orientar sobre obligaciones, plazos y canales aplicables."),
    "denuncias": ("📣", "Canal de Denuncias", "Espacio para informar sobre el canal oficial y las medidas de protección."),
    "rvl": (icono_rvl_html, "Registro de Visitas RVL", "Espacio de orientación operativa sobre el Registro de Visitas en Línea."),
    "guias": ("✅", "Checklists y Guías", "Repositorio de materiales preventivos y herramientas de consulta rápida."),
    "derivacion": ("💼", "Derivar a UFII", "Espacio para identificar cuándo corresponde solicitar orientación directa a la UFII."),
    "transparencia": ("🔎", "Transparencia y PTE", "Consulta el Portal de Transparencia Estándar de DIRIS y la ruta de verificación del componente 4."),
    "marco": ("📚", "Base legal y procesos", "Consulta las normas vigentes y cómo se enlazan con la demostración del Modelo."),
    "seguimiento": ("📊", "Seguimiento del Modelo", "Visualiza la ruta de acciones, responsables, indicadores y medios de verificación."),
    "neutralidad": ("🗳️", "Neutralidad electoral 2026", "Orientación preventiva sobre reglas de neutralidad y publicidad estatal durante el proceso electoral."),
    "componente": ("🛡️", "Componente del Modelo", "Revisa sus acciones y ejemplos de evidencia."),
}


def pagina_modulo_info(simbolo: str, titulo: str, descripcion: str, contenido: str) -> str:
    """Construye una pantalla informativa manteniendo la identidad visual de INTEGRID-LN."""
    return f"""
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRID-LN</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <div class="topic-bar" role="heading" aria-level="1">INTEGRID-LN · Plataforma de Integridad Institucional</div>
        <section class="info-page panel">
            <div class="info-intro">
                <div class="info-icon">{simbolo}</div>
                <div><h2>{titulo}</h2><p>{descripcion}</p></div>
            </div>
            {contenido}
        </section>
    </main>
    """


modulo_actual = st.query_params.get("modulo", "")

if modulo_actual == "modelo":
    componentes_html = "".join(
        f'<a class="component-link" href="?modulo=componente&n={numero}" target="_self">'
        f'<article class="component-card"><span class="component-number">{numero}</span>'
        f'<strong>{html.escape(datos["titulo"])}</strong><p>{html.escape(datos["resumen"])}</p>'
        f'<small>Ver acciones y evidencias →</small></article></a>'
        for numero, datos in COMPONENTES.items()
    )
    pagina = f"""
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRID-LN</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <div class="topic-bar" role="heading" aria-level="1">INTEGRID-LN · Plataforma de Integridad Institucional</div>

        <section class="model-page panel">
            <div class="model-intro">
                <div class="model-big-shield">🛡️</div>
                <div>
                    <h2>Modelo de Integridad vigente</h2>
                    <p>Conjunto de orientaciones para fortalecer la capacidad preventiva y defensiva de las entidades públicas frente a la corrupción y las prácticas contrarias a la ética.</p>
                </div>
            </div>

            <div class="model-section">
                <h3>Los 9 componentes oficiales</h3>
                <p class="model-section-lead">Abre cada tarjeta para ver tareas, responsabilidades y ejemplos de sustento. Las referencias son orientativas para esta maqueta.</p>
                <div class="component-grid">
                    {componentes_html}
                </div>
            </div>

            <div class="model-section">
                <h3>Tres procesos de implementación</h3>
                <p class="model-section-lead">La Directiva N.° 001-2026-PCM/SIP organiza las tareas en planificación, desarrollo de los componentes y seguimiento y evaluación.</p>
                <div class="stage-grid">
                    <div class="stage"><span>Proceso 1</span><strong>Planificación</strong></div>
                    <div class="stage"><span>Proceso 2</span><strong>Desarrollo</strong></div>
                    <div class="stage"><span>Proceso 3</span><strong>Seguimiento y evaluación</strong></div>
                </div>
            </div>
            <div class="model-section">
                <h3>Cinco etapas de evaluación del ICP</h3>
                <p class="model-section-lead">Son niveles de evaluación de la implementación; no son los mismos tres procesos anteriores.</p>
                <div class="stage-grid five">
                    <div class="stage"><span>Etapa 1</span><strong>Inicial</strong></div>
                    <div class="stage"><span>Etapa 2</span><strong>Institucionalización</strong></div>
                    <div class="stage"><span>Etapa 3</span><strong>Estandarización</strong></div>
                    <div class="stage"><span>Etapa 4</span><strong>Eficacia</strong></div>
                    <div class="stage"><span>Etapa 5</span><strong>Impacto</strong></div>
                </div>
            </div>

            <div class="model-section diris-box">
                <strong>Aplicación en DIRIS Lima Norte</strong>
                <p>El Programa de Integridad 2026 fue aprobado por Resolución Directoral N.° D000352-2026-DG-DIRIS.LN. Esta demostración muestra rutas y ejemplos, sin reportar avances oficiales; el seguimiento real requiere vincular acciones aprobadas, responsables, medios de verificación y validaciones de las unidades competentes.</p>
            </div>

            <div class="model-section diris-box">
                <strong>¿Qué significa para ti?</strong>
                <p>El modelo ayuda a prevenir riesgos, actuar con imparcialidad, reconocer posibles conflictos de intereses, utilizar correctamente los canales institucionales y proteger la confianza en el servicio público.</p>
            </div>

            <div class="model-actions">
                <a class="back-button" href="?" target="_self">← Volver al inicio</a>
                <a class="source-button" href="?modulo=marco" target="_self">Ver base legal y procesos →</a>
                <a class="source-button" href="{PROGRAMA_DIRIS_2026}" target="_blank" rel="noopener noreferrer">Programa DIRIS 2026 ↗</a>
                <a class="source-button" href="{DIRECTIVA_MODELO}" target="_blank" rel="noopener noreferrer">Directiva N.° 001-2026 ↗</a>
            </div>
        </section>
    </main>
    """
elif modulo_actual == "etica":
    pagina = """
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRID-LN</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <div class="topic-bar" role="heading" aria-level="1">INTEGRID-LN · Plataforma de Integridad Institucional</div>

        <section class="ethics-page panel">
            <div class="ethics-intro">
                <div class="ethics-icon">⚖️</div>
                <div>
                    <h2>Consultas de Ética</h2>
                    <p>Orientación preventiva para reconocer dilemas éticos y tomar decisiones compatibles con los principios, deberes y prohibiciones de la función pública.</p>
                </div>
            </div>

            <div class="ethics-section">
                <h3>¿Sobre qué situaciones puedes consultar?</h3>
                <p class="ethics-lead">Describe únicamente el tipo de situación. No incluyas nombres, DNI, documentos, evidencias ni datos sensibles.</p>
                <div class="situation-grid">
                    <article class="situation-card"><span class="situation-icon">🔄</span><strong>Conflicto de intereses</strong><p>Cuando un interés personal, familiar, laboral o económico podría afectar tu imparcialidad.</p></article>
                    <article class="situation-card"><span class="situation-icon">🎁</span><strong>Regalos, favores o ventajas</strong><p>Cuando te ofrecen o solicitan un beneficio relacionado con tus funciones o decisiones.</p></article>
                    <article class="situation-card"><span class="situation-icon">🏛️</span><strong>Recursos e información pública</strong><p>Dudas sobre el uso de bienes del Estado, información reservada o privilegios del cargo.</p></article>
                    <article class="situation-card"><span class="situation-icon">🛑</span><strong>Presiones, amenazas o acoso</strong><p>Situaciones que afectan la dignidad de una persona o buscan forzar una actuación indebida.</p></article>
                </div>
            </div>

            <div class="ethics-section">
                <h3>Lo que establece el Código de Ética</h3>
                <p class="ethics-lead">La Ley N.° 27815 organiza las pautas de conducta en principios, deberes y prohibiciones éticas.</p>
                <div class="ethics-columns">
                    <article class="ethics-column principles">
                        <h4>Principios que orientan</h4>
                        <div class="ethics-tags">
                            <span class="ethics-tag">Respeto</span><span class="ethics-tag">Probidad</span><span class="ethics-tag">Eficiencia</span><span class="ethics-tag">Idoneidad</span><span class="ethics-tag">Veracidad</span><span class="ethics-tag">Lealtad y obediencia</span><span class="ethics-tag">Justicia y equidad</span><span class="ethics-tag">Lealtad al Estado de derecho</span>
                        </div>
                    </article>
                    <article class="ethics-column duties">
                        <h4>Deberes de consulta frecuente</h4>
                        <div class="ethics-tags">
                            <span class="ethics-tag">Transparencia</span><span class="ethics-tag">Discreción</span><span class="ethics-tag">Ejercicio adecuado del cargo</span><span class="ethics-tag">Uso adecuado de bienes del Estado</span><span class="ethics-tag">Responsabilidad</span>
                        </div>
                    </article>
                    <article class="ethics-column bans">
                        <h4>Prohibiciones que limitan</h4>
                        <div class="ethics-tags">
                            <span class="ethics-tag">Intereses en conflicto</span><span class="ethics-tag">Ventajas indebidas</span><span class="ethics-tag">Proselitismo político</span><span class="ethics-tag">Mal uso de información privilegiada</span><span class="ethics-tag">Presionar, amenazar o acosar</span>
                        </div>
                    </article>
                </div>
            </div>

            <div class="ethics-section">
                <h3>Ruta preventiva: ¿qué hago ante una duda?</h3>
                <div class="decision-route">
                    <div class="route-step">Identifica qué decisión, función o recurso público está involucrado.</div>
                    <div class="route-step">Reconoce si existe un interés particular, beneficio, presión o riesgo para la imparcialidad.</div>
                    <div class="route-step">Evita actuar apresuradamente y solicita orientación antes de tomar una decisión.</div>
                    <div class="route-step">Consulta a la UFII sin compartir información sensible en este chatbot.</div>
                </div>
            </div>

            <div class="ethics-section ethics-alert">
                <strong>Importante:</strong> INTEGRID-LN brinda orientación preventiva y general. No califica infracciones, no determina responsabilidades y no impone sanciones. Si deseas comunicar un posible acto de corrupción, utiliza el canal institucional correspondiente y evita describir aquí a las personas o las evidencias.
            </div>

            <div class="model-actions">
                <a class="back-button" href="?" target="_self">← Volver al inicio</a>
                <a class="source-button" href="https://www.gob.pe/institucion/jne/normas-legales/8133444-ley-del-codigo-de-etica-de-la-funcion-publica-ley-n-27815" target="_blank" rel="noopener noreferrer">Consultar Ley N.° 27815 ↗</a>
                <a class="source-button" href="https://www.gob.pe/institucion/saludpol/noticias/606119-guia-de-principios-deberes-y-prohibiciones-eticas-de-la-funcion-publica" target="_blank" rel="noopener noreferrer">Ver guía oficial ↗</a>
            </div>
        </section>
    </main>
    """
elif modulo_actual == "neutralidad":
    pagina = pagina_modulo_info(
        "🗳️",
        "Neutralidad electoral 2026",
        "Guía preventiva para el personal de DIRIS Lima Norte durante las elecciones regionales y municipales del 4 de octubre de 2026.",
        f"""
        <div class="info-section info-note blue"><strong>Designación institucional:</strong> la R. D. N.° D000173-2026-DG-DIRIS.LN designó al Oficial de Integridad Institucional de DIRIS Lima Norte como Oficial de Integridad Electoral, en adición a sus funciones. Esta ruta especial complementa las reglas de la PCM y los lineamientos del JNE.</div>
        <div class="info-section">
            <h3>Situaciones que requieren una consulta preventiva</h3>
            <div class="info-grid cols-3">
                <article class="info-card"><span class="info-card-icon">🏢</span><strong>Recursos de la entidad</strong><p>Dudas sobre uso de instalaciones, vehículos, tiempo de trabajo o canales institucionales con fines electorales.</p></article>
                <article class="info-card"><span class="info-card-icon">📣</span><strong>Comunicaciones públicas</strong><p>Revisar con las áreas competentes la publicidad estatal, difusión institucional e imagen de autoridades durante el proceso electoral.</p></article>
                <article class="info-card"><span class="info-card-icon">👥</span><strong>Conducta en funciones</strong><p>Prevenir actos de proselitismo, presiones o uso del cargo para favorecer una opción política.</p></article>
            </div>
        </div>
        <div class="info-section">
            <h3>Ruta de orientación y sustento</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Identifica la actividad institucional o decisión sobre la que existe duda antes de publicarla o ejecutarla.</div>
                <div class="process-step"><span>2</span>Consulta al Oficial de Integridad Electoral designado y a las áreas competentes; la guía no reemplaza una decisión institucional.</div>
                <div class="process-step"><span>3</span>Conserva, en el sistema institucional autorizado, la consulta, la orientación y el sustento o ajuste adoptado.</div>
                <div class="process-step"><span>4</span>Si corresponde comunicar una presunta infracción, utiliza el canal oficial competente; este chatbot no recibe reportes ni pruebas.</div>
            </div>
        </div>
        <div class="info-section info-note yellow"><strong>Para la presentación:</strong> son ejemplos de orientación, no casos reales ni una declaración de cumplimiento. Confirmar quién ocupa actualmente el cargo designado y el procedimiento interno antes de usar este módulo como canal formal.</div>
        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="{NORMA_NEUTRALIDAD_PCM}" target="_blank" rel="noopener noreferrer">PCM · R. SIP N.° 003-2026 ↗</a>
            <a class="source-button" href="{LINEAMIENTOS_JNE}" target="_blank" rel="noopener noreferrer">JNE · R. N.° 000021-2026 ↗</a>
            <a class="source-button" href="{RESOLUCIONES_DIRIS}" target="_blank" rel="noopener noreferrer">DIRIS · R. D. N.° D000173-2026 ↗</a>
            <a class="source-button" href="{ELECCIONES_2026}" target="_blank" rel="noopener noreferrer">Calendario ONPE ↗</a>
        </div>
        """,
    )
elif modulo_actual == "declaraciones":
    tipo_declaracion = st.query_params.get("tipo", "")
    rutas_declaracion = {
        "intereses": """<div class="info-section info-note blue"><strong>Ruta DJI · ejemplo:</strong> confirma con el área que administra los obligados si tu cargo o función está comprendido; ingresa al sistema oficial de la Contraloría; completa y firma en la oportunidad aplicable; conserva el cargo de presentación. Una orientación recibida por chat no demuestra que la DJI fue presentada.</div>""",
        "patrimonio": """<div class="info-section info-note blue"><strong>Ruta Bienes y Rentas · ejemplo:</strong> verifica la condición de obligado y la oportunidad con la unidad encargada; utiliza la plataforma oficial indicada, registra y firma la declaración y guarda la constancia correspondiente. No compartas información patrimonial en este chat.</div>""",
        "otras": """<div class="info-section info-note blue"><strong>Otros formatos:</strong> consulta el documento interno vigente y el área competente antes de completar una declaración de incompatibilidades, impedimentos o conflicto de intereses; INTEGRID-LN no inventa obligaciones adicionales.</div>""",
    }
    detalle_declaracion = rutas_declaracion.get(tipo_declaracion, "")
    pagina = pagina_modulo_info(
        "📄",
        "Declaraciones Juradas",
        "Guía para identificar el tipo de declaración, confirmar si corresponde presentarla y utilizar el canal oficial adecuado.",
        f"""
        <div class="info-section">
            <h3>¿Qué declaración necesitas revisar?</h3>
            <p class="info-lead">No todas las declaraciones aplican a todas las personas. La condición de obligado debe confirmarse según el cargo, la función y la comunicación del área responsable.</p>
            <div class="info-grid cols-3">
                <a class="guide-link" href="?modulo=declaraciones&tipo=intereses" target="_self"><span>🔗</span><strong>Declaración Jurada de Intereses</strong><small>Selecciona para ver un ejemplo de ruta de presentación.</small></a>
                <a class="guide-link" href="?modulo=declaraciones&tipo=patrimonio" target="_self"><span>🏠</span><strong>Ingresos, Bienes y Rentas</strong><small>Selecciona para ver la ruta aplicable a sujetos comprendidos.</small></a>
                <a class="guide-link" href="?modulo=declaraciones&tipo=otras" target="_self"><span>🗂️</span><strong>Otras declaraciones institucionales</strong><small>Selecciona para identificar el documento y responsable.</small></a>
            </div>
        </div>
        {detalle_declaracion}

        <div class="info-section">
            <h3>Ruta rápida para presentar correctamente</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Confirma con el área responsable si estás comprendido como obligado y qué declaración corresponde.</div>
                <div class="process-step"><span>2</span>Identifica el momento de presentación comunicado: inicio, actualización periódica o cese, según corresponda.</div>
                <div class="process-step"><span>3</span>Ingresa únicamente al sistema oficial indicado y revisa la información antes de firmar y enviar.</div>
                <div class="process-step"><span>4</span>Conserva la constancia y comunica oportunamente cualquier dificultad técnica al área responsable.</div>
            </div>
        </div>

        <div class="info-section info-note yellow"><strong>Importante:</strong> INTEGRID-LN no determina quién está obligado ni calcula plazos individuales. No ingreses en este chatbot datos patrimoniales, familiares, documentos de identidad, claves ni declaraciones completas.</div>

        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="https://www.gob.pe/7368-presentar-declaracion-jurada-de-intereses-dji" target="_blank" rel="noopener noreferrer">Declaración de Intereses ↗</a>
            <a class="source-button" href="https://www.gob.pe/13479-registrar-tu-declaracion-jurada-de-ingresos-y-de-bienes-y-rentas-ddjj-registrar-al-administrador-de-la-entidad-para-presentar-la-declaracion-jurada" target="_blank" rel="noopener noreferrer">Bienes y Rentas ↗</a>
        </div>
        """,
    )
elif modulo_actual == "denuncias":
    pagina = pagina_modulo_info(
        "📣",
        "Canal de Denuncias",
        "Información segura para comunicar un presunto acto de corrupción mediante la Plataforma Digital Única de Denuncias del Ciudadano.",
        """
        <div class="info-section">
            <h3>Antes de denunciar</h3>
            <p class="info-lead">Utiliza este módulo para conocer la ruta. Los hechos, nombres y evidencias deben registrarse en el canal oficial, nunca en el chatbot.</p>
            <div class="info-grid cols-3">
                <article class="info-card"><span class="info-card-icon">🧭</span><strong>Identifica la entidad</strong><p>Selecciona la entidad pública donde habría ocurrido el presunto acto de corrupción.</p></article>
                <article class="info-card"><span class="info-card-icon">📝</span><strong>Describe los hechos</strong><p>Indica fecha, lugar, motivo y una descripción clara. Adjunta sustento solo si lo tienes disponible.</p></article>
                <article class="info-card"><span class="info-card-icon">🔐</span><strong>Elige la modalidad</strong><p>La plataforma permite denunciar de forma anónima o identificada y entrega un código de seguimiento.</p></article>
            </div>
        </div>

        <div class="info-section">
            <h3>Ruta en la plataforma oficial</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Ingresa a la Plataforma Digital Única de Denuncias del Ciudadano.</div>
                <div class="process-step"><span>2</span>Selecciona la entidad y registra la información solicitada sobre los hechos.</div>
                <div class="process-step"><span>3</span>Elige si presentarás la denuncia de forma anónima o identificándote.</div>
                <div class="process-step"><span>4</span>Guarda el código asignado para consultar posteriormente el estado del trámite.</div>
            </div>
        </div>

        <div class="info-section info-note green"><strong>Medidas de protección:</strong> el Decreto Legislativo N.° 1327 contempla mecanismos de protección para denunciantes de buena fe. Su procedencia debe ser solicitada y evaluada conforme a la normativa aplicable.</div>
        <div class="info-section info-note red"><strong>No confundas los canales:</strong> una denuncia por presunta corrupción no es lo mismo que una queja por atención, un reclamo de servicio, una controversia laboral o una emergencia de salud.</div>

        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="https://www.gob.pe/21129-denunciar-un-presunto-acto-de-corrupcion" target="_blank" rel="noopener noreferrer">Presentar denuncia ↗</a>
            <a class="source-button" href="https://www.gob.pe/institucion/presidencia/normas-legales/2614867-1327" target="_blank" rel="noopener noreferrer">Medidas de protección ↗</a>
        </div>
        """,
    )
elif modulo_actual == "rvl":
    pagina = pagina_modulo_info(
        icono_rvl_html,
        "Registro de Visitas RVL",
        "Orientación para registrar y publicar información completa y oportuna sobre las visitas y agendas oficiales de la entidad, conforme a la directiva vigente.",
        f"""
        <div class="info-section">
            <h3>¿Para qué sirve?</h3>
            <p class="info-lead">El Registro de Visitas en Línea publica, en tiempo real, la información de las visitas que se producen en las entidades públicas. La directiva considera visitante a una persona natural o a quien representa a una persona jurídica, pública o privada, nacional o extranjera.</p>
            <div class="info-grid cols-3">
                <article class="info-card"><span class="info-card-icon">{icono_rvl_html}</span><strong>Persona visitante</strong><p>Identifica a la persona natural o al representante de una persona jurídica que ingresa a la entidad.</p></article>
                <article class="info-card"><span class="info-card-icon">🕒</span><strong>Registro en tiempo real</strong><p>La entrada y la salida se registran regularmente en tiempo real y, excepcionalmente, hasta las 23:59 del día de ingreso.</p></article>
                <article class="info-card"><span class="info-card-icon">📅</span><strong>Agendas oficiales</strong><p>Publican actividades oficiales de la alta dirección y determinadas gestiones de intereses atendidas fuera de la entidad.</p></article>
            </div>
        </div>

        <div class="info-section">
            <h3>Información que debe consignarse</h3>
            <div class="info-grid cols-3">
                <article class="info-card"><strong>Identificación y tipo</strong><p>Fecha; nombres, apellidos y documento de identidad; y tipo de persona: natural o jurídica.</p></article>
                <article class="info-card"><strong>Destino y motivo</strong><p>Motivo de visita, persona visitada o servidor responsable, cargo, unidad de organización y lugar específico.</p></article>
                <article class="info-card"><strong>Control de permanencia</strong><p>Hora de ingreso y hora de salida. La visita comienza con el ingreso y culmina con la salida.</p></article>
            </div>
        </div>

        <div class="info-section">
            <h3>Verificación operativa básica</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Corrobora la identidad del visitante con un documento válido con fotografía.</div>
                <div class="process-step"><span>2</span>Registra el tipo de persona, el motivo, el destino, la persona visitada y el lugar específico.</div>
                <div class="process-step"><span>3</span>Confirma el ingreso y revisa que todos los datos obligatorios sean correctos y completos.</div>
                <div class="process-step"><span>4</span>Al culminar la visita, registra la hora de salida. Si hubo una omisión, aplica la ruta de registro extemporáneo.</div>
            </div>
        </div>

        <div class="info-section info-note blue"><strong>Norma vigente:</strong> la Directiva N.° 003-2026-PCM/SIP, aprobada mediante Resolución N.° 008-2026-PCM/SIP del 23 de julio de 2026, establece las disposiciones para el uso del Registro de Visitas en Línea y del Registro de Agendas Oficiales.</div>
        <div class="info-section info-note yellow"><strong>Importante:</strong> no todo ingreso constituye una visita registrable. La directiva contempla excepciones, por ejemplo, determinados servicios de apoyo, trámites regulares en espacios de atención al público, menores de edad y otros supuestos específicos. Ante una duda operativa, consulta a la UFII.</div>

        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="https://visitas.servicios.gob.pe/" target="_blank" rel="noopener noreferrer">Abrir Registro de Visitas ↗</a>
            <a class="source-button" href="https://www.gob.pe/institucion/pcm/normas-legales/8417717-008-2026-pcm-sip" target="_blank" rel="noopener noreferrer">Directiva vigente ↗</a>
        </div>
        """,
    )
elif modulo_actual == "guias":
    pagina = pagina_modulo_info(
        "✅",
        "Checklists y Guías",
        "Herramientas de consulta rápida para verificar acciones preventivas antes de continuar con un trámite o solicitar orientación.",
        f"""
        <div class="info-section">
            <h3>Elige la guía que necesitas</h3>
            <p class="info-lead">Estas ayudas resumen verificaciones básicas. Puedes abrir el módulo relacionado para revisar la explicación y las fuentes oficiales.</p>
            <div class="info-grid cols-3">
                <a class="guide-link" href="?modulo=etica" target="_self"><span>⚖️</span><strong>Antes de una decisión ética</strong><small>Identifica intereses, beneficios, presiones, recursos públicos y posibles riesgos.</small></a>
                <a class="guide-link" href="?modulo=declaraciones" target="_self"><span>📄</span><strong>Antes de presentar una declaración</strong><small>Confirma obligación, tipo, momento, sistema oficial y constancia de presentación.</small></a>
                <a class="guide-link" href="?modulo=denuncias" target="_self"><span>📣</span><strong>Antes de presentar una denuncia</strong><small>Identifica entidad, fecha, lugar, descripción, modalidad y código de seguimiento.</small></a>
                <a class="guide-link" href="?modulo=rvl" target="_self"><span class="guide-rvl-icon">{icono_rvl_html}</span><strong>Antes de cerrar una visita</strong><small>Verifica identidad, destino, motivo, información completa y registro de salida.</small></a>
                <a class="guide-link" href="?modulo=derivacion" target="_self"><span>💼</span><strong>Antes de derivar a la UFII</strong><small>Define el tema, la orientación requerida y el canal correcto sin exponer datos sensibles.</small></a>
                <a class="guide-link" href="?modulo=modelo" target="_self"><span>🛡️</span><strong>Modelo de Integridad</strong><small>Consulta nueve componentes, tres procesos de implementación y cinco etapas de evaluación.</small></a>
                <a class="guide-link" href="?modulo=transparencia" target="_self"><span>🔎</span><strong>Antes de revisar el PTE</strong><small>Selecciona rubro y periodo, conserva enlace y fecha, coordina observaciones con el responsable.</small></a>
                <a class="guide-link" href="?modulo=seguimiento" target="_self"><span>📊</span><strong>Antes de reportar una acción</strong><small>Vincula componente, Programa anual, responsable, fecha y medio de verificación.</small></a>
            </div>
        </div>

        <div class="info-section">
            <h3>Checklist universal antes de enviar</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>¿Identifiqué correctamente el tema y el canal que corresponde?</div>
                <div class="process-step"><span>2</span>¿Evité colocar datos personales o sensibles en espacios no autorizados?</div>
                <div class="process-step"><span>3</span>¿Revisé la información y utilicé una fuente o sistema oficial?</div>
                <div class="process-step"><span>4</span>¿Guardé la constancia, código o evidencia de la acción realizada?</div>
            </div>
        </div>

        <div class="info-section info-note yellow"><strong>Versión demostrativa:</strong> estos checklists no reemplazan formatos, directivas, manuales ni instrucciones internas. Los materiales descargables serán incorporados después de la validación de la UFII.</div>
        <div class="model-actions"><a class="back-button" href="?" target="_self">← Volver al inicio</a></div>
        """,
    )
elif modulo_actual == "derivacion":
    pagina = pagina_modulo_info(
        "💼",
        "Derivar a la UFII",
        "Ruta para identificar cuándo corresponde solicitar orientación o asistencia técnica a la Unidad Funcional de Integridad Institucional.",
        """
        <div class="info-section">
            <h3>¿Cuándo corresponde consultar a la UFII?</h3>
            <div class="info-grid cols-4">
                <article class="info-card"><span class="info-card-icon">⚖️</span><strong>Duda ética preventiva</strong><p>Cuando necesitas orientación antes de tomar una decisión vinculada con tus funciones.</p></article>
                <article class="info-card"><span class="info-card-icon">🛡️</span><strong>Modelo de Integridad</strong><p>Para asistencia sobre componentes, actividades, evidencias o responsabilidades de implementación.</p></article>
                <article class="info-card"><span class="info-card-icon">⚠️</span><strong>Riesgos de integridad</strong><p>Cuando identificas una situación o proceso vulnerable que requiere una medida preventiva.</p></article>
                <article class="info-card"><span class="info-card-icon">🧭</span><strong>Canal institucional</strong><p>Cuando no sabes qué oficina o mecanismo corresponde para atender correctamente tu situación.</p></article>
            </div>
        </div>

        <div class="info-section">
            <h3>La UFII orienta, pero no reemplaza a otras instancias</h3>
            <div class="info-grid cols-2">
                <article class="info-card"><span class="info-card-icon">✅</span><strong>Sí corresponde</strong><ul class="info-list"><li>Orientación preventiva en integridad y ética pública.</li><li>Asistencia para implementar el Modelo de Integridad.</li><li>Orientación sobre canales de denuncia y medidas preventivas.</li><li>Articulación y seguimiento de acciones de integridad.</li></ul></article>
                <article class="info-card"><span class="info-card-icon">🚫</span><strong>No corresponde</strong><ul class="info-list"><li>Determinar responsabilidades o imponer sanciones.</li><li>Resolver controversias laborales o administrativas.</li><li>Reemplazar a Recursos Humanos, Asesoría Jurídica, Secretaría Técnica u OCI.</li><li>Recibir datos sensibles mediante este chatbot.</li></ul></article>
            </div>
        </div>

        <div class="info-section">
            <h3>Ruta de derivación</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Define en una frase el tema y la orientación que necesitas.</div>
                <div class="process-step"><span>2</span>Evita incluir inicialmente nombres, DNI, historias clínicas, evidencias o información reservada.</div>
                <div class="process-step"><span>3</span>Utiliza el correo o anexo institucional confirmado por la UFII.</div>
                <div class="process-step"><span>4</span>Sigue las indicaciones recibidas y conserva la constancia de la consulta o derivación.</div>
            </div>
        </div>

        <div class="info-section contact-box">
            <div class="contact-item"><span>Correo configurado en el prototipo</span><strong>integridad@dirisln.gob.pe</strong></div>
            <div class="contact-item"><span>Anexo configurado en el prototipo</span><strong>2005</strong></div>
        </div>
        <div class="info-section info-note yellow"><strong>Validación requerida:</strong> la coordinadora de la UFII debe confirmar el correo, el anexo, los horarios y la ruta interna antes de presentar esta versión como canal institucional definitivo.</div>

        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="https://www.gob.pe/institucion/pcm/normas-legales/7644478-002-2026-pcm-sip" target="_blank" rel="noopener noreferrer">Directiva del Modelo de Integridad ↗</a>
        </div>
        """,
    )
elif modulo_actual == "componente":
    try:
        numero_componente = int(st.query_params.get("n", "0"))
    except ValueError:
        numero_componente = 0
    datos_componente = COMPONENTES.get(numero_componente)
    if datos_componente:
        pasos_componente = "".join(
            f'<div class="process-step"><span>{indice}</span>{html.escape(accion)}</div>'
            for indice, accion in enumerate(datos_componente["acciones"], 1)
        )
        pagina = pagina_modulo_info(
            "🛡️",
            f'Componente {numero_componente} · {html.escape(datos_componente["titulo"])}',
            html.escape(datos_componente["resumen"]),
            f"""
            <div class="info-section">
                <h3>¿Cómo se aplicaría?</h3>
                <div class="process-grid">{pasos_componente}</div>
            </div>
            <div class="info-section info-note blue"><strong>¿Quién interviene?</strong> {html.escape(datos_componente["roles"])}</div>
            <div class="info-section info-note green"><strong>Ejemplo de medio de verificación:</strong> {html.escape(datos_componente["ejemplo"])}</div>
            <div class="info-section info-note yellow"><strong>Alcance de esta demostración:</strong> las acciones describen una ruta de trabajo, no acreditan cumplimiento ni sustituyen los criterios específicos de la guía de evaluación y el Programa de Integridad aprobado de DIRIS.</div>
            <div class="model-actions">
                <a class="back-button" href="?modulo=modelo" target="_self">← Ver los nueve componentes</a>
                <a class="source-button" href="?modulo={datos_componente['ruta']}" target="_self">Abrir ruta relacionada →</a>
                <a class="source-button" href="{DIRECTIVA_MODELO}" target="_blank" rel="noopener noreferrer">Directiva N.° 001-2026 ↗</a>
            </div>
            """,
        )
    else:
        pagina = pagina_modulo_info("🛡️", "Componente no encontrado", "Selecciona una de las nueve tarjetas del Modelo.", '<a class="back-button" href="?modulo=modelo" target="_self">Ver componentes</a>')
elif modulo_actual == "transparencia":
    pagina = pagina_modulo_info(
        "🔎",
        "Transparencia y Portal de Transparencia Estándar",
        "Componente 4 del Modelo: información pública, acceso a la información, visitas y agendas, datos abiertos y rendición de cuentas.",
        f"""
        <div class="info-section">
            <h3>Consulta el PTE oficial de DIRIS Lima Norte</h3>
            <p class="info-lead">Puedes revisar información de la entidad por rubro: datos generales, planeamiento, presupuesto, personal, contrataciones, actividades oficiales, acceso a la información y registro de visitas.</p>
            <a class="source-button" href="{PTE_DIRIS}" target="_blank" rel="noopener noreferrer">Abrir Portal de Transparencia de DIRIS Lima Norte ↗</a>
        </div>
        <div class="info-section">
            <h3>Seis tareas del componente 4</h3>
            <div class="info-grid cols-3">
                <article class="info-card"><strong>4.1 · Actualizar el PTE</strong><p>El funcionario responsable publica la información; la UFII verifica periódicamente la actualización y coordina los hallazgos.</p></article>
                <article class="info-card"><strong>4.2 · Solicitudes de información</strong><p>Comprobar que exista responsable designado y se atiendan las solicitudes conforme a la normativa aplicable.</p></article>
                <article class="info-card"><strong>4.3 · Registro de Visitas</strong><p>Verificar que el RVL mantenga datos completos, precisos y oportunos.</p></article>
                <article class="info-card"><strong>4.4 · Agendas oficiales</strong><p>Revisar la actualización del registro de actividades oficiales de la Alta Dirección.</p></article>
                <article class="info-card"><strong>4.5 · Datos abiertos</strong><p>Coordinar con gobierno y transformación digital la apertura de conjuntos de datos pertinentes.</p></article>
                <article class="info-card"><strong>4.6 · Rendición de cuentas</strong><p>Conocer los mecanismos institucionales de información pública y participación.</p></article>
            </div>
        </div>
        <div class="info-section">
            <h3>Demostración de verificación del PTE</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Seleccionar rubro, periodo y criterio de revisión conforme a los lineamientos aplicables.</div>
                <div class="process-step"><span>2</span>Registrar URL oficial, fecha de consulta y resultado de la verificación.</div>
                <div class="process-step"><span>3</span>Comunicar el hallazgo al responsable del PTE y documentar su respuesta.</div>
                <div class="process-step"><span>4</span>Volver a verificar y conservar la ficha y el enlace como sustento.</div>
            </div>
        </div>
        <div class="info-section info-note yellow"><strong>Competencias separadas:</strong> INTEGRID-LN puede orientar y facilitar el seguimiento; no publica ni modifica el PTE. Los responsables designados y los criterios de verificación deben confirmarse con los documentos institucionales y los lineamientos de transparencia.</div>
        <div class="model-actions">
            <a class="back-button" href="?" target="_self">← Volver al inicio</a>
            <a class="source-button" href="?panel=evidencias" target="_self">Ver seguimiento simulado →</a>
            <a class="source-button" href="{LINEAMIENTO_PTE}" target="_blank" rel="noopener noreferrer">Lineamiento PTE · R. D. N.° 066-2025 ↗</a>
            <a class="source-button" href="{DIRECTIVA_MODELO}" target="_blank" rel="noopener noreferrer">Directiva: tareas 4.1 a 4.6 ↗</a>
        </div>
        """,
    )
elif modulo_actual == "marco":
    pagina = pagina_modulo_info(
        "📚",
        "Base legal y ruta de implementación",
        "Normas de implementación, evaluación y materias específicas que orientan esta demostración; sus obligaciones corresponden a la entidad, no al prototipo.",
        f"""
        <div class="info-section">
            <h3>Marco principal</h3>
            <div class="legal-cards">
                <article class="legal-card"><strong>D. S. N.° 148-2024-PCM</strong><p>Aprueba el Modelo de Integridad, sus principios, componentes y criterios generales.</p><a href="{NORMA_MODELO}" target="_blank" rel="noopener noreferrer">Consultar norma ↗</a></article>
                <article class="legal-card"><strong>Directiva N.° 001-2026-PCM/SIP</strong><p>Implementación del Modelo; aprobada por la Resolución de Secretaría N.° 002-2026-PCM/SIP. Desarrolla tres procesos, tareas, roles y anexos.</p><a href="{DIRECTIVA_MODELO}" target="_blank" rel="noopener noreferrer">Consultar directiva ↗</a></article>
                <article class="legal-card"><strong>Directiva N.° 001-2025-PCM/SIP</strong><p>Evaluación de la implementación para determinar el ICP; aprobada por Resolución N.° 009-2025 y modificada por Resolución N.° 007-2026.</p><a href="{NORMA_EVALUACION}" target="_blank" rel="noopener noreferrer">Evaluación ↗</a> · <a href="{MODIFICACION_EVALUACION}" target="_blank" rel="noopener noreferrer">Modificación ↗</a></article>
                <article class="legal-card"><strong>Guía de evaluación de Etapa 2 (V2)</strong><p>Instrumento de preguntas y medios de verificación para institucionalización, aprobado por Resolución N.° 004-2025-PCM/SIP; hay precisiones de la Resolución N.° 006-2026.</p><a href="https://www.gob.pe/institucion/pcm/normas-legales/6594541-004-2025-pcm-sip" target="_blank" rel="noopener noreferrer">Ver guía ↗</a> · <a href="https://www.gob.pe/institucion/pcm/normas-legales/8094545-006-2026-pcm-sip" target="_blank" rel="noopener noreferrer">Precisiones ↗</a></article>
            </div>
        </div>
        <div class="info-section">
            <h3>Normas por tema</h3>
            <div class="legal-cards">
                <article class="legal-card"><strong>Ética · Ley N.° 27815</strong><p>Principios, deberes y prohibiciones de la función pública.</p><a href="https://www.gob.pe/institucion/jne/normas-legales/8133444-ley-del-codigo-de-etica-de-la-funcion-publica-ley-n-27815" target="_blank" rel="noopener noreferrer">Consultar ley ↗</a></article>
                <article class="legal-card"><strong>Declaración de intereses · Ley N.° 31227</strong><p>Competencias de la Contraloría para recibir y controlar declaraciones juradas de intereses de sujetos comprendidos.</p><a href="https://www.gob.pe/7368-presentar-declaracion-jurada-de-intereses-dji" target="_blank" rel="noopener noreferrer">Ruta oficial DJI ↗</a></article>
                <article class="legal-card"><strong>Denuncias · D. Leg. N.° 1327</strong><p>Medidas de protección y tratamiento de denuncias por presunta corrupción.</p><a href="https://www.gob.pe/21129-denunciar-un-presunto-acto-de-corrupcion" target="_blank" rel="noopener noreferrer">Canal oficial ↗</a></article>
                <article class="legal-card"><strong>RVL y agendas · Directiva N.° 003-2026-PCM/SIP</strong><p>Uso del RVL y del Registro de Agendas Oficiales; aprobada por Resolución N.° 008-2026-PCM/SIP.</p><a href="https://www.gob.pe/institucion/pcm/normas-legales/8417717-008-2026-pcm-sip" target="_blank" rel="noopener noreferrer">Consultar directiva ↗</a></article>
                <article class="legal-card"><strong>Transparencia · Ley N.° 27806 y R. D. N.° 066-2025-JUS/DGTAIPD</strong><p>Acceso a la información pública y lineamiento específico para implementar y actualizar el PTE.</p><a href="{PTE_DIRIS}" target="_blank" rel="noopener noreferrer">PTE de DIRIS ↗</a> · <a href="{LINEAMIENTO_PTE}" target="_blank" rel="noopener noreferrer">Lineamiento ↗</a></article>
                <article class="legal-card"><strong>Neutralidad electoral 2026 · PCM y JNE</strong><p>La R. SIP N.° 003-2026-PCM/SIP precisa el rol adicional de Oficial de Integridad Electoral; la R. N.° 000021-2026-P/JNE establece lineamientos para su designación y funciones.</p><a href="{NORMA_NEUTRALIDAD_PCM}" target="_blank" rel="noopener noreferrer">PCM ↗</a> · <a href="{LINEAMIENTOS_JNE}" target="_blank" rel="noopener noreferrer">JNE ↗</a></article>
                <article class="legal-card"><strong>Evaluación ICP 2026 · Resolución N.° 009-2026-PCM/SIP</strong><p>Cronograma del proceso de evaluación; se consulta para coordinar las fechas aplicables, sin atribuir una etapa específica a DIRIS desde esta maqueta.</p><a href="https://www.gob.pe/institucion/pcm/normas-legales/8518085-009-2026-pcm-sip" target="_blank" rel="noopener noreferrer">Ver cronograma ↗</a></article>
            </div>
        </div>
        <div class="info-section">
            <h3>Documentos propios de DIRIS Lima Norte</h3>
            <div class="legal-cards">
                <article class="legal-card"><strong>Programa de Integridad 2026 · R. D. N.° D000352-2026</strong><p>Documento técnico aprobado para el año fiscal 2026. Su matriz vigente debe servir de entrada al seguimiento operativo.</p><a href="{PROGRAMA_DIRIS_2026}" target="_blank" rel="noopener noreferrer">Consultar programa ↗</a></article>
                <article class="legal-card"><strong>Organización interna · R. D. N.° D000822-2025</strong><p>Actualiza la organización interna funcional; revisar conjuntamente las modificaciones posteriores, entre ellas la R. D. N.° D000218-2026, al identificar responsables.</p><a href="https://www.gob.pe/institucion/dirislimanorte/normas-legales/7172278-d000822-2025-dg-diris-ln" target="_blank" rel="noopener noreferrer">Organización ↗</a> · <a href="https://www.gob.pe/institucion/dirislimanorte/normas-legales/7781453-d000218-2026-dg-diris-ln" target="_blank" rel="noopener noreferrer">Modificación ↗</a></article>
                <article class="legal-card"><strong>Integridad electoral · R. D. N.° D000173-2026</strong><p>Designa al Oficial de Integridad Institucional como Oficial de Integridad Electoral de DIRIS Lima Norte, en adición a sus funciones. Confirmar la persona que ejerce el cargo actualmente.</p><a href="{RESOLUCIONES_DIRIS}" target="_blank" rel="noopener noreferrer">Ver resoluciones DIRIS ↗</a></article>
            </div>
        </div>
        <div class="info-section info-note blue"><strong>Uso institucional:</strong> relacionar cada tarea con el Programa de Integridad vigente de DIRIS, el área ejecutora, su evidencia oficial y la pregunta aplicable de la guía de evaluación. Esta página orienta la presentación y no asigna puntuaciones del ICP.</div>
        <div class="model-actions"><a class="back-button" href="?" target="_self">← Volver al inicio</a><a class="source-button" href="?modulo=modelo" target="_self">Explorar los nueve componentes →</a></div>
        """,
    )
elif modulo_actual == "seguimiento":
    pagina = pagina_modulo_info(
        "📊",
        "Seguimiento del Modelo de Integridad",
        "Una ruta de trabajo desde el Programa de Integridad anual hasta informes verificables; por ahora todos los datos del panel son ficticios.",
        """
        <div class="info-section">
            <h3>De actividad a medio de verificación</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Tomar una acción del Programa de Integridad aprobado y vincularla con su componente y periodo.</div>
                <div class="process-step"><span>2</span>Identificar el área ejecutora, responsable, meta y criterio de revisión.</div>
                <div class="process-step"><span>3</span>Registrar resultado, observación y documento o enlace de sustento, con fecha.</div>
                <div class="process-step"><span>4</span>Consolidar, comunicar brechas y generar un informe para las autoridades competentes.</div>
            </div>
        </div>
        <div class="info-section info-note green"><strong>Indicadores propuestos:</strong> tareas verificadas / tareas programadas; observaciones atendidas / observaciones comunicadas; acciones sustentadas / acciones ejecutadas. Para calcularlos se requieren fuentes institucionales y definiciones aprobadas.</div>
        <div class="info-section info-note yellow"><strong>Panel actual:</strong> las tarjetas del inicio muestran cifras de maqueta y no guardan registros. La información real solo podría incorporarse con autenticación, roles, registro persistente y validación de las unidades competentes.</div>
        <div class="model-actions"><a class="back-button" href="?" target="_self">← Volver al inicio</a><a class="source-button" href="?panel=evidencias" target="_self">Ver reporte demostrativo →</a><a class="source-button" href="?modulo=marco" target="_self">Consultar normas →</a></div>
        """,
    )
if modulo_actual in modulos:
    st.html(pagina)
    st.stop()

if panel_vista_inicio in {"consultas", "orientaciones", "alertas", "derivaciones", "evidencias"}:
    st.html(pagina_panel_enfocado(panel_vista_inicio))
    st.stop()

cabecera_inicio = pagina_inicio.split('<section class="hero panel">', 1)[0] + "</main>"
resto_inicio = '<main class="integri-shell"><aside class="notice panel">' + pagina_inicio.split('<aside class="notice panel">', 1)[1]

st.html(cabecera_inicio)

columna_robot, columna_chat = st.columns([1, 2], gap="medium")

with columna_robot:
    with st.container(border=True):
        ruta_robot = Path(__file__).parent / "assets" / "integri_robot.png"
        if ruta_robot.exists():
            st.image(ruta_robot, width="stretch")
        else:
            st.html('<div class="robot-fallback" aria-label="Mascota no disponible">🤖</div>')
        st.markdown("<div style='text-align:center;color:#0a2459;font-weight:800;'>INTEGRID-LN</div>", unsafe_allow_html=True)
        st.caption("Asistente virtual de orientación preventiva")
        st.html(
            """
            <a class="model-access" href="?modulo=modelo" target="_self">
                <span class="model-shield">🛡️</span>
                <span><strong>Modelo de Integridad vigente</strong><small>Conoce los 9 componentes</small></span>
                <span class="model-arrow">›</span>
            </a>
            """
        )

with columna_chat:
    saludo_inicial = """
    <div class="chat-message bot">
        <div class="chat-label">INTEGRID-LN</div>
        <div class="chat-bubble">¡Hola! ¿En qué puedo ayudarte?</div>
    </div>
    """
    st.html(
        f"""
        <section class="embedded-chat-box">
            <div class="embedded-chat-heading">
                <div class="mini-avatar">🤖</div>
                <div><strong>INTEGRID-LN</strong><small>Activo · Respuestas guiadas sin API</small></div>
            </div>
            <div class="chat-history">{historial_invertido_html}{saludo_inicial}</div>
        </section>
        """
    )

    with st.form("formulario_chat", clear_on_submit=True, border=False):
        columna_pregunta, columna_enviar = st.columns([5, 1])
        with columna_pregunta:
            pregunta = st.text_input(
                "Mensaje para INTEGRID-LN",
                placeholder="Escribe tu duda...",
                label_visibility="collapsed",
            )
        with columna_enviar:
            enviar = st.form_submit_button("Enviar", width="stretch")

    if enviar and pregunta.strip():
        pregunta_limpia = pregunta.strip()
        st.session_state.historial_chat.append(("usuario", pregunta_limpia))
        st.session_state.historial_chat.append(("integri", respuesta_guiada(pregunta_limpia)))
        st.rerun()

    columna_seguridad, columna_borrar = st.columns([4, 1])
    with columna_seguridad:
        st.caption("🔒 No ingreses nombres, DNI ni datos sensibles.")
    with columna_borrar:
        if st.session_state.historial_chat and st.button("Limpiar", width="stretch"):
            st.session_state.historial_chat = []
            st.rerun()

st.html(resto_inicio)
