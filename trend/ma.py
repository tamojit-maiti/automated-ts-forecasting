# -*- coding: utf-8 -*-
"""
Moving Average Trend Estimator
"""
from trend import base_trend

class MA(BaseTrendEstimator):

    def __init__(self):
        self.n_steps = None
        self.fitted_ = None
        self.forecasted_ = None


    def fit(self, y:pd.Series, X:pd.DataFrame = None)->object:
        """

        :param y: [series] variable / target variable (for multivariate time_series)
        :param X: [dataframe] exogenous variables (for multivariate time_series)
        :return: [object] self
        """
        self.fitted_ = y.rolling(self.n_steps)
        return self

    def predict(self, y:pd.Series, n_steps:int = 5, X:pd.DataFrame = None)->pd.Series:
        """

        :param y: [series] variable / target variable (for multivariate time_series)
        :param X: [dataframe] exogenous variables (for multivariate time_series)
        :param n: [int] number of time-steps to estimate trend
        :return: Trend values for the next 'n' steps
        """
        self.forecasted_ = np.arrya([self.fitted_]*n_steps)
        return self.forecasted_



