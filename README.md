# automated-ts-forecasting
> forecasting a single time-series is easy, forecasting multiple-time series is **hard**

## Motivation

Forecasting at scale calls for an entirely new approach that the current paradigm of 'looking at ACF/PACF plots to squeeze out model parameters' cannot be applied, because the number of time-series involved tend to be in the hundreds, if not thousands. This is particularly the case in retail, where inventory optimization solutions require a robust demand forecasting solution for thousands of SKUs. The demands of several SKUs can be cross-correlated and additionally lagged.  

## Structure

The success of any good forecasting package lies in its ability to innately differentiate between model behaviour, sampling errors, outliers and noise. We aim to estimate each of the time series constituents and then move on to prediction. 
- ### Trend
- ### Seasonality
- ### Outliers
- ### Noise

## Research so far

I've scoured the interwebs and stumbled upon very few resources to go about in the topic. Whatever meagre resources I've managed to track down are listed below. 

- [Medium - On the Automation of Time Series Forecasting Models](https://towardsdatascience.com/on-the-automation-of-time-series-forecasting-models-technical-and-organizational-considerations-286db3120c8e)
- [Python package - AutoTS](https://pypi.org/project/AutoTS/)
- [Cross Validated - Is it possible to automate time-series forecasting?](https://stats.stackexchange.com/questions/380599/is-it-possible-to-automate-time-series-forecasting)
- [Cross Validated - Time Series Forecasting is an iterative process much like peeling an onion](https://stats.stackexchange.com/a/254496/122124)
- [Cross-Validated - Flowchart for Automated Time Seres Forecasting](https://i.stack.imgur.com/5rqlo.png)
