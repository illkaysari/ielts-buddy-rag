import json
from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# JSON dosyalarının yolları
data_folder = "data"
files = ["ielts_new.json", "ielts_old.json"]

# Tüm soruları ve cevapları tek bir listeye al
texts = []
for f in files:
    path = os.path.join(data_folder, f)
    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
            for item in data:
                question = item.get("question") or item.get("Q") or item.get("instruction") or ""
                answer = item.get("answer") or item.get("A") or item.get("response") or ""
                if question and answer:
                    texts.append(f"Q: {question}\nA: {answer}")

print(f"Toplam {len(texts)} soru-cevap yüklendi.")

# Metinleri küçük parçalara böl
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.create_documents(texts)
print(f"Toplam {len(docs)} metin parçası oluşturuldu.")

# Embedding modeli
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Chroma veritabanına kaydet
Chroma.from_documents(docs, embeddings, persist_directory="vectordb").persist()
print("✅ Veri başarıyla vektör veritabanına kaydedildi (vectordb klasörüne).")
