# FTMO Challenge Simulator



💼 **FTMO Challenge Simulator** is an interactive Streamlit web app designed to simulate the popular FTMO trading challenge.  
It allows traders to test their strategy against customizable parameters such as account size, profit target, max daily loss, and trading days, providing a realistic equity curve and trade log.

---

## Features

- Customizable simulation parameters via sidebar input:
  - Account size (starting balance)
  - Profit target percentage
  - Maximum daily loss percentage
  - Maximum total loss percentage
  - Number of trading days
  - Mean daily return (profit/loss)
  - Daily return standard deviation (volatility)

- Realistic daily return simulation using a normal distribution  
- Equity curve visualization with matplotlib  
- Detailed trade log with day-wise PnL and balance  
- Pass/fail outcome based on FTMO challenge rules  

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/heinhtoonaing/ftmo-challenge-simulator.git
   cd ftmo-challenge-simulator

Try with this link: https://ftmo-challenge-simulator.streamlit.app/
