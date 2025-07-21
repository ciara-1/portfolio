# Multivariate Analysis of Hospital-Acquired Infections (Tableau Project)

This project explores multivariate healthcare-associated infection (HAI) metrics across hospitals in Harris County using Tableau visualizations. The dashboard was built as part of a multivariate analysis assignment to assess infection severity and patterns using a parallel coordinate plot and heatmap.

---

## Project Goals

- Visualize hospital-level infection rates across 6 CDC-monitored conditions
- Identify outliers and patterns using multivariate visualizations
- Explore infection disparities between facilities in a high-density county

---

## Dataset

- **Source**: Medicare Hospital Compare (CMS Open Data)
- **File**: `Healthcare Associated Infections - Hospital.csv`
- **Filtered**: Only includes hospitals located in Harris County, Texas

### Infection Metrics Tracked:
1. Catheter-Associated Urinary Tract Infections (CAUTI)  
2. Central Line-Associated Blood Stream Infections (CLABSI)  
3. Clostridium difficile (C. diff.)  
4. Methicillin-resistant Staphylococcus Aureus (MRSA)  
5. Surgical Site Infection - Hysterectomy  
6. Surgical Site Infection - Colon Surgery

---

## Visualizations

### Heatmap
- Uses a diverging red-blue palette to highlight infection rates (red = above national avg)
- Sorted by cumulative infection severity score
- Includes filters by hospital name and county

### Parallel Coordinate Plot
- Each line represents a hospital’s full infection profile
- Colored by average infection score using a calculated field:  
  `WINDOW_AVG(SUM([Score]))`
- Interactive tooltips reveal hospital name and address

---

## Tools & Techniques

- **Tool**: Tableau Desktop
- **Techniques**:
  - Heatmaps
  - Parallel coordinate plots
  - Wildcard filters
  - WINDOW_AVG and Detail-level customization
  - Data cleaning and custom sorting
  - Visual encoding using calculated fields

---

## Screenshot

[Dashboard Preview](./HW14_Heatmap_ParallelPlot.png)

---

## 📂 Files Included

- `HW14_Heatmap_ParallelPlot.png`: Final dashboard screenshot
- `Healthcare_Infections_Hospitals.csv`: Filtered dataset used in Tableau
- `project_description.md`: This project overview

---

## 🎓 Course: HI 6340 – Health Information Visualization and Visual Analytics  
**Institution**: UTHealth School of Biomedical Informatics  
**Instructor**: [Add name if appropriate]

