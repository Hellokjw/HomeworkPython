import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

## x축: 날짜, y축: 일일 누적 확진자 수 / 일일 누적 격리해제자 수
date = ['07.12', '07.13', '07.14', '07.15', '07.16', '07.17', '07.18'] 
corona1 = [1100, 1150, 1615, 1600, 1535, 1454, 1451] ## 일일 누적 확진자 수
corona2 = [427, 565, 739, 1018, 604, 647, 993] ## 일일 누적 격리해제자 수

plt.subplot(2, 1, 2)
plt.plot(date, corona1) ## 일일 누적 확진자 수를 통계로 나타냄.
plt.plot(date, corona2) ## 일일 누적 격리해제자 수를 통계로 나타냄.


plt.title("2021년 일일 누적 확진자 추세(2021.07.12 ~ 2021.07.18)")
plt.xlabel("날짜")
plt.ylabel("신규 확진자 수")

plt.subplots_adjust(left = 0.1, bottom = 0.1, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.35)
plt.show()
