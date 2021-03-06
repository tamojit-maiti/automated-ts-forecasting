import numpy as np

class TimeSeries:
    """
    Defines the BaseClass TimeSeries
    """

    def __init__(self, y, X=None):
        """
        Initializes an instance of the TimeSeries class
        :param X: (optional) dataframe indexed by dates containing exogenous variables
        :param y: variable / target variable (in case of multivariate time series)
        """
        self.X = X
        self.y = y

    def __repr__(self):
        """
        Representation of a TimeSeries object
        :return: returns  a general description (the shape and frequency) of the time_series passed
        """
        if self.X is None:
            is_multivariate = False
        else:
            is_multivariate = True

        return 'The time_series is ' \
               + ('univariate' if self.X is None else 'multivariate') + ' with ' \
               + str(np.array(self.y).shape[0]) + ' time steps ' \
               + is_multivariate*('and '
                                  + ('None' if self.X is None else str(np.array(self.X).shape[1]))
                                  + 'exogenous variables')
