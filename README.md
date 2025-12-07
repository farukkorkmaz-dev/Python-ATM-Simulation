# 🏦 Python ATM Simulation

A secure, console-based ATM simulation project developed with Python.
This project demonstrates core programming concepts including file handling, user authentication, and modular design.

## 🚀 Features
* **Secure Login:** PIN authentication system with a 3-attempt lockout mechanism.
* **Data Persistence:** Balances and PIN changes are saved automatically to a `.txt` file (`bank_data.txt`), ensuring data isn't lost when the program closes.
* **Core Banking Operations:** Withdraw, Deposit, Check Balance, and Change PIN.
* **Transaction History:** Logs all transactions with timestamps during the session.
* **Error Handling:** Prevents crashes from invalid user inputs (e.g., entering letters instead of numbers).

## 🛠️ Technologies Used
* **Python 3.x**
* **File I/O** (Text-based database simulation)
* **DateTime Module** (For transaction timestamps)
* **OS Module** (For file path verification)

## 📂 Project Structure
* `atm_simulation.py`: The main source code containing all logic.
* `bank_data.txt`: Automatically created file to store user data (Balance & PIN).
* `dist/`: Contains the executable (.exe) version for Windows usage.

## 🔮 Future Improvements (To-Do)
* [ ] Integration with SQLite Database for better data management.
* [ ] Graphical User Interface (GUI) using Tkinter.
