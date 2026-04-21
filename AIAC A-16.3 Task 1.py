import sqlite3
from datetime import datetime

# Create Hospital Management Database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# ============== SCHEMA CREATION ==============

# Table 1: Doctors
cursor.execute('''
    CREATE TABLE Doctors (
        DoctorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL UNIQUE,
        Specialization TEXT NOT NULL,
        ContactNumber TEXT NOT NULL UNIQUE,
        Email TEXT NOT NULL UNIQUE,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Table 2: Patients
cursor.execute('''
    CREATE TABLE Patients (
        PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender TEXT CHECK(Gender IN ('Male', 'Female', 'Other')),
        ContactNumber TEXT NOT NULL UNIQUE,
        Email TEXT NOT NULL UNIQUE,
        Address TEXT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Table 3: Appointments
cursor.execute('''
    CREATE TABLE Appointments (
        AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        DoctorID INTEGER NOT NULL,
        PatientID INTEGER NOT NULL,
        AppointmentDate DATE NOT NULL,
        AppointmentTime TIME NOT NULL,
        Status TEXT DEFAULT 'Scheduled' CHECK(Status IN ('Scheduled', 'Completed', 'Cancelled')),
        Reason TEXT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
        FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
        UNIQUE(DoctorID, PatientID, AppointmentDate, AppointmentTime)
    )
''')

# ============== INSERT SAMPLE DATA ==============

doctors_data = [
    ('Dr. Rajesh Kumar', 'Cardiology', '9876543210', 'rajesh@hospital.com'),
    ('Dr. Priya Sharma', 'Dermatology', '9876543211', 'priya@hospital.com'),
    ('Dr. Amit Patel', 'Orthopedics', '9876543212', 'amit@hospital.com'),
    ('Dr. Neha Verma', 'Neurology', '9876543213', 'neha@hospital.com'),
]

cursor.executemany('''
    INSERT INTO Doctors (Name, Specialization, ContactNumber, Email)
    VALUES (?, ?, ?, ?)
''', doctors_data)

patients_data = [
    ('Ajay Singh', '1990-05-15', 'Male', '8765432101', 'ajay@email.com', '123 Main St'),
    ('Sanya Menon', '1985-08-22', 'Female', '8765432102', 'sanya@email.com', '456 Oak Ave'),
    ('Vikram Nair', '1992-03-10', 'Male', '8765432103', 'vikram@email.com', '789 Pine Rd'),
    ('Diya Kapoor', '1988-12-05', 'Female', '8765432104', 'diya@email.com', '321 Elm St'),
    ('Rohan Gupta', '1995-07-18', 'Male', '8765432105', 'rohan@email.com', '654 Maple Dr'),
]

cursor.executemany('''
    INSERT INTO Patients (Name, DateOfBirth, Gender, ContactNumber, Email, Address)
    VALUES (?, ?, ?, ?, ?, ?)
''', patients_data)

appointments_data = [
    (1, 1, '2024-02-15', '10:00:00', 'Completed', 'Heart Checkup'),
    (1, 2, '2024-02-16', '11:00:00', 'Scheduled', 'Chest Pain'),
    (2, 1, '2024-02-17', '14:00:00', 'Scheduled', 'Skin Rash'),
    (2, 3, '2024-02-18', '15:30:00', 'Completed', 'Acne Treatment'),
    (3, 4, '2024-02-19', '09:00:00', 'Scheduled', 'Knee Pain'),
    (1, 5, '2024-02-20', '10:30:00', 'Scheduled', 'Routine Checkup'),
    (4, 2, '2024-02-21', '16:00:00', 'Completed', 'Headache Consultation'),
    (3, 1, '2024-02-22', '11:00:00', 'Scheduled', 'Fracture Check'),
]

cursor.executemany('''
    INSERT INTO Appointments (DoctorID, PatientID, AppointmentDate, AppointmentTime, Status, Reason)
    VALUES (?, ?, ?, ?, ?, ?)
''', appointments_data)

conn.commit()

# ============== QUERIES ==============

print("=" * 80)
print("HOSPITAL MANAGEMENT SYSTEM - DATABASE QUERIES")
print("=" * 80)

# Query 1: List all appointments for a specific doctor
print("\n[QUERY 1] All Appointments for Dr. Rajesh Kumar (Doctor ID: 1)")
print("-" * 80)
query1 = '''
    SELECT 
        a.AppointmentID,
        d.Name AS DoctorName,
        p.Name AS PatientName,
        a.AppointmentDate,
        a.AppointmentTime,
        a.Status,
        a.Reason
    FROM Appointments a
    JOIN Doctors d ON a.DoctorID = d.DoctorID
    JOIN Patients p ON a.PatientID = p.PatientID
    WHERE a.DoctorID = 1
    ORDER BY a.AppointmentDate DESC
'''

cursor.execute(query1)
appointments_doctor = cursor.fetchall()
for row in appointments_doctor:
    print(f"Apt ID: {row[0]}, Doctor: {row[1]}, Patient: {row[2]}, "
          f"Date: {row[3]}, Time: {row[4]}, Status: {row[5]}, Reason: {row[6]}")

# Query 2: Retrieve patient history by patient ID
print("\n[QUERY 2] Patient History for Ajay Singh (Patient ID: 1)")
print("-" * 80)
query2 = '''
    SELECT 
        p.PatientID,
        p.Name,
        p.DateOfBirth,
        p.Gender,
        p.ContactNumber,
        p.Email,
        COUNT(a.AppointmentID) AS TotalAppointments,
        GROUP_CONCAT(DISTINCT d.Specialization) AS DoctorsConsulted
    FROM Patients p
    LEFT JOIN Appointments a ON p.PatientID = a.PatientID
    LEFT JOIN Doctors d ON a.DoctorID = d.DoctorID
    WHERE p.PatientID = 1
    GROUP BY p.PatientID
'''

cursor.execute(query2)
patient_history = cursor.fetchone()
if patient_history:
    print(f"Patient ID: {patient_history[0]}")
    print(f"Name: {patient_history[1]}")
    print(f"Date of Birth: {patient_history[2]}")
    print(f"Gender: {patient_history[3]}")
    print(f"Contact: {patient_history[4]}")
    print(f"Email: {patient_history[5]}")
    print(f"Total Appointments: {patient_history[6]}")
    print(f"Doctors Consulted: {patient_history[7]}")

# Query 2b: Detailed appointment history
print("\nDetailed Appointment History:")
query2b = '''
    SELECT 
        a.AppointmentID,
        d.Name AS DoctorName,
        d.Specialization,
        a.AppointmentDate,
        a.AppointmentTime,
        a.Status,
        a.Reason
    FROM Appointments a
    JOIN Doctors d ON a.DoctorID = d.DoctorID
    WHERE a.PatientID = 1
    ORDER BY a.AppointmentDate DESC
'''

cursor.execute(query2b)
for row in cursor.fetchall():
    print(f"  Apt: {row[0]}, Doctor: {row[1]} ({row[2]}), "
          f"Date: {row[3]}, Time: {row[4]}, Status: {row[5]}, Reason: {row[6]}")

# Query 3: Count total patients treated by each doctor
print("\n[QUERY 3] Total Patients Treated by Each Doctor")
print("-" * 80)
query3 = '''
    SELECT 
        d.DoctorID,
        d.Name AS DoctorName,
        d.Specialization,
        COUNT(DISTINCT a.PatientID) AS TotalPatientsTreated,
        COUNT(a.AppointmentID) AS TotalAppointments,
        SUM(CASE WHEN a.Status = 'Completed' THEN 1 ELSE 0 END) AS CompletedAppointments
    FROM Doctors d
    LEFT JOIN Appointments a ON d.DoctorID = a.DoctorID
    GROUP BY d.DoctorID, d.Name, d.Specialization
    ORDER BY TotalPatientsTreated DESC
'''

cursor.execute(query3)
doctor_stats = cursor.fetchall()
for row in doctor_stats:
    print(f"Doctor ID: {row[0]}, Name: {row[1]}, Specialization: {row[2]}, "
          f"Patients: {row[3]}, Appointments: {row[4]}, Completed: {row[5]}")

# Additional Query: Appointments by Status
print("\n[BONUS QUERY] Appointment Summary by Status")
print("-" * 80)
query_bonus = '''
    SELECT 
        Status,
        COUNT(*) AS Count
    FROM Appointments
    GROUP BY Status
'''

cursor.execute(query_bonus)
for row in cursor.fetchall():
    print(f"Status: {row[0]}, Count: {row[1]}")

conn.close()
print("\n" + "=" * 80)