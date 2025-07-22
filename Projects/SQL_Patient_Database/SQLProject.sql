# Create Patients table
CREATE TABLE Patients (
    MRNO INT PRIMARY KEY,
    LastName VARCHAR(50),
    FirstName VARCHAR(50),
    MiddleInit CHAR(1),
    DOB DATE,
    Gender CHAR(1),
    Address VARCHAR(100),
    City VARCHAR(50),
    State CHAR(2),
    Zipcode VARCHAR(10),
    EmailAddress VARCHAR(100),
    Phone VARCHAR(20),
    MothersMaiden VARCHAR(50),
    MaritalStatus VARCHAR(20),
    Occupation VARCHAR(100),
    Employer VARCHAR(100),
    BloodType VARCHAR(3),
    Weight DECIMAL(4,1),
    Height VARCHAR(10),
    AdmitDate DATE
);

# Create Diagnoses table
CREATE TABLE Diagnoses (
    ID INT PRIMARY KEY,
    MRNO INT,
    DX1 VARCHAR(10),
    Description1 VARCHAR(255),
    DX2 VARCHAR(10),
    Description2 VARCHAR(255),
    DX3 VARCHAR(10),
    Description3 VARCHAR(255),
    CONSTRAINT fk_has_patients FOREIGN KEY (MRNO)
        REFERENCES Patients (MRNO) ON DELETE RESTRICT
);

# 1. Count total patients
SELECT COUNT(*) AS Total_Patients
FROM Patients;

# 2. Count male patients
SELECT COUNT(*) AS Male_Patients
FROM Patients
WHERE Gender = 'M';

# 3. Count female patients
SELECT COUNT(*) AS Female_Patients
FROM Patients
WHERE Gender = 'F';

# 4. Find all female patients with A- blood type
SELECT MRNO, LastName, FirstName, BloodType
FROM Patients
WHERE Gender = 'F' AND BloodType = 'A-';

# 5. Count female patients with A- blood type
SELECT COUNT(*) AS Female_BloodType
FROM Patients
WHERE Gender = 'F' AND BloodType = 'A-';

# 6. Count patients from Houston, TX
SELECT COUNT(*) AS Houston_TX
FROM Patients
WHERE City = 'Houston' AND State = 'TX';

# 7. Diagnoses for patient named 'Marc Knight'
SELECT d.*
FROM Diagnoses d
JOIN Patients p ON d.MRNO = p.MRNO
WHERE p.FirstName = 'Marc' AND p.LastName = 'Knight';

# 8. Patients admitted after May 2, 2021
SELECT *
FROM Patients
WHERE AdmitDate > '2021-05-02';

# 9. Count patients diagnosed with at least two conditions
SELECT COUNT(*) AS Two_Conditions_Or_More
FROM (
    SELECT MRNO,
           SUM(CASE WHEN DX1 != '' THEN 1 ELSE 0 END) +
           SUM(CASE WHEN DX2 != '' THEN 1 ELSE 0 END) +
           SUM(CASE WHEN DX3 != '' THEN 1 ELSE 0 END) AS TotalDiagnoses
    FROM Diagnoses
    GROUP BY MRNO
    HAVING TotalDiagnoses >= 2
) AS DiagnosisCounts;

# 10. Patients with "Hypertension" in any description
SELECT DISTINCT p.FirstName, p.LastName
FROM Patients p
JOIN Diagnoses d ON p.MRNO = d.MRNO
WHERE d.Description1 LIKE '%Hypertension%'
   OR d.Description2 LIKE '%Hypertension%'
   OR d.Description3 LIKE '%Hypertension%';

# 11. Patients diagnosed with "Diabetes" and their admit date and blood type
SELECT DISTINCT p.FirstName, p.LastName, p.AdmitDate, p.BloodType
F
