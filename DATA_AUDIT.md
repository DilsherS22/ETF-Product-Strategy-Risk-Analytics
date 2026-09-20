# Data Verification Log

This file documents the provenance of every external numeric input used in the project. The analytical outputs are calculated from the bundled source files; they are not manually entered performance figures.

## Verification date

September 19, 2026.

## Historical ETF prices

`data/monthly_adjusted_prices.csv` contains month-end **adjusted prices** from August 2023 through August 2026 for SPY, QQQ, IWM, EFA, EEM, AGG, LQD, HYG, GLD, and VNQ.

Each series was checked against the corresponding Digrin monthly price-history table on September 19, 2026. The workbook and repository intentionally identify Digrin as the provider rather than implying that these are exchange-official prices. Adjusted-price histories can be revised by providers after distributions; the bundled CSV is the snapshot used for this analysis.

## Emerging-markets peer data

The peer-set file uses issuer-reported values and preserves field-level dates because AUM, holdings, and expense ratios are not always updated on the same day.

| Ticker | AUM used | AUM date | Expense ratio | Expense date | Holdings | Holdings date | Primary source |
|---|---:|---|---:|---|---:|---|---|
| EEM | $31.2748bn | 2026-09-18 | 0.72% | Current prospectus | 1,185 | 2026-09-17 | iShares |
| IEMG | $161.7844bn | 2026-09-18 | 0.09% | Current prospectus | 2,860 | 2026-09-17 | iShares |
| VWO | $127.3bn | 2026-08-31 | 0.06% | 2026-02-27 | 6,338 | 2026-07-31 | Vanguard |
| SPEM | $17.49008bn | 2026-09-16 | 0.07% | Fund information as of 2026-09-17 | 2,980 | 2026-09-16 | State Street |
| SCHE | $12.892369bn | 2026-09-18 | 0.06% | Effective 2026-06-11 | 2,219 | 2026-09-17 | Schwab |

The full URLs are in `data/em_etf_peer_set.csv` and `data/source_manifest.csv`.

## Risk-free series

`data/risk_free_monthly.csv` uses the Federal Reserve Board H.15 **3-month Treasury constant-maturity yield**, distributed through FRED as series `DGS3MO`.

For each ETF return month from September 2023 through August 2026, the project uses the last available business-day DGS3MO observation for that month. The exact FRED observation date is stored alongside the return-month label. The annual yield is converted to a monthly equivalent as:

`(1 + annual_yield)^(1/12) - 1`

Sharpe and Sortino ratios therefore use month-specific excess returns rather than one rounded risk-free assumption.

## Derived metrics

The following are calculated from the bundled CSV files by `analysis.py` and, independently, by formulas in the Excel workbook:

- total return;
- CAGR;
- annualized monthly volatility;
- Sharpe ratio;
- Sortino ratio;
- month-end maximum drawdown;
- historical monthly 95% VaR;
- beta versus SPY; and
- monthly-return correlations.

## Important limitations

- The analysis contains 36 monthly return observations, so risk estimates are sample-sensitive.
- Maximum drawdown is based on month-end observations and can miss deeper intramonth losses.
- Historical VaR from 36 monthly observations is a diagnostic, not a production risk model.
- Competitor data are point-in-time issuer snapshots with field-specific dates.
- Digrin is a public third-party historical-price provider; it is cited explicitly so the data source is not obscured.
