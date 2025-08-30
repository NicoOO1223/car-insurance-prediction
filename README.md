# 🚗 Car Insurance Outcome Analysis

This project uses **logistic regression** to determine the most predictive feature for a **binary car insurance outcome**.  
Each feature is analyzed individually to evaluate its predictive power.

---

## 📌 Project Overview

- Dataset: `car_insurance.csv` (contains features like driving experience, age, vehicle info, etc.)
- Goal: Identify the **single most predictive feature** for the target outcome
- Approach:
  1. Load dataset and identify predictors
  2. Fit **univariate logistic regression** models (one feature at a time)
  3. Predict outcomes and calculate accuracy
  4. Rank features based on accuracy
  5. Output the best predictor

- Example Result: `driving_experience` with accuracy `0.77710`

---

## 🛠️ Tech Stack

- **Python** – scripting and analysis  
- **Pandas / NumPy** – data manipulation  
- **Statsmodels** – logistic regression modeling  

---
