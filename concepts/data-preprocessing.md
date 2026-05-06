# 🧹 Data Preprocessing for Machine Learning

---

# 🧠 Why Data Preprocessing Matters

Real-world datasets are rarely clean or directly usable.

Data may contain:

* missing values
* categorical text labels
* inconsistent scales
* noisy information
* duplicated or irrelevant data

Machine Learning algorithms require structured numerical input, so preprocessing transforms raw data into a format suitable for training models.

> “The quality of preprocessing often impacts model performance more than the complexity of the algorithm itself.”

---

# 📍 1. Importing Libraries

Machine Learning workflows depend heavily on external libraries.

---

## 🔹 NumPy

Used for:

* numerical computations
* array operations
* mathematical functions

Example:

```python id="h0mzkm"
import numpy as np
```

---

## 🔹 Pandas

Used for:

* importing datasets
* managing tabular data
* preprocessing operations

Example:

```python id="vqyyvi"
import pandas as pd
```

---

## 🔹 Scikit-learn

Provides:

* preprocessing tools
* train-test splitting
* encoders
* scaling utilities

---

# 📍 2. Importing the Dataset

---

## 🔹 CSV Files

Datasets are commonly stored in:

```python id="bdp71z"
.csv
```

(CSV = Comma Separated Values)

Each row represents a data record and each column represents a feature.

---

## 🔹 Reading Dataset

Used:

```python id="10qy6j"
pd.read_csv()
```

to load the dataset into a DataFrame.

---

## 🔹 Features and Target Variables

Datasets are generally divided into:

### ➤ Features (`X`)

Input variables used for prediction.

Example:

* Age
* Salary
* Country

---

### ➤ Target (`Y`)

Output variable to predict.

Example:

* Purchased / Not Purchased

---

## 🔹 Separation

Example:

```python id="7l8cmr"
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values
```

---

# 📍 3. Handling Missing Data

---

# 🔹 Problem

Real-world data frequently contains missing values.

Reasons:

* human error
* incomplete forms
* corrupted records
* unavailable information

---

## 🔹 Why Missing Data is Dangerous

Missing values can:

* reduce model accuracy
* distort patterns
* cause training failures

---

# 🔹 Common Solutions

---

## ➤ 1. Remove Rows/Columns

Simple but risky because:

* information may be lost
* dataset becomes smaller

---

## ➤ 2. Imputation

Replace missing values with statistical estimates.

---

# 🔹 SimpleImputer

Used:

```python id="0jwmdo"
SimpleImputer
```

from:

```python id="uqo4ry"
sklearn.impute
```

---

# 🔹 Imputation Strategies

---

## ➤ Mean Imputation

Replace missing values with average.

Example:

```python id="48o2ea"
[10, 20, NaN, 40]
Mean = 23.3
```

---

## ➤ Median Imputation

Useful when dataset contains outliers.

---

## ➤ Most Frequent

Used mainly for categorical features.

---

# 🔹 Example

```python id="8bjq2e"
imputer = SimpleImputer(
    missing_values=np.nan,
    strategy="mean"
)
```

---

# 📍 4. Encoding Categorical Data

---

# 🔹 Problem

Machine Learning algorithms cannot directly process text labels.

Example:

```python id="3a74og"
India
France
Germany
```

Algorithms require numerical representations.

---

# 🔹 Label Encoding

Converts categories into numbers.

Example:

```python id="zdfqfy"
Yes -> 1
No  -> 0
```

---

## 🔹 Problem with Label Encoding on Features

Suppose:

```python id="7jlwm4"
India  -> 0
France -> 1
Germany -> 2
```

This unintentionally creates ordering:

```python id="jlwm0k"
Germany > France > India
```

which has no real meaning.

---

# 🔹 One Hot Encoding

Converts categories into binary vectors.

Example:

```python id="vw24s4"
India   -> [1,0,0]
France  -> [0,1,0]
Germany -> [0,0,1]
```

---

# 🔹 Why One Hot Encoding is Better

It:

* removes false ordering
* represents categories independently
* improves model understanding

---

# 🔹 OneHotEncoder

Used:

```python id="b4g03e"
OneHotEncoder
```

from:

```python id="2gwc12"
sklearn.preprocessing
```

---

# 🔹 ColumnTransformer

Used to apply encoding only on selected columns.

Example:

```python id="mcrz2t"
ColumnTransformer
```

---

# 📍 5. Splitting Dataset into Training and Test Sets

---

# 🔹 Why Split Data?

A model must be evaluated on unseen data.

Testing on training data gives unrealistically high performance.

---

# 🔹 Training Set

Used for:

* learning patterns
* fitting the model

---

# 🔹 Test Set

Used for:

* evaluating performance
* checking generalization

---

# 🔹 Common Split

```python id="mwj47o"
80% -> Training
20% -> Testing
```

---

# 🔹 train_test_split

Used:

```python id="8kj0kw"
train_test_split()
```

from:

```python id="g3gsz0"
sklearn.model_selection
```

---

# 🔹 Example

```python id="cwswb6"
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=0
)
```

---

# 📍 6. Feature Scaling

---

# 🔹 Problem

Features may have very different ranges.

Example:

```python id="9y06y4"
Age    -> 25
Salary -> 500000
```

Large-valued features dominate computations.

---

# 🔹 Why Scaling Matters

Many ML algorithms rely on:

* Euclidean distance
* gradient descent optimization

Without scaling:

* convergence slows
* optimization becomes unstable
* models become biased toward larger features

---

# 🔹 Standardization (Z-score Normalization)

Transforms data into:

```python id="3lfx0w"
Mean ≈ 0
Standard deviation ≈ 1
```

---

# 🔹 Formula

```python id="b93tuk"
z = (x - mean) / standard deviation
```

---
# 🔹 Mathematical Intuition Behind Standardization


## 📌 Standardization Formula

Feature standardization transforms data using:

```text
z = (x - mean) / standard deviation
```

Where:

* `x` = original feature value
* `mean` = average of the feature
* `standard deviation` = spread of the feature values

The transformed value is called the **z-score**.

---

# 🧠 Why Does the Mean Become 0?

Suppose we have a feature:

```text
[10, 20, 30]
```

---

## 🔹 Step 1: Calculate Mean

```text
Mean = (10 + 20 + 30) / 3
      = 60 / 3
      = 20
```

---

## 🔹 Step 2: Subtract Mean from Every Value

```text
10 - 20 = -10
20 - 20 = 0
30 - 20 = 10
```

New transformed values:

```text
[-10, 0, 10]
```

---

## 🔹 Step 3: Calculate Mean Again

```text
(-10 + 0 + 10) / 3 = 0
```

👉 Subtracting the mean centers the entire dataset around zero.

---

# 🧠 Why Does Standard Deviation Become 1?

Current transformed values:

```text
[-10, 0, 10]
```

Their standard deviation is approximately:

```text
8.16
```

---

## 🔹 Step 4: Divide Every Value by Standard Deviation

```text
-10 / 8.16 ≈ -1.22
0 / 8.16 = 0
10 / 8.16 ≈ 1.22
```

New scaled values:

```text
[-1.22, 0, 1.22]
```

Now:

* mean ≈ 0
* standard deviation ≈ 1

---

# 🔍 Intuition Behind Standardization

Standardization performs two important operations:

| Operation                    | Purpose               |
| ---------------------------- | --------------------- |
| Subtract mean                | centers data around 0 |
| Divide by standard deviation | normalizes spread     |

---

# 🤖 Why Standardization Matters in Machine Learning

Many Machine Learning algorithms depend on:

* Euclidean distance
* gradient descent optimization
* weight updates

Without scaling:

```text
Age = 25
Salary = 500000
```

Salary dominates calculations because of larger magnitude.

After standardization:

* features become comparable
* optimization becomes more stable
* gradient descent converges faster

---

# ⚠️ Important Understanding

Standardization does NOT:

* remove outliers
* change relationships between features
* normalize data to range [0,1]

It only:

* centers the data
* rescales the spread

---

# 🧠 Final Insight

> “Standardization helps Machine Learning algorithms treat features more fairly by centering the data around zero and normalizing the scale of variation.”

# 🔹 StandardScaler

Used:

```python id="r1t5x9"
StandardScaler
```

from:

```python id="mg4r94"
sklearn.preprocessing
```

---

# 🔹 Correct Workflow

```python id="c15wva"
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

# ⚠️ Important Concept: Data Leakage

---

# 🔹 What is Data Leakage?

When information from the test set unintentionally influences the training process.

---

# 🔹 Common Mistake

Incorrect:

```python id="qdkjlwm"
X_test = scaler.fit_transform(X_test)
```

This fits scaler separately on test data.

---

# 🔹 Why It Is Wrong

The model indirectly learns information from the test set.

This causes:

* unrealistic evaluation
* inflated performance metrics

---

# 🔹 Correct Approach

Fit scaler only on training data:

```python id="m9p6ny"
scaler.fit(X_train)
```

Then transform both datasets:

```python id="lwn5y5"
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

---

# 📍 7. Complete ML Preprocessing Pipeline

---

# 🔹 Workflow

```text id="k9r0xp"
Import Libraries
→ Load Dataset
→ Handle Missing Data
→ Encode Categorical Features
→ Split Train/Test Data
→ Apply Feature Scaling
→ Train Model
```

---

# 🤖 Why Preprocessing is Critical in ML

Good preprocessing:

* improves accuracy
* stabilizes optimization
* reduces bias
* improves generalization

Poor preprocessing can completely degrade model performance.

---

# 🧠 Key Insights

* ML models require clean numerical data
* Missing values must be handled carefully
* One Hot Encoding prevents false category ordering
* Feature scaling is essential for many algorithms
* Train-test separation prevents overfitting
* Data leakage can invalidate evaluation

---

# 🧠 Final Insight

> “Machine Learning models learn patterns from data — preprocessing ensures those patterns are meaningful, consistent, and reliable.”
