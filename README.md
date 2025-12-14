# GradeCast AI 🚀

Hey! 👋 Welcome to **GradeCast AI**.

This is a project I built to solve a common student problem: the anxiety of not knowing where you stand. We all worry about whether we're studying enough or if that one missed class will ruin our grade, right? I created this app to take the guesswork out of your academic performance.

It combines **Machine Learning** with your daily habits to instantly predict your final grade and pass probability.

> **Live Demo:** [https://gradecast-ai.onrender.com](https://gradecast-ai.onrender.com)

---

## 💡 What Makes This Special?

I didn't just want a simple calculator. I built this to be **smart and stylish**:

* **It Learns in Real-Time:** Unlike static apps, this system retrains its internal models every time the server starts. It takes raw historical data and learns the patterns between study hours, attendance, and success.
* **Dual-Engine Prediction:** It doesn't just give you a "Yes" or "No." I implemented two separate algorithms: **Logistic Regression** to figure out if you'll pass, and **Linear Regression** to pinpoint your exact score (0-100).
* **No More Guesswork:** It gives you a concrete probability percentage (e.g., "98.5% chance of passing"), so you know exactly how safe you are.
* **Glassmorphism UI:** Because educational tools don't have to look boring. It features a modern, dark-themed "Majin Studio" design that looks great on both laptop and mobile.

---

## 🛠️ How It Works (The Tech)

* **The Brains:** Python & Flask
* **The Logic:** Scikit-Learn (Linear & Logistic Regression)
* **The Data:** Pandas (Data processing & cleaning)
* **The Look:** Custom CSS (Glassmorphism & Responsive Design)

---

## 🚀 How to Run It

I made it super simple to get this running on your local machine.

### The Manual Way
1.  **Clone this repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/gradecast-ai.git](https://github.com/YOUR_USERNAME/gradecast-ai.git)
    cd gradecast-ai
    ```
2.  **Install the libraries:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the server:**
    ```bash
    python app.py
    ```
4.  **Start Predicting:**
    Go to `http://127.0.0.1:5000` in your browser!

---

## 👥 The Team

Built with ❤️ by:
* **Dhanush (Prince Vegeta)**

---

## ⚠️ Just a Heads Up (Disclaimer)

**Please don't use this as a guarantee.**
I built this as a demonstration of how ML applies to education. The predictions are estimates based on historical trends, not a crystal ball. Keep studying hard!
