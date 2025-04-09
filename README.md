
---

**VOLATILITY MISPRICING STRATEGY**  
*(Inspired by Question 2.13 from* Heard on the Street*)  

---

**1. Overview**

This project simulates a trading opportunity based on volatility mispricing in financial markets. The idea comes from a conceptual error described in Question 2.13 of *Heard on the Street* by Timothy Crack.

In real markets, volatility is often estimated from daily returns and then scaled up to price options with longer expiries (like 1 month or 3 months). However, this assumes that returns are independent and identically distributed (i.i.d.). If they aren’t — and the actual realized monthly volatility is significantly higher — then the options will be **underpriced** when using scaled-up daily vol.

This simulation captures that scenario, where we "buy" an underpriced call option and observe the profit when real volatility plays out.

---

**2. Core Idea**

- You have daily, weekly, and monthly return data.
- Ideally, volatilities should scale with time:
  
  - monthly variance ≈ 20 × daily variance  
  - monthly volatility ≈ √20 × daily volatility  

- But if your observed monthly volatility is much higher than expected from daily estimates, then daily returns are **underestimating market risk**.

- If traders price options using this lower daily-based volatility, they are **mispricing options downward**.
- By **buying** those underpriced options, you can profit when true volatility materializes.

---

**3. What the Code Does**

- Simulates a 1-month path of stock prices using the **realized (high) volatility** — e.g., 30%.
- Prices a European call option using **lower volatility** — e.g., 20%, as if estimated from daily returns.
- Calculates:
  - The price you would have paid (underestimated volatility).
  - The payoff at expiry using the simulated final stock price.
  - Your profit: **Payoff – Premium Paid**
- Also plots the stock path and strike price for visualization.

---

**4. Requirements**

You need Python 3 and the following libraries:

- numpy  
- scipy  
- matplotlib  

Install them using pip if needed:

```
pip install numpy scipy matplotlib
```

---

**5. How to Run**

1. Save the Python script as `vol_arbitrage_simulation.py`.
2. Open your terminal or command line in the same folder.
3. Run:

```
python vol_arbitrage_simulation.py
```

4. You’ll see a plot of the stock path and output showing:
   - Option price using incorrect volatility
   - Payoff at expiry
   - Profit earned from exploiting the mispricing

---

**6. Key Insight**

If you find that actual realized volatility (e.g., from monthly returns) is **consistently higher** than scaled daily volatility, you should avoid using Black-Scholes pricing based on daily vol. Instead:

- Use the longer-term vol directly
- Recognize that others using daily vol may be underpricing options
- Exploit this by buying the underpriced options and holding until expiry (or hedging dynamically)

This is a form of **volatility arbitrage**, and this simple project demonstrates how even a clean theoretical model like Black-Scholes can mislead if the inputs are wrong.

---

L
