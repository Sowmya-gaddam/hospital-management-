import sqlite3

# ---------------- DATABASE CONNECTION ----------------
conn = sqlite3.connect(
    'hospital.db',
    check_same_thread=False
)

cursor = conn.cursor()

# ---------------- USERS TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    '''
)

# ---------------- PATIENTS TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        disease TEXT,
        phone TEXT
    )
    '''
)

# ---------------- DOCTORS TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        specialization TEXT,
        availability TEXT
    )
    '''
)

# ---------------- APPOINTMENTS TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        doctor_name TEXT,
        date TEXT,
        time TEXT,
        status TEXT
    )
    '''
)

# ---------------- BILLS TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS bills (
        bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        amount REAL,
        payment_status TEXT
    )
    '''
)

# ---------------- MEDICINE TABLE ----------------
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS medicines (
        medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine_name TEXT,
        company TEXT,
        quantity INTEGER,
        expiry_date TEXT,
        price REAL
    )
    '''
)

# ---------------- SAVE CHANGES ----------------
conn.commit()