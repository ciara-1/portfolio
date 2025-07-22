# Quick Sort Pivot Comparison — Python Benchmarking

**Tool:** Python  
**Focus:** Algorithm design and performance benchmarking

---

## Project Goal

Evaluate and compare the average running time of Quick Sort using two pivot strategies:
- Fixed pivot: first element
- Random pivot: randomly selected element

---

## Tasks Performed

- Implemented two Quick Sort variants:
  - `quick_sort_with_first_pivot()`
  - `quick_sort_with_random_pivot()`
- Generated test datasets:
  - Random arrays
  - Pre-sorted arrays
  - Reversed arrays
  - Uniform arrays
- Measured execution time using Python’s `time` module

---

## Key Findings

- **Randomized pivot** consistently outperformed the **fixed pivot** approach in average-case runtime.
- **Fixed pivot** suffered worst-case performance with sorted or reversed arrays.
- Demonstrates importance of pivot strategy in recursive sorting algorithms.

---

## Files Included

- `Project2.py`: Python script with complete class implementation and test scenario
- `project_description.md` : This project overview
---

*Note: This was a self-contained benchmarking project using standard Python libraries for performance testing.*
