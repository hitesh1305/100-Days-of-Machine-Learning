# 📘 Logistic Regression — Concepts

---

# 🧠 What is Logistic Regression?

Logistic Regression is a supervised Machine Learning algorithm used for **classification problems**.

Unlike Linear Regression:
- which predicts continuous numerical values

Logistic Regression predicts:
- probabilities
- class labels

---

# 📌 Purpose of Logistic Regression

Used when the target variable belongs to categories.

Examples:
- spam detection
- disease prediction
- customer purchase prediction
- pass or fail prediction

---

# 📂 Dataset Used

Dataset file used:

```text
datasets/Social_Network_Ads.csv
```

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

# 📌 Features Used

| Feature | Meaning |
|---|---|
| Age | customer age |
| Estimated Salary | customer salary |

Target:
- Purchased

---

# 📌 Classification vs Regression

| Linear Regression | Logistic Regression |
|---|---|
| predicts numbers | predicts categories |
| continuous output | discrete output |
| house price prediction | spam detection |
| salary prediction | disease prediction |

---

# 🧠 Why Linear Regression Cannot Be Used

Linear Regression outputs:
```text
values from -∞ to +∞
```

But classification requires:
```text
probabilities between 0 and 1
```

Predictions like:
```text
1.5 or -0.4
```

are invalid probabilities.

---

# 📌 Sigmoid Function

Logistic Regression uses:
- Sigmoid Function

to convert values into:
```text
0 → 1
```

range.

---

# 📈 Sigmoid Function Formula

```text
σ(z) = 1 / (1 + e^(-z))
```

---

# 🧠 Sigmoid Function Intuition

The sigmoid function creates:
- an S-shaped curve

Behavior:

| Input | Output |
|---|---|
| large positive | close to 1 |
| large negative | close to 0 |
| near 0 | around 0.5 |

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

The sigmoid function is then applied on:
```text
z
```

to generate probabilities.

---

# 📌 Probability Prediction

Logistic Regression predicts:
- probability of belonging to a class

Example:

```text
ŷ = 0.82
```

means:
- 82% probability of purchase.

---

# 📌 Decision Boundary

Logistic Regression separates classes using:
- decision boundary

Typical threshold:

| Probability | Predicted Class |
|---|---|
| ≥ 0.5 | 1 |
| < 0.5 | 0 |

---

# 📌 Binary Classification

Output classes:

| Value | Meaning |
|---|---|
| 0 | Not Purchased |
| 1 | Purchased |

---

# 📌 Workflow Followed

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

as independent variables.

---

# 📌 Target Variable

Selected:
- Purchased column

as dependent variable.

---

# ✂️ Train-Test Split

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

# 📌 Feature Scaling

Used:

```python
StandardScaler()
```

to standardize features.

---

# 🧠 Why Feature Scaling Was Important

Features had different ranges:
- Age
- Salary

Without scaling:
- larger values dominate optimization

Scaling helps:
- faster convergence
- stable training
- fair contribution of features

---

# 🔹 Standardization Formula

```text
z = (x - mean) / standard deviation
```

After scaling:
- mean ≈ 0
- standard deviation ≈ 1

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
| True Positive (TP) | correctly predicted positive |
| True Negative (TN) | correctly predicted negative |
| False Positive (FP) | incorrectly predicted positive |
| False Negative (FN) | incorrectly predicted negative |

---

# 📌 Why Confusion Matrix Matters

Accuracy alone may not reveal:
- exact model mistakes

Confusion Matrix helps analyze:
- prediction quality
- classification behavior

---

# 📈 Visualization

Used Matplotlib scatter plot for visualization.

Visualized:
- Age
- Estimated Salary
- class labels

---

# 📌 Visualization Intuition

Each point represents:
- one customer

Point color represents:
- purchased or not purchased

Visualization helps understand:
- class distribution
- feature relationships

---

# 📌 Important sklearn Functions Used

| Function | Purpose |
|---|---|
| `StandardScaler()` | feature scaling |
| `train_test_split()` | dataset splitting |
| `LogisticRegression()` | model creation |
| `fit()` | model training |
| `predict()` | prediction |
| `confusion_matrix()` | evaluation |

---

# 🧠 Key Concepts Learned

- classification problems
- sigmoid function
- probability prediction
- feature scaling
- confusion matrix
- binary classification
- decision boundary
- model evaluation basics

---

# 🧠 Challenges Faced

- Understanding probability-based prediction
- Understanding sigmoid function intuition
- Understanding confusion matrix values
- Understanding why scaling matters
- Understanding classification vs regression

---

# 🔁 How I Solved Them

- Connected sigmoid outputs with probability intuition
- Compared Linear Regression and Logistic Regression
- Visualized classification behavior using scatter plots
- Understood confusion matrix step-by-step

---

# 📈 What I Improved

- understanding of classification algorithms
- understanding of probability predictions
- understanding of evaluation techniques
- understanding of feature scaling importance
- understanding of supervised classification workflow

---

# 📌 Real World Applications

Logistic Regression is used in:
- spam detection
- fraud detection
- customer churn prediction
- disease diagnosis
- marketing prediction systems

---

# 🧠 Important Insight

Linear Regression predicts:
```text
numbers
```

Logistic Regression predicts:
```text
probabilities and classes
```

---

# 🚀 Final Understanding

Logistic Regression is essentially:
> a linear model combined with a sigmoid function to perform classification.

---

# 🧠 Final Insight

> “Logistic Regression transforms linear relationships into probability-based classification decisions.”