from matplotlib import pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

date = ['07.12', '07.13', '07.14', '07.15', '07.16', '07.17', '07.18']

value_a = [1063, 1097, 1568, 1555, 1476, 1401, 1402] ## 국내발생
value_b = [37, 53, 47, 45, 60, 51, 52] ## 해외유입

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

value_a_x = create_x(2, 0.8, 1, 7)
value_b_x = create_x(2, 0.8, 2, 7)

ax = plt.subplot()
ax.bar(value_a_x, value_a, color= "red")
ax.bar(value_b_x, value_b, color= "green")

middle_x = [(a+b)/2 for (a,b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(date)

plt.legend(['해외유입', '국내발생'])
plt.title('코로나19 신규 확진자 현황(2021.07.12 ~ 2021.07.18)')
plt.xlabel('날짜')
plt.ylabel('신규 확진자 수')

plt.show()

##t = 2 # There are two sets of data: A and B
##w = 0.8 # We generally want bars to be 0.8
##n = 1 # A is first set of data
##d = 6 # There are 5 topics we're plotting
