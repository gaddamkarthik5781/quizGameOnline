# Quiz Game System

## Overview

The **Quiz Game System** is a Python-based console application that provides an interactive platform for users to participate in multiple-choice quizzes. The system includes features like account creation, secure login, dynamic question loading, and score calculation.

---

## Features

### 1. **Account Creation**
- Users can create a new account by entering their details such as name, gender, username, and password.
- Each account is assigned a unique account number automatically.

### 2. **Login**
- Users log in securely using their account number and password.
- Ensures only authorized access to the quiz system.

### 3. **Quiz Gameplay**
- Dynamically loads quiz questions from an external file (`questions.txt`).
- Questions are multiple-choice with four options.
- Validates user responses and displays the correct answer when the user is wrong.

### 4. **Score Tracking**
- The system calculates the score based on correct responses.
- Displays a final score at the end of the quiz.

### 5. **Data Persistence**
- Account details are stored securely in a file (`accounts.txt`) for reuse across sessions.
- The quiz system can be restarted without losing user data.

---

## Requirements

- Python 3.6 or higher.

---

## How to Run

1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Run the program using the command:
   ```bash
   python quiz_sys_main.py
