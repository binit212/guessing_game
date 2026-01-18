# 🎯 Guess The Number Game (Flask Web App)

A full-stack web-based guessing game built with Flask where players compete on a **global leaderboard** powered by PostgreSQL.  
The game includes difficulty levels, score calculation, session-based gameplay, and cloud database integration.

🔗 **Live Demo:**  
https://guessing-game-1-gd9r.onrender.com/

---

## 🚀 Features

- 🎮 Interactive guessing game
- 🧠 Difficulty levels (Easy / Medium / Hard)
- 🔐 Session-based player handling
- 📝 Guess history tracking
- ❌ Duplicate guess prevention
- ⏱ Time-based scoring system
- 🏆 Global leaderboard (PostgreSQL)
- 🎨 Modern responsive UI
- ☁ Cloud deployment on Render

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- Jinja2 Templates

### Backend
- Python
- Flask

### Database
- PostgreSQL (Render Cloud)

### Deployment
- Gunicorn
- Render Hosting

---

## ⚙ Installation (Run Locally)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Binit212/guessing_game.git
cd guessing_game
```
2️⃣ Create Virtual Environment

  ```bash
  python -m venv venv
  ```
Activate:

Windows

```bash
venv\Scripts\activate
 ```
Mac/Linux

```bash
  source venv/bin/activate
 ```
3️⃣ Install Dependencies

 ```bash
 pip install -r requirements.txt
 ```
4️⃣ Set Environment Variable

Create DATABASE_URL environment variable:

Windows (PowerShell)

 ```bash
setx DATABASE_URL "your_postgresql_connection_string"
  ```
 Restart terminal after setting.

 5️⃣ Run Application

 ```bash
python app.py
```
6️⃣ Open Browser

Visit:
 ```bash
http://127.0.0.1:5000
```

## 🎮 How To Play

- Enter your name
- Select difficulty
- Guess the number
- Avoid duplicate guesses
- Win using fewer attempts and less time
- View your rank on leaderboard


## 📊 Scoring Logic

Score is calculated using:

- Remaining attempts
- Time taken to guess correctly

Higher score + lower time = higher leaderboard rank.


## 📁 Project Structure
```
guessing_game/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── index.html
│   └── leaderboard.html
│
└── static/
    └── style.css
```

## 🔒 Security Practices

- Environment variables used for database credentials
- Parameterized SQL queries (prevents SQL injection)
- Flask sessions for per-user game isolation
- Secrets never hardcoded


## 📌 Future Improvements

- User authentication system
- Player profiles
- Sound effects
- Multiplayer rooms
- Admin dashboard
- PostgreSQL analytics
- Mobile app version


## 👨‍💻 Author

Developed by **BINIT**

GitHub:  
https://github.com/Binit212


⭐ If you like this project, please give it a star!

