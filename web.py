import gradio as gr

from rag.chain import RAGChain


print("Inicializando RAG...")

rag = RAGChain()

print("RAG listo.")


def responder(pregunta):

    if not pregunta.strip():
        return "Escribe una pregunta."

    return rag.responder(pregunta)


demo = gr.Interface(

    fn=responder,

    inputs=gr.Textbox(

        label="Pregunta",

        placeholder="Escribe una pregunta sobre los documentos..."

    ),

    outputs=gr.Textbox(

        label="Respuesta"

    ),

    title="🤖 AI Agent - RAG",

    description="Chatbot basado en LangChain + FAISS + Gemini"

)


demo.launch()