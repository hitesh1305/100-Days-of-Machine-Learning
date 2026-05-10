# 📘 Day 09 — Logistic Regression

---

# 🎯 Objective

Understand Logistic Regression for binary classification problems and learn how Machine Learning models classify data into categories instead of predicting continuous numerical values.

The goal was to understand:
- classification problems
- sigmoid intuition
- probability-based prediction
- decision boundaries
- confusion matrix evaluation

---

# 🧠 Introduction to Logistic Regression

Logistic Regression is a supervised Machine Learning algorithm used for **classification tasks**.

Unlike Linear Regression:
- which predicts continuous values

Logistic Regression predicts:
- probabilities
- class labels

---

# 📌 Classification Problem

Classification is used when:
- outputs belong to categories

Examples:
- spam or not spam
- disease or no disease
- purchased or not purchased
- pass or fail

---

# 📂 Dataset Used

Dataset file used:

```text
datasets/day-09-Social_Network_Ads.csv
```

---

# 📌 Problem Statement

Predict whether a customer will purchase a product based on:
- Age
- Estimated Salary

Target variable:
- Purchased (0 or 1)

---

# 🧠 Features and Target

| Variable | Meaning |
|---|---|
| Age | Independent feature |
| Estimated Salary | Independent feature |
| Purchased | Target variable |

---

# 📈 Why Logistic Regression?

Linear Regression is not suitable for classification because:
- outputs can go below 0 or above 1
- classification requires probabilities

Logistic Regression solves this using:
- Sigmoid Function

---

# 📌 Sigmoid Function

The sigmoid function converts values into probabilities between:
```text
0 and 1
```

Formula:

```text
σ(z) = 1 / (1 + e^(-z))
```

---

# 🧠 Intuition of Sigmoid Function

The sigmoid function creates an S-shaped curve.

Large positive values:
```text
→ close to 1
```

Large negative values:
```text
→ close to 0
```

This makes it ideal for binary classification.

---

# 📌 Logistic Regression Equation

```text
z = b0 + b1x1 + b2x2
```

Where:
- `x1` = Age
- `x2` = Estimated Salary
- `b0` = intercept
- `b1`, `b2` = coefficients

The sigmoid function is then applied to:
```text
z
```

to generate probability.

---

# 📌 Binary Classification

Output classes:

| Value | Meaning |
|---|---|
| 0 | Not Purchased |
| 1 | Purchased |

---

# ⚙️ Workflow Followed

---

# 🔹 Step 1 — Data Preprocessing

Imported:
- NumPy
- Pandas
- Matplotlib

---

# 📂 Dataset Import

Dataset loaded using:

```python
pd.read_csv()
```

---

# 📌 Feature Selection

Selected:
- Age
- Estimated Salary

as input features.

---

# 📌 Target Variable

Selected:
- Purchased column

as target variable.

---

# ✂️ Train-Test Split

Used:

```python
train_test_split()
```

to divide data into:
- training set
- testing set

Split used:

```text
75% Training
25% Testing
```

---

# 📌 Feature Scaling

Used:

```python
StandardScaler()
```

to standardize features.

---

# 🧠 Why Scaling is Important Here

Logistic Regression depends heavily on:
- distances
- optimization

Features with large magnitudes can dominate training.

Scaling ensures:
- features contribute more equally

---

# 🔹 Step 2 — Training Logistic Regression Model

Imported:

```python
LogisticRegression()
```

from:

```python
sklearn.linear_model
```

---

# 📌 Model Training

Used:

```python
classifier.fit(X_train, y_train)
```

The model learned:
- coefficients
- decision boundary

from training data.

---

# 🔹 Step 3 — Prediction

Generated predictions using:

```python
classifier.predict(X_test)
```

Predictions stored in:

```python
y_pred
```

---

# 🔹 Step 4 — Evaluation

Used:

```python
confusion_matrix()
```

to evaluate classification performance.

---

# 📌 Confusion Matrix

Confusion Matrix compares:
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

# 🧠 Why Confusion Matrix Matters

Accuracy alone can sometimes be misleading.

Confusion Matrix helps understand:
- exact prediction behavior
- where model makes mistakes

---

# 📈 Visualization

Used Matplotlib to visualize:
- customer data points
- classification regions

Scatter plot displayed:
- Age
- Estimated Salary
- purchase classes

---

# 📌 Decision Boundary

Logistic Regression creates a decision boundary separating:
- purchased customers
- non-purchased customers

The boundary helps classify new unseen data.

---

# 🧠 Key Concepts Learned

---

# 📌 Classification vs Regression

| Regression | Classification |
|---|---|
| predicts numbers | predicts categories |
| continuous output | discrete output |
| salary prediction | spam detection |

---

# 📌 Probability-Based Prediction

Logistic Regression predicts:
- probability of belonging to a class

---

# 📌 Sigmoid Function

Maps values into:
```text
0 → 1
```

range.

---

# 📌 Decision Boundary

Separates different prediction classes.

---

# 📌 Feature Scaling

Important because:
- features operate on different scales
- scaling stabilizes optimization

---

# 📌 Confusion Matrix

Used for evaluating classification performance.

---

# 🧠 Challenges Faced

- Understanding why Linear Regression cannot be used for classification
- Understanding probability outputs
- Understanding sigmoid function intuition
- Understanding confusion matrix components
- Understanding decision boundary visualization

---

# 🔁 How I Solved Them

- Connected sigmoid function with probability intuition
- Compared regression vs classification carefully
- Understood confusion matrix step-by-step
- Visualized classification behavior using plots

---

# 📈 What I Improved Today

- Understanding of classification problems
- Understanding of Logistic Regression workflow
- Understanding probability-based prediction
- Understanding evaluation using confusion matrix
- Understanding feature scaling importance

---

# 🚀 Next Step

- Learn evaluation metrics:
  - accuracy
  - precision
  - recall
  - F1-score

- Learn K-Nearest Neighbors (KNN)
- Understand decision boundaries more deeply

---

# 🧠 Final Insight

> “Logistic Regression does not predict exact values — it predicts the probability of belonging to a class.”