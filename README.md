# 🧠 IELTS Buddy RAG Chatbot  
*Akbank GenAI Bootcamp – Next Generation Project Camp*

This project presents an *IELTS speaking practice chatbot* built using *Retrieval-Augmented Generation (RAG)* architecture. The chatbot generates semantically grounded responses to user queries by drawing from a dataset of IELTS Speaking sample question-answer pairs.

---

## 🎯 Project Goal

The aim of this project is to enable language learners preparing for the IELTS Speaking exam to interact with an AI-powered assistant capable of producing *natural and personalized responses. The chatbot can both **retrieve information directly* from sample answers and *generate new, original responses* via the *Gemini API*.

---

## 📊 Dataset

The dataset consists of sample question-answer pairs from *IELTS Speaking Parts 1, 2, and 3*. Each record is structured as follows:

```json
{
  "instruction": "Do you have a bike now?",
  "response": "Yes, I do have a bike now. I use it mainly for short trips around my neighborhood..."
}

## ⚙️ Tech Stack


|Layer                     |Technology                            |
|--------------------------|--------------------------------------|
|*LLM / Generation Model*|Google Gemini API (⁠ gemini-2.0-flash ⁠)|
|*Embedding Model*       |⁠ text-embedding-004 ⁠                  |
|*Vector Database*       |ChromaDB                              |
|*Framework*             |LangChain                             |
|*Interface*             |Streamlit                             |
|*Programming Language*  |Python 3.11                           |
|*Package Management*    |pip, ⁠ requirements.txt ⁠               |


---

## 🧩 RAG Pipeline

	1.	User input (question) is received
	2.	Vector similarity search retrieves the most relevant IELTS answers from ChromaDB
	3.	Gemini API uses this context to generate a new, natural response
	4.	Streamlit interface displays both the input and the generated output 

📈 Böylece chatbot hem bilgiye dayalı hem de özgün cevaplar sunar. 

## 💬 Sample Dialogue
**User:** What do you usually do in your free time?
**Chatbot:** Well, it really depends on how much free time I actually have. If I'm just talking about a spare hour or two, I usually unwind by listening to music or catching up on news online.

## 🖥️ Setup & Usage
bash
⁠Clone the repo and install dependencies
git clone https://github.com/illkaysari/ielts-buddy-rag.git  
cd ielts-buddy-rag  
python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  

## 🧠 Build the Vector Data Base

bash
Copy the Code
python src/ingest.py

## 💬 Launch the Chatbot
bash
Copy the Code
streamlit run src/app.py
The chatbot can be used via the page that opens in the browser.

## 🌐 Live Demo

## 👉 Streamlit Web App: https://ielts-buddy-rag.streamlit.app

Users can ask questions via the web interface and receive an instant reply.

## 🏁 Conclusion
This project demonstrates the potential of RAG architecture in the field of language education. IELTS Buddy is built on a scalable foundation — future versions could extend support to other exams such as TOEFL and YDS.


## 👩‍💻 Developer
  İlkay Sarı 
