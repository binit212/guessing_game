# 🎯 Guess The Number Game (Flask Web App)

A full-stack web-based guessing game built with Flask where players compete on a live leaderboard.  
The game includes difficulty levels, score calculation, session-based gameplay, and database-backed rankings.

🔗 Live Demo: https://guessing-game-6l9j.onrender.com

---

## 🚀 Features

- 🎮 Interactive Guessing Game
- 🧠 Difficulty Levels (Easy / Medium / Hard)
- 🔐 Session-based user handling
- 📝 Guess History Tracking
- ❌ Duplicate Guess Prevention
- ⏱ Time-based Score System
- 🏆 Persistent Leaderboard (SQLite)
- 🎨 Modern UI with animations
- 📱 Responsive Design
- ☁ Deployed on Render

---

## 🛠 Tech Stack

**Frontend**
- HTML
- CSS
- Jinja2 Templates

**Backend**
- Python
- Flask

**Database**
- SQLite

**Deployment**
- Gunicorn
- Render Cloud Hosting

---

## ⚙ Installation (Run Locally)

  ### 1️⃣ Clone Repository

   ```bash
    git clone https://github.com/Binit212/guessing_game.git
   ```
 ### Navigate to the project folder
  ```bash
    cd guessing_game
   ```
### 2️⃣ Install Dependencies
   ```bash
    pip install -r requirements.txt
   ```

### 3️⃣ Run Application

  ```bash
    python app.py
   ```

### 4️⃣ Open Browser
   ```bash
    Visit:http://127.0.0.1:5000
   ```

## 🎮 How To Play

1. Enter your name
2. Select difficulty
3. Guess the number
4. Avoid duplicate guesses
5. Try to win with minimum time & attempts
6. Compete on leaderboard

---

## 📊 Scoring Logic

Score is calculated using:

- Remaining attempts
- Time taken to guess correctly

Higher score + lower time = higher rank.

---

## 📁 Project Structure
  ```
project-folder/
│
├── app.py
├── leaderboard.db
├── requirements.txt
├── Procfile
│
├── templates/
│ ├── index.html
│ └── leaderboard.html
│
└── static/
└── style.css
  ```
---

## 🔒 Security Notes

- Sessions are used to manage player data
- SQL Injection prevention using parameterized queries
- Production server handled by Gunicorn

---

## 📌 Future Improvements

- Multiplayer rooms
- Sound effects
- PostgreSQL cloud database
- Player profiles
- Admin dashboard
- Authentication system

---

## 👨‍💻 Author

Developed by: **BINIT**  
GitHub: https://github.com/Binit212

---

⭐ If you like this project, give it a star!

