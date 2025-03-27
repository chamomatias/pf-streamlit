import streamlit as st
from groq import Groq
from datetime import datetime

# Reemplaza con tu API key de Groq
GROQ_API_KEY = "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"

def build_prompt(personas: int, calorias: int, dias: int, dieta: str) -> str:
    """
    Construye el prompt para la API de Groq solicitando un menú por día.
    Se especifica que cada comida debe incluir los ingredientes con su cantidad y unidad de medida,
    y al final indicar el total de calorías consumidas en el formato (Calorías: XX).
    Además, se solicita la lista de compras con las unidades correspondientes.
    """
    dieta_str = f" Tené en cuenta la dieta {dieta}." if dieta and dieta != "Ninguna" else ""
    prompt = (
        f"Generá un menú completo para {personas} personas, con un requerimiento diario de no más de {calorias} calorías, "
        f"para un total de {dias} días.{dieta_str}\n\n"
        "El menú debe estar en formato Markdown con el siguiente esquema para cada día:\n\n"
    )
    
    for dia in range(1, dias + 1):
        prompt += (
            f"### Día {dia}:\n"
            f"- **Desayuno:** Descripción del platillo, indicando los ingredientes con su cantidad y unidad de medida (por ejemplo, '500 grs de carne'). "
            f"Al final, agregar entre paréntesis el total de calorías consumidas en el formato (Calorías: XX).\n"
            f"- **Colación de la mañana:** Misma estructura que el desayuno.\n"
            f"- **Almuerzo:** Misma estructura que el desayuno.\n"
            f"- **Merienda:** Misma estructura que el desayuno.\n"
            f"- **Colación de la tarde:** Misma estructura que el desayuno.\n"
            f"- **Cena:** Misma estructura que el desayuno.\n\n"
        )
    
    prompt += (
        "Al finalizar TODOS los días, escribí exactamente la siguiente sección:\n\n"
        "## Lista de compras:\n"
        "- **Carnes:** (indicar cantidad con unidades, por ejemplo, '1 kg de pechuga de pollo')\n"
        "- **Verduras:**\n"
        "- **Frutas:**\n"
        "- **Lácteos:**\n"
        "- **Otros:**\n\n"
        "Asegurate de incluir las unidades de medida correspondientes (kg, gr, ml, unidades, etc.)."
    )
    
    return prompt

def call_groq_api(prompt: str) -> str:
    """
    Envía el prompt a la API de Groq y devuelve el texto de la respuesta.
    """
    try:
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error al llamar a la API de Groq: {e}")
        return None

def parse_response(respuesta: str):
    """
    Separa la respuesta en dos partes:
    1. El menú (todo lo anterior a '## Lista de compras:')
    2. La lista de compras (a partir de '## Lista de compras:')
    """
    if not respuesta:
        return None, None

    marcador = "## Lista de compras:"
    idx = respuesta.find(marcador)
    if idx == -1:
        st.error("No se encontró la sección '## Lista de compras:' en la respuesta.")
        return None, None

    menu = respuesta[:idx].strip()
    lista_compras = respuesta[idx:].strip()
    return menu, lista_compras

def guardar_lista_compras(lista_compras: str) -> str:
    """
    Guarda la lista de compras en un archivo de texto cuyo nombre incluye un prefijo de timestamp.
    Devuelve el nombre del archivo si tuvo éxito.
    """
    try:
        # Generar timestamp en formato "aammddHHMM"
        timestamp = datetime.now().strftime("%y%m%d%H%M")
        filename = f"{timestamp}_lista_de_compras.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(lista_compras)
        return filename
    except Exception as e:
        st.error(f"Error al guardar la lista de compras: {e}")
        return None

def main():
    st.title("Generador de Menús y Listas de Compras")
    st.markdown("""
        Esta aplicación genera menús diarios personalizados y listas de compras basadas en tus preferencias. 
        Ingresa la cantidad de comensales, el máximo de calorías diarias, la cantidad de días y el tipo de dieta.
        Cada día se presentará de forma estructurada, con cada comida en su propio renglón, especificando los ingredientes 
        (con su cantidad y unidad de medida) y el total de calorías consumidas.
    """)

    # Entradas del usuario
    personas = st.number_input("Cantidad de comensales", min_value=1, value=4)
    calorias = st.number_input("Calorías máximas diarias", min_value=500, value=2000)
    dias = st.number_input("Cantidad de días", min_value=1, value=7)
    dieta = st.selectbox("Tipo de dieta", ["Ninguna", "Vegetariana", "Sin TACC", "Vegana", "Baja en carbohidratos"])

    if st.button("Generar Menú y Lista de Compras"):
        prompt = build_prompt(personas, calorias, dias, dieta)
        st.info("Enviando solicitud a la API de Groq. Esto puede tardar unos segundos...")
        respuesta = call_groq_api(prompt)

        if respuesta:
            menu, lista_compras = parse_response(respuesta)
            if menu and lista_compras:
                st.subheader("Menú Generado")
                st.markdown(menu)
                
                st.subheader("Lista de Compras")
                st.markdown(lista_compras)
                
                # Guardar la lista de compras en un archivo con prefijo de timestamp
                filename = guardar_lista_compras(lista_compras)
                if filename:
                    with open(filename, "r", encoding="utf-8") as f:
                        file_contents = f.read()
                    st.download_button(
                        label="Descargar lista de compras",
                        data=file_contents,
                        file_name=filename,
                        mime="text/plain",
                    )

if __name__ == "__main__":
    main()
