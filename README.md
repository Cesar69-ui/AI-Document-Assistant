# 🤖 AI Document Assistant

Asistente inteligente basado en Inteligencia Artificial para consultar documentación empresarial mediante lenguaje natural utilizando la arquitectura **RAG (Retrieval-Augmented Generation)**.

Este proyecto fue desarrollado como parte del **Challenge Final de Alura Latam**, integrando procesamiento de documentos, recuperación de información mediante bases vectoriales y generación de respuestas utilizando modelos de lenguaje.

---

# 📌 Descripción

AI Document Assistant permite realizar preguntas sobre documentación interna de una empresa y obtener respuestas precisas fundamentadas únicamente en el contenido de los documentos proporcionados.

El sistema procesa documentos PDF, genera embeddings mediante Sentence Transformers, almacena la información en una base vectorial FAISS y utiliza Google Gemini para generar respuestas contextualizadas.

Empresa utilizada para este proyecto:

**Santos Pegasus Soluciones**

---

# 🚀 Tecnologías utilizadas

- Python 3.11
- LangChain
- Google Gemini
- HuggingFace Embeddings
- Sentence Transformers
- FAISS
- Gradio
- PyPDF
- python-dotenv

---

# 📄 Documentación utilizada

El agente fue entrenado utilizando documentación técnica de Santos Pegasus Soluciones:

- Manual de Onboarding
- Guía Oficial de Ingeniería Back-end
- Protocolo de Respuesta a Incidentes
- Arquitectura de Microservicios

---

# 🧠 Arquitectura del sistema

```
                     Usuario
                        │
                        ▼
             Interfaz Web (Gradio)
                        │
                        ▼
                  LangChain RAG
                        │
                        ▼
          Recuperación desde FAISS
                        │
                        ▼
              Google Gemini (LLM)
                        │
                        ▼
         Respuesta basada en documentos
```

---

# ⚙️ Funcionamiento

El flujo de trabajo del asistente sigue las siguientes etapas:

1. El usuario escribe una pregunta en lenguaje natural.
2. LangChain consulta la base vectorial FAISS.
3. Se recuperan los fragmentos de documentos más relevantes.
4. Google Gemini genera una respuesta utilizando únicamente el contexto recuperado.
5. La respuesta es presentada al usuario mediante la interfaz desarrollada con Gradio.

---

# 📁 Estructura del proyecto

```
AI-Document-Assistant
│
├── app.py
├── web.py
├── build_vectorstore.py
├── README.md
├── requirements.txt
├── .env.example
│
├── data
│
├── rag
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── llm.py
│   └── chain.py
│
├── vectorstore
│
├── assets
│
└── screenshots
```

---

# ⚙️ Instalación

## Clonar el repositorio

```bash
git clone https://github.com/MicroservicesCesar69-ui/AI-Document-Assistant.git
```

## Entrar al proyecto

```bash
cd AI-Document-Assistant
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno virtual

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configurar variables de entorno

Crear un archivo `.env` con el siguiente contenido:

```text
GOOGLE_API_KEY=TU_API_KEY
```

## Construir la base vectorial

```bash
python build_vectorstore.py
```

## Ejecutar la aplicación

Modo consola

```bash
python app.py
```

Modo interfaz web (Gradio)

```bash
python web.py
```

---

# 💬 Preguntas de ejemplo

- ¿Cómo funciona el proceso de onboarding?
- ¿Qué arquitectura utiliza la empresa?
- ¿Qué tecnologías utiliza el backend?
- ¿Cómo se gestionan los incidentes?
- ¿Qué ventajas ofrece la arquitectura de microservicios?
- ¿Cuál es el protocolo de respuesta a incidentes?

---

# 📷 Evidencias

## Funcionamiento local

El asistente fue ejecutado correctamente en un entorno local utilizando Gradio como interfaz web.

### Interfaz del asistente

![Interfaz](screenshots/interfaz.png)

### Ejecución del proyecto

Durante la ejecución se cargaron correctamente los documentos utilizados para construir la base vectorial.

![Terminal](screenshots/terminal.png)

---

## Despliegue en Oracle Cloud Infrastructure (OCI)

Se realizó la configuración del despliegue utilizando Oracle Cloud Infrastructure (OCI). Sin embargo, durante la creación de la instancia Always Free (VM.Standard.A1.Flex), Oracle devolvió un error temporal de capacidad en la región seleccionada, por lo que no fue posible completar el despliegue.

Este inconveniente corresponde a una limitación temporal de disponibilidad de infraestructura por parte de Oracle y no a un problema del proyecto.

![Oracle OCI](screenshots/oracle_error.png)
```

---

## Construcción de la base vectorial

Agregar una captura del proceso de creación del vectorstore.

Ejemplo:

```
screenshots/vectorstore.png
```

---

## Despliegue

Como parte del Challenge se configuró el proceso de despliegue utilizando **Oracle Cloud Infrastructure (OCI)**.

Durante el desarrollo se realizaron las siguientes configuraciones:

- Creación de Virtual Cloud Network (VCN)
- Configuración de Public Subnet
- Configuración de Internet Gateway
- Configuración de Compute Instance
- Configuración de claves SSH

Durante la creación de la instancia Oracle Cloud devolvió el siguiente mensaje:

> **Out of capacity for shape VM.Standard.A1.Flex in availability domain AD-1**

Este mensaje corresponde a una limitación temporal de capacidad de Oracle Cloud en la región utilizada y no a un error de implementación del proyecto.

Como evidencia del proceso se incluyen capturas de pantalla de la configuración realizada y del mensaje emitido por Oracle Cloud.

Ejemplos:

```
screenshots/oracle_vcn.png

screenshots/oracle_subnet.png

screenshots/oracle_instance.png

screenshots/oracle_capacity_error.png
```

---

# 📌 Características principales

- Consulta documentos PDF mediante lenguaje natural.
- Arquitectura RAG utilizando LangChain.
- Recuperación semántica mediante FAISS.
- Integración con Google Gemini.
- Interfaz web desarrollada con Gradio.
- Base vectorial construida mediante Sentence Transformers.

---

# 👨‍💻 Autor

**Dr. César**

GitHub:

https://github.com/MicroservicesCesar69-ui

---

# 📄 Licencia

Proyecto desarrollado con fines académicos como parte del Challenge Final de Alura Latam.