# 🤖 AI Document Assistant

Asistente inteligente basado en Inteligencia Artificial para responder preguntas sobre documentación empresarial utilizando la arquitectura RAG (Retrieval-Augmented Generation).

Este proyecto fue desarrollado como parte del Challenge Final de Alura Latam.

---

# 📌 Descripción

AI Document Assistant permite consultar documentación interna de una empresa utilizando lenguaje natural.

El sistema analiza documentos PDF, genera embeddings, almacena la información en una base de datos vectorial FAISS y utiliza Google Gemini para generar respuestas basadas únicamente en el contenido de los documentos.

Empresa utilizada para el proyecto:

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
- dotenv

---

# 📄 Documentos utilizados

El agente fue entrenado utilizando documentación técnica de Santos Pegasus Soluciones:

- Onboarding
- Backend
- Incidents
- Microservices

---

# 🧠 Arquitectura del proyecto

```
Usuario
      │
      ▼
Interfaz Web (Gradio)
      │
      ▼
LangChain
      │
      ▼
Retriever (FAISS)
      │
      ▼
Google Gemini
      │
      ▼
Respuesta basada en los documentos
```

---

# 📁 Estructura del proyecto

```
AI-Document-Assistant/

│

├── app.py

├── build_vectorstore.py

├── README.md

├── requirements.txt

├── .env

├── data/

├── rag/

│ ├── loader.py

│ ├── splitter.py

│ ├── embeddings.py

│ ├── vectorstore.py

│ ├── llm.py

│ └── chain.py

├── vectorstore/

└── screenshots/
```

---

# ⚙️ Instalación

Clonar el repositorio

```bash
git clone https://github.com/MicroservicesCesar69-ui/AI-Document-Assistant.git
```

Entrar al proyecto

```bash
cd AI-Document-Assistant
```

Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno virtual

Windows

```bash
.venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear archivo `.env`

```
GOOGLE_API_KEY=TU_API_KEY
```

Construir la base vectorial

```bash
python build_vectorstore.py
```

Ejecutar el asistente

```bash
python app.py
```

---

# 💬 Preguntas de ejemplo

- ¿Cómo funciona el proceso de onboarding?
- ¿Qué arquitectura utiliza la empresa?
- ¿Qué tecnologías utiliza el backend?
- ¿Cómo se gestionan los incidentes?
- ¿Qué ventajas ofrece la arquitectura de microservicios?

---

# 📷 Capturas

## Interfaz

Agregar aquí una captura de la aplicación ejecutándose.

```
screenshots/interfaz.png
```

## Oracle Cloud

Agregar aquí una captura del despliegue en OCI.

```
screenshots/oracle.png
```

---

# ☁️ Deploy

El proyecto será desplegado en Oracle Cloud Infrastructure (OCI).

---

# 👨‍💻 Autor

Desarrollado por:

**Dr. César**

GitHub:

https://github.com/MicroservicesCesar69-ui