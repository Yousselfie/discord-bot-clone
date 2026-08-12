import chromadb

def retrieve(question, k=4): #4 chunks (grabs 4 most relevant chunks to message)
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("knowledge")
    results = collection.query(query_texts=[question], n_results=k)
    return "\n\n".join(results["documents"][0]) #the 4 chunks separated by two lines to be returned as a single string as the context of the llm
