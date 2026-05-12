# 📘 K-Nearest Neighbors (KNN) — Concepts

---

# 🧠 What is K-Nearest Neighbors (KNN)?

K-Nearest Neighbors (KNN) is a supervised Machine Learning algorithm used mainly for:
- classification problems
- regression problems

It is one of the simplest and most intuitive Machine Learning algorithms.

---

# 📌 Main Idea Behind KNN

KNN works using a very simple intuition:

> “Similar data points are usually close to each other.”

The algorithm predicts the class of a new data point based on:
- nearby labeled data points

---

# 📌 Example Intuition

Suppose:
- most nearby customers purchased a product

Then:
- the new customer is also likely to purchase it.

---

# 🧠 KNN is a Lazy Learning Algorithm

KNN does not:
- build an explicit mathematical model during training.

Instead:
- it memorizes the training data
- predictions happen during testing time

This is why KNN is called:
- instance-based learning
- lazy learning algorithm

---

# 📌 Types of Learning in KNN

---

# 🔹 Non-Parametric Algorithm

KNN is non-parametric because:
- it does not assume any underlying data distribution

Unlike some algorithms:
- KNN does not assume data is linear or normally distributed.

---

# 🔹 Instance-Based Learning

KNN stores:
- training instances directly

Instead of learning:
- equations
- coefficients
- weights

---

# 🔹 Supervised Learning

KNN learns from:
- labeled training data

Meaning:
- inputs already have known outputs.

---

# 📌 How KNN Works

KNN classification involves:

1. storing labeled data points
2. calculating distance from new point
3. finding nearest neighbors
4. majority voting

---

# 🧠 Step-by-Step Workflow

---

# 🔹 Step 1 — Choose Value of K

Select:
```text
K = number of nearest neighbors
```

Example:
```text
K = 3
```

means:
- algorithm checks nearest 3 points.

---

# 🔹 Step 2 — Compute Distance

Calculate distance between:
- new data point
- all training points

---

# 🔹 Step 3 — Find Nearest Neighbors

Select:
- K closest points

---

# 🔹 Step 4 — Majority Voting

The class occurring most frequently among neighbors becomes:
- predicted class

---

# 📌 Example

Suppose:
```text
K = 5
```

Nearest neighbors:

| Neighbor | Class |
|---|---|
| 1 | Purchased |
| 2 | Purchased |
| 3 | Not Purchased |
| 4 | Purchased |
| 5 | Not Purchased |

Majority class:
```text
Purchased
```

Prediction:
```text
Purchased
```

---

# 📌 Distance Measures in KNN

Distance calculation is the most important part of KNN.

---

# 🔹 Euclidean Distance

Most commonly used distance metric.

Formula:

```text
√((x2 - x1)^2 + (y2 - y1)^2)
```

For multiple dimensions:

```text
√((x1-y1)^2 + (x2-y2)^2 + ... + (xn-yn)^2)
```

---

# 🧠 Euclidean Distance Intuition

Represents:
- straight line distance between two points

---

# 🔹 Manhattan Distance

Distance measured along axes.

Formula:

```text
|x1-y1| + |x2-y2| + ...
```

Useful in:
- grid-like movement problems

---

# 🔹 Hamming Distance

Used mainly for:
- categorical variables

Measures:
- number of differing positions

---

# 🔹 Minkowski Distance

Generalized form of:
- Euclidean
- Manhattan distance

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
- less sensitive to noise

Disadvantages:
- computationally expensive
- may ignore local patterns
- underfitting risk

---

# 🧠 Common Practice

Try multiple K values and:
- choose best performing one.

---

# 📌 Why Feature Scaling is Important in KNN

KNN relies completely on:
- distance calculations

Features with larger magnitude dominate distances.

Example:

| Feature | Range |
|---|---|
| Age | 18–60 |
| Salary | 20000–100000 |

Salary would dominate:
- Euclidean distance

---

# 🔹 Solution: Feature Scaling

Use:
- Standardization
- Normalization

before applying KNN.

---

# 📌 KNN for Classification

Output:
- class label

Examples:
- spam/not spam
- pass/fail
- purchased/not purchased

---

# 📌 KNN for Regression

KNN can also predict:
- continuous values

For regression:
- average of nearest neighbors is used.

---

# 📌 Advantages of KNN

- simple and intuitive
- easy to implement
- no training phase
- works well on smaller datasets
- handles non-linear patterns

---

# 📌 Limitations of KNN

- computationally expensive for large datasets
- slow prediction time
- sensitive to irrelevant features
- sensitive to feature scaling
- affected by noisy data

---

# 📌 Curse of Dimensionality

As number of features increases:
- distance calculations become less meaningful

This reduces:
- KNN performance

---

# 📌 Applications of KNN

Used in:
- recommendation systems
- pattern recognition
- image classification
- fraud detection
- medical diagnosis

---

# 📌 Important sklearn Functions

---

## 🔹 KNeighborsClassifier()

Creates KNN classifier.

---

## 🔹 fit()

Stores training data.

---

## 🔹 predict()

Predicts class labels.

---

# 🧠 Key Concepts Learned

- supervised learning
- lazy learning
- instance-based learning
- distance metrics
- Euclidean distance
- majority voting
- feature scaling importance
- value of K
- overfitting vs underfitting

---

# 🧠 Important Insight

KNN does not truly “learn” a model.

Instead:
> it remembers the training data and makes predictions based on nearby examples.

---

# 🚀 Real Understanding

KNN classification is essentially:
> finding the most similar neighboring data points and predicting based on their majority class.

---

# 🧠 Final Insight

> “KNN predicts by comparing similarity — nearby points usually belong to similar classes.”