import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def crear_llm():
    """
    Carga el modelo Gemini utilizando la API Key
    almacenada en el archivo .env.
    """

    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key
    )

    return llm