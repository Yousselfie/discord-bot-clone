import chromadb, glob, os

client = chromadb.PersistentClient(path="./chroma_db") # saves to disk
collection = client.get_or_create_collection("knowledge")

# load and chunk my knowledge documents
docs, ids = [], []
for path in glob.glob("knowledge/*.md"):
    text = open(path, encoding="utf-8").read()
    # chunking ~500 char pieces
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    for j, chunk in enumerate(chunks):
        docs.append(chunk)
        ids.append(f"{os.path.basename(path)}-{j}")

collection.add(documents=docs, ids=ids) #chroma embeds these automatically
print(f"Indexed {len(docs)} chunks")
