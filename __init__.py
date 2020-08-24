from trend import base_trend, ma
from time_series import base_ts

a =[1,2,3,4,5,6,7,8,9]
trend_model = MA()
print(trend_model.predict(a))