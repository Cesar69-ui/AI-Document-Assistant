from rag.vectorstore import cargar_vectorstore
from rag.llm import crear_llm


class RAGChain:

    def __init__(self):

        print("Cargando base vectorial...")

        self.vectorstore = cargar_vectorstore()

        print("✅ Base vectorial cargada.")

        self.llm = crear_llm()

    def responder(self, pregunta):

        resultados = self.vectorstore.similarity_search(
            pregunta,
            k=5
        )

        contexto = "\n\n".join(
            [doc.page_content for doc in resultados]
        )

        prompt = f"""
Responde únicamente utilizando la información del contexto.

Si la respuesta no aparece en el contexto responde:

"No encontré esa información en los documentos."

Contexto:

{contexto}

Pregunta:

{pregunta}
"""

        respuesta = self.llm.invoke(prompt)

        contenido = respuesta.content

        if isinstance(contenido, list):

            texto = ""

            for bloque in contenido:

                if (
                    isinstance(bloque, dict)
                    and bloque.get("type") == "text"
                ):

                    texto += bloque.get("text", "")

            return texto

        return contenido