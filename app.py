from flask import Flask, render_template, request, redirect, url_for, session
import random
import time
import os
import psycopg2


def get_db_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL not set")

    conn = psycopg2.connect(database_url)
    conn.autocommit = True
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            name TEXT,
            score INTEGER,
            time REAL
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


app = Flask(__name__)
app.secret_key = "supersecretkey123"


def save_score(name, score, time_taken):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores (name, score, time) VALUES (%s, %s, %s)",
        (name, score, time_taken)
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, score, time FROM scores ORDER BY score DESC, time ASC"
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


@app.route("/leaderboard")
def leaderboard():
    scores = get_leaderboard()
    last_player = session.pop("last_player", "")
    message = session.pop("win_message", "")

    return render_template(
        "leaderboard.html",
        scores=scores,
        last_player=last_player,
        message=message
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("home"))


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""
    guess = None

    if request.method == "POST" and "secret_number" not in session:

        difficulty = request.form["difficulty"]
        session["difficulty"] = difficulty

        if difficulty == "easy":
            session["max_attempts"] = 7
            session["secret_number"] = random.randint(1, 10)

        elif difficulty == "medium":
            session["max_attempts"] = 5
            session["secret_number"] = random.randint(1, 50)

        else:
            session["max_attempts"] = 3
            session["secret_number"] = random.randint(1, 100)

        session["attempts"] = 0
        session["start_time"] = time.time()
        session["guess_history"] = []

    if request.method == "POST":

        guess = int(request.form["guess"])

        # Save player name only once
        if "player_name" not in session:
            session["player_name"] = request.form["player_name"]

        player_name = session["player_name"]

        if guess in session.get("guess_history", []):
            message = f" You already guessed {guess}! Try a new number."

            return render_template(
                "index.html",
                message=message,
                player_name=player_name,
                difficulty=session.get("difficulty"),
                range_hint=get_range_hint(session.get("difficulty")),
                guess_history=session.get("guess_history")
            )

        session["guess_history"].append(guess)

        session["attempts"] += 1

        secret_number = session.get("secret_number")
        max_attempts = session.get("max_attempts")
        attempts = session.get("attempts")

        remaining = max_attempts - attempts

        if guess == secret_number:

            end_time = time.time()
            time_taken = round(end_time - session["start_time"], 2)

            score = max(0, (max_attempts - attempts + 1)
                        * 10 - int(time_taken))

            save_score(player_name, score, time_taken)

            session["last_player"] = player_name
            session["win_message"] = f" You won, {player_name}! Score saved."

            return redirect(url_for("leaderboard"))

        if attempts >= max_attempts:

            correct_number = secret_number
            session.clear()

            message = f" Game Over! The number was {correct_number}."

            return render_template("index.html", message=message)

        if guess > secret_number:
            message = f"Too high! Attempts left: {remaining}"
        else:
            message = f"Too low! Attempts left: {remaining}"

    difficulty = session.get("difficulty", "")
    guess_history = session.get("guess_history", [])
    player_name = session.get("player_name", "")

    return render_template(
        "index.html",
        message=message,
        player_name=player_name,
        difficulty=difficulty,
        range_hint=get_range_hint(difficulty),
        guess_history=guess_history
    )


def get_range_hint(difficulty):
    if difficulty == "easy":
        return "1 to 10"
    elif difficulty == "medium":
        return "1 to 50"
    elif difficulty == "hard":
        return "1 to 100"
    return ""


if __name__ == "__main__":
    init_db()
    app.run()
