
# 🕵️‍♂️ DisAppearMsg

A simple Flask-based web application that allows users to create **self-destructing messages** through short links. Each message can be viewed a limited number of times before it's automatically deleted. Built with Python + Flask, with two backend options: **MySQL** or **JSON file-based**.

---

## 🎥 Demo Video

[![Watch the demo](https://raw.githubusercontent.com/prajwalkedari/DisAppearMsg/refs/heads/main/Demo_vid.gif)](https://raw.githubusercontent.com/prajwalkedari/DisAppearMsg/refs/heads/main/Demo_vid.mp4)

> 🔗 **Click to watch demo**  


---

## 🚀 Features

- 🔒 One-time/limited-time secret message sharing
- 💥 Messages delete automatically after view limit
- 🔗 Short, shareable URLs (e.g., `/msg/Ab12`)
- 📦 Two storage modes:
  - `main_MySql.py`: uses MySQL database
  - `main_json.py`: uses local `data.json` file

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prajwalkedari/DisAppearMsg.git
cd DisAppearMsg
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
# Activate
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux

# Install
pip install -r requirements.txt
```

---

## 💾 Backend Options

### 🔹 Option A: Use `main_MySql.py` (MySQL)

#### 1. Create Database

```sql
CREATE DATABASE disappear_db;

USE disappear_db;

CREATE TABLE keylink (
    id INT AUTO_INCREMENT PRIMARY KEY,
    msg TEXT NOT NULL,
    link VARCHAR(10) UNIQUE NOT NULL,
    counter INT DEFAULT 1
);
```

#### 2. Configure DB in Python

Edit `main_MySql.py`:

```python
config = {
    "host": "localhost",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "disappear_db",
    "table": "keylink"
}
```

#### 3. Run

```bash
python main_MySql.py
```

---

### 🔹 Option B: Use `main_json.py` (JSON file-based)

This version stores messages in a local file `data.json`.

#### 1. Ensure `data.json` exists:

Create a blank file if not already:

```json
{}
```

#### 2. Run

```bash
python main_json.py
```

---

## 🌐 Access the App

Visit in browser:

```text
http://127.0.0.1:5000/
```

---

## 💡 How It Works

1. User submits a message
2. A unique short link (e.g., `/msg/Ab12`) is generated
3. Visiting that link decreases the view counter
4. When counter hits 0, the message is deleted (from DB or JSON)

---

## 📁 Project Structure

```
DisAppearMsg/
│
├── main_MySql.py       # MySQL version
├── main_json.py        # JSON version
├── data.json           # For JSON storage
├── templates/          # HTML files
├── static/             # CSS (optional)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ✅ Example

```text
POST message: "My OTP is 123456"
→ /msg/MPTl

→ Access 1: counter = 2
→ Access 2: counter = 1
→ Access 3: counter = 0 → message deleted
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Built by **Prajwal Kedari**  
GitHub: [@prajwalkedari](https://github.com/prajwalkedari)


Pull requests and suggestions welcome!
