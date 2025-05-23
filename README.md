# Generador de Pedidos de Compras

## Problemática

El día a día de una familia implica planificar las comidas semanales, lo cual puede ser un desafío. Pensar qué cocinar, cubrir todas las comidas del día, respetar un valor calórico específico y hacer una compra eficiente para toda la semana puede ser una tarea demandante. Muchas familias improvisan las comidas o repiten platos por falta de tiempo o ideas, lo que afecta la variedad nutricional y la organización del hogar. Además, preparar la lista de compras sin un sistema ordenado genera compras incompletas, innecesarias o poco eficientes. La ausencia de una herramienta que resuelva la generación de menús y la planificación de compras complica la gestión del tiempo, afecta la alimentación familiar y genera gastos innecesarios. Esta problemática afecta a cualquier familia que desee comer mejor, ahorrar tiempo y dinero, y hacer una única compra semanal bien organizada.

## Solución Propuesta

La solución consiste en una aplicación web pensada para familias, que permite generar menús diarios completos en base a necesidades calóricas, cantidad de personas y duración del plan. La app, impulsada por inteligencia artificial, crea automáticamente comidas para cada momento del día (desayuno, colaciones, almuerzo, merienda y cena) de forma balanceada y variada. Además, una vez generado el menú, la aplicación elabora una lista de compras optimizada, agrupando los ingredientes por sectores (carnes, verduras, lácteos, etc.) para facilitar una única visita semanal al supermercado. Esto reduce el tiempo de organización, evita compras innecesarias y mejora la eficiencia en la cocina y en el presupuesto del hogar. Como valor agregado, el usuario podrá elegir si desea adaptar los menús a una dieta específica (por ejemplo: vegetariana, sin TACC, etc.), personalizando aún más la experiencia. La integración de IA permite automatizar una tarea cotidiana que muchas veces se vuelve un problema, ofreciendo creatividad, variedad y una solución simple a una necesidad diaria.

## Propuesta de Aplicación Web con IA

### Nombre de la App:
Generador de pedidos de compras

### Función principal:
La aplicación permite generar automáticamente un menú completo adaptado a un valor calórico diario, cantidad de días y número de personas. A partir de ese menú, genera una lista de compras agrupada por sectores, para realizar una única compra semanal.

### ¿Cómo se integra la IA?
La IA genera los menús diarios equilibrados en base al prompt que se arma con los datos ingresados por el usuario. También puede adaptarse a restricciones alimentarias específicas. Además, compila automáticamente los ingredientes en una lista organizada.

### Ventajas y beneficios:
- Ahorro de tiempo
- Mejora en la alimentación familiar
- Organización eficiente de compras
- Adaptabilidad a dietas especiales
- Disminución del estrés cotidiano

## Prompt Inicial

### Prompt propuesto:
"Generá un menú completo para [X] personas, con un requerimiento diario de [Y] calorías, para un total de [Z] días. Cada día debe incluir desayuno, colación de la mañana, almuerzo, merienda, colación de la tarde y cena. Las comidas deben ser variadas, equilibradas y fáciles de preparar. Si se indica un tipo de dieta (por ejemplo, vegetariana o sin TACC), tenelo en cuenta. Al finalizar, generá una lista de ingredientes agrupados por categorías (carnes, verduras, lácteos, etc.) para facilitar una única compra semanal."

### Justificación:
Este prompt es flexible y permite adaptar los menús a las necesidades de cualquier familia. Integra la generación de menús y la planificación de compras en un solo paso.

## Factibilidad Económica

La aplicación es viable económicamente tanto para el desarrollo como para su uso doméstico. Con una sola consulta semanal a la IA se puede generar un menú completo, lo que minimiza los costos si se usa una API como la de OpenAI. Además, el proyecto puede comenzar con herramientas gratuitas como Streamlit y escalar a planes freemium. También es posible integrar modelos de código abierto para evitar costos por consulta.

## Requerimientos Técnicos

### Herramientas necesarias:
1. Streamlit: desarrollo y despliegue de la app.
2. Visual Studio Code + Amazon CodeWhisperer: soporte IA para desarrollo.
3. ChatGPT activado: validación de prompts.
4. OpenAI API Key: integración programática de IA.


## Puedes verlo en:
https://pfinal.streamlit.app/