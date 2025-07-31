# Python Mini Projects Collection

This repository contains three Python console projects demonstrating basic programming concepts, input validation, file handling, and simple game logic.

---

## ATM System

A simple ATM console application that allows users to:

- Check account balance
- Deposit money
- Withdraw money
- View transaction history

**Features:**

- User data stored in CSV file with account number, name, and balance
- Separate transaction history files per account
- Validations for account existence, sufficient balance, and menu choices

---

## Books Management

A console app managing a collection of books, with features to:

- Add new books with title, author, and publication year
- List all books
- Search for a book by title

**Features:**

- Input validation for empty fields and publication year correctness
- Prevent duplicate book titles
- Encapsulated `Book` class with properties

---

## Hangman Game

A simple Hangman game playable in either English or Georgian:

- Randomly chooses a word based on selected language
- Player guesses letters with limited attempts
- Displays guessed letters and current word progress
- Validates input length and already guessed letters
- Allows replaying the game

---

## How to Run

Run any of the Python scripts individually:

```bash
python ATM.py
python Books_management.py
python Hangman.py
