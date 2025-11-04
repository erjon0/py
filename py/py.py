#!/usr/bin/env python3
"""
Advanced Multitool Utility
===========================
A comprehensive Python utility combining:
- Math, text, and file tools
- Mock weather API
- SQLite database manager
- Web scraping (BeautifulSoup)
- Email sending (SMTP)
- Encryption & decryption (Fernet)
- Basic sentiment analysis
- Logging, CLI, and structured design

Author: ChatGPT (GPT-5)
"""

import os
import sys
import math
import json
import random
import time
import logging
import sqlite3
import smtplib
import requests
from typing import List, Dict, Any
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup

# -------------------- Logging -------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler("advanced_multitool.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# -------------------- Math Tools -------------------- #

class MathTools:
    """Mathematical helper class."""

    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Negative number not allowed.")
        return math.prod(range(1, n + 1)) or 1

    @staticmethod
    def fibonacci(n: int) -> List[int]:
        a, b = 0, 1
        seq = []
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# -------------------- Text Tools -------------------- #

class TextTools:
    """Text processing and sentiment analysis."""

    POSITIVE_WORDS = {"good", "great", "awesome", "love", "excellent", "happy"}
    NEGATIVE_WORDS = {"bad", "terrible", "sad", "angry", "hate", "awful"}

    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())

    @staticmethod
    def char_count(text: str) -> int:
        return len(text)

    @staticmethod
    def reverse(text: str) -> str:
        return text[::-1]

    @staticmethod
    def sentiment(text: str) -> str:
        words = set(text.lower().split())
        pos = len(words & TextTools.POSITIVE_WORDS)
        neg = len(words & TextTools.NEGATIVE_WORDS)
        if pos > neg:
            return "Positive 😊"
        elif neg > pos:
            return "Negative 😞"
        else:
            return "Neutral 😐"

# -------------------- File Tools -------------------- #

class FileManager:
    """Basic file and JSON management."""

    @staticmethod
    def list_files(directory: str) -> List[str]:
        try:
            return os.listdir(directory)
        except FileNotFoundError:
            logger.error("Directory not found.")
            return []

    @staticmethod
    def create_file(filename: str, content: str = "") -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Created file: {filename}")

    @staticmethod
    def read_json(filepath: str) -> Dict[str, Any]:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error reading JSON: {e}")
            return {}

    @staticmethod
    def write_json(filepath: str, data: Dict[str, Any]) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Saved JSON to {filepath}")

# -------------------- Weather API (Mock) -------------------- #

class WeatherAPI:
    """Mock weather API with fake data."""

    @staticmethod
    def get_weather(city: str) -> Dict[str, Any]:
        logger.info(f"Fetching weather for {city}...")
        time.sleep(1)
        return {
            "city": city.title(),
            "temperature": round(random.uniform(-5, 40), 1),
            "condition": random.choice(["Sunny", "Rainy", "Cloudy", "Snowy"]),
            "timestamp": datetime.now().isoformat()
        }

# -------------------- Database -------------------- #

class DatabaseManager:
    """SQLite database utility."""

    def __init__(self, db_name: str = "multitool.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT,
                    created_at TEXT
                )
            """)
        logger.info("Database ready.")

    def add_note(self, title: str, content: str):
        with self.conn:
            self.conn.execute(
                "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
                (title, content, datetime.now().isoformat())
            )
        logger.info(f"Added note: {title}")

    def get_notes(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, content, created_at FROM notes")
        rows = cursor.fetchall()
        return [{"id": r[0], "title": r[1], "content": r[2], "created_at": r[3]} for r in rows]

# -------------------- Encryption -------------------- #

class CryptoTool:
    """Encryption and decryption via Fernet (symmetric)."""

    def __init__(self, key_file: str = "secret.key"):
        self.key_file = key_file
        self.key = self.load_or_create_key()

    def load_or_create_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as f:
            f.write(key)
        logger.info("Generated new encryption key.")
        return key

    def encrypt(self, message: str) -> str:
        f = Fernet(self.key)
        return f.encrypt(message.encode()).decode()

    def decrypt(self, token: str) -> str:
        f = Fernet(self.key)
        return f.decrypt(token.encode()).decode()

# -------------------- Web Scraping -------------------- #

class WebScraper:
    """Fetch and parse web page titles."""

    @staticmethod
    def get_page_title(url: str) -> str:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.title.string if soup.title else "No title found"
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return "Error"

# -------------------- Email Sending -------------------- #

class EmailSender:
    """Send simple email using SMTP."""

    @staticmethod
    def send_email(sender: str, password: str, recipient: str, subject: str, message: str):
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)
            logger.info("Email sent successfully.")
        except Exception as e:
            logger.error(f"Email failed: {e}")

# -------------------- CLI -------------------- #

def display_menu():
    print("\n=== Advanced Multitool ===")
    print("1. Math Tools")
    print("2. Text Tools")
    print("3. File Tools")
    print("4. Weather (Mock)")
    print("5. Database Notes")
    print("6. Encryption")
    print("7. Web Scraping")
    print("8. Send Email")
    print("0. Exit")

def main():
    db = DatabaseManager()
    crypto = CryptoTool()

    while True:
        display_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            n = int(input("Number: "))
            print(f"Factorial: {MathTools.factorial(n)}")
            print(f"Fibonacci: {MathTools.fibonacci(n)}")
            print(f"Prime: {MathTools.is_prime(n)}")

        elif choice == "2":
            text = input("Enter text: ")
            print(f"Word count: {TextTools.word_count(text)}")
            print(f"Sentiment: {TextTools.sentiment(text)}")

        elif choice == "3":
            dir_path = input("Directory: ")
            print(FileManager.list_files(dir_path))

        elif choice == "4":
            city = input("City: ")
            print(json.dumps(WeatherAPI.get_weather(city), indent=4))

        elif choice == "5":
            print("\n1. Add Note  2. View Notes")
            sub = input("Choose: ")
            if sub == "1":
                title = input("Title: ")
                content = input("Content: ")
                db.add_note(title, content)
            else:
                for note in db.get_notes():
                    print(f"{note['id']}. {note['title']} — {note['created_at']}")

        elif choice == "6":
            msg = input("Message to encrypt: ")
            token = crypto.encrypt(msg)
            print("Encrypted:", token)
            print("Decrypted:", crypto.decrypt(token))

        elif choice == "7":
            url = input("Enter URL: ")
            print("Page Title:", WebScraper.get_page_title(url))

        elif choice == "8":
            sender = input("Your Email: ")
            pwd = input("Password: ")
            to = input("To: ")
            subject = input("Subject: ")
            msg = input("Message: ")
            EmailSender.send_email(sender, pwd, to, subject, msg)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        sys.exit(0)
