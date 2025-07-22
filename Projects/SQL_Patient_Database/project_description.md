# SQL-Based Patient & Diagnosis Database — Healthcare Data Exploration

This project demonstrates the design and implementation of a patient diagnosis relational database using SQL. The assignment focused on relational schema modeling, data exploration queries, and joining patient health data to support healthcare analytics use cases.

---

## Project Components

### 1. Schema Design

Two tables were created with primary-foreign key relationships:

- **Patients**
  - Fields include demographic details, blood type, address, and admission dates
  - Primary Key: `MRNO`

- **Diagnoses**
  - Stores up to 3 diagnosis codes per patient
  - Foreign Key: `MRNO` references Patients

[View Full SQL Schema & Queries](../SQL_Patient_Database/SQLProject.sql)

---

## 🔍 Query Highlights

The SQL queries answered real-world data questions such as:

- Total number of patients
- Gender and blood type breakdowns
- Patients from specific cities/states
- Diagnoses filtering by keyword (e.g., "Hypertension", "Diabetes")
- Multi-condition patient identification
- Admission date filters
- Diagnoses linked to named individuals (e.g., "Marc Knight")

Example:
```sql
SELECT COUNT(*) AS Female_BloodType
FROM Patients
WHERE Gender = 'F' AND BloodType = 'A-';
