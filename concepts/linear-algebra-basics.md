# Linear Algebra for Machine Learning 
---

## 📌 Why Linear Algebra Matters

Machine Learning is not just code — it is **math applied to data**.

Most ML operations involve:

* vectors (data)
* matrices (datasets)
* transformations (models)

---

## 🔹 Scalars, Vectors, Matrices, Tensors

### Scalar

* A single number
* Example: 5

---

### Vector

* 1D array of numbers
* Represents a data point

Example:

```
[2, 4, 6]
```

---

### Matrix

* 2D collection of numbers
* Represents a dataset

Example:

```
[ [1, 2],
  [3, 4] ]
```

---

### Tensor

* Generalization of matrices to higher dimensions

👉 Used in deep learning (images, videos)

---

## 🔹 Basic Matrix Operations

### Addition

* Element-wise

### Multiplication

* Row × Column rule

👉 Important in:

* neural networks
* feature transformations

---

## 🔹 Determinant

### What it tells:

* Whether a matrix is invertible

### Key idea:

* If determinant = 0 → matrix is **singular** (not invertible)

---

## 🔹 Identity Matrix

### Definition:

* Diagonal = 1, rest = 0

Example:

```
[ [1, 0],
  [0, 1] ]
```

### Role:

* Acts like “1” in matrix multiplication

---

## 🔹 Inverse of a Matrix

### Concept:

* Matrix that “undoes” another matrix

If:

```
A × A⁻¹ = I
```

### Important:

* Exists only if determinant ≠ 0

---

## 🔹 Singular Matrix

* Matrix with determinant = 0
* Cannot be inverted

👉 Important in ML:

* causes problems in regression models

---

## 🔹 Eigenvalues & Eigenvectors

### Intuition:

* Eigenvector = direction that doesn’t change
* Eigenvalue = how much it scales

---

### Why important:

* Used in:

  * PCA (dimensionality reduction)
  * understanding data variance

---

## 🔹 Singular Value Decomposition (SVD)

### Concept:

* Breaks matrix into simpler components


### Why useful:

* dimensionality reduction
* noise removal
* recommendation systems

---

## 🔹 Problems in Tensor Analysis

* High dimensional data → computationally expensive
* Memory usage increases rapidly
* Harder to visualize and interpret

---

## 🧠 Key Insights

* Data = vectors
* Dataset = matrix
* Model = transformation

👉 Machine Learning = transforming data using matrices

---

## 🔁 Revision Notes

* Determinant → invertibility
* Eigenvalues → direction + scaling
* SVD → matrix decomposition
* Vectors → data representation

---

## 🎯 What to Remember for Interviews

* Why determinant matters
* When matrix inverse fails
* What eigenvalues represent
* Where SVD is used

---

## 🧠 Final Thought

> “Linear algebra is not just math — it is the language of Machine Learning.”
