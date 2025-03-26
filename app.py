import streamlit as st
from groq import Groq

# Reemplaza con tu API key de Groq
GROQ_API_KEY = "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"

def generar_menu_y_lista_de_compras(personas, calorias, dias, dieta=""):
    """
    Genera un menú completo y una lista de compras utilizando la API de Groq.

    Args:
        personas (int): Cantidad de personas para el menú.
        calorias (int): Requerimiento calórico diario.
        dias (int): Cantidad de días para el menú.
        dieta (str, opcional): Tipo de dieta (vegetariana, sin TACC, etc.). Defaults to "".

    Returns:
        str: El menú generado y la lista de compras.
    """

    client = Groq(api_key=GROQ_API_KEY)

    prompt = f"Generá un menú completo para {personas} personas, con un requerimiento diario de {calorias} calorías, para un total de {dias} días. Cada día debe incluir desayuno, colación de la mañana, almuerzo, merienda, colación de la tarde y cena. Las comidas deben ser variadas, equilibradas y fáciles de preparar."
    if dieta:
        prompt += f" Tené en cuenta la dieta {dieta}."
    prompt += " Al finalizar, generá una lista de ingredientes agrupados por categorías (carnes, verduras, lácteos, etc.) con las unidades de medida (ej: kg, gr, ml, unidades) para facilitar una única compra semanal."

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile" # Usando el modelo especificado
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error al generar el menú: {e}"

# Interfaz de Streamlit
st.title("Generador de Menús y Listas de Compras")

personas = st.number_input("Cantidad de personas", min_value=1, value=4)
calorias = st.number_input("Calorías diarias", min_value=1000, value=2000)
dias = st.number_input("Cantidad de días", min_value=1, value=7)
dieta = st.selectbox("Tipo de dieta", ["Ninguna", "Vegetariana", "Sin TACC"])

if st.button("Generar Menú y Lista de Compras"):
    resultado = generar_menu_y_lista_de_compras(personas, calorias, dias, dieta)
    st.subheader("Menú y Lista de Compras Generados:")
    st.write(resultado)
    st.markdown("---")

    # Extract shopping list and write to file
    try:
        # Improved extraction of shopping list
        last_cena_index = resultado.rfind("Cena:")  # Find the last occurrence of "Cena:"
        last_almuerzo_index = resultado.rfind("Almuerzo:")
        last_desayuno_index = resultado.rfind("Desayuno:")

        if last_cena_index != -1:
            menu = resultado[:last_cena_index + len("Cena:")].strip()
            shopping_list = resultado[last_cena_index + len("Cena:"):].strip()
        elif last_almuerzo_index != -1:
            menu = resultado[:last_almuerzo_index + len("Almuerzo:")].strip()
            shopping_list = resultado[last_almuerzo_index + len("Almuerzo:"):].strip()
        elif last_desayuno_index != -1:
            menu = resultado[:last_desayuno_index + len("Desayuno:")].strip()
            shopping_list = resultado[last_desayuno_index + len("Desayuno:"):].strip()

            # Format the shopping list
            formatted_list = ""
            for line in shopping_list.splitlines():
                line = line.strip()
                if line:
                    formatted_list += line + "\n"

            # Write the formatted shopping list to a file
            with open("lista_de_compras.txt", "w", encoding="utf-8") as f:
                f.write(formatted_list)

            st.success("Lista de compras guardada en 'lista_de_compras.txt'")

            # Create a download link for the shopping list
            with open("lista_de_compras.txt", "r", encoding="utf-8") as f:
                file_contents = f.read()
            st.download_button(
                label="Descargar lista de compras",
                data=file_contents,
                file_name="lista_de_compras.txt",
                mime="text/plain",
            )
        else:
            st.error("No se pudo identificar el menú y la lista de compras.")

    except Exception as e:
        st.error(f"Error al procesar la lista de compras: {e}")
