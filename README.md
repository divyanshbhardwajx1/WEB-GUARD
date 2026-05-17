🛡️ Web Guard — Web Vulnerability Scanner
🚀 Overview

Web Guard is a Python-based Web Application Vulnerability Scanner designed to identify common security vulnerabilities in web applications. The project focuses on automating basic penetration testing tasks such as detecting SQL Injection (SQLi) and Cross-Site Scripting (XSS) vulnerabilities through crawling and payload-based testing.

Built for learning and cybersecurity research purposes, Web Guard helps developers and security enthusiasts understand how vulnerabilities are discovered during real-world VAPT (Vulnerability Assessment & Penetration Testing) processes.

✨ Features
🔎 Website Crawling & Link Extraction
💉 SQL Injection Detection
⚠️ Cross-Site Scripting (XSS) Detection
📄 Form Discovery & Analysis
🤖 Automated Payload Testing
📊 Vulnerability Reporting
🧠 Beginner-Friendly Architecture
🛠️ Technologies Used
🐍 Python
🌐 Flask
🍜 BeautifulSoup
📡 Requests
🎨 HTML / CSS
⚡ JavaScript
📂 Project Structure
Web-Guard/
│
├── app.py
├── database.py
├── test_db.py
├── vulnerable_app.py
│
├── scanner/
│   ├── crawler.py
│   ├── sqli_scanner.py
│   └── xss_scanner.py
│
├── templates/
├── static/
│
└── reports/
⚙️ Installation
📥 Clone the Repository
git clone https://github.com/divyanshbhardwajx1/WEB-GUARD.git
cd WEB-GUARD
🧪 Create Virtual Environment
python -m venv venv
▶️ Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
📦 Install Dependencies
pip install -r requirements.txt
🚀 Running the Project
python app.py

The application will run locally on:

http://127.0.0.1:5000
🧠 How It Works
🔍 The crawler extracts links and forms from the target website
💥 Test payloads are injected into forms and URLs
📡 Responses are analyzed for vulnerability indicators
📑 Vulnerabilities are displayed in reports/dashboard
🚨 Vulnerabilities Covered
💉 SQL Injection (SQLi)
⚠️ Cross-Site Scripting (XSS)
🎯 Learning Objectives

This project was built to:

🛡️ Understand VAPT workflows
🌐 Learn web application security testing
🤖 Practice Python automation
🔐 Explore secure coding techniques
📚 Gain hands-on cybersecurity experience
🚧 Future Improvements
🔑 Authentication Testing
🧾 CSRF Detection
🖼️ Clickjacking Detection
📄 PDF Report Generation
⚡ Multi-threaded Scanning
🧠 Advanced Payload Engine
📊 Admin Dashboard
⚠️ Disclaimer

This project is developed strictly for educational and ethical security testing purposes only. Do not use this tool against systems or websites without proper authorization.

👨‍💻 Author
Divyansh Bhardwaj

🔐 Cybersecurity & VAPT Enthusiast

🌐 GitHub: https://github.com/divyanshbhardwajx1
💼 LinkedIn: https://www.linkedin.com/in/divyansh-bhardwaj1/
