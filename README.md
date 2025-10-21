# 🧠 IELTS Buddy RAG Chatbot  
**Akbank GenAI Bootcamp – Yeni Nesil Proje Kampı**  

Bu proje kapsamında, **Retrieval-Augmented Generation (RAG)** mimarisi kullanılarak bir **IELTS konuşma pratiği chatbot’u** geliştirilmiştir.  
Chatbot, kullanıcıdan gelen sorulara IELTS Speaking part'ındaki örnek soru-cevap veri seti üzerinden anlam temelli yanıtlar üretir.  

---

## 🎯 Projenin Amacı  
Bu çalışmanın amacı, dil öğrenen kullanıcıların IELTS Speaking sınavına hazırlanırken **doğal ve kişiselleştirilmiş yanıtlar** üretebilen bir yapay zeka destekli asistan ile etkileşim kurmasını sağlamaktır.  
Chatbot, hem örnek yanıtlardan **doğrudan bilgi çekebilir** (retrieval) hem de **Gemini API** aracılığıyla yeni, özgün cevaplar **üretebilir (generation)**.  

---

## 📊 Veri Seti  

Kullanılan veri seti, **IELTS Speaking Part 1-2-3** bölümlerine ait örnek soru-cevaplardan oluşmaktadır.  
Her kayıt şu formatta yapılandırılmıştır:  

```json
{
  "instruction": "Do you have a bike now?",
  "response": "Yes, I do have a bike now. I use it mainly for short trips around my neighborhood..."
}
⚙️ Kullanılan Teknolojiler
Katman	Teknoloji
LLM / Generation Model	Google Gemini API (gemini-2.0-flash)
Embedding Model	text-embedding-004 (Google Generative AI Embeddings)
Vektör Veritabanı	ChromaDB
Framework	LangChain
Arayüz	Streamlit
Programlama Dili	Python 3.11
Paket Yönetimi	pip, requirements.txt

🧩 Mimari Akış (RAG Pipeline)
1️⃣ Kullanıcı girişi (soru) alınır
2️⃣ Vektör benzerliği ile en yakın IELTS yanıtları ChromaDB üzerinden bulunur
3️⃣ Gemini API modeli, bu bağlamı kullanarak yeni, doğal bir yanıt üretir
4️⃣ Streamlit arayüzü, hem girdiyi hem de üretimi kullanıcıya gösterir

📈 Böylece chatbot hem bilgiye dayalı hem de özgün cevaplar sunar.

💬 Örnek Diyalog
Kullanıcı: What do you usually do in your free time?
Chatbot:

Well, it really depends on how much free time I actually have. If I'm just talking about a spare hour or two, I usually unwind by listening to music or catching up on news online.

🖥️ Çalıştırma Kılavuzu
🔧 Ortam Kurulumu
bash
Kodu kopyala
git clone https://github.com/illkaysari/ielts-buddy-rag.git  
cd ielts-buddy-rag  
python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt  
🧠 Vektör Veritabanı Oluşturma
bash
Kodu kopyala
python src/ingest.py
💬 Chatbot’u Başlatma
bash
Kodu kopyala
streamlit run src/app.py
Tarayıcıda açılacak sayfa üzerinden chatbot kullanılabilir.

🌐 Web Arayüzü
👉 Streamlit Web Uygulaması (Deploy Link) (isteğe bağlı olarak eklenecektir)

Kullanıcı, web arayüzü üzerinden soru yazarak anında yanıt alabilir.

🏁 Sonuç
Bu proje, RAG mimarisinin dil eğitimi alanındaki potansiyelini göstermektedir.
IELTS Buddy, yalnızca IELTS’e yönelik değil, ilerleyen sürümlerde TOEFL, YDS gibi sınavlar için de ölçeklenebilir bir altyapıya sahiptir.

👩‍💻 Geliştirici
İlkay Sarı
📍 Antalya, Türkiye

yaml
Kodu kopyala

---
