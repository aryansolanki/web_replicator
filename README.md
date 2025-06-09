# 🌐 Web Replicator

A full-stack web application that takes a public website URL, scrapes the website for design context, and generates HTML to replicate the website as closely as possible.

---

## 📁 Project Structure

web_replicator/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── clone.py
│   │   ├── services/
│   │   │   └── scraper.py
│   │   ├── utils/
│   │   │   └── cleaner.py
│   │   └── main.py
│   ├── venv/ (DO NOT COMMIT)
│   ├── .env (DO NOT COMMIT)
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── README.md
│
├── .gitignore
└── README.md


---

## 🚀 How to Run

### Backend Setup (Python)

1. **Navigate to the backend:**
   ```bash
   cd backend
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   - On Windows:
     ```powershell
     .\venv\Scripts\activate
     ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up environment variables:**
   - Create a `.env` file and add:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
6. **Start the backend server:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

### Frontend Setup (Node.js)

1. **Navigate to the frontend:**
   ```bash
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the frontend:**
   ```bash
   npm run dev
   ```

---

## 🔒 Environment Variables

- Make sure to create a `.env` file inside the **backend** folder and add:
  ```
  GEMINI_API_KEY=your_gemini_api_key_here
  ```

---

## 🤝 Contributing

Feel free to fork and contribute to this project! PRs are welcome.

---

## 📝 Notes

- This project uses HTTP scraping by default. Playwright scraping can be enabled if needed.
- Adjust CORS settings and environment variables as needed.

---

## 📧 Contact

For questions or suggestions, please reach out via GitHub issues or discussions.

---
