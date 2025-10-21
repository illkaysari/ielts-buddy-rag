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