import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]  # 平方值

# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=10)
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=10)  # 渐变色
# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])  # x和y轴坐标的最小最大值

# plt.show()
plt.savefig('squares_plot.png')  # 保存图表
