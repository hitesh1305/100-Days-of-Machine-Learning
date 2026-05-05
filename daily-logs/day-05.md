# Day 05 — Pandas & Probability Foundations

---

## 📌 Objective

Transition from numerical arrays (NumPy) to structured datasets using Pandas, and build a foundational understanding of probability concepts used in Machine Learning.

---

## 🧠 What I Worked On

Today focused on two major areas:

### 1. Pandas (Data Handling)

* Understanding structured data using DataFrames
* Performing data inspection, selection, filtering
* Creating new features (columns)
* Handling missing values
* Performing basic statistical analysis

---

### 2. Probability (Conceptual Understanding)

* Basics of probability and rules
* Conditional probability and Bayes theorem
* Random variables and probability distributions
* Understanding uncertainty in data

---

# ⚙️ Pandas — Practical Work

---

## 🔹 Series

* Created a Pandas Series
* Understood it as a single labeled column

---

## 🔹 DataFrame

* Created structured datasets using dictionaries
* Understood rows and columns as tabular data

---

## 🔹 Data Inspection

Used:

* `head()` → first rows
* `tail()` → last rows
* `shape` → dataset dimensions
* `columns` → feature names
* `info()` → data types and null values

---

## 🔹 Reading & Writing Data

* Saved dataset using `to_csv()`
* Loaded dataset using `read_csv()`

👉 Important for real-world workflows

---

## 🔹 Data Selection

* Selected single columns
* Selected multiple columns
* Accessed rows using:

  * `iloc` (index-based)
  * `loc` (label-based)

---

## 🔹 Data Filtering

Applied conditions:

```python
df[df["Score"] > 84]
```

👉 Used to extract meaningful subsets

---

## 🔹 Feature Engineering

Created new columns:

* Boolean column (`Passed`)
* Derived column (`Score_Percentage`)
* Added categorical column (`City`)

---

## 🔹 Descriptive Statistics

Used:

* `mean()`
* `min()`
* `max()`
* `describe()`

👉 Summarizes dataset properties

---

## 🔹 Handling Missing Data

* Removed null values using `dropna()`
* Filled missing values using `fillna()` with mean

👉 Important for real-world datasets

---

# 📊 Probability — Conceptual Learning

---

## 🔹 Topics Covered

* Basic probability rules
* Conditional probability
* Bayes theorem
* Random variables
* Probability distributions

---

## 🔹 Key Understanding

* Probability models uncertainty in data
* Helps in making predictions
* Forms the foundation of many ML algorithms

---

# 🔍 Key Insights

* Data is not just numbers—it has structure and meaning
* Pandas simplifies real-world dataset handling
* Filtering and transformation are core operations
* Missing data handling is critical in ML pipelines
* Probability helps models reason under uncertainty

---

# ❗ Challenges Faced

* Understanding difference between `loc` and `iloc`
* Thinking in terms of dataframes instead of lists
* Connecting probability theory to ML intuition

---

# 🔁 How I Resolved Them

* Practiced with small datasets
* Repeated operations like filtering and selection
* Focused on understanding concepts instead of memorizing

---

# 📘 Code Implementation

* [Day 05 Pandas Code](../projects/day-05-pandas)

---

# 📈 What I Improved Today

* Ability to work with structured datasets
* Understanding of real-world data workflows
* Introduction to probabilistic thinking

---

# 🧠 Revision Note

> “Pandas helps structure data, probability helps interpret it — together they form the foundation of Machine Learning.”
