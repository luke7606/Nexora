# nexora_mvp_app.py

import streamlit as st
import openai

# CONFIGURACION
st.set_page_config(page_title="Nexora IA Advisor", layout="centered")
st.title("🤖 Nexora | Recomendador Inteligente por IA")
st.markdown("""
Este MVP simula cómo Nexora puede generar recomendaciones de gestión y KPIs personalizados.
Completá los datos de tu equipo y recibí una sugerencia basada en IA.
""")

# CLAVE Y ENDPOINT DE OPENROUTER
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

# FORMULARIO DE ENTRADA
with st.form("formulario_equipo"):
    industria = st.selectbox("Industria", ["Tecnología", "Finanzas", "Marketing", "Educación", "Salud", "Otro"])
    cultura = st.selectbox("Cultura del equipo", ["Innovadora", "Estructurada", "Creativa", "Orientada a resultados", "Caótica"])
    objetivo = st.text_input("Objetivo principal del equipo", placeholder="Ej: Mejorar entregas a tiempo")
    kpi = st.text_input("KPI principal", placeholder="Ej: Velocidad de entrega")
    enviar = st.form_submit_button("Generar recomendación IA")

# FUNCION IA CON OPENROUTER
def generar_recomendacion(industria, cultura, objetivo, kpi):
    prompt = f"""
Actuá como un experto en gestión de equipos con enfoque en KPIs y uso de inteligencia artificial. 
A partir de la siguiente información, generá una recomendación de flujo de trabajo, KPIs adicionales sugeridos y prácticas de mejora continua. 
Sé concreto y adaptado al perfil del equipo.

Industria: {industria}
Cultura del equipo: {cultura}
Objetivo principal: {objetivo}
KPI principal: {kpi}
"""
    respuesta = openai.ChatCompletion.create(
        model="mistralai/mistral-7b-instruct",  # Alternativas: openchat/openchat-3.5, anthropic/claude-2, etc.
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content.strip()

# RESULTADO
if enviar:
    if not all([industria, cultura, objetivo, kpi]):
        st.warning("Por favor completá todos los campos.")
    else:
        with st.spinner("Generando recomendación personalizada..."):
            resultado = generar_recomendacion(industria, cultura, objetivo, kpi)
            st.success("✅ Recomendación generada:")
            st.markdown(f"""
#### 💡 Recomendación Nexora
{resultado}
""")
