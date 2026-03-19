import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA en Psicología Organizacional", layout="wide")

# Título Principal y Datos de la Alumna
st.title("Marco Teórico: Uso Ético de la IA en Psicología Organizacional")
st.markdown("**Facultad de Psicología UADY**")
st.markdown("**Estudiante:** Suárez Robertos Karla Gabriela")
st.markdown("**Fecha:** 12 de febrero del 2026")

st.divider()

# Menú lateral para navegar
st.sidebar.title("Secciones")
menu = st.sidebar.radio("Selecciona una sección:", 
    ["1. Introducción", 
     "2. Automatización y Eficiencia", 
     "3. Desafíos Éticos", 
     "4. IA Generativa", 
     "5. Reflexión Final", 
     "Referencias"])

if menu == "1. Introducción":
    st.header("1. Introducción")
    st.write("La integración de la Inteligencia Artificial (IA) en las organizaciones ha pasado de ser una tendencia emergente a un componente estructural de la competitividad contemporánea.")
    st.write("En la Gestión de Recursos Humanos (GRH), la IA transforma la eficiencia operativa y la toma de decisiones estratégicas.")
    st.info("Este análisis aborda tres ejes: automatización y eficiencia, riesgos éticos y sesgo, y la relación con el factor humano.")

elif menu == "2. Automatización y Eficiencia":
    st.header("2. Automatización y Eficiencia en los Procesos de GRH")
    st.write("El motor principal de la IA es la búsqueda de eficiencia. Permite automatizar tareas como el cribado de currículos y programación de entrevistas.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Beneficios")
        st.success("Optimiza tiempos y recursos, liberando a los profesionales para actividades estratégicas.")
    with col2:
        st.subheader("Analítica Predictiva")
        st.write("Permite prever tendencias como la rotación de personal y necesidades de capacitación.")
    
    st.warning("Nota: Su implementación puede ser compleja en organizaciones con recursos limitados.")

elif menu == "3. Desafíos Éticos":
    st.header("3. Desafíos Éticos: Sesgo, Explicabilidad y Privacidad")
    st.error("Riesgo: Los sistemas pueden reproducir prejuicios estructurales en la selección de personal.")
    st.write("La **IA Explicable (XAI)** surge para detectar sesgos y aumentar la transparencia organizacional.")
    st.write("Además, la recopilación masiva de datos plantea retos en privacidad bajo normativas como el GDPR.")

elif menu == "4. IA Generativa":
    st.header("4. IA Generativa y el Factor Humano")
    st.write("Herramientas generativas optimizan la comunicación y redacción de puestos, pero requieren supervisión para evitar desinformación.")
    st.subheader("Colaboración Humano-Máquina")
    st.write("La IA actúa como soporte analítico, pero no sustituye la empatía y el juicio ético del profesional de RR.HH.")

elif menu == "5. Reflexión Final":
    st.header("5. Reflexión")
    st.write("**Capacidades de la IA en el ámbito académico:**")
    st.write("- **Ventaja:** Eficaz para estructurar, organizar y sintetizar información con claridad.")
    st.write("- **Limitación:** No sustituye el criterio crítico ni la interpretación profunda del investigador.")
    st.markdown("> La validación académica y la responsabilidad intelectual siguen siendo tareas humanas fundamentales.")

elif menu == "Referencias":
    st.header("Referencias Bibliográficas")
    st.write("- Albaroudi, A., Mansouri, H., & Alameer, R. (2024).")
    st.write("- Chávez-Betancourt, R., et al. (2024).")
    st.write("- David, R. (2023).")
    st.write("- Ghosh, S., et al. (2024).")
    st.write("- Malik, N., et al. (2023).")
    st.write("- Ncube, S. (2024).")
    st.write("- Nicholas, V., & Umarani, C. (2025).")
    st.write("- Radonjic, A., et al. (2024).")
    st.write("- Rane, N., et al. (2023).")
    st.write("- Yawson, R. (2024).")
