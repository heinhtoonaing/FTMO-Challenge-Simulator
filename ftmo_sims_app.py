import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="FTMO Challenge Simulator", layout="wide")
st.title("💼 FTMO Challenge Simulator")

# Sidebar inputs
st.sidebar.header("🔧 Simulation Settings")
account_size = st.sidebar.number_input("Account Size ($)", value=100000, step=1000)
profit_target_pct = st.sidebar.slider("Profit Target (%)", 5, 20, 10)
max_daily_loss_pct = st.sidebar.slider("Max Daily Loss (%)", 1, 10, 5)
max_total_loss_pct = st.sidebar.slider("Max Total Loss (%)", 2, 15, 10)
trading_days = st.sidebar.slider("Trading Days", 10, 60, 30)
mean_daily_return = st.sidebar.slider("Mean Daily Return ($)", -500, 1000, 300)
daily_stddev = st.sidebar.slider("Daily Return Std Dev ($)", 100, 3000, 1500)
simulate_button = st.sidebar.button("▶️ Run Simulation")

if simulate_button:
    # Derived values
    profit_target = account_size * profit_target_pct / 100
    max_daily_loss = account_size * max_daily_loss_pct / 100
    max_total_loss = account_size * max_total_loss_pct / 100

    # Generate returns
    np.random.seed(42)
    daily_returns = np.random.normal(loc=mean_daily_return, scale=daily_stddev, size=trading_days)

    balance = account_size
    equity_curve = [balance]
    trade_log = []
    result = ""

    for day, pnl in enumerate(daily_returns, 1):
        balance += pnl
        equity_curve.append(balance)

        trade_log.append({
            "Day": day,
            "PnL": round(pnl, 2),
            "Balance": round(balance, 2),
            "Cumulative Gain": round(balance - account_size, 2)
        })

        drawdown = account_size - balance

        if pnl < -max_daily_loss:
            result = f"❌ Day {day}: Daily loss limit exceeded!"
            break
        if drawdown > max_total_loss:
            result = f"❌ Day {day}: Total loss limit exceeded!"
            break
        if balance >= account_size + profit_target:
            result = f"✅ Day {day}: Profit target achieved! 🎉 You passed the FTMO Challenge!"
            break
    else:
        result = "❌ Challenge failed. You did not reach the profit target."

    # Show results
    st.subheader("📊 Simulation Result")
    st.write(result)

    # Equity Curve Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(equity_curve, marker='o')
    ax.axhline(account_size, color='gray', linestyle='--', label='Starting Balance')
    ax.axhline(account_size + profit_target, color='green', linestyle='--', label='Profit Target')
    ax.axhline(account_size - max_total_loss, color='red', linestyle='--', label='Max Drawdown')
    ax.set_title('Equity Curve')
    ax.set_xlabel('Trading Day')
    ax.set_ylabel('Balance ($)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Trade Log Table
    st.subheader("📄 Trade Log")
    df_log = pd.DataFrame(trade_log)
    st.dataframe(df_log, use_container_width=True)

else:
    st.info("Set your parameters on the left and click **Run Simulation** to begin.")
# This code provides a Streamlit app that simulates the FTMO Challenge, allowing users to set parameters and visualize results.
# The app includes a sidebar for input settings, generates random daily returns, tracks the equity curve, and displays results in a user-friendly format.   