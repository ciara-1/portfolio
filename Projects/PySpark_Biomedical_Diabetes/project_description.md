# PySpark Biomedical Concept Relations & Diabetes Prediction

## Summary
This two-part project demonstrates the use of PySpark for big data preprocessing and machine learning in biomedical informatics.

### Part I: UMLS Concept Relations
- **Goal:** Preprocess and count unique biomedical concept pairs from `rel.csv`.
- **Tasks:**
  - Alphabetically order each pair (e.g., `(c1, c2)` becomes `(c1, c2)` if `c1 < c2`; else `(c2, c1)`).
  - Count frequency of each ordered pair.
  - Output the result as `pair-count.txt`.

### Part II: Diabetes Prediction Using Random Forest
- **Dataset:** `diabetes.csv` with 8 clinical predictors and a binary outcome (diabetic or not).
- **Tasks:**
  - Clean data by removing rows with zeros in critical fields (`BMI`, `BloodPressure`, `Glucose`).
  - Apply one-hot encoding to the `Pregnancies` column.
  - Use `VectorAssembler` to prepare features.
  - Split data (70/30) with seed 2017.
  - Train a Random Forest classifier with 20 trees.
  - Evaluate using ROC curve AUC.

## Tools & Technologies
- **Apache Spark (PySpark)**
- **Jupyter Notebook**
- **MLlib (Random Forest, ROC evaluation)**

## 📁 Files Included
- `Assignment3.ipynb`: Code and results  
- `Assignment3.html`: Rendered notebook  
- `diabetes.csv` & `rel.csv`: Datasets used  
- `pair-count.txt`: Output from Part I  
