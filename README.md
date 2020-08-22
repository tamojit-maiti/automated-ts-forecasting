# automated-ts-forecasting
> forecasting a single time-series is easy, forecasting multiple-time series is **hard**

## Motivation

Forecasting at scale calls for an entirely new approach that the current paradigm of 'looking at ACF/PACF plots to squeeze out model parameters' cannot be applied, because the number of time-series involved tend to be in the hundreds, if not thousands. This is particularly the case in retail, where inventory optimization solutions require a robust demand forecasting solution for thousands of SKUs. The demands of several SKUs can be cross-correlated and additionally lagged.  

## Research so far

I've scoured the interwebs and stumbled upon very few resources to go about in the topic. Whatever meagre resources I've managed to track down are listed below. 

- [On the Automation of Time Series Forecasting Models](https://towardsdatascience.com/on-the-automation-of-time-series-forecasting-models-technical-and-organizational-considerations-286db3120c8e)
- [AutoTS](https://pypi.org/project/AutoTS/)
- [Is it possible to automate time-series forecasting](https://stats.stackexchange.com/questions/380599/is-it-possible-to-automate-time-series-forecasting)
