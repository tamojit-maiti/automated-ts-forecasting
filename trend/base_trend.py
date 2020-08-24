# -*- coding: utf-8 -*-
"""
Base Class for all Trend Estimators
"""

import pandas as pd

class BaseTrendEstimator:
    """
    Abstract Class for all Trend Estimators
    """

    def __init__(self):
        """
        Initializes an instance of the Trend Class
        """
        pass

    def fit(self, y:pd.Series , X:pd.DataFrame = None)->object:
        """
        Fits a trend line

        :param y: [series] variable / target variable (for multivariate time-series)
        :param X: [dataframe] exogenous variables (for multivariate time-series)
        :return: TrendEstimator object
        """
        pass

    def predict(self, y:pd.Series ,n:int, X: pd.DataFrame = None )-> pd.Series:
        """
        :param y: [series] variable / target variable (for multivariate time-series)
        :param X: [dataframe] exogenous variables (for multivariate time-series)
        :param n: [int] number of time-steps to estimate trend
        :return: Trend values for the next 'n' steps
        """
        pass



