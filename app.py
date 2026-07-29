from rag.chain import RAGChain


def main():

    rag = RAGChain()

    while True:

        pregunta = input("\nPregunta (escribe 'salir' para terminar): ")

        if pregunta.lower() == "salir":
            break

        respuesta = rag.responder(pregunta)

        print("\nRespuesta:\n")
        print(respuesta)


if __name__ == "__main__":
    main()