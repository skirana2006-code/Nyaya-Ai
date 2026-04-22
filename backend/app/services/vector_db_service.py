import chromadb

# Initialize Chroma client
client = chromadb.Client()

# Create collection
collection = client.get_or_create_collection(name="legal_docs")


def store_embeddings(chunks, embeddings):
    """
    Store text chunks and their embeddings in ChromaDB
    """

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )