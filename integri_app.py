# VERSION INTEGRI: RVL_ICONO_HTML_CSS_COMPATIBLE - 31/07/2026
import base64
import html
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="INTEGRI | Asistente de Integridad Institucional",
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
    f'<img class="robot" src="data:image/png;base64,{robot}" alt="Mascota INTEGRI">'
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
    if any(p in consulta for p in ("hola", "buenos días", "buenos dias", "buenas tardes", "ayuda", "qué puedes", "que puedes")):
        return (
            "¡Hola! Soy INTEGRI. Puedo orientarte sobre ética pública, Modelo de Integridad, "
            "declaraciones juradas, canal de denuncias, Registro de Visitas RVL, checklists y derivación a la UFII."
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
            "desde el botón «Consultas de Ética». INTEGRI brinda orientación preventiva, pero no califica infracciones ni determina sanciones."
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
        "ética, Modelo de Integridad, declaraciones juradas, denuncias, RVL, guías o derivación a la UFII."
    )


if "historial_chat" not in st.session_state:
    st.session_state.historial_chat = []
if "ultima_consulta" not in st.session_state:
    st.session_state.ultima_consulta = ""

mensajes = []
for autor, mensaje in st.session_state.historial_chat:
    clase = "user" if autor == "usuario" else "bot"
    etiqueta = "Tú" if autor == "usuario" else "INTEGRI"
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
    font-size: clamp(3.9rem, 8vw, 6.3rem);
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
    padding: .78rem 1rem;
    color: white;
    text-align: center;
    font-size: clamp(1rem, 2.2vw, 1.35rem);
    font-weight: 700;
    background: linear-gradient(135deg, #073b85, #0664b7 58%, #063c87);
    border: 1px solid #042f72;
    border-radius: 9px;
    box-shadow: 0 7px 14px rgba(1,52,125,.18), inset 0 1px rgba(255,255,255,.25);
}

.topic-bar span { padding: 0 .8rem; white-space: nowrap; }
.topic-bar span + span { border-left: 2px solid rgba(255,255,255,.85); }

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

.footer-nav {
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
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
.stage-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:.75rem; }
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
    .topic-bar { line-height:1.8; padding:.55rem .3rem; }
    .topic-bar span { padding:0 .35rem; }
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
    .source-grid { grid-template-columns:1fr; }
    .admin-header { align-items:flex-start; }
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
    .situation-grid, .decision-route { grid-template-columns:1fr; }
    .info-grid.cols-2, .info-grid.cols-3, .info-grid.cols-4, .process-grid, .contact-box { grid-template-columns:1fr; }
}
</style>
""",
    unsafe_allow_html=True,
)


pagina = f"""
<main class="integri-shell">
    <header class="brand">
        <h1>INTEGRI</h1>
        <div class="brand-line"></div>
        <h2>Asistente de Integridad Institucional</h2>
        <p>Unidad Funcional de Integridad Institucional (UFII)</p>
    </header>

    <nav class="topic-bar" aria-label="Áreas de orientación">
        <span>Orientación Normativa</span><span>Canal de Denuncias</span><span>Registro de Visitas</span>
    </nav>

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
        <span class="notice-i">i</span><span>INTEGRI orienta, no decide ni sanciona</span>
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
        </div>
    </section>

    <footer class="footer-nav">
        <div>💬 &nbsp; Ayuda</div>
        <div>🔎 &nbsp; Seguimiento de consulta</div>
        <a href="?modulo=panel_admin&vista=resumen" target="_self">🔐 &nbsp; Acceso administrativo (demo)</a>
    </footer>
</main>
"""

pagina_inicio = pagina

modulos = {
    "modelo": ("🛡️", "Modelo de Integridad", "Espacio para orientar sobre los componentes y acciones preventivas del Modelo de Integridad."),
    "etica": ("⚖️", "Consultas de Ética", "Espacio para brindar orientación preventiva ante dudas y dilemas éticos."),
    "declaraciones": ("📄", "Declaraciones Juradas", "Espacio para orientar sobre obligaciones, plazos y canales aplicables."),
    "denuncias": ("📣", "Canal de Denuncias", "Espacio para informar sobre el canal oficial y las medidas de protección."),
    "rvl": (icono_rvl_html, "Registro de Visitas RVL", "Espacio de orientación operativa sobre el Registro de Visitas en Línea."),
    "guias": ("✅", "Checklists y Guías", "Repositorio de materiales preventivos y herramientas de consulta rápida."),
    "derivacion": ("💼", "Derivar a UFII", "Espacio para identificar cuándo corresponde solicitar orientación directa a la UFII."),
    "panel_admin": ("🔐", "Panel administrativo", "Vista demostrativa de seguimiento y control para usuarios autorizados."),
}


def pagina_modulo_info(simbolo: str, titulo: str, descripcion: str, contenido: str) -> str:
    """Construye una pantalla informativa manteniendo la identidad visual de INTEGRI."""
    return f"""
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRI</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <nav class="topic-bar" aria-label="Áreas de orientación">
            <span>Orientación Normativa</span><span>Canal de Denuncias</span><span>Registro de Visitas</span>
        </nav>
        <section class="info-page panel">
            <div class="info-intro">
                <div class="info-icon">{simbolo}</div>
                <div><h2>{titulo}</h2><p>{descripcion}</p></div>
            </div>
            {contenido}
        </section>
    </main>
    """


def pagina_panel_control(vista: str) -> str:
    """Construye un panel administrativo interactivo con datos ficticios."""
    vistas_validas = {"resumen", "consultas", "alertas", "derivaciones", "fuentes"}
    vista = vista if vista in vistas_validas else "resumen"

    if vista == "consultas":
        detalle = """
        <section class="admin-section">
            <h3>Consultas registradas - ejemplo mensual</h3>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Código</th><th>Fecha</th><th>Canal</th><th>Tema clasificado</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>INT-2026-001</td><td>03/07/2026</td><td>Chat web</td><td>Conflicto de intereses</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-2026-002</td><td>05/07/2026</td><td>Chat web</td><td>Declaración jurada</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-2026-003</td><td>08/07/2026</td><td>Correo</td><td>Modelo de Integridad</td><td><span class="status-pill sent">Derivada</span></td></tr>
                    <tr><td>INT-2026-004</td><td>11/07/2026</td><td>Chat web</td><td>Registro de Visitas</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-2026-005</td><td>15/07/2026</td><td>Anexo</td><td>Canal de denuncias</td><td><span class="status-pill wait">En seguimiento</span></td></tr>
                    <tr><td>INT-2026-006</td><td>19/07/2026</td><td>Chat web</td><td>Regalos o ventajas</td><td><span class="status-pill ok">Orientada</span></td></tr>
                </tbody>
            </table></div>
        </section>
        """
    elif vista == "alertas":
        detalle = """
        <section class="admin-section">
            <h3>Alertas preventivas identificadas - ejemplos</h3>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Alerta</th><th>Situación general</th><th>Acción preventiva</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>AL-001</td><td>Posible conflicto de intereses</td><td>Orientación previa a la decisión</td><td><span class="status-pill ok">Atendida</span></td></tr>
                    <tr><td>AL-002</td><td>Ofrecimiento de obsequio</td><td>Recordatorio de prohibiciones y canal interno</td><td><span class="status-pill ok">Atendida</span></td></tr>
                    <tr><td>AL-003</td><td>Registro RVL incompleto</td><td>Verificación de datos y registro de salida</td><td><span class="status-pill wait">En seguimiento</span></td></tr>
                    <tr><td>AL-004</td><td>Consulta sobre información reservada</td><td>Derivación al responsable competente</td><td><span class="status-pill sent">Derivada</span></td></tr>
                </tbody>
            </table></div>
        </section>
        """
    elif vista == "derivaciones":
        detalle = """
        <section class="admin-section">
            <h3>Seguimiento de derivaciones a la UFII - ejemplos</h3>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Código</th><th>Tema</th><th>Fecha de derivación</th><th>Responsable</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>DER-001</td><td>Asistencia sobre componente del Modelo</td><td>08/07/2026</td><td>UFII</td><td><span class="status-pill ok">Cerrada</span></td></tr>
                    <tr><td>DER-002</td><td>Orientación ética especializada</td><td>12/07/2026</td><td>UFII</td><td><span class="status-pill wait">En revisión</span></td></tr>
                    <tr><td>DER-003</td><td>Incidencia operativa RVL</td><td>18/07/2026</td><td>UFII / RVL</td><td><span class="status-pill sent">Derivada</span></td></tr>
                    <tr><td>DER-004</td><td>Consulta sobre canal competente</td><td>24/07/2026</td><td>UFII</td><td><span class="status-pill ok">Cerrada</span></td></tr>
                </tbody>
            </table></div>
        </section>
        """
    elif vista == "fuentes":
        detalle = """
        <section class="admin-section">
            <h3>¿De dónde saldrían los datos reales?</h3>
            <div class="source-grid">
                <article class="source-card"><strong>1. Chat y formularios INTEGRI</strong><p>Generarían código, fecha, canal, tema consultado y respuesta brindada, sin exponer datos sensibles en el tablero.</p></article>
                <article class="source-card"><strong>2. Registro de atención UFII</strong><p>Incorporaría responsable, estado, fecha de derivación, acciones efectuadas y fecha de cierre.</p></article>
                <article class="source-card"><strong>3. Archivos institucionales</strong><p>Podrían integrarse mediante Excel/CSV, una base de datos autorizada o conexiones con sistemas institucionales.</p></article>
            </div>
        </section>
        <section class="admin-section">
            <h3>Estructura propuesta para la base de seguimiento</h3>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Campo</th><th>Ejemplo ficticio</th><th>Uso en el panel</th></tr></thead>
                <tbody>
                    <tr><td>codigo_consulta</td><td>INT-2026-001</td><td>Trazabilidad sin mostrar identidad</td></tr>
                    <tr><td>fecha_hora</td><td>03/07/2026 10:25</td><td>Seguimiento por periodo</td></tr>
                    <tr><td>canal</td><td>Chat web</td><td>Distribución por canal</td></tr>
                    <tr><td>tema</td><td>Conflicto de intereses</td><td>Demanda temática</td></tr>
                    <tr><td>estado</td><td>Orientada</td><td>Seguimiento de atención</td></tr>
                    <tr><td>derivacion</td><td>No / Sí</td><td>Control de casos derivados</td></tr>
                </tbody>
            </table></div>
        </section>
        """
    else:
        detalle = """
        <section class="admin-section">
            <h3>Temas consultados durante el mes de ejemplo</h3>
            <div class="topic-bars">
                <div class="topic-row"><span>Ética pública</span><div class="topic-track"><div class="topic-fill" style="width:76%"></div></div><b>16</b></div>
                <div class="topic-row"><span>Declaraciones juradas</span><div class="topic-track"><div class="topic-fill" style="width:52%"></div></div><b>11</b></div>
                <div class="topic-row"><span>Registro de Visitas</span><div class="topic-track"><div class="topic-fill" style="width:38%"></div></div><b>8</b></div>
                <div class="topic-row"><span>Canal de denuncias</span><div class="topic-track"><div class="topic-fill" style="width:33%"></div></div><b>7</b></div>
            </div>
        </section>
        <section class="admin-section">
            <h3>Actividad reciente - muestra</h3>
            <div class="admin-table-wrap"><table class="admin-table">
                <thead><tr><th>Código</th><th>Canal</th><th>Tema</th><th>Estado</th></tr></thead>
                <tbody>
                    <tr><td>INT-2026-006</td><td>Chat web</td><td>Regalos o ventajas</td><td><span class="status-pill ok">Orientada</span></td></tr>
                    <tr><td>INT-2026-005</td><td>Anexo</td><td>Canal de denuncias</td><td><span class="status-pill wait">En seguimiento</span></td></tr>
                    <tr><td>INT-2026-004</td><td>Chat web</td><td>Registro de Visitas</td><td><span class="status-pill ok">Orientada</span></td></tr>
                </tbody>
            </table></div>
        </section>
        """

    tabs = "".join(
        f'<a class="{"active" if vista == clave else ""}" href="?modulo=panel_admin&vista={clave}" target="_self">{etiqueta}</a>'
        for clave, etiqueta in (
            ("resumen", "Resumen"),
            ("consultas", "Consultas"),
            ("alertas", "Alertas"),
            ("derivaciones", "Derivaciones"),
            ("fuentes", "Origen de datos"),
        )
    )

    return f"""
    <main class="integri-shell">
        <nav class="topic-bar" aria-label="Áreas de orientación">
            <span>Orientación Normativa</span><span>Canal de Denuncias</span><span>Registro de Visitas</span>
        </nav>
        <section class="admin-page panel">
            <header class="admin-header">
                <div class="admin-lock">🔐</div>
                <div><h2>Panel de control UFII</h2><p>Seguimiento administrativo de orientaciones, alertas y derivaciones.</p></div>
                <div class="admin-demo-badge">MAQUETA INTERACTIVA</div>
            </header>
            <nav class="admin-tabs">{tabs}</nav>
            <div class="admin-kpis">
                <a class="admin-kpi" href="?modulo=panel_admin&vista=consultas" target="_self"><span>💬</span><strong>Consultas recibidas</strong><b>42</b><small>Abrir registro de ejemplo →</small></a>
                <a class="admin-kpi" href="?modulo=panel_admin&vista=consultas" target="_self"><span>✅</span><strong>Orientaciones brindadas</strong><b>36</b><small>Revisar estados →</small></a>
                <a class="admin-kpi" href="?modulo=panel_admin&vista=alertas" target="_self"><span>⚠️</span><strong>Alertas preventivas</strong><b>7</b><small>Ver situaciones →</small></a>
                <a class="admin-kpi" href="?modulo=panel_admin&vista=derivaciones" target="_self"><span>🗂️</span><strong>Derivaciones a UFII</strong><b>6</b><small>Ver seguimiento →</small></a>
            </div>
            {detalle}
            <p class="demo-disclaimer"><strong>Datos completamente simulados:</strong> esta pantalla muestra cómo podría funcionar el panel administrativo. No contiene carga laboral, casos ni resultados reales de la UFII. En producción requerirá autenticación y permisos.</p>
            <div class="model-actions"><a class="back-button" href="?" target="_self">← Volver al inicio público</a></div>
        </section>
    </main>
    """


modulo_actual = st.query_params.get("modulo", "")
vista_panel = st.query_params.get("vista", "resumen")

if modulo_actual == "panel_admin":
    pagina = pagina_panel_control(vista_panel)
elif modulo_actual == "modelo":
    pagina = """
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRI</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <nav class="topic-bar" aria-label="Áreas de orientación">
            <span>Orientación Normativa</span><span>Canal de Denuncias</span><span>Registro de Visitas</span>
        </nav>

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
                <p class="model-section-lead">Seleccionamos la idea principal de cada componente para explicarla de manera clara y práctica.</p>
                <div class="component-grid">
                    <article class="component-card"><span class="component-number">1</span><strong>Compromiso de la Alta Dirección</strong><p>Asegura liderazgo y condiciones institucionales para fortalecer una cultura de integridad.</p></article>
                    <article class="component-card"><span class="component-number">2</span><strong>Gestión de riesgos</strong><p>Identifica y mitiga procesos vulnerables a delitos y prácticas contrarias a la ética.</p></article>
                    <article class="component-card"><span class="component-number">3</span><strong>Políticas de integridad pública</strong><p>Establece estándares de cumplimiento y responsabilidades para la entidad y sus servidores.</p></article>
                    <article class="component-card"><span class="component-number">4</span><strong>Transparencia, datos abiertos y rendición de cuentas</strong><p>Promueve el acceso a la información, la transparencia y la rendición de cuentas.</p></article>
                    <article class="component-card"><span class="component-number">5</span><strong>Controles internos, externos y auditorías</strong><p>Fortalece los mecanismos de control y la atención diligente de las acciones de auditoría.</p></article>
                    <article class="component-card"><span class="component-number">6</span><strong>Comunicación y capacitación</strong><p>Desarrolla inducción, difusión y capacitación continua para un desempeño ético.</p></article>
                    <article class="component-card"><span class="component-number">7</span><strong>Canal de denuncias</strong><p>Asegura la gestión de denuncias de corrupción y las medidas de protección correspondientes.</p></article>
                    <article class="component-card"><span class="component-number">8</span><strong>Supervisión y monitoreo</strong><p>Evalúa el avance del modelo y genera información para tomar decisiones de mejora.</p></article>
                    <article class="component-card"><span class="component-number">9</span><strong>Encargado del Modelo de Integridad</strong><p>Articula los componentes y orienta a las áreas para su implementación oportuna.</p></article>
                </div>
            </div>

            <div class="model-section">
                <h3>Etapas de implementación</h3>
                <div class="stage-grid">
                    <div class="stage"><span>Etapa 1</span><strong>Inicial</strong></div>
                    <div class="stage"><span>Etapa 2</span><strong>Institucionalización</strong></div>
                    <div class="stage"><span>Etapa 3</span><strong>Estandarización</strong></div>
                </div>
            </div>

            <div class="model-section diris-box">
                <strong>Aplicación en DIRIS Lima Norte</strong>
                <p>Próximamente incorporaremos aquí los avances, responsables, actividades y evidencias institucionales. Esta información será publicada únicamente después de ser validada por la UFII.</p>
            </div>

            <div class="model-section diris-box">
                <strong>¿Qué significa para ti?</strong>
                <p>El modelo ayuda a prevenir riesgos, actuar con imparcialidad, reconocer posibles conflictos de intereses, utilizar correctamente los canales institucionales y proteger la confianza en el servicio público.</p>
            </div>

            <div class="model-actions">
                <a class="back-button" href="?" target="_self">← Volver al inicio</a>
                <a class="source-button" href="https://www.gob.pe/integridad" target="_blank" rel="noopener noreferrer">Consultar fuente oficial PCM ↗</a>
            </div>
        </section>
    </main>
    """
elif modulo_actual == "etica":
    pagina = """
    <main class="integri-shell">
        <header class="brand">
            <h1>INTEGRI</h1>
            <div class="brand-line"></div>
            <h2>Asistente de Integridad Institucional</h2>
            <p>Unidad Funcional de Integridad Institucional (UFII)</p>
        </header>
        <nav class="topic-bar" aria-label="Áreas de orientación">
            <span>Orientación Normativa</span><span>Canal de Denuncias</span><span>Registro de Visitas</span>
        </nav>

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
                <strong>Importante:</strong> INTEGRI brinda orientación preventiva y general. No califica infracciones, no determina responsabilidades y no impone sanciones. Si deseas comunicar un posible acto de corrupción, utiliza el canal institucional correspondiente y evita describir aquí a las personas o las evidencias.
            </div>

            <div class="model-actions">
                <a class="back-button" href="?" target="_self">← Volver al inicio</a>
                <a class="source-button" href="https://www.gob.pe/institucion/jne/normas-legales/8133444-ley-del-codigo-de-etica-de-la-funcion-publica-ley-n-27815" target="_blank" rel="noopener noreferrer">Consultar Ley N.° 27815 ↗</a>
                <a class="source-button" href="https://www.gob.pe/institucion/saludpol/noticias/606119-guia-de-principios-deberes-y-prohibiciones-eticas-de-la-funcion-publica" target="_blank" rel="noopener noreferrer">Ver guía oficial ↗</a>
            </div>
        </section>
    </main>
    """
elif modulo_actual == "declaraciones":
    pagina = pagina_modulo_info(
        "📄",
        "Declaraciones Juradas",
        "Guía para identificar el tipo de declaración, confirmar si corresponde presentarla y utilizar el canal oficial adecuado.",
        """
        <div class="info-section">
            <h3>¿Qué declaración necesitas revisar?</h3>
            <p class="info-lead">No todas las declaraciones aplican a todas las personas. La condición de obligado debe confirmarse según el cargo, la función y la comunicación del área responsable.</p>
            <div class="info-grid cols-3">
                <article class="info-card"><span class="info-card-icon">🔗</span><strong>Declaración Jurada de Intereses</strong><p>Informa vínculos familiares, políticos, económicos, comerciales e institucionales que podrían ser relevantes para la función pública.</p></article>
                <article class="info-card"><span class="info-card-icon">🏠</span><strong>Ingresos, Bienes y Rentas</strong><p>Registra información patrimonial de autoridades, funcionarios o servidores comprendidos en la normativa aplicable.</p></article>
                <article class="info-card"><span class="info-card-icon">🗂️</span><strong>Otras declaraciones institucionales</strong><p>Pueden existir formatos vinculados con incompatibilidades, impedimentos o conflictos de intereses. Deben validarse con el área responsable.</p></article>
            </div>
        </div>

        <div class="info-section">
            <h3>Ruta rápida para presentar correctamente</h3>
            <div class="process-grid">
                <div class="process-step"><span>1</span>Confirma con el área responsable si estás comprendido como obligado y qué declaración corresponde.</div>
                <div class="process-step"><span>2</span>Identifica el momento de presentación comunicado: inicio, actualización periódica o cese, según corresponda.</div>
                <div class="process-step"><span>3</span>Ingresa únicamente al sistema oficial indicado y revisa la información antes de firmar y enviar.</div>
                <div class="process-step"><span>4</span>Conserva la constancia y comunica oportunamente cualquier dificultad técnica al área responsable.</div>
            </div>
        </div>

        <div class="info-section info-note yellow"><strong>Importante:</strong> INTEGRI no determina quién está obligado ni calcula plazos individuales. No ingreses en este chatbot datos patrimoniales, familiares, documentos de identidad, claves ni declaraciones completas.</div>

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
                <a class="guide-link" href="?modulo=modelo" target="_self"><span>🛡️</span><strong>Modelo de Integridad</strong><small>Consulta sus nueve componentes y las etapas de implementación.</small></a>
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
if modulo_actual in modulos:
    st.html(pagina)
    if modulo_actual == "panel_admin":
        csv_demostrativo = """codigo,fecha,canal,tema,estado,derivacion
INT-2026-001,03/07/2026,Chat web,Conflicto de intereses,Orientada,No
INT-2026-002,05/07/2026,Chat web,Declaración jurada,Orientada,No
INT-2026-003,08/07/2026,Correo,Modelo de Integridad,Derivada,Sí
INT-2026-004,11/07/2026,Chat web,Registro de Visitas,Orientada,No
INT-2026-005,15/07/2026,Anexo,Canal de denuncias,En seguimiento,Sí
"""
        st.download_button(
            "⬇️ Descargar base CSV de ejemplo",
            data=csv_demostrativo.encode("utf-8-sig"),
            file_name="INTEGRI_seguimiento_datos_simulados.csv",
            mime="text/csv",
            use_container_width=True,
        )
        st.caption("🔐 En la versión real, este panel y sus descargas estarían disponibles solamente para usuarios autorizados.")
    st.stop()

cabecera_inicio = pagina_inicio.split('<section class="hero panel">', 1)[0] + "</main>"
resto_inicio = '<main class="integri-shell"><aside class="notice panel">' + pagina_inicio.split('<aside class="notice panel">', 1)[1]

st.html(cabecera_inicio)

columna_robot, columna_chat = st.columns([1, 2], gap="medium")

with columna_robot:
    with st.container(border=True):
        st.image(Path(__file__).parent / "assets" / "integri_robot.png", use_container_width=True)
        st.markdown("<div style='text-align:center;color:#0a2459;font-weight:800;'>INTEGRI</div>", unsafe_allow_html=True)
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
        <div class="chat-label">INTEGRI</div>
        <div class="chat-bubble">¡Hola! ¿En qué puedo ayudarte?</div>
    </div>
    """
    st.html(
        f"""
        <section class="embedded-chat-box">
            <div class="embedded-chat-heading">
                <div class="mini-avatar">🤖</div>
                <div><strong>INTEGRI</strong><small>Activo · Respuestas guiadas sin API</small></div>
            </div>
            <div class="chat-history">{historial_invertido_html}{saludo_inicial}</div>
        </section>
        """
    )

    with st.form("formulario_chat", clear_on_submit=True, border=False):
        columna_pregunta, columna_enviar = st.columns([5, 1])
        with columna_pregunta:
            pregunta = st.text_input(
                "Mensaje para INTEGRI",
                placeholder="Escribe tu duda...",
                label_visibility="collapsed",
            )
        with columna_enviar:
            enviar = st.form_submit_button("Enviar", use_container_width=True)

    if enviar and pregunta.strip():
        pregunta_limpia = pregunta.strip()
        st.session_state.historial_chat.append(("usuario", pregunta_limpia))
        st.session_state.historial_chat.append(("integri", respuesta_guiada(pregunta_limpia)))
        st.rerun()

    columna_seguridad, columna_borrar = st.columns([4, 1])
    with columna_seguridad:
        st.caption("🔒 No ingreses nombres, DNI ni datos sensibles.")
    with columna_borrar:
        if st.session_state.historial_chat and st.button("Limpiar", use_container_width=True):
            st.session_state.historial_chat = []
            st.rerun()

st.html(resto_inicio)
