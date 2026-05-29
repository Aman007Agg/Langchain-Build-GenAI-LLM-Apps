import streamlit as st
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from openai import models

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# llm = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)
llm = ChatOllama(model="llama3.2")

outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are a professional blogger.
    Create an outline for a blog post on the following topic: {topic}
    The outline should include:
    - Introduction
    - 3 main points with subpoints
    - Conclusion
    """
)

introduction_prompt = PromptTemplate(
    input_variables=["outline"],
    template="""You are a professional blogger.
    Write an engaging introduction paragraph based on the following
    outline:{outline}
    The introduction should hook the reader and provide a brief
    overview of the topic.
    """
)

first_chain = outline_prompt | llm | StrOutputParser()
second_chain = introduction_prompt | llm
overall_chain = first_chain | second_chain

st.title("Blog Post Generator")

topic = st.text_input("Input Topic")

if topic:
    response = overall_chain.invoke({"topic": topic})
    st.write(response.content)

