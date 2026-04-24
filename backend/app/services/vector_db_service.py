import numpy as np

store = {"chunks": [], "embeddings": []}

def store_embeddings(chunks, embeddings):
    store["chunks"] = chunks
    store["embeddings"] = embeddings

def query_embeddings(query_embedding, n_results=3):
    if not store["embeddings"]:
        return []
    
    embs = np.array(store["embeddings"])
    query = np.array(query_embedding)
    
    scores = np.dot(embs, query) / (np.linalg.norm(embs, axis=1) * np.linalg.norm(query) + 1e-9)
    top_indices = np.argsort(scores)[::-1][:n_results]
    
    return [store["chunks"][i] for i in top_indices]