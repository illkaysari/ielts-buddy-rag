import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate

# 🔹 Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🔹 Vector DB & embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
vectordb = Chroma(persist_directory="vectordb", embedding_function=embeddings)
retriever = vectordb.as_retriever(search_kwargs={"k": 5})

# 🔹 Prompt template
prompt_template = """
You are an IELTS Speaking Coach AI.
Use the given examples in context as inspiration only — don't copy them.
Respond naturally, fluently, and with IELTS-level expressions.

Context:
{context}

Question:
{question}

Now respond as a fluent IELTS candidate would:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# 🔹 Chat function
def ask_ielts(question):
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt.format(context=context, question=question))
    return response.text.strip()

# 🔹 Streamlit UI
st.set_page_config(page_title="IELTS Buddy Coach", page_icon="🎓", layout="centered")
st.title("🎓 IELTS Buddy Coach")
st.write("Ask me any IELTS Speaking question and I’ll help you answer naturally!")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", placeholder="Type your IELTS Speaking question...")

if st.button("Ask") and user_input:
    answer = ask_ielts(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Coach", answer))

for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑‍🎓 {speaker}:** {text}")
    else:
        st.markdown(f"**🤖 {speaker}:** {text}")
