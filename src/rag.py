import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_core.runnables import RunnableMap, RunnableLambda


import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate

# 🔹 Gemini API anahtarı
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🔹 Embedding modeli
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 🔹 Vektör veritabanını yükle
vectordb = Chroma(persist_directory="vectordb", embedding_function=embeddings)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# 🔹 Prompt (cevap biçimi)
prompt_template = """
You are IELTS Speaking Coach AI.
Use the following context to answer naturally and clearly.

Context: {context}
Question: {question}

Answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# 🔹 Sorgu fonksiyonu
def ask_ielts(question: str):
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt.format(context=context, question=question))
    return response.text.strip()

if __name__ == "__main__":
    print("🤖 IELTS Buddy Chatbot is ready! Type your question (or 'exit' to quit):")
    while True:
        q = input("You: ")
        if q.lower() == "exit":
            break
        print("Bot:", ask_ielts(q))
