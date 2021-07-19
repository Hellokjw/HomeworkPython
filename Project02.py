import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

## x축: 날짜, y축: 신규 확진자 수
date = ['07.12', '07.13', '07.14', '07.15', '07.16', '07.17', '07.18']

As = [1063, 1097, 1568, 1555, 1476, 1401, 1402] ## 국내발생
Bs = [37, 53, 47, 45, 60, 51, 52] ## 해외유입

accumulate = np.add(As, Bs)

x = range(len(date))
plt.bar(x, Bs, color= "green")
plt.bar(x, As, bottom = Bs, color= "red")

ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(date)

plt.legend(['해외유입', '국내발생'])
plt.title('코로나19 신규 확진자 현황(2021.07.12 ~ 2021.07.18)')
plt.xlabel('날짜')
plt.ylabel('신규 확진자 수')
plt.show()

