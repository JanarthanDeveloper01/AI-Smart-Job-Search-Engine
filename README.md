# 💼 AI Smart Job Search Engine

An **AI-powered web application** that analyzes a user's resume and recommends **relevant job roles** along with **direct job search links** from platforms like LinkedIn, Indeed, and Naukri.

---

## 📌 Features

* 📄 Upload Resume (PDF / DOCX)
* 🤖 AI-based Resume Analysis using Gemini API
* 🎯 Dynamic Job Role Detection (based on skills)
* 🔁 Hybrid AI + Rule-based fallback system
* 🔎 Job Recommendations for multiple roles
* 🔗 Direct job links (LinkedIn, Indeed, Naukri)
* 📊 Resume vs Job Match Score (ML-based)

---

## 🧠 How It Works

```text
Upload Resume
      ↓
Extract Text (PDF/DOCX)
      ↓
AI analyzes resume (Gemini API)
      ↓
Detects relevant job roles
      ↓
Fallback logic ensures accuracy
      ↓
Search jobs for each role
      ↓
Display job links + match score
```

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Google Gemini API
* **Machine Learning:** Scikit-learn (TF-IDF + Cosine Similarity)

### 📚 Libraries Used

* pdfplumber
* python-docx
* google-generativeai
* scikit-learn
* python-dotenv

---

## 📂 Project Structure

```
AI-Smart-Job-Search-Engine/
│
├── app.py
├── ai_role_extractor.py
├── resume_parser.py
├── job_search.py
├── job_matcher.py
├── requirements.txt
├── README.md
│
└── utils/
      └── helper.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/JanarthanDeveloper01/AI-Smart-Job-Search-Engine.git
cd AI-Smart-Job-Search-Engine
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```bash
python -m streamlit run app.py
```

---

## 📸 Example Output

* AI Suggested Roles:

  * Data Analyst
  * Machine Learning Engineer
  * Backend Developer

* Job Recommendations:

  * LinkedIn job links
  * Indeed job links
  * Match Score %

---

## 🔐 Security Note

* Do NOT upload `.env` file to GitHub
* Keep API keys private

---

## 🌟 Future Improvements

* 🔥 Real-time job scraping (LinkedIn API)
* 📍 Location-based job filtering
* 📉 Skill gap detection
* 📄 Resume improvement suggestions
* 📊 Job ranking system

---


If you like this project, consider giving it a ⭐ on GitHub!
