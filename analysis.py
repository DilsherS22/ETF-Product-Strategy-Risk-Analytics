"""Rebuild the ETF risk metrics and four charts from the bundled source data."""

from pathlib import Path
import math

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter, StrMethodFormatter
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
PERIODS_PER_YEAR = 12


def calculate_metrics(prices: pd.DataFrame, monthly_rf: pd.Series):
    returns = prices.pct_change(fill_method=None).dropna()
    monthly_rf = monthly_rf.reindex(returns.index)
    if monthly_rf.isna().any():
        raise ValueError("Risk-free series does not cover every return month.")

    rows = []
    for ticker in prices:
        ret = returns[ticker]
        excess = ret - monthly_rf
        volatility = ret.std(ddof=1) * math.sqrt(PERIODS_PER_YEAR)
        downside = excess.clip(upper=0.0)
        downside_dev = math.sqrt((downside.pow(2)).mean()) * math.sqrt(PERIODS_PER_YEAR)
        drawdown = (prices[ticker] / prices[ticker].cummax() - 1).min()
        years = len(ret) / PERIODS_PER_YEAR

        rows.append({
            "Ticker": ticker,
            "Total Return": prices[ticker].iloc[-1] / prices[ticker].iloc[0] - 1,
            "CAGR": (prices[ticker].iloc[-1] / prices[ticker].iloc[0]) ** (1 / years) - 1,
            "Annualized Volatility": volatility,
            "Sharpe Ratio": excess.mean() / ret.std(ddof=1) * math.sqrt(PERIODS_PER_YEAR),
            "Sortino Ratio": excess.mean() * PERIODS_PER_YEAR / downside_dev,
            "Max Drawdown": drawdown,
            "Historical VaR 95% (Monthly)": -ret.quantile(0.05),
            "Beta vs SPY": ret.cov(returns["SPY"]) / returns["SPY"].var(ddof=1),
        })

    metrics = pd.DataFrame(rows).set_index("Ticker")
    return returns, metrics, returns.corr()


def clean_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.18, linewidth=0.7)


def save_charts(prices, metrics, correlation, peers):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(metrics["Annualized Volatility"], metrics["CAGR"], s=70)
    for ticker, row in metrics.iterrows():
        ax.annotate(ticker, (row["Annualized Volatility"], row["CAGR"]), xytext=(5, 5), textcoords="offset points")
    ax.set(title="Three-Year Risk–Return Map", xlabel="Annualized volatility", ylabel="CAGR")
    ax.xaxis.set_major_formatter(PercentFormatter(1.0)); ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    clean_axes(ax)
    fig.text(0.01, 0.01, "Aug 2023–Aug 2026; month-end adjusted prices.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUTPUTS / "risk_return_map.png", dpi=220, bbox_inches="tight"); plt.close(fig)

    selected = ["SPY", "QQQ", "EEM", "AGG", "GLD", "VNQ"]
    fig, ax = plt.subplots(figsize=(10, 6))
    prices[selected].div(prices[selected].iloc[0]).mul(100).plot(ax=ax, linewidth=1.8)
    ax.set(title="Growth of $100 Across Representative ETFs", xlabel="", ylabel="Value of $100")
    ax.yaxis.set_major_formatter(StrMethodFormatter("${x:,.0f}")); ax.legend(ncol=3, frameon=False); clean_axes(ax)
    fig.text(0.01, 0.01, "Aug 2023–Aug 2026; month-end adjusted prices.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUTPUTS / "growth_of_100.png", dpi=220, bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.8, 7.2))
    image = ax.imshow(correlation.values, vmin=-1, vmax=1, aspect="equal")
    ax.set_xticks(range(len(correlation)), labels=correlation.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(correlation)), labels=correlation.index)
    for i in range(len(correlation)):
        for j in range(len(correlation)):
            ax.text(j, i, f"{correlation.iloc[i, j]:.2f}", ha="center", va="center", fontsize=7)
    ax.set_title("Monthly Return Correlation Matrix"); fig.colorbar(image, ax=ax, fraction=0.045, pad=0.04, label="Correlation")
    fig.text(0.01, 0.01, "Aug 2023–Aug 2026; based on monthly returns.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUTPUTS / "correlation_heatmap.png", dpi=220, bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(peers["Expense_Ratio"], peers["AUM_bn"], s=85)
    label_offsets = {"SPEM": (6, 10), "SCHE": (6, -14)}
    for _, row in peers.iterrows():
        offset = label_offsets.get(row["Ticker"], (6, 6))
        ax.annotate(row["Ticker"], (row["Expense_Ratio"], row["AUM_bn"]), xytext=offset, textcoords="offset points")
    ax.set(title="Emerging-Markets ETF Competitive Positioning", xlabel="Expense ratio", ylabel="AUM ($bn)")
    ax.xaxis.set_major_formatter(PercentFormatter(1.0)); clean_axes(ax)
    fig.text(0.01, 0.01, "Issuer-reported AUM and expense ratios; field dates vary by fund.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUTPUTS / "em_competitor_positioning.png", dpi=220, bbox_inches="tight"); plt.close(fig)


def main():
    OUTPUTS.mkdir(exist_ok=True)
    prices = pd.read_csv(DATA / "monthly_adjusted_prices.csv", parse_dates=["Date"], index_col="Date")
    peers = pd.read_csv(DATA / "em_etf_peer_set.csv")
    rf = pd.read_csv(DATA / "risk_free_monthly.csv", parse_dates=["Date"], index_col="Date")["Monthly_Risk_Free_Return"]

    returns, metrics, correlation = calculate_metrics(prices, rf)
    returns.to_csv(OUTPUTS / "monthly_returns.csv", index_label="Date")
    metrics.to_csv(OUTPUTS / "risk_metrics.csv")
    correlation.to_csv(OUTPUTS / "correlation_matrix.csv")
    save_charts(prices, metrics, correlation, peers)
    print(metrics.round(4).to_string())


if __name__ == "__main__":
    main()
