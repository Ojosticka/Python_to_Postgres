# 🐘 Python to PostgreSQL CSV Loader

This project provides a simple and reusable Python script that uploads multiple CSV files from a local folder into a PostgreSQL database.  
It uses **Pandas**, **SQLAlchemy**, and **python-dotenv** to handle data loading and credential management securely.

---

## 📁 Project Structure

PYTHON_TO_POSTGRES/
│
├── venv/ # Virtual environment (ignored by Git)
├── .env # Environment variables (database credentials)
├── .gitignore # Files and folders ignored by Git
├── main.py # Main Python script to upload CSVs
├── requirements.txt # Project dependencies
└── readme.md # Project documentation

---

## ⚙️ Prerequisites

Before running this project, ensure that you have:

- **Python 3.8+**
- **PostgreSQL** installed and running locally or remotely
- The ability to connect to your PostgreSQL database (user, password, host, port, database)

---

## 🚀 Setup Instructions

### 1️⃣ Clone or download the repository
```bash
git clone <your-repo-url>
cd PYTHON_TO_POSTGRES
```

2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Create a .env file
Create a file named .env in the root directory and add your PostgreSQL credentials:

```ini

DB_NAME=posey_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

Make sure .env is included in .gitignore to keep credentials private.

🧠 How It Works
The script loads database credentials from .env using python-dotenv.

It loops through all CSV files in the specified folder.

Each CSV is read into a Pandas DataFrame.

Using SQLAlchemy, each DataFrame is written into a PostgreSQL table with the same name as the CSV file (without .csv).

🧩 Usage
Run the script:

```bash
python main.py
```
You’ll be prompted to enter the full path to the folder containing your CSV files, e.g.:

Enter full path to folder containing CSV files: C:\Users\Tobi\Documents\csv_folder
The script will:

Connect to PostgreSQL

Create (or replace) tables matching each CSV filename

Upload all CSV data into those tables

Example output:

Importing accounts.csv into table: accounts
Successfully imported accounts.csv into 'accounts'

Importing transactions.csv into table: transactions
Successfully imported transactions.csv into 'transactions'

🎯 All CSVs imported successfully!
🧰 Example Folder

C:\Users\Tobi\Documents\csv_folder
│
├── accounts.csv
├── customers.csv
└── transactions.csv
This will create three tables in PostgreSQL:

- accounts
- customers
- transactions

🧪 Troubleshooting
psycopg2 or sqlalchemy not found:
```bash
Run pip install -r requirements.txt again.
```
Connection errors:
Double-check credentials in .env and ensure PostgreSQL is running and accessible.

Permission denied:
If on Windows, ensure your user has permission to access the CSV folder.

🧾 Dependencies
Your requirements.txt should include (approximate versions):

- pandas
- sqlalchemy
- python-dotenv
- psycopg2-binary


🧤 Contributing
Feel free to fork the repository and enhance the script — for example:

- Add error handling per file (skip failed uploads)
- Log upload activity to a text file
- Add support for incremental uploads instead of replacing tables

🪪 License
This project is released under the MIT License.

Author: Oluwatobi Ojo
Purpose: Demonstration of Python automation to load structured data into PostgreSQL.
