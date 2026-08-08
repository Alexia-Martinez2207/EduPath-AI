# 🎓 EduPath AI

### Detecta señales. Actúa a tiempo.

EduPath AI es una plataforma de inteligencia educativa desarrollada para **estimar el rendimiento académico de estudiantes e identificar señales que podrían requerir atención temprana**.

El proyecto surge de una pregunta sencilla:

> **¿Qué pasaría si pudiéramos identificar que un estudiante necesita apoyo antes de que su rendimiento académico se vea seriamente afectado?**

Las instituciones educativas generan constantemente información sobre sus estudiantes: asistencia, hábitos de estudio, participación en actividades, apoyo familiar y antecedentes académicos, entre otros factores.

EduPath AI busca aprovechar esta información para transformarla en resultados claros y comprensibles que puedan servir como apoyo para la toma de decisiones.

---

## 🌐 Aplicación en línea

EduPath AI cuenta con una aplicación web funcional desarrollada en Streamlit.

Puede probarse directamente desde cualquier navegador, sin instalar ningún programa:

**👉 Aplicación EduPath AI:**  
https://edupath-ai-dorykjkgjwtdrych9ka2yn.streamlit.app

---

# 💡 ¿Qué problema busca resolver?

El bajo rendimiento académico no siempre aparece de manera repentina.

Antes de que un estudiante presente dificultades importantes pueden existir diferentes señales relacionadas con su comportamiento académico y su entorno.

Por ejemplo:

- número de ausencias;
- horas dedicadas al estudio;
- participación en tutorías;
- nivel de apoyo familiar;
- actividades extracurriculares;
- participación deportiva;
- actividades musicales;
- voluntariado;
- características personales y académicas.

Analizar todos estos factores individualmente puede resultar complicado, especialmente cuando una institución trabaja con una gran cantidad de estudiantes.

**EduPath AI propone utilizar los datos como una herramienta de apoyo para identificar patrones y facilitar una intervención más oportuna.**

---

# 🚀 ¿Qué es EduPath AI?

EduPath AI es una aplicación que permite ingresar información relacionada con un estudiante y obtener una **estimación de su promedio académico esperado**.

Sin embargo, el objetivo de la plataforma no es simplemente generar un número.

El resultado se presenta de una forma fácil de interpretar e incluye:

- 📊 Promedio académico estimado.
- 🚦 Nivel de riesgo académico.
- 💪 Fortalezas identificadas.
- ⚠️ Señales que podrían requerir atención.
- 💡 Recomendaciones para apoyar al estudiante.
- 📝 Interpretación general de su perfil.

De esta manera, los resultados de un modelo predictivo se convierten en información que puede ser comprendida por usuarios que no necesariamente tienen conocimientos de Ciencia de Datos o Inteligencia Artificial.

---

# 👥 ¿A quién está dirigido?

EduPath AI fue diseñado pensando principalmente en el ámbito educativo.

Entre sus posibles usuarios se encuentran:

### 👩‍🏫 Docentes

Puede servir como herramienta complementaria para identificar estudiantes que podrían requerir mayor seguimiento.

### 🏫 Instituciones educativas

Permite visualizar cómo el análisis de datos puede incorporarse a estrategias de prevención y acompañamiento académico.

### 🧑‍💼 Tutores y orientadores

Puede proporcionar una primera lectura del perfil académico del estudiante y ayudar a identificar aspectos sobre los cuales prestar mayor atención.

### 👨‍👩‍👧 Familias

La información se presenta utilizando un lenguaje comprensible, facilitando la interpretación del resultado.

### 🎓 Estudiantes

Puede ayudar a reconocer fortalezas y aspectos de su comportamiento académico que podrían mejorarse.

> **Importante:** EduPath AI es una herramienta de apoyo y no pretende sustituir la evaluación, experiencia o criterio de docentes, orientadores o instituciones educativas.

---

# ⚙️ ¿Cómo funciona?

El funcionamiento de EduPath AI puede resumirse en cuatro etapas:

### 1. Información del estudiante

El usuario proporciona diferentes características académicas, personales y relacionadas con su entorno.

### 2. Análisis

La información es procesada por el modelo predictivo desarrollado durante el proyecto.

### 3. Predicción

La plataforma genera una estimación del rendimiento académico esperado.

### 4. Interpretación

EduPath AI transforma el resultado en información más sencilla de comprender, mostrando fortalezas, señales de atención y recomendaciones.

En términos simples:

```text
Información del estudiante
          ↓
     Análisis de datos
          ↓
  Estimación académica
          ↓
Interpretación del resultado
          ↓
     Recomendaciones
```

---

# 🧠 Desarrollo del modelo

Para construir EduPath AI se siguió un proceso completo de Ciencia de Datos.

El proyecto incluyó:

1. Exploración del conjunto de datos.
2. Revisión de calidad de la información.
3. Preparación y transformación de variables.
4. Análisis exploratorio.
5. Selección de variables.
6. División de datos para entrenamiento y prueba.
7. Entrenamiento de diferentes modelos.
8. Evaluación y comparación de resultados.
9. Selección del modelo final.
10. Integración del modelo dentro de una aplicación web.

Se evaluaron cuatro enfoques diferentes:

- Regresión Lineal.
- Random Forest.
- XGBoost.
- Red Neuronal.

El propósito de comparar diferentes alternativas fue seleccionar el modelo que mostrara un buen desempeño con datos que no había observado durante su entrenamiento.

---

# 📊 Resultados obtenidos

Los modelos fueron evaluados tanto sobre datos de entrenamiento como sobre datos de prueba.

| Modelo | MAE Train | RMSE Train | R² Train | MAE Test | RMSE Test | R² Test |
|---|---:|---:|---:|---:|---:|---:|
| **Regresión Lineal** | 0.1592 | 0.1962 | 0.9541 | **0.1553** | **0.1966** | **0.9532** |
| XGBoost | 0.1292 | 0.1626 | 0.9685 | 0.1678 | 0.2138 | 0.9447 |
| Red Neuronal | 0.1457 | 0.1832 | 0.9600 | 0.1800 | 0.2290 | 0.9366 |
| Random Forest | 0.0712 | 0.0889 | 0.9906 | 0.1883 | 0.2429 | 0.9286 |

### 🏆 Modelo seleccionado: Regresión Lineal

Aunque algunos modelos consiguieron resultados especialmente buenos durante el entrenamiento, la **Regresión Lineal presentó el mejor desempeño sobre el conjunto de prueba**, con un R² de **0.9532**.

También mostró valores similares entre entrenamiento y prueba, lo que indica un comportamiento estable frente a datos no utilizados durante el ajuste del modelo.

Por esta razón fue seleccionada para integrarse en EduPath AI.

---

# 📏 ¿Qué significan estas métricas?

Para facilitar la lectura a personas que no estén familiarizadas con Machine Learning:

### MAE — Error Absoluto Medio

Representa, en promedio, qué tan alejadas se encuentran las predicciones del valor real.

**Un valor menor indica menor error.**

### RMSE — Raíz del Error Cuadrático Medio

También mide el error de las predicciones, pero penaliza con mayor intensidad los errores grandes.

**Un valor menor es mejor.**

### R² — Coeficiente de determinación

Indica qué proporción de la variación observada puede explicar el modelo.

Un R² de **0.9532** indica que, sobre el conjunto de prueba utilizado en este proyecto, el modelo explica aproximadamente el **95.32 % de la variabilidad del rendimiento académico**.

---

# 📂 Estructura del repositorio

El repositorio está organizado para separar cada componente del proyecto:

```text
EduPath-AI/
│
├── App/
│   ├── app.py
│   ├── requirements.txt
│   ├── modelo_gpa.pkl
│   ├── services/
│   ├── ui/
│   ├── views/
│   └── .streamlit/
│
├── Notebook/
│   ├── Proyecto_Final.ipynb
│   └── Student_performance_data.csv
│
├── Reporte/
│   └── Reporte_Final_EduPath_AI.pdf
│
└── README.md
```

### 📓 `Notebook/`

Contiene el proceso de Ciencia de Datos utilizado para desarrollar el proyecto, desde la exploración de los datos hasta la comparación de los modelos.

### 💻 `App/`

Contiene la aplicación web EduPath AI y los archivos necesarios para ejecutarla.

### 📄 `Reporte/`

Contiene el documento técnico en el que se describe con mayor detalle el desarrollo del proyecto.

---

# ▶️ ¿Cómo revisar el notebook?

El archivo principal del análisis es:

```text
Notebook/Proyecto_Final.ipynb
```

Puede abrirse utilizando:

- Google Colab;
- Jupyter Notebook;
- JupyterLab;
- Visual Studio Code con soporte para notebooks.

## Opción recomendada: Google Colab

Para una persona que no tenga configurado Python en su computadora, Google Colab es la alternativa más sencilla.

1. Descargar el archivo `Proyecto_Final.ipynb`.
2. Entrar a Google Colab.
3. Seleccionar **Archivo → Subir notebook**.
4. Abrir el notebook.
5. Ejecutar las celdas en orden.

El conjunto de datos utilizado se encuentra dentro de la carpeta `Notebook/`.

> Para reproducir el análisis es necesario que el notebook tenga acceso al archivo `Student_performance_data.csv`.

---

# 🌐 ¿Cómo probar EduPath AI?

La forma más sencilla **no requiere instalar absolutamente nada**.

Solo es necesario abrir:

https://edupath-ai-dorykjkgjwtdrych9ka2yn.streamlit.app

La aplicación se ejecuta directamente desde el navegador.

Una vez dentro:

1. Ingresar las características solicitadas del estudiante.
2. Seleccionar **Analizar estudiante**.
3. Esperar el procesamiento.
4. Consultar el promedio académico estimado.
5. Revisar el nivel de riesgo.
6. Consultar las fortalezas.
7. Revisar las señales de atención.
8. Consultar las recomendaciones generadas.

---

# 💻 ¿Cómo ejecutar la aplicación localmente?

Para usuarios que deseen revisar el código y ejecutar EduPath AI en su computadora:

### 1. Descargar o clonar el repositorio

```bash
git clone https://github.com/Alexia-Martinez2207/EduPath-AI.git
```

### 2. Entrar a la carpeta de la aplicación

```bash
cd EduPath-AI/App
```

### 3. Crear un entorno virtual

```bash
python3 -m venv .venv
```

### 4. Activar el entorno

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 6. Ejecutar EduPath AI

```bash
python -m streamlit run app.py
```

Después de unos segundos, la aplicación se abrirá en el navegador.

---

# 🛠️ Tecnologías utilizadas

El proyecto integra diferentes herramientas de Ciencia de Datos y desarrollo:

- **Python** — lenguaje principal del proyecto.
- **Pandas** — manipulación y análisis de datos.
- **NumPy** — operaciones numéricas.
- **Scikit-learn** — entrenamiento y evaluación de modelos.
- **XGBoost** — modelo de aprendizaje supervisado.
- **TensorFlow / Keras** — desarrollo de la red neuronal.
- **Streamlit** — construcción de la aplicación web.
- **GitHub** — almacenamiento y documentación del proyecto.
- **Streamlit Community Cloud** — despliegue de la aplicación.

---

# 🔎 Alcance del proyecto

EduPath AI fue desarrollado como un **prototipo académico**.

Los resultados deben interpretarse dentro del contexto del conjunto de datos utilizado para entrenar y evaluar los modelos.

Por lo tanto, la plataforma:

- no sustituye la evaluación académica profesional;
- no determina por sí sola el futuro académico de un estudiante;
- no debe utilizarse como único criterio para tomar decisiones;
- funciona como una demostración de cómo la Ciencia de Datos puede utilizarse como herramienta de apoyo en educación.

---

# 🚀 Trabajo futuro

EduPath AI puede continuar evolucionando.

Algunas posibilidades son:

- integración con plataformas escolares;
- análisis periódico del desempeño;
- generación automática de alertas;
- seguimiento histórico por estudiante;
- paneles institucionales;
- incorporación de nuevos factores académicos;
- herramientas adicionales de explicabilidad;
- evaluación con información proveniente de diferentes instituciones educativas.

La visión a futuro es convertir la plataforma en una herramienta que permita pasar de un enfoque **reactivo** a uno **preventivo**.

---

# 🎯 Visión de EduPath AI

La tecnología no sustituye la experiencia de docentes, tutores u orientadores.

Su valor se encuentra en proporcionar herramientas que permitan aprovechar mejor la información disponible.

**EduPath AI busca utilizar los datos para detectar señales, facilitar decisiones y promover intervenciones oportunas.**

> ### Detecta señales. Actúa a tiempo.

---

# 🎓 Contexto académico

Proyecto desarrollado como parte del:

**Diplomado en Ciencia de Datos**  
**Universidad Nacional Autónoma de México**  
**Facultad de Estudios Superiores Acatlán**

Agosto de 2026.

---

# 👩‍💻 Autora

**Alexia Abigail Martínez Gómez**

Proyecto Final — Diplomado en Ciencia de Datos  
UNAM | Facultad de Estudios Superiores Acatlán
