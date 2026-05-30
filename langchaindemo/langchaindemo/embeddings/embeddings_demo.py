import os
# from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# llm=OpenAIEmbeddings(api_key=OPENAI_API_KEY)
llm = OllamaEmbeddings(model="llama3.2")

text = input("Enter the text")
response = llm.embed_query(text)
print(response)