# 🛡️ Web Guard — Web Vulnerability Scanner

## 🚀 Overview
Web Guard is a Python-based **Web Application Vulnerability Scanner** designed to identify common security vulnerabilities in web applications. The project focuses on automating basic penetration testing tasks such as detecting **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** vulnerabilities through crawling and payload-based testing.

Built for learning and cybersecurity research purposes, Web Guard helps developers and security enthusiasts understand how vulnerabilities are discovered during real-world **VAPT (Vulnerability Assessment & Penetration Testing)** processes.

---

# ✨ Features
- 🔎 Website Crawling & Link Extraction  
- 💉 SQL Injection Detection  
- ⚠️ Cross-Site Scripting (XSS) Detection  
- 📄 Form Discovery & Analysis  
- 🤖 Automated Payload Testing  
- 📊 Vulnerability Reporting  
- 🧠 Beginner-Friendly Architecture  

---

# 🛠️ Technologies Used
- 🐍 Python  
- 🌐 Flask  
- 🍜 BeautifulSoup  
- 📡 Requests  
- 🎨 HTML / CSS  
- ⚡ JavaScript  

---


# ⚙️ Installation

## 📥 Clone the Repository

```bash
git clone https://github.com/divyanshbhardwajx1/WEB-GUARD.git
cd WEB-GUARD
```

## 🧪 Create Virtual Environment

```bash
python -m venv venv
```

## ▶️ Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

```bash
python app.py
```

The application will run locally on:

```bash
http://127.0.0.1:5000
```

---

# 🧠 How It Works
1. 🔍 The crawler extracts links and forms from the target website  
2. 💥 Test payloads are injected into forms and URLs  
3. 📡 Responses are analyzed for vulnerability indicators  
4. 📑 Vulnerabilities are displayed in reports/dashboard  

---

# 🚨 Vulnerabilities Covered
- 💉 SQL Injection (SQLi)  
- ⚠️ Cross-Site Scripting (XSS)  

---

# 🎯 Learning Objectives
This project was built to:
- 🛡️ Understand VAPT workflows  
- 🌐 Learn web application security testing  
- 🤖 Practice Python automation  
- 🔐 Explore secure coding techniques  
- 📚 Gain hands-on cybersecurity experience  

---

# 🚧 Future Improvements
- 🔑 Authentication Testing  
- 🧾 CSRF Detection  
- 🖼️ Clickjacking Detection  
- 📄 PDF Report Generation  
- ⚡ Multi-threaded Scanning  
- 🧠 Advanced Payload Engine  
- 📊 Admin Dashboard  

---

# ⚠️ Disclaimer
This project is developed strictly for **educational and ethical security testing purposes only**. Do not use this tool against systems or websites without proper authorization.

---

# 👨‍💻 Author

## Divyansh Bhardwaj  
🔐 Cybersecurity & VAPT Enthusiast  

- 🌐 GitHub: https://github.com/divyanshbhardwajx1  
- 💼 LinkedIn: https://www.linkedin.com/in/divyansh-bhardwaj1/
