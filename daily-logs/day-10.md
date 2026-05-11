# 📘 Day 10 — Revision of Data Cleaning & Data Preprocessing Techniques

---

# 🎯 Objective

Revise and strengthen the foundational concepts of:
- data cleaning
- data preprocessing
- feature engineering
- feature scaling
- dimensionality reduction
- feature selection

The goal was to build stronger intuition about why preprocessing is one of the most important stages in Machine Learning workflows.

---

# 🧠 Why Data Preprocessing Matters

Raw real-world data is rarely:
- complete
- clean
- consistent
- structured

Machine Learning models cannot learn effectively from noisy or poor-quality data.

Data preprocessing helps:
- improve data quality
- reduce noise
- improve model performance
- improve training stability

---

# 📌 Understanding Data Cleaning

Data cleaning refers to:
> identifying and correcting inaccurate, incomplete, duplicate, or inconsistent data.

---

# 🧠 Common Data Quality Issues

Real-world datasets often contain:
- missing values
- duplicate rows
- inconsistent formatting
- incorrect labels
- outliers
- noisy data

These issues negatively affect:
- model accuracy
- training stability
- prediction reliability

---

# 📌 Missing Data Handling

Missing values are one of the most common preprocessing problems.

Missing data may occur because:
- user did not provide information
- sensor failure
- corrupted records
- incomplete collection process

---

# 🔍 Common Techniques for Handling Missing Values

---

## 🔹 Mean Imputation

Replace missing values using:
- average value of the column

Useful when:
- data distribution is relatively normal

---

## 🔹 Median Imputation

Replace missing values using:
- middle value of sorted data

Useful when:
- dataset contains outliers

---

## 🔹 Mode Imputation

Replace missing values using:
- most frequent value

Useful for:
- categorical data

---

# 🧠 Important Insight

Poor missing value handling can:
- bias the model
- reduce prediction quality
- distort data distribution

---

# 📌 Categorical Data Encoding

Machine Learning models operate on:
```text
numerical data
```

not:
```text
text labels
```

Examples of categorical data:
- Male/Female
- Yes/No
- Country names

---

# 🔹 Label Encoding

Converts categories into:
```text
integer labels
```

Example:

| Category | Encoded |
|---|---|
| Male | 0 |
| Female | 1 |

---

# ⚠️ Problem with Label Encoding

Models may incorrectly assume:
```text
1 > 0
```

creating false ordinal relationships.

---

# 🔹 One Hot Encoding

Creates separate binary columns for each category.

Example:

| Country | India | USA | UK |
|---|---|---|---|
| India | 1 | 0 | 0 |
| USA | 0 | 1 | 0 |

---

# 🧠 Why One Hot Encoding is Important

It prevents:
- false ranking assumptions
- incorrect numerical relationships

---

# 📌 Feature Scaling

Different features may have different ranges.

Example:

| Feature | Range |
|---|---|
| Age | 18–60 |
| Salary | 20000–100000 |

Large magnitude features can dominate:
- distance calculations
- optimization

---

# 🔹 Standardization

Transforms data using:

```text
z = (x - mean) / standard deviation
```

After standardization:
- mean ≈ 0
- standard deviation ≈ 1

---

# 🧠 Why Standardization Helps

Helps algorithms:
- converge faster
- train more stably
- treat features more equally

Especially important for:
- Logistic Regression
- KNN
- SVM
- Neural Networks

---

# 🔹 Normalization

Normalization scales values into:
```text
0 → 1
```

range.

Common formula:

```text
(x - min) / (max - min)
```

---

# 📌 Difference Between Normalization and Standardization

| Standardization | Normalization |
|---|---|
| mean = 0 | range = 0 to 1 |
| handles outliers better | sensitive to outliers |
| used frequently in ML | used in bounded scaling |

---

# 📌 Feature Engineering

Feature Engineering means:
> creating better input features from raw data.

This is one of the most powerful steps in Machine Learning.

---

# 🧠 Examples of Feature Engineering

From:
```text
Date of Birth
```

Create:
- age
- birth year
- age group

From:
```text
timestamp
```

Create:
- hour
- day
- month
- weekday

---

# 📌 Why Feature Engineering Matters

Better features often improve performance more than:
- changing algorithms

Good features help models:
- discover patterns more effectively

---

# 📌 Feature Selection

Feature Selection means:
> selecting the most useful features for training.

Not all variables contribute positively.

Some may:
- add noise
- increase complexity
- create overfitting

---

# 🔍 Benefits of Feature Selection

- reduces dimensionality
- improves training speed
- improves generalization
- reduces overfitting

---

# 📌 Dimensionality Reduction

Dimensionality Reduction reduces:
- number of features

while preserving:
- important information

---

# 🧠 Why Dimensionality Reduction is Needed

Too many features can cause:
- overfitting
- computational cost
- curse of dimensionality

---

# 🔹 PCA (Principal Component Analysis)

PCA transforms data into:
- lower-dimensional representation

while preserving maximum variance.

---

# 📌 Data Leakage

Data leakage occurs when:
- information from test data leaks into training

This causes:
- unrealistically high performance
- misleading evaluation

---

# 🧠 Example of Leakage

Scaling entire dataset before train-test split.

Correct approach:
- split first
- scale training data
- transform test data separately

---

# 📌 Importance of Preprocessing Pipeline

A good preprocessing pipeline:
- improves data quality
- improves learning stability
- improves model performance
- improves generalization

---

# 🧠 Key Concepts Revised Today

- data cleaning
- missing value handling
- categorical encoding
- one hot encoding
- standardization
- normalization
- feature engineering
- feature selection
- dimensionality reduction
- data leakage

---

# 📈 What I Improved Today

- strengthened preprocessing intuition
- improved understanding of feature preparation
- revised scaling techniques deeply
- improved understanding of data quality importance
- reinforced ML workflow understanding

---

# 📚 References Used

- DataCamp — Data Preprocessing
- Tableau — Data Cleaning
- IBM — Feature Engineering
- DataCamp — Normalization vs Standardization
- IBM — Dimensionality Reduction
- IBM — Feature Selection

---

# 🚀 Next Step

- Continue strengthening ML algorithms
- Learn evaluation metrics deeply
- Understand model optimization techniques
- Apply preprocessing concepts in larger projects

---

# 🧠 Final Insight

> “In Machine Learning, model quality is heavily dependent on data quality. Good preprocessing often matters more than complex algorithms.”