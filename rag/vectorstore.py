from langchain_community.vectorstores import FAISS
from rag.embeddings import crear_embeddings


def crear_vectorstore(chunks):

    embeddings = crear_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Guardar automáticamente en disco
    vectorstore.save_local("vectorstore")

    print("✅ Base vectorial guardada en disco.")

    return vectorstore


def cargar_vectorstore():

    embeddings = crear_embeddings()

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore