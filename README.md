# **Heston Model for European Option Pricing**

This Python program calculates the price of European options using the **Heston Model**, a widely used stochastic volatility model in quantitative finance. The program allows users to input key parameters, computes the option price through numerical integration, and offers a modular design for further extensions.



## **Features**

- **Option Pricing**: Calculates European option prices based on the Heston stochastic volatility model.
- **User-Friendly Interface**: Prompts users to input the required model parameters interactively.
- **Numerical Integration**: Utilizes the characteristic function of the Heston model for accurate pricing through integration.
- **Extensibility**: The implementation allows for easy customization and extension of the model.



## **How It Works**

1. **Model Parameters**:
   - **\( S_0 \)**: Initial price of the underlying asset.
   - **\( K \)**: Strike price.
   - **\( T \)**: Time to maturity (in years).
   - **\( r \)**: Risk-free interest rate.
   - **\( v_0 \)**: Initial variance (square of the initial volatility).
   - **\( \theta \)**: Long-term average variance.
   - **\( \kappa \)**: Speed of mean reversion of variance to its long-term average.
   - **\( \sigma \)**: Volatility of volatility (vol of var).
   - **\( \rho \)**: Correlation between asset price and volatility.

2. **Characteristic Function**:
   - Computes the characteristic function of the log of the asset price under the risk-neutral measure.

3. **Numerical Integration**:
   - Integrates the real part of the characteristic function to calculate the option price.

4. **User Interaction**:
   - Prompts users to enter model parameters interactively.



## **Requirements**

- Python 3.x
- Libraries:
  - `numpy`
  - `scipy`
  - `matplotlib` (optional, for visualization if extended)

Install required libraries using pip:
```bash
pip install numpy scipy matplotlib
```

---

## **Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/heston-model-option-pricing.git
   cd heston-model-option-pricing
   ```

2. **Run the Program**:
   ```bash
   python heston_model.py
   ```

3. **Follow the Prompts**:
   - Enter the required inputs when prompted (initial price, strike price, maturity, etc.).
   - View the calculated European option price.

---

## **Example**

### Input:
```plaintext
Please enter the parameters for the Heston model:
Initial price of the underlying asset (e.g., 100): 100
Strike price (e.g., 100): 100
Time to maturity (in years) (e.g., 1): 1
Risk-free rate (e.g., 0.05): 0.05
Initial volatility (variance) (e.g., 0.04): 0.04
Long-term variance (e.g., 0.04): 0.04
Rate of mean reversion (e.g., 2.0): 2.0
Volatility of volatility (e.g., 0.5): 0.5
Correlation between asset price and volatility (e.g., -0.7): -0.7
```

### Output:
```plaintext
The European option price using the Heston model is: 12.3456
```

---

## **File Structure**

```
heston-model-option-pricing/
│
├── heston_model.py      # Main Python script for option pricing
├── README.md            # Documentation file
```

---

## **Key Functions**

- **`HestonModel.characteristic_function(u)`**:
  - Computes the characteristic function of the Heston model.
- **`HestonModel.heston_price(num_points=1000, max_iter=10)`**:
  - Calculates the European option price using numerical integration.
- **`get_input(prompt, type_cast=float)`**:
  - Helper function for interactive user input with type validation.

---

## **Limitations**

- Assumes constant risk-free rate and no dividends.
- Pricing is specific to European options and may not apply to American or exotic options without modifications.
