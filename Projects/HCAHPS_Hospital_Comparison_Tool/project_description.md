# Hospital Comparison Dashboard – HCAHPS Scores

This final project dashboard allows users to compare hospitals using the HCAHPS dataset. Filters enable comparisons by state, county, zip code, hospital name, and patient experience questions. Rankings are calculated based on patient satisfaction percent scores.

---

## Project Objectives

- Enable faceted filtering of hospitals by region
- Compare hospital profiles and rank by average patient satisfaction
- Allow detailed comparison of specific questions (e.g., doctor/nurse communication)

---

## Key Features

### Filter Capabilities
- Faceted filters: State → County → Zip
- Search and select by hospital name
- Filter by survey question (e.g., “Definitely Recommend”, “Doctor Communication”)

### Ranking & Profiles
- Bar chart rankings by average percent score
- Individual hospital profiles visualized with heatmaps and bar charts
- Color-coded scores highlight best/worst performers (above or below 75%)

---

## Design Rationale

- Filters and charts follow visualization best practices and HCAHPS usability standards
- Overview → Zoom/Filter → Detail-on-demand layout
- Simplified labels, appropriate color contrast, hover-to-detail
  
- **Accessibility:** To support a user-friendly comparison of hospitals by geography, I implemented faceted filters for HCAHPS Question, State, ZIP Code, County Name, and Hospital Name using Tableau’s “Only Relevant Values” option. This setup ensures that each filter dynamically updates based on the previous selection, enabling users to filter from broader state-level data to specific counties and ZIP codes. For example, when a user selects Texas, only counties within Texas and their corresponding ZIP codes are displayed, enabling faster and more accurate filtering. The worksheet displays hospitals on the y-axis and average HCAHPS answer percentages on the x-axis, using color-coded bars segmented by question. This layout aligns with Shneiderman’s visual information-seeking mantra, where users get an overview through aggregated comparisons and can focus on specific areas by narrowing geographic filters. By placing the filters at the top of the worksheet, I enhance visibility and usability, consistent with UI design best practices that promote a left-to-right, top-down scanning pattern. This design supports regional overviews and localized comparisons for informed decision-making.
- **Color Coding:** To ensure consistent and intuitive interpretation of hospital performance, I applied a reversed red–blue diverging palette to all visualizations where color encodes HCAHPS score magnitude. In this scheme, higher scores are shown in red, while lower scores are in blue. This perceptual mapping improves immediate comprehension. I applied this reversed diverging scale uniformly across the “Compare Best Hospitals,” “Hospital Rankings,” and “Compare Profiles” worksheets to maintain consistency in how performance is visualized. For question-based comparisons in the “Hospital Comparison by Location” and “Hospital Comparison by Name” worksheets, I used Tableau Classic 10 palette to distinguish HCAHPS question types by color rather than score, avoiding visual confusion between question identity and score magnitude. These design decisions follow established data visualization best practices by reducing cognitive load, reinforcing interpretive consistency, and supporting fast, accurate analysis of hospital quality metrics.
-  **Usability:** I applied multiple usability principles to ensure the dashboard was intuitive and accessible for users with varying levels of technical proficiency. Clear titles, axis labels, tooltips, and color legends are used throughout to make each visualization easy to interpret. Interactive filters are positioned at the top of the dashboard, enabling users to explore the data by HCAHPS Question, State, ZIP Code, County Name, and Hospital Name without confusion. This design aligns with Shneiderman’s Mantra by structuring the dashboard to provide a high-level overview through the Compare Profiles heatmap, dynamic filtering and question selection for zoom and filter, and tooltip-enabled mark labels and contextual ranking for details on demand. I chose each chart type to communicate specific insights. For example, heatmaps reveal multivariate performance trends, bar charts highlight ranked hospital performance, and grouped and stacked bar charts support question-level and geographic comparisons. Additionally, consistent use of reversed red–blue diverging scales for performance and categorical palettes for question types ensures visual clarity. This approach reduces cognitive load, reinforces trust in the data, and supports users in identifying both gaps and strengths in hospital quality metrics.




---

## Screenshot

![Dashboard Preview](./TermProject.png)

---

## Files Included

- `TermProject.png`: Dashboard screenshot
- `HCAHPS Hospital.csv`: Dataset used
- `project_description.md`: This project overview
