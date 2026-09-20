# Interview Notes

## 30-second version

I built this project to combine the strategic and quantitative sides of investment management. I mapped the competitive structure of major emerging-markets ETFs, then built a multi-asset risk framework covering return, volatility, Sharpe and Sortino ratios, drawdowns, VaR, beta, and correlations. The strategic takeaway was that broad emerging-markets beta is already highly fee-competitive, so a new product would need a differentiated investment outcome rather than another low-cost clone. I translated that into a hypothetical quality-and-risk systematic ETF concept and identified the commercial and portfolio-construction tests required before launch.

## 90-second version

The project starts with a product-development question: if an asset manager wanted to expand in emerging-markets ETFs, is there a strong case for another broad passive product? I compared major competitors on fees, scale, benchmark design, holdings, and positioning, which showed a mature, fee-compressed category with several scaled incumbents.

I then built a cross-asset quantitative framework in Python and Excel using ten ETFs across U.S. equities, international equities, bonds, credit, real estate, and gold. I calculated total return, CAGR, annualized volatility, Sharpe and Sortino ratios, maximum drawdown, historical VaR, beta to SPY, and a correlation matrix. That let me separate return from risk and identify where diversification actually came from.

Instead of concluding that the highest-return asset was automatically the best product opportunity, I combined both analyses. The strategy case proposes testing a systematic emerging-markets quality-and-risk concept with profitability, balance-sheet, liquidity, concentration, and drawdown controls. The analysis produces a product hypothesis, not a launch recommendation. A real decision would still need demand research, capacity, trading-cost, distribution, fee, and economic analysis.

## Questions to be ready for

### Why these ETFs?
They create a compact cross-asset universe with recognizable liquid proxies for major equity, fixed-income, real-estate, and commodity exposures, while EEM links the risk analysis directly to the product-strategy case.

### Why monthly data?
The bundled version is reproducible and compact, and monthly data are sufficient to demonstrate the framework. I explicitly flag that drawdown and VaR are less precise at monthly frequency. A production version would use a longer sample and higher-frequency data where appropriate.

### How did you handle the risk-free rate?
I used the Federal Reserve’s 3-month Treasury constant-maturity series (FRED DGS3MO), took the last available observation for each return month, converted the annual yield to a monthly equivalent, and calculated excess returns month by month. That is more defensible than applying one rounded rate across the full sample.

### What would you improve next?
I would add ETF fund-flow history, rolling tracking error, factor-exposure analysis, liquidity/spread data, scenario stress testing, and a simple product P&L / break-even AUM model. For the hypothetical strategy, I would backtest the actual quality-and-risk signal rather than infer product viability from category-level evidence.

### What was the hardest part?
The main challenge was connecting two analytical lenses: market/product strategy and portfolio risk. The goal was to avoid a purely quantitative ranking and instead use the metrics to inform a commercially relevant product-development question.
