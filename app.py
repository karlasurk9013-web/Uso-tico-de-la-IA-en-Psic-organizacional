import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA en Psicología Organizacional", layout="wide")

# Título Principal
st.title("Marco Teórico: Uso Ético de la IA en Psicología Organizacional [cite: 5]")
st.markdown(f"**Estudiante:** Suárez Robertos Karla Gabriela [cite: 3]  \n**Fecha:** 12 de febrero del 2026 [cite: 4]")

st.divider()

# Menú lateral para navegar el artículo
menu = st.sidebar.radio("Secciones del Artículo", 
    ["Introducción", "Automatización y Eficiencia", "Desafíos Éticos", "IA Generativa", "Reflexión Final", "Referencias"])

if menu == "Introducción":
    st.header("1. Introducción")
    st.write("La integración de la Inteligencia Artificial (IA) en las organizaciones ha dejado de ser una tendencia emergente para convertirse en un componente estructural de la competitividad contemporánea[cite: 6].")
    st.write("En la Gestión de Recursos Humanos (GRH), la IA transforma la eficiencia operativa y la lógica de la toma de decisiones estratégicas[cite: 7].")
    st.info("Este análisis aborda tres ejes: automatización, riesgos éticos y el factor humano[cite: 9].")

elif menu == "Automatización y Eficiencia":
    st.header("2. Automatización y Eficiencia en los Procesos de GRH [cite: 11]")
    st.write("El motor principal es la búsqueda de eficiencia organizacional[cite: 12].")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Beneficios Operativos")
        st.write("* Automatización de tareas repetitivas como cribado de currículos[cite: 13].")
        st.write("* Programación de entrevistas y optimización de recursos[cite: 13].")
    with col2:
        st.subheader("Analítica Predictiva")
        st.write("* Previsión de tendencias como rotación de personal[cite: 16].")
        st.write("* Identificación de necesidades de capacitación[cite: 16].")
    st.warning("Limitación: La implementación puede ser un 'mixed bag' con dificultades técnicas en organizaciones con pocos recursos[cite: 18, 19].")

elif menu == "Desafíos Éticos":
    st.header("3. Desafíos Éticos: Sesgo, Explicabilidad y Privacidad [cite: 20]")
    st.error("### Sesgo Algorítmico")
    st.write("Los sistemas entrenados con datos históricos pueden reproducir prejuicios estructurales que afectan la selección[cite: 21, 22].")
    
    st.subheader("Soluciones y Privacidad")
    st.write("La IA Explicable (XAI) permite detectar y supervisar estos sesgos[cite: 24].")
    st.write("La recopilación masiva de datos plantea retos éticos y regulatorios como el cumplimiento del GDPR[cite: 26, 27].")

elif menu == "IA Generativa":
    st.header("4. IA Generativa y el Factor Humano [cite: 29]")
    st.write("Herramientas generativas optimizan la redacción de descripciones de puestos y la comunicación[cite: 31].")
    st.write("Sin embargo, existen riesgos de desinformación si falta supervisión[cite: 32].")
    st.success("La IA actúa como soporte analítico, pero no sustituye la empatía y el juicio ético del profesional[cite: 33, 34].")

elif menu == "Reflexión Final":
    st.header("5. Reflexión sobre el uso de IA en la Academia [cite: 37]")
    st.write("La IA es eficaz para estructurar, organizar y sintetizar información con coherencia[cite: 39, 40].")
    st.markdown("> **Limitación clave:** No sustituye el criterio crítico ni la evaluación ética del investigador[cite: 41].")
    st.write("La validación académica y responsabilidad intelectual siguen siendo tareas humanas fundamentales[cite: 43].")

elif menu == "Referencias":
    st.header("Referencias Bibliográficas [cite: 44]")
    st.write("- Albaroudi, A., et al. (2024). [cite: 45]")
    st.write("- Chávez-Betancourt, R., et al. (2024). [cite: 47]")
    st.write("- David, R. (2023). [cite: 49]")
    st.write("- Ghosh, S., et al. (2024). [cite: 50]")
    st.write("- Malik, N., et al. (2023). [cite: 52]")
    st.write("- Ncube, S. (2024). [cite: 53]")
    st.write("- Nicholas, V., & Umarani, C. (2025). [cite: 55]")
    st.write("- Radonjic, A., et al. (2024). [cite: 56]")
    st.write("- Rane, N., et al. (2023). [cite: 58]")
    st.write("- Yawson, R. (2024). [cite: 59]")
