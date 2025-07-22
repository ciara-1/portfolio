# Deviation Analysis of Patient Safety Indicators – Tableau Dashboard

This project analyzes AHRQ Patient Safety Indicators (PSIs) across 12 months using bullet graphs, small multiples, and forecasting models. The goal is to identify whether the hospital is meeting monthly and annual safety targets.

---

## Project Goals

- Evaluate year-to-date performance against annual PSI targets
- Forecast year-end totals based on current trends
- Support resource allocation decisions using data-driven insights

---

## Visualizations

### 1. **Bullet Graph: YTD Performance**
- Visualizes total cases vs. target threshold
- Uses calculated fields to color metrics that exceed target values

### 2. **Small Multiples Bar Charts**
- Monthly trends shown per metric, scaled independently
- Horizontal and vertical layouts for comparative readability

### 3. **Forecasting Bullet Graph**
- Projects end-of-year metrics based on average monthly performance
- Combines actuals and projections using calculated fields

### 4. **Dashboard**
- Combines trends, forecasts, and deviation status
- Answers CQO's key questions: Are we on track? Where are we over/under?

---

## Techniques & Tools

- Calculated fields: YTD totals, "Exceeded Target", Forecast projection
- Independent axes scaling per metric
- Dotted lines for monthly targets
- Tableau Dashboard best practices: Shneiderman’s mantra, labels, highlights

---

## Screenshot

![Dashboard Preview](./Unit7.png)

---

## Files Included

- `Unit7.png`: Dashboard screenshot
- `Unit 7 Homework Deviation Analysis.xlsx`: Dataset used
- `project_description.md`: This project overview
