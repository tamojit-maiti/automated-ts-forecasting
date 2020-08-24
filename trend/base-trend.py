# -*- coding: utf-8 -*-
"""
Base Class for all Trend Estimators
"""

import numpy as np
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

    def fit(self, y:pd.Series , X:pd.DataFrame = None):
        """
        Fits a trend line

        :param y: [series] variable / target variable (for multivariate time-series)
        :param X: [dataframe] exogenous variables (for multivariate time-series)
        :return: TrendEstimator object
        """
        return pass

    def predict(self, y: pd.Series ,n:int, X: pd.dataframe = None ):
        """

        :param y: [series] variable / target variable (for multivariate time-series)
        :param X: [dataframe] exogenous variables (for multivariate time-series)
        :param n: [int] number of time-steps to estimate trend
        :return: Trend values for the next 'n' steps
        """
        