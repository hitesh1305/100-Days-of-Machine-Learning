# Day 04 — NumPy Basics & Data Manipulation

---

## 📌 Objective

Understand how data is represented and manipulated efficiently using NumPy, and transition from Python lists to vectorized operations.

---

## 🧠 What I Worked On

Today I focused on learning NumPy fundamentals, including:

* Array creation and structure
* Vectorized operations
* Indexing and slicing
* Reshaping data
* Basic statistical operations
* Boolean masking (data filtering)

---

## ⚙️ Key Concepts Implemented

### 🔹 Array Creation

* Created 1D and 2D arrays using `np.array`
* Generated special arrays:

  * zeros (`np.zeros`)
  * ones (`np.ones`)
  * random values (`np.random.rand`)

---

### 🔹 Array Properties

Explored core attributes:

* `shape` → dimensions of array
* `ndim` → number of dimensions
* `size` → total elements

---

### 🔹 Python vs NumPy Performance

Compared execution speed:

* Python list comprehension
* NumPy vectorized operations

👉 Observed that NumPy is significantly faster due to optimized internal implementation.

---

### 🔹 Indexing & Slicing

* Accessed elements using indices
* Extracted rows and columns
* Used slicing for subarrays

---

### 🔹 Vectorized Operations

Performed operations without loops:

* addition, subtraction
* multiplication, division
* power operations

---

### 🔹 Linear Algebra Basics

* Dot product (`np.dot`)
* Cross product (`np.cross`)

---

### 🔹 Reshaping & Flattening

* Converted 1D → 2D using `reshape`
* Flattened arrays using `flatten()`

---

### 🔹 Broadcasting

Applied operations between arrays and scalars:

```python
arr + 10
```

👉 Demonstrates how NumPy avoids explicit loops.

---

### 🔹 Statistical Operations

Used built-in functions:

* mean (`np.mean`)
* sum (`np.sum`)
* max (`np.max`)
* min (`np.min`)

---

### 🔹 Boolean Masking (Important)

Filtered data using conditions:

```python
arr[arr > 25]
```

---

### 🔹 Mini Data Task

* Calculated mean of dataset
* Extracted elements greater than mean

This simulates basic data filtering used in ML pipelines.

---

## 🔍 Key Insights

* NumPy arrays are more efficient than Python lists
* Vectorization removes need for explicit loops
* Boolean masking is a powerful tool for filtering data
* Understanding array structure (`shape`, `ndim`) is essential for ML

---

## ❗ Challenges Faced

* Understanding how NumPy operations work without loops
* Connecting operations to real-world data processing

---

## 🔁 How I Resolved Them

* Practiced small examples step-by-step
* Compared Python vs NumPy implementations
* Focused on intuition instead of memorizing functions

---

## 📘 Code Implementation

* [Day 04 NumPy Code](../projects/day-04-numpy)

---

## 📈 What I Improved Today

* Understanding of efficient data handling
* Ability to perform vectorized operations
* Confidence in working with structured data

---

## 📊 Additional Learning (Statistics)

Also studied core statistical concepts including:
- measures of central tendency (mean, median, mode)
- spread (variance, standard deviation, IQR)
- distributions and skewness
- correlation and covariance
- outlier detection

These concepts are essential for understanding data before applying ML models.

---

## 🎯 Next Step

* Explore advanced NumPy operations (2D arrays, axis-based operations)
* Move to Pandas for real-world data handling
* Start applying NumPy concepts in ML problems

---

## 🧠 Revision Note

> “NumPy is not just a library — it is how machines efficiently process data.”
