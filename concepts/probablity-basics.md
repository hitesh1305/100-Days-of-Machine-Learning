# 📊 Probability Foundations for Machine Learning

---

## 🧠 Why Probability Matters in Machine Learning

Machine Learning models operate in environments where **uncertainty is inherent**.
Probability provides the mathematical framework to:

* quantify uncertainty
* model randomness
* make predictions
* evaluate outcomes

> “Machine Learning is fundamentally about making probabilistic decisions from data.”

---

# 📍 1. Basic Probability Concepts

---

## 🔹 Definition

Probability measures the likelihood of an event occurring.

```
P(E) = (Number of favorable outcomes) / (Total number of outcomes)
```

---

## 🔹 Range of Probability

```
0 ≤ P(E) ≤ 1
```

* **0** → Impossible event
* **1** → Certain event

---

## 🔹 Types of Events

### ➤ Simple Event

Single outcome
Example: rolling a 3 on a die

### ➤ Compound Event

Multiple outcomes
Example: rolling an even number

---

## 🔹 Sample Space

Set of all possible outcomes

Example:

```
S = {1, 2, 3, 4, 5, 6}
```

---

## 🔹 Event

Subset of sample space

Example:

```
A = {2, 4, 6}
```

---

# 📍 2. Fundamental Probability Rules

---

## 🔹 Complement Rule

```
P(A') = 1 − P(A)
```

---

## 🔹 Addition Rule

For two events A and B:

```
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```

---

## 🔹 Multiplication Rule

```
P(A ∩ B) = P(A) × P(B | A)
```

If independent:

```
P(A ∩ B) = P(A) × P(B)
```

---

# 📍 3. Conditional Probability

---

## 🔹 Definition

Probability of event A given event B has occurred:

```
P(A | B) = P(A ∩ B) / P(B)
```

---

## 🧠 Intuition

We **update probability** based on new information.

---

## 🔹 Example

If we know a person is a student (B), probability of them studying ML (A) changes.

---

# 📍 4. Independence of Events

---

## 🔹 Definition

Two events are independent if:

```
P(A | B) = P(A)
```

---

## 🔹 Equivalent Condition

```
P(A ∩ B) = P(A) × P(B)
```

---

## 🧠 Intuition

Occurrence of one event does not affect the other.

---

# 📍 5. Bayes’ Theorem

---

## 🔹 Formula

```
P(A | B) = (P(B | A) × P(A)) / P(B)
```

---

## 🧠 Intuition

* Converts **likelihood → posterior probability**
* Updates belief after observing data

---

## 🔹 Components

* Prior → P(A)
* Likelihood → P(B | A)
* Evidence → P(B)
* Posterior → P(A | B)

---

## 🤖 Use in Machine Learning

* Naive Bayes classifier
* Spam filtering
* Medical diagnosis

---

# 📍 6. Random Variables

---

## 🔹 Definition

A variable whose value depends on the outcome of a random experiment.

---

## 🔹 Types

### ➤ Discrete Random Variable

* Takes countable values
* Example: number of heads

---

### ➤ Continuous Random Variable

* Takes infinite values
* Example: height, temperature

---

# 📍 7. Probability Distributions

---

## 🔹 Definition

A function that describes how probabilities are distributed over values.

---

## 🔹 Types

### ➤ Discrete Distribution

* Uses Probability Mass Function (PMF)

---

### ➤ Continuous Distribution

* Uses Probability Density Function (PDF)

---

# 📍 8. Probability Mass Function (PMF)

---

## 🔹 Definition

```
P(X = x)
```

Gives probability of discrete variable taking a value.

---

## 🔹 Properties

* All probabilities ≥ 0
* Sum of probabilities = 1

---

# 📍 9. Probability Density Function (PDF)

---

## 🔹 Definition

Describes probability density for continuous variables.

---

## 🔹 Key Property

```
Area under curve = 1
```

---

## 🧠 Important Note

For continuous variables:

```
P(X = x) = 0
```

We use intervals instead.

---

# 📍 10. Cumulative Distribution Function (CDF)

---

## 🔹 Definition

```
F(x) = P(X ≤ x)
```

---

## 🧠 Intuition

Probability up to a value.

---

# 📍 11. Expectation (Mean of Random Variable)

---

## 🔹 Formula (Discrete)

```
E(X) = Σ x · P(x)
```

---

## 🔹 Formula (Continuous)

```
E(X) = ∫ x f(x) dx
```

---

## 🧠 Intuition

Average expected value.

---

# 📍 12. Variance of Random Variable

---

## 🔹 Formula

```
Var(X) = E[(X − μ)²]
```

---

## 🔹 Alternate Form

```
Var(X) = E(X²) − [E(X)]²
```

---

## 🧠 Intuition

Measures spread around mean.

---

# 📍 13. Standard Deviation

---

## 🔹 Formula

```
SD = √Var(X)
```

---

## 🧠 Intuition

Spread in original units.

---

# 📍 14. Common Distributions

---

## 🔹 Normal Distribution

* Bell-shaped
* Symmetrical

```
Mean = Median = Mode
```

---

### Properties

* 68% within 1 SD
* 95% within 2 SD
* 99.7% within 3 SD

---

## 🔹 Uniform Distribution

* All values equally likely

---

## 🔹 Binomial Distribution

* Fixed trials
* Success/failure

---

## 🔹 Poisson Distribution

* Counts events over time/space

---

# 📍 15. Law of Large Numbers

---

## 🔹 Statement

As sample size increases:

```
Sample mean → Population mean
```

---

## 🧠 Importance

* Justifies using sample data

---

# 📍 16. Central Limit Theorem (CLT)

---

## 🔹 Statement

For large samples:

```
Sampling distribution → Normal distribution
```

---

## 🧠 Importance

* Basis of many ML assumptions
* Enables statistical inference

---

# 📍 17. Role of Probability in Machine Learning

---

## 🔹 1. Classification

* Naive Bayes

---

## 🔹 2. Predictions

* Probabilistic outputs

---

## 🔹 3. Uncertainty Handling

* Confidence levels

---

## 🔹 4. Model Assumptions

* Data distribution assumptions

---

## 🔹 5. Optimization

* Likelihood functions

---

# 🧠 Final Insight

> “Probability allows machine learning models to reason, predict, and make decisions under uncertainty.”
