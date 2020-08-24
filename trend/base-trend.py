# -*- coding: utf-8 -*-
"""
Base Class for all Trend Estimators
"""
import numpy as np

class BaseTrendEstimator():
    """
    Abstract Class for all Trend Estimators
    """

    def __init__(self):
        """
        Initializes an instance of the Trend Class
        """
        pass

    def fit(self, y, X = None):
        """
        Fits trend of y
        :return: series containing trend_y, indexed by
        """
