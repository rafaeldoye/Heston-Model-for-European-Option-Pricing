import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Heston Model for options
class HestonModel:
    def __init__(self, S0, K, T, r, v0, theta, kappa, sigma, rho):
        """
        Initialize the Heston model parameters.
        S0: Initial price of the underlying asset
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        v0: Initial volatility (variance)
        theta: Long-run average variance
        kappa: Rate of mean reversion
        sigma: Volatility of volatility
        rho: Correlation between asset and volatility
        """
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.v0 = v0
        self.theta = theta
        self.kappa = kappa
        self.sigma = sigma
        self.rho = rho
    
    def characteristic_function(self, u):
        """
        Heston model characteristic function for a given value of 'u'.
        """
        i = 1j  # imaginary unit
        lambda_ = np.sqrt(self.sigma ** 2 * (u ** 2 + i * u))
        d1 = i * u * np.log(self.S0 / self.K) + self.r * i * u * self.T
        d2 = -0.5 * u ** 2 * self.v0 * self.T
        return np.exp(d1 + d2) * np.exp(self.kappa * self.T * (self.theta - self.v0)) / (lambda_ ** 2 + (u - self.rho * self.sigma) ** 2)

    def heston_price(self, num_points=1000, max_iter=10):
        """
        Calculate the European option price using numerical integration.
        """
        def integrand(u):
            i = 1j  # Imaginary unit (defined here to avoid the error)
            characteristic_func = self.characteristic_function(u)
            real_part = np.real(np.exp(-i * u * np.log(self.S0 / self.K)) * characteristic_func)
            return real_part

        # Integration range (u from 0 to large values)
        u_values = np.linspace(0, num_points, num_points)
        integral_result = integrate.quad(integrand, 0, max_iter)

        return integral_result[0]

# Function to get user input
def get_input(prompt, type_cast=float):
    while True:
        try:
            return type_cast(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Get user inputs for the Heston model parameters
print("Please enter the parameters for the Heston model:")

S0 = get_input("Initial price of the underlying asset (e.g., 100): ")
K = get_input("Strike price (e.g., 100): ")
T = get_input("Time to maturity (in years) (e.g., 1): ")
r = get_input("Risk-free rate (e.g., 0.05): ")
v0 = get_input("Initial volatility (variance) (e.g., 0.04): ")
theta = get_input("Long-term variance (e.g., 0.04): ")
kappa = get_input("Rate of mean reversion (e.g., 2.0): ")
sigma = get_input("Volatility of volatility (e.g., 0.5): ")
rho = get_input("Correlation between asset price and volatility (e.g., -0.7): ")

# Create an instance of HestonModel
heston = HestonModel(S0, K, T, r, v0, theta, kappa, sigma, rho)

# Calculate the option price
option_price = heston.heston_price()

print(f"The European option price using the Heston model is: {option_price}")
