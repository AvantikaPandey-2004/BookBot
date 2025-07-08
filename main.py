from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_milvus import Milvus
from dotenv import load_dotenv
import os
import csv

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize Gemini embeddings
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)

# Connect to Milvus vector store
vectorstore = Milvus(embedding_function=embedding, collection_name="books_index")

# Load book data from CSV
def load_documents_from_csv(file_path):
    documents = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            content = f"Title: {row['title']}\nAuthor: {row['author']}\nDescription: {row['description']}"
            documents.append({"content": content, "metadata": {"title": row['title'], "author": row['author']}})
    return documents

books_data = load_documents_from_csv("data/books.csv")

# Index into Milvus
for doc in books_data:
    vectorstore.add_document(doc)

print("✅ Book data indexed successfully using Gemini embeddings.")
