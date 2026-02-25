# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 09:39:14 2026

@author: Personal
"""
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Initialize ChromaDB (local, in-memory)
client = chromadb.Client()
collection = client.create_collection(name="syllabus")

# 3. Load syllabus and split into chunks
with open("syllabus.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# 4. Embed and store chunks
embeddings = model.encode(lines).tolist()

collection.add(
    documents=lines,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(lines))]
)

print("Syllabus loaded and indexed.\n")

# 5. CLI loop
while True:
    query = input("Ask a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    # 6. Embed the query
    query_embedding = model.encode([query]).tolist()

    # 7. Retrieve relevant chunks
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=2
    )

    retrieved_docs = results["documents"][0]

    # 8. Simple RAG-style response
    print("\nRelevant Information:")
    for doc in retrieved_docs:
        print("-", doc)

    print("\nAnswer (based on syllabus):")
    print(retrieved_docs[0])
    print("-" * 50)

