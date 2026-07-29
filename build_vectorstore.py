from rag.loader import cargar_documentos
from rag.splitter import dividir_documentos
from rag.vectorstore import crear_vectorstore


def main():

    print("📄 Cargando documentos...")

    documentos = cargar_documentos()

    print(f"Documentos cargados: {len(documentos)}")

    print("\n✂ Dividiendo documentos...")

    chunks = dividir_documentos(documentos)

    print(f"Chunks generados: {len(chunks)}")

    print("\n🧠 Creando embeddings y FAISS...")

    crear_vectorstore(chunks)

    print("\n🎉 Base vectorial creada correctamente.")


if __name__ == "__main__":
    main()