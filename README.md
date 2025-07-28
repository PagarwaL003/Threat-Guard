# 🛡️ ThreatGuard

**Detect Scam Emails & Malicious URLs with FastAPI, Gemini AI & Streamlit**

ThreatGuard is a smart web application that allows users to detect scam content in emails (via PDF/TXT upload) and classify URLs as benign, phishing, malware, or defacement. 
It uses Google Gemini AI for threat analysis, backed by a FastAPI backend and an interactive Streamlit frontend.

---

## 🚀 Features

- 📄 **Scam Email Detection**: Upload PDF or TXT files containing email or message content to identify potential scams.
- 🌐 **URL Threat Classification**: Check any URL to detect phishing, malware, defacement, or benign content.
- 🤖 **AI-Powered Analysis**: Integrates with **Google Gemini Pro API** for intelligent, contextual detection.
- 💻 **Modern UI**: Built with Streamlit for simplicity and ease of use.
- ⚡ **FastAPI Backend**: High-performance API handling and secure communication.

---

## 🧰 Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| **Frontend** | Streamlit                |
| **Backend**  | FastAPI                  |
| **AI Engine**| Google Gemini Pro API    |
| **Language** | Python                   |
| **Utilities**| PyPDF2                   |

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/PagarwaL003/Threat-Guard
cd URL_File_Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Google Gemini API Key

- Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- Open `main.py` and replace the placeholder with your API key:
  ```python
  os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
  ```

### 4. Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

### 5. Run the Streamlit UI

Open a new terminal and run:
```bash
streamlit run app.py
```

---

🌐 Access the App
Once running, open your browser and go to:

http://localhost:8501

---

## File Structure

```
URL_File_Detection/
│
├── app.py          # Streamlit UI
├── main.py         # FastAPI backend
├── requirements.txt # Dependencies
└── README.md
```

---

# 📌 Usage Guide

### 🔍 Scam Email Detection  
Upload a `.pdf` or `.txt` file containing email content.  
The AI will analyze and classify it as **Scam** or **Legit**.

---

### 🧪 URL Threat Detection  
Enter a full URL (e.g., `https://example.com`).  
The app will return one of the following:  
- ✅ Benign  
- ❗ Phishing  
- 🛑 Malware  
- 🚨 Defacement

---

### 🔐 Notes  
- Ensure the **FastAPI server (`main.py`) is running** before launching the **Streamlit UI**.  
- A valid **Google Gemini API key** is required for detection features.  
- This is an **experimental project** — do not use it in production without proper security testing.

---