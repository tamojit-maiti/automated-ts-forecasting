# automated-ts-forecasting
> forecasting a single time-series is easy, forecasting multiple-time series is **hard**

## Motivation

Forecasting at scale calls for an entirely new approach that the current paradigm of 'looking at ACF/PACF plots to squeeze out model parameters' cannot be applied, because the number of time-series involved tend to be in the hundreds, if not thousands. This is particularly the case in retail, where inventory optimization solutions require a robust demand forecasting solution for thousands of SKUs. The demands of several SKUs can be cross-correlated and additionally lagged.  
