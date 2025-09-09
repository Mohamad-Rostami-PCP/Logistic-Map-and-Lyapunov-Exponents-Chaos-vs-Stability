
# 🔀 Logistic Map and Lyapunov Exponents: Chaos vs Stability

This project explores the **logistic map** and quantifies chaos by calculating **Lyapunov exponents**, showing the difference between stable and chaotic regimes.

---

## 📂 Code Structure
- **main.py** → logistic map iteration, trajectory comparison for close initial conditions, and Lyapunov exponent calculation.

---

## 🔑 Important Variables
- `r` → logistic map parameter controlling dynamics  
- `x0`, `x0_prime` → two nearby initial conditions  
- `N` → number of iterations  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Change `r` to explore different regimes:
   - $r < 3$: stable, convergent dynamics  
   - $r > 3.57$: chaotic regime  
3. Adjust `x0` and `x0_prime` to test sensitivity to initial conditions.  
4. Run:
   ```bash
   python main.py

---

## 🧠 Physical/Statistical Intuition

* Logistic map:

  $$
  x_{n+1} = r x_n (1 - x_n)
  $$

* Lyapunov exponent:


  $$\lambda = \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n \ln \left|\frac{dx_{i+1}}{dx_i}\right|$$

* \$\lambda > 0\$ → chaos (exponential divergence).

* \$\lambda < 0\$ → stability (convergence to fixed point or cycle).

---

## 🧮 Numerical Models

* **Iterative mapping** (logistic equation)
* **Lyapunov exponent estimation**
* **Chaos vs stability analysis**

