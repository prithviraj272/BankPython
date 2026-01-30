# Simple Bank Management System (OOP)

A lightweight Python-based Banking System that demonstrates **Object-Oriented Programming (OOP)** principles. This application manages user data using Python dictionaries for fast lookup and efficient data handling.

## 🚀 Features
* **Account Creation:** Generates a unique account number for every new user.
* **Deposit & Withdrawal:** Real-time balance updates with validation logic.
* **Balance Inquiry:** Instant access to account details via the account number.
* **OOP Design:** Utilizes classes and methods to ensure clean, maintainable code.
* **Dictionary-Based Storage:** Uses a nested dictionary structure for $O(1)$ data retrieval.

## 🛠️ How It Works
The system is built around a `Bank` class that acts as the data controller:
1.  **Data Structure:** All information is stored in `self.accounts` where the key is the `account_number` and the value is a dictionary containing `name` and `balance`.
2.  **Validation:** The system prevents withdrawals if the amount exceeds the available balance.

## 💻 Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/bank-management-system.git](https://github.com/yourusername/bank-management-system.git)
