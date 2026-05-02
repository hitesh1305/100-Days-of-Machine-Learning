# Day 02 — Problem Solving & Algorithm Optimization

---

## 📌 Objective

Strengthen problem-solving skills by moving from basic solutions to optimized approaches.

---

## 🧠 What I Worked On

Focused on understanding **different levels of solution efficiency** instead of just solving problems.

---

### 🔹 1. Prime Number

Implemented three approaches:

* Naive approach (check till n)
* Efficient approach (check till √n)
* Optimal approach (6k ± 1 optimization)

---

### 🔹 2. GCD (Greatest Common Divisor)

* Euclidean algorithm (optimized approach using remainder)

---

### 🔹 3. Fibonacci Series

* Recursive implementation
* Observed inefficiency due to repeated calculations

---

## 🔍 Key Insights

* The same problem can have **multiple levels of efficiency**
* Optimization often comes from:

  * reducing search space
  * identifying mathematical patterns

---

### 💡 Prime Number Insight

* Numbers greater than 3 can be written in the form:

  * 6k, 6k ± 1, 6k ± 2, 6k ± 3

* Only **6k ± 1** need to be checked

* This significantly reduces unnecessary checks

---

### 💡 GCD Insight

* Instead of checking all factors:

  > gcd(a, b) = gcd(b, a % b)

* This reduces the problem size quickly and efficiently

---

### 💡 Fibonacci Insight

* Recursive approach leads to repeated computation
* Highlights need for:

  * iterative solutions
  * or dynamic programming

---

## ❗ Challenges Faced

* Initially struggled with:

  * understanding the **6k ± 1 optimization** for prime numbers
* It was unclear why other numbers could be ignored

---

## 🔁 How I Resolved It

* Referred to a detailed explanation and video

* Understood that:

  * multiples of 2 and 3 eliminate most candidates
  * leaving only 6k ± 1 as possible primes

* This clarified both:

  * the logic
  * and the efficiency improvement

---

## 📘 Code Implementation

* [Day 02 Problem Solving Code](../projects/day-02-problem-solving)

Includes:

* Prime number (naive → optimal)
* GCD (Euclidean)
* Fibonacci (recursive)

---

## 📈 What I Improved Today

* Ability to compare multiple approaches
* Understanding of algorithm efficiency
* Confidence in breaking down complex logic

---

## 🎯 Next Step

* Focus on writing cleaner and reusable code
* Move towards structured programming (functions, modular logic)
