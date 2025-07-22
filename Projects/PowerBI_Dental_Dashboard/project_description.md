# Power BI Dashboard for Clinical Documentation & Quality Monitoring

This capstone project for the BMI 6000 Practicum involved designing and developing a reusable Power BI dashboard to assess clinical documentation completeness and compliance with quality-of-care metrics at the UTHealth Houston School of Dentistry. It was created in collaboration with the Texas Center for Oral Healthcare Quality and Safety (TCOHQS).

---

## Project Objective

To transform the static, retrospective QAIR (Quality Assurance Indices Review) report into an interactive, auto-updating dashboard that supports real-time documentation monitoring and quality improvement across key clinical metrics.

---

## Data Source

- **System**: Axium Electronic Health Record (EHR)
- **Scope**: De-identified patient records from January 2025
- **Metrics Tracked**:
  - General consent status
  - Caries risk assessments (CRA)
  - Fluoride application
  - Treatment plan activity
  - Radiograph status
  - Periodontal documentation
  - Oral hygiene education

---

## Tools & Techniques

- **Platform**: Microsoft Power BI
- **ETL**: Excel preprocessing + DAX transformations
- **Modeling**:
  - Calculated columns (e.g., Completed vs. Overdue)
  - Custom DAX measures for compliance scoring
- **Visualization**:
  - Pie charts, tables, and filters for dental class year & provider group
  - Monthly auto-refresh for trend analysis

---

## Key Features

- **Class Year & Provider Filters**: Enables cohort-based analysis of documentation trends (e.g., DS2025 vs. DS2026)
- **Interactive Analysis**: Drill-downs by documentation type
- **Behavioral Insights**: Identify gaps early in training cycles
- **Reusable Template**: Built-in DAX measure library for future expansion

---

## Results & Impact

- Increased visibility into documentation practices
- Shifted reporting from static to dynamic
- Highlighted class-year differences in compliance behavior
- Empowered faculty and QA teams with data for feedback and planning

---

## Lessons Learned

- **Data Standardization is Critical**: Raw EHR fields required extensive parsing
- **Reusability Matters**: Designing scalable DAX logic saved time
- **User Feedback Improves Design**: Early testing guided filter layout and metric grouping
- **Educational Value**: Dashboards revealed new teaching opportunities to improve early compliance

---

## Future Recommendations

- Expand to additional periodontal metrics (MOBIL, FURC, POCKET, etc.)
- Develop views tailored to faculty vs. students
- Integrate benchmarking by provider group or class year
- Evaluate the impact of documentation interventions over time
- Embed into larger institutional quality frameworks

---

## Institution

**UTHealth Houston School of Dentistry**  
Texas Center for Oral Healthcare Quality and Safety (TCOHQS)

---

## Course

**BMI 6000: Practicum in Biomedical Informatics**

