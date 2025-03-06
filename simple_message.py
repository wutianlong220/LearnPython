import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子以确保结果可复现（可选）
np.random.seed(42)

# 生成随机数据
x = np.arange(1, 6)  # 横坐标范围 1 到 5
y1 = np.random.randint(0, 101, size=5)  # 第一组随机纵坐标
y2 = np.random.uniform(0, 6.1, size=5)  # 第二组随机纵坐标
y3 = np.random.randint(10, 91, size=5)  # 第三组随机纵坐标

# 绘制折线图
fig, ax = plt.subplots(figsize=(10, 6))  # 设置图形大小

# 第一条折线
ax.plot(x, y1, marker='o', linestyle='-', color='b', label='Line 1')

# 第二条折线
ax.plot(x, y2, marker='x', linestyle='--', color='r', label='Line 2')

# 第三条折线
ax.plot(x, y3, marker='s', linestyle='-.', color='g', label='Line 3')

# 添加标题和标签
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Three-Line Chart')

# 添加图例
ax.legend()

# 显示图表
plt.show()