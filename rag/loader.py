from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def cargar_documentos(ruta="data"):
    """
    Carga todos los archivos PDF de la carpeta indicada.
    """

    carpeta = Path(ruta)
    documentos = []

    for archivo in carpeta.glob("*.pdf"):
        print(f"Cargando: {archivo.name}")

        try:
            loader = PyPDFLoader(str(archivo))
            documentos.extend(loader.load())
            print(f"✓ {archivo.name} cargado correctamente")

        except Exception as e:
            print(f"✗ Error en {archivo.name}")
            print(e)

    return documentos