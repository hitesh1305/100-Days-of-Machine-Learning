# 📘 Day 12 — Decision Tree Classification

---

# 🎯 Objective

Understand the intuition behind Decision Tree Classification and learn how Machine Learning models make predictions using rule-based hierarchical splitting.

The goal was to understand:
- entropy
- information gain
- impurity reduction
- recursive splitting
- decision boundaries
- overfitting in trees

---

# 🧠 Introduction to Decision Trees

Decision Tree is a supervised Machine Learning algorithm used for:
- classification
- regression

In this project:
- Decision Tree was used for classification.

---

# 📌 Main Idea Behind Decision Trees

Decision Trees work like:
- flowcharts
- sequences of decisions

The algorithm repeatedly asks:
> “Which condition best separates the data?”

until it reaches a final prediction.

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
datasets/day-12-Social_Network_Ads.csv
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

# 🧠 Decision Tree Intuition

Suppose the model asks:

```text
Age > 30?
```

If:
```text
YES
```

then:
```text
Salary > 50000?
```

Eventually:
- the model reaches a prediction.

This creates:
- a tree-like decision structure.

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

Feature scaling is generally:
- less important for Decision Trees

because:
- trees split using conditions
- not distance calculations

However:
- scaling can still be applied for consistency.

---

# 🔹 Step 4 — Training the Decision Tree Model

Imported:

```python
DecisionTreeClassifier()
```

from:

```python
sklearn.tree
```

---

# 📌 Criterion Used

Used:

```python
criterion = 'entropy'
```

Meaning:
- the tree uses entropy to measure impurity.

---

# 📌 Model Training

Used:

```python
classifier.fit(X_train, y_train)
```

The model learned:
- optimal splitting rules
- hierarchical decisions

from training data.

---

# 📌 Structure of a Decision Tree

A Decision Tree contains:

| Component | Meaning |
|---|---|
| Root Node | first split |
| Decision Node | condition/question |
| Leaf Node | final prediction |
| Branch | outcome of decision |

---

# 📌 Root Node

The starting point of the tree.

Represents:
- the best first split in the dataset.

---

# 📌 Decision Nodes

Internal nodes containing:
- splitting conditions

Example:

```text
Age > 35?
```

---

# 📌 Leaf Nodes

Final nodes.

Represent:
- class predictions

Example:
```text
Purchased
```

---

# 📌 Branches

Represent:
- outcomes of decisions

Example:
```text
YES / NO
```

---

# 📌 Entropy

Entropy measures:
> impurity or randomness in the data.

---

# 📈 Entropy Formula

:contentReference[oaicite:0]{index=0}

---

# 🧠 Entropy Intuition

| Situation | Entropy |
|---|---|
| pure node | low entropy |
| mixed node | high entropy |

---

# 📌 Example of Pure Node

| Purchased | Count |
|---|---|
| Yes | 10 |
| No | 0 |

Entropy:
```text
0
```

Completely pure.

---

# 📌 Example of Impure Node

| Purchased | Count |
|---|---|
| Yes | 5 |
| No | 5 |

Entropy:
```text
high
```

Highly mixed.

---

# 📌 Information Gain

Decision Trees choose splits using:
- Information Gain

---

# 🧠 Information Gain Meaning

Measures:
> reduction in impurity after splitting.

The tree selects:
- the split with highest information gain.

---

# 📈 Information Gain Formula

:contentReference[oaicite:1]{index=1}

---

# 📌 Recursive Splitting

Decision Trees repeatedly:
- split the data
- create smaller groups
- improve purity

This process continues recursively.

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

Used visualization to observe:
- customer distribution
- classification regions
- tree-based prediction behavior

---

# 📌 Decision Boundary

Decision Trees create:
- non-linear decision boundaries

Unlike:
- Logistic Regression (linear boundaries)

---

# 📌 Overfitting in Decision Trees

Decision Trees can easily:
- memorize training data

especially when:
- trees become too deep.

---

# 🧠 Overfitting Intuition

Deep trees:
- fit noise
- reduce generalization ability

Result:
- strong training performance
- weak testing performance

---

# 📌 Underfitting

Very shallow trees:
- fail to capture patterns

Result:
- poor learning performance

---

# 📌 Bias vs Variance Intuition

| Tree Type | Behavior |
|---|---|
| shallow tree | high bias |
| deep tree | high variance |

---

# 📌 Pruning

Pruning removes:
- unnecessary branches

to improve:
- generalization

---

# 📌 Advantages of Decision Trees

- easy to understand
- interpretable
- handles non-linear relationships
- minimal preprocessing required
- works with numerical and categorical data

---

# 📌 Limitations

- prone to overfitting
- unstable to small data changes
- can create overly complex structures

---

# 📌 Feature Importance

Decision Trees naturally identify:
- important features

Features used near the root:
- usually contribute more strongly.

---

# 📌 Important sklearn Functions Used

| Function | Purpose |
|---|---|
| `DecisionTreeClassifier()` | Decision Tree model |
| `fit()` | model training |
| `predict()` | prediction |
| `confusion_matrix()` | evaluation |

---

# 🧠 Key Concepts Learned

- entropy
- information gain
- recursive splitting
- impurity reduction
- overfitting
- underfitting
- feature importance
- non-linear decision boundaries

---

# 🧠 Challenges Faced

- Understanding entropy intuition
- Understanding how trees split data
- Understanding information gain
- Understanding recursive partitioning
- Understanding overfitting in trees

---

# 🔁 How I Solved Them

- Connected entropy with impurity intuition
- Visualized splitting step-by-step
- Compared pure vs impure nodes
- Related deep trees with memorization

---

# 📈 What I Improved Today

- understanding of tree-based learning
- understanding of impurity reduction
- understanding of hierarchical decision systems
- understanding of overfitting intuition
- understanding of classification workflows

---

# 📌 Real World Applications

Decision Trees are used in:
- fraud detection
- medical diagnosis
- customer segmentation
- recommendation systems
- risk analysis

---

# 🧠 Important Insight

Decision Trees do not:
- learn equations
- calculate nearest distances

Instead:
> they learn sequences of decisions that split data effectively.

---

# 🚀 Final Understanding

Decision Trees are essentially:
> intelligent rule-based systems that recursively divide data into purer groups.

---

# 🧠 Final Insight

> “Decision Trees classify data by learning the questions that best separate different categories.”