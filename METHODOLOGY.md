# Methodology

## Objective

This project evaluates two linked questions:

1. How do major asset-class ETFs compare on return and risk over a common three-year window?
2. In a fee-compressed emerging-markets ETF category, what type of product-development hypothesis is more differentiated than another broad-beta clone?

The analysis is a portfolio case study in investment-management strategy, ETF product research, and quantitative risk analytics. It is not investment advice.

## Universe

### Multi-asset risk universe

- SPY — U.S. large-cap equity
- QQQ — U.S. growth / technology-heavy equity
- IWM — U.S. small-cap equity
- EFA — developed markets ex-U.S.
- EEM — emerging-markets equity
- AGG — U.S. core bonds
- LQD — investment-grade corporate credit
- HYG — high-yield credit
- GLD — gold
- VNQ — U.S. listed real estate

### Emerging-markets competitor set

EEM, IEMG, VWO, SPEM, and SCHE are used to study fees, scale, benchmark design, portfolio breadth, and issuer positioning.

## Embedded historical window

The bundled workbook uses month-end adjusted prices from August 2023 through August 2026, producing 36 monthly return observations per ETF. The bundled monthly data make the repository reproducible without requiring an external API call.


## Metrics

**Total return:** ending adjusted price divided by beginning adjusted price, minus one.

**CAGR:** annualized compound growth rate over the three-year sample.

**Annualized volatility:** sample standard deviation of monthly returns multiplied by the square root of 12.

**Sharpe ratio:** mean monthly excess return over the month-end 3-month U.S. Treasury yield, divided by the sample standard deviation of monthly ETF returns and annualized by the square root of 12. The Treasury series is FRED DGS3MO.

**Sortino ratio:** annualized mean monthly excess return divided by annualized downside deviation. Downside observations are negative ETF excess returns relative to the aligned monthly DGS3MO rate; positive excess-return months contribute zero downside.

**Maximum drawdown:** largest peak-to-trough decline measured from the observed adjusted-price series. Monthly observations can understate intramonth losses.

**Historical VaR:** the 5th percentile of monthly returns, presented as a positive loss magnitude. With 36 observations, this is a project diagnostic rather than an institutional production VaR model.

**Beta versus SPY:** covariance of the ETF's monthly returns with SPY divided by the variance of SPY returns.

**Correlation:** Pearson correlation of monthly ETF returns over the common sample.

## Product-strategy framework

The product-development case combines quantitative evidence with competitor research and evaluates differentiation across investment outcome, portfolio construction, risk controls, fees, active/systematic design, liquidity, capacity, distribution positioning, and investor use case.

The hypothetical quality-and-risk EM concept is a research hypothesis only. A real launch decision would require deeper work on factor efficacy, trading costs, tax considerations, capacity, index/licensing costs, distribution demand, seed capital, break-even economics, compliance, and implementation risk.

## Limitations

- The bundled analysis uses a relatively short three-year sample.
- Results are period-dependent and are not expected-return forecasts.
- Digrin adjusted prices are used as a practical total-return proxy. Adjusted histories can be revised by data providers after distributions, so the repository pins the exact snapshot used for the analysis.
- Competitor product statistics change and should be refreshed before quoting exact current figures publicly.
- The framework is intentionally simpler than an institutional portfolio-risk system.
