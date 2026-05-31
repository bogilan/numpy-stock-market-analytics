import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# STOCK MARKET ANALYTICS WITH NUMPY
# Simulate stock prices using a random walk model and
# perform financial analysis using NumPy.
# ==========================================================

# Ensure reproducible results
np.random.seed(42)

# ==========================================================
# CONFIGURATION
# ==========================================================

# Number of trading days to simulate
days = 365

# Company labels used in reporting and visualizations
stock_names = [
    "Apple",
    "Tesla",
    "Nvidia",
    "Amazon",
    "Microsoft"
]

# Starting stock prices for each company
# Shape: (5,)
starting_prices = np.array([
    180,
    250,
    450,
    140,
    330
])

# ==========================================================
# GENERATE DAILY RETURNS
# ==========================================================

# Simulate daily percentage returns using a normal distribution
# loc   = average daily return (0.1%)
# scale = volatility (2%)
#
# Shape: (365, 5)
# Rows    -> trading days
# Columns -> stocks
daily_returns = np.random.normal(
    loc=0.001,
    scale=0.02,
    size=(days, len(stock_names))
)

# ==========================================================
# CREATE STOCK PRICE MATRIX
# ==========================================================

# Preallocate a matrix for storing simulated prices
# Shape: (365, 5)
stock_prices = np.zeros(
    (days, len(stock_names))
)

# Initialize first day prices
stock_prices[0] = starting_prices

# ==========================================================
# PRICE SIMULATION
# ==========================================================

# Random walk model:
#
# Price_today = Price_yesterday × (1 + Daily_Return)
#
# NumPy performs element-wise calculations across
# the entire row, eliminating the need for nested loops.
for day in range(1, days):

    stock_prices[day] = (
        stock_prices[day - 1]
        * (1 + daily_returns[day])
    )

# Round values for cleaner presentation
stock_prices = np.round(stock_prices, 2)

# ==========================================================
# RESULTS PREVIEW
# ==========================================================

print("\n========== STOCK SUMMARY ==========\n")

for i, stock in enumerate(stock_names):

    print(
        f"{stock}: "
        f"Start ${stock_prices[0, i]} -> "
        f"End ${stock_prices[-1, i]}"
    )

# ==========================================================
# VISUALIZATION
# ==========================================================

plt.figure(figsize=(14, 7))

# Plot each stock's price history
for i, stock in enumerate(stock_names):

    plt.plot(
        stock_prices[:, i],
        label=stock
    )

plt.title("Simulated Stock Prices")
plt.xlabel("Trading Days")
plt.ylabel("Price ($)")
plt.legend()

plt.show()
