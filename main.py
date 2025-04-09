import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes Call Option Pricing
def black_scholes_call(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

# Simulate stock path
def simulate_stock(S0, mu, sigma_real, T, steps):
    dt = T / steps
    returns = np.random.normal((mu - 0.5 * sigma_real**2) * dt, sigma_real * np.sqrt(dt), steps)
    price_path = S0 * np.exp(np.cumsum(returns))
    return price_path

# Parameters
S0 = 100            # Initial stock price
K = 100             # Strike price
r = 0.01            # Risk-free rate
T = 1/12            # 1 month
steps = 21          # 21 trading days in a month
mu = 0.05           # Drift

# Vol estimates
sigma_real = 0.30   # Realized (monthly) vol
sigma_misused = 0.20  # Daily vol scaled up incorrectly

# Simulate path
np.random.seed(42)
path = simulate_stock(S0, mu, sigma_real, T, steps)
S_T = path[-1]

# Calculate payoff
option_price_misused = black_scholes_call(S0, K, r, sigma_misused, T)
realized_payoff = max(S_T - K, 0)
profit = realized_payoff - option_price_misused

# Plot
plt.plot(path, label="Stock Path")
plt.axhline(K, color='gray', linestyle='--', label='Strike Price')
plt.title("Simulated Stock Path Over 1 Month")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# Output
print(f"Option Price using daily vol (underpriced): {option_price_misused:.2f}")
print(f"Realized Payoff at Expiry: {realized_payoff:.2f}")
print(f"Profit from underpricing: {profit:.2f}")
