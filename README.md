# Web Replicator

A **full-stack web application** that takes a public website URL, **scrapes its HTML**, and **uses an LLM (Gemini 2.5 Pro)** to generate a **replicated HTML page** that closely mimics the design of the original site. This project helps designers and developers understand and reuse web layouts while stripping out unnecessary analytics or ads.

---

## 🚀 Project Overview

- **Backend:** FastAPI (Python)
  - Scrapes websites using HTTP and (optionally) Playwright for JavaScript-heavy sites.
  - Calls the Gemini 2.5 Pro model to generate clean, aesthetic HTML output.
  - Includes a modular structure with separate services and utilities.

- **Frontend:** React (or your chosen framework)
  - Sends the website URL to the backend.
  - Displays the cloned HTML result.
  - Supports easy local development.

- **LLM Integration:**
  - Uses Gemini 2.5 Pro from Google’s API.
  - Accepts cleaned HTML from the scraper and generates high-quality replicated HTML.

---

## 🗂️ Project Structure
'''
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
'''

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


## 📝 Notes

- This project uses HTTP scraping by default. Playwright scraping can be enabled if needed.
- Adjust CORS settings and environment variables as needed.

---

🔥 Usage
Open the frontend app in your browser.

Enter the URL of the site you want to replicate.

The backend scrapes the site, cleans the HTML, sends it to Gemini 2.5 Pro, and returns a replicated HTML page.

The frontend displays the result.

---

🔎 Additional Notes
✅ The project uses HTTP scraping by default for speed and reliability. Playwright (browser-based scraping) is optional but recommended for JavaScript-heavy sites.
✅ Gemini 2.5 Pro is used for high-quality, aesthetic HTML generation.
✅ The .env file should never be committed to GitHub (it’s already in .gitignore).
✅ This app is intended for educational and prototyping purposes; respect the robots.txt and terms of use of the target websites.

---

📃 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

🤝 Contributions
Feel free to fork the repo, submit pull requests, or suggest improvements!

