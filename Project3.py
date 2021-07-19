import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

py.plot("corona_now.csv")
columns = ['국어','수학','영어','과학']
data.plot(kind='line', x='1', y= columns, ax= ax)
data.plot(kind='line', x='2', y='국어', ax= ax)
data.plot(kind='line', x='3', y='영어', ax= ax)
data.plot(kind='line', x='4', y='수학', ax= ax)
data.plot(kind='line', x='5', y='과학', ax= ax)

plt.show()
