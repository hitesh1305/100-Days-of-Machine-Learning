# 📘 Day 11 — K-Nearest Neighbors (KNN)

---

# 🎯 Objective

Understand the intuition behind the K-Nearest Neighbors (KNN) algorithm and implement a KNN classification model for predicting customer purchase behavior.

The goal was to understand:
- instance-based learning
- distance-based classification
- nearest neighbor intuition
- importance of feature scaling
- effect of value of K

---

# 🧠 Introduction to KNN

K-Nearest Neighbors (KNN) is a supervised Machine Learning algorithm used mainly for:
- classification
- regression

In this project:
- KNN was used for binary classification.

---

# 📌 Main Idea Behind KNN

KNN works on a simple intuition:

> “Data points that are close to each other are likely to belong to the same class.”

Instead of learning equations:
- KNN memorizes training data
- predictions are made using nearby examples

---

# 📌 Problem Statement

Predict whether a customer will purchase a product based on:
- Age
- Estimated Salary

Target Variable:
```text
Purchased (0 or 1)
```

---

# 📂 Dataset Used

Dataset file used:

```text
datasets/day-11-Social_Network_Ads.csv
```

---

# 📌 Features Used

| Feature | Meaning |
|---|---|
| Age | customer age |
| Estimated Salary | customer salary |

Target:
- Purchased

---

# 🧠 Type of Learning in KNN

---

# 🔹 Supervised Learning

KNN uses:
- labeled training data

to predict:
- labels for new unseen data.

---

# 🔹 Instance-Based Learning

KNN does not:
- train a mathematical model

Instead:
- it stores training examples directly.

---

# 🔹 Non-Parametric Algorithm

KNN does not assume:
- any underlying data distribution.

This makes KNN:
- flexible
- capable of handling non-linear data.

---

# 📌 Workflow Followed

---

# 🔹 Step 1 — Importing Libraries

Imported:
- NumPy
- Pandas
- Matplotlib

---

# 📂 Dataset Import

Loaded dataset using:

```python
pd.read_csv()
```

---

# 📌 Feature Selection

Selected:
- Age
- Estimated Salary

as independent variables.

---

# 📌 Target Variable

Selected:
- Purchased column

as dependent variable.

---

# 🔹 Step 2 — Train-Test Split

Used:

```python
train_test_split()
```

to divide dataset into:
- training set
- testing set

Split used:

```text
75% Training
25% Testing
```

---

# 🔹 Step 3 — Feature Scaling

Used:

```python
StandardScaler()
```

to standardize feature values.

---

# 🧠 Why Feature Scaling is Important in KNN

KNN relies completely on:
- distance calculations

Without scaling:
- features with larger ranges dominate distances.

Example:

| Feature | Range |
|---|---|
| Age | 18–60 |
| Salary | 20000–100000 |

Salary would heavily dominate:
- Euclidean distance calculations

Scaling ensures:
- fair contribution of all features.

---

# 📌 Standardization Formula

```text
z = (x - mean) / standard deviation
```

After scaling:
- mean ≈ 0
- standard deviation ≈ 1

---

# 🔹 Step 4 — Training KNN Model

Imported:

```python
KNeighborsClassifier()
```

from:

```python
sklearn.neighbors
```

---

# 📌 KNN Model Parameters

Used:

```python
n_neighbors = 5
```

Meaning:
- algorithm checks nearest 5 neighbors.

---

# 📌 Distance Metric Used

Used:

```python
metric = 'minkowski'
p = 2
```

This corresponds to:
- Euclidean Distance

---

# 📌 Euclidean Distance Formula

```text
√((x2 - x1)^2 + (y2 - y1)^2)
```

---

# 🧠 Euclidean Distance Intuition

Represents:
- straight-line distance between points.

The nearest points influence:
- final prediction.

---

# 🔹 Step 5 — Prediction

Generated predictions using:

```python
classifier.predict(X_test)
```

Predictions stored in:

```python
y_pred
```

---

# 🔹 Step 6 — Evaluation

Used:

```python
confusion_matrix()
```

to evaluate classification performance.

---

# 📌 Confusion Matrix

Compares:
- actual labels
- predicted labels

---

# 📊 Components of Confusion Matrix

| Component | Meaning |
|---|---|
| True Positive | correctly predicted positive |
| True Negative | correctly predicted negative |
| False Positive | incorrectly predicted positive |
| False Negative | incorrectly predicted negative |

---

# 📈 Visualization

Used Matplotlib scatter plot to visualize:
- Age
- Estimated Salary
- customer classes

---

# 📌 Visualization Intuition

Each point represents:
- one customer

Color represents:
- purchase class

Visualization helps understand:
- how classes are distributed.

---

# 📌 How KNN Makes Predictions

For a new unseen point:

1. compute distances to all training points
2. find nearest K points
3. perform majority voting
4. assign predicted class

---

# 📌 Majority Voting

Example:

If nearest neighbors are:

| Neighbor | Class |
|---|---|
| 1 | Purchased |
| 2 | Purchased |
| 3 | Not Purchased |
| 4 | Purchased |
| 5 | Not Purchased |

Prediction:
```text
Purchased
```

because majority neighbors belong to:
```text
Purchased class
```

---

# 📌 Importance of Value of K

Choosing correct K is very important.

---

# 🔹 Small K Value

Example:
```text
K = 1
```

Advantages:
- captures local patterns

Disadvantages:
- sensitive to noise
- overfitting risk

---

# 🔹 Large K Value

Advantages:
- smoother predictions
- less noise sensitivity

Disadvantages:
- computationally expensive
- may underfit data

---

# 🧠 Important Insight

Choosing K involves balancing:
- overfitting
- underfitting

---

# 📌 Advantages of KNN

- simple and intuitive
- easy to implement
- no training phase
- handles non-linear boundaries

---

# 📌 Limitations of KNN

- slow for large datasets
- sensitive to feature scaling
- sensitive to noisy data
- high memory usage
- affected by curse of dimensionality

---

# 📌 Curse of Dimensionality

As number of features increases:
- distances become less meaningful

This can reduce:
- KNN performance significantly.

---

# 📌 Important sklearn Functions Used

| Function | Purpose |
|---|---|
| `StandardScaler()` | feature scaling |
| `train_test_split()` | dataset splitting |
| `KNeighborsClassifier()` | KNN classifier |
| `fit()` | store training data |
| `predict()` | prediction |
| `confusion_matrix()` | evaluation |

---

# 🧠 Key Concepts Learned

- supervised learning
- instance-based learning
- lazy learning
- Euclidean distance
- feature scaling
- nearest neighbors
- majority voting
- overfitting vs underfitting
- value of K

---

# 🧠 Challenges Faced

- Understanding why scaling is important
- Understanding distance calculations
- Understanding how K affects prediction
- Understanding majority voting intuition

---

# 🔁 How I Solved Them

- Connected KNN with geometric intuition
- Visualized neighboring points
- Understood Euclidean distance mathematically
- Compared effects of small and large K values

---

# 📈 What I Improved Today

- understanding of distance-based learning
- understanding of classification intuition
- understanding of feature scaling importance
- understanding of nearest neighbor prediction
- understanding of model evaluation basics

---

# 📌 Real World Applications

KNN is used in:
- recommendation systems
- image recognition
- fraud detection
- medical diagnosis
- pattern recognition

---

# 🧠 Important Insight

KNN does not truly “learn” a mathematical model.

Instead:
> it predicts using similarity and nearby examples.

---

# 🚀 Final Understanding

KNN classification is essentially:
> finding the closest neighboring points and predicting based on their majority class.

---

# 🧠 Final Insight

> “KNN predicts by comparing similarity — nearby points usually belong to similar categories.”