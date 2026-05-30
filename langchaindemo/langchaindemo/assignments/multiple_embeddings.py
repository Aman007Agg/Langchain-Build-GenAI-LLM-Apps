import os
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

# from langchaindemo.langchaindemo.rag.historyaware_rag_demo import embeddings

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
embeddings = OllamaEmbeddings(model="llama3.2")

response = embeddings.embed_documents(
    [
        "I love playing video games",
        "I am going to the movie",
        "I love coding",
        "Hello World!"
    ]
)

print(len(response))
print(response[0])
