import matplotlib.pyplot as plt
import matplotlib

# 设置 matplotlib 支持中文的字体
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 系统中支持中文的字体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：白砂糖含量和对应的评分（随机评分）
sugar_amounts = [40, 60, 80, 100, 120]  # 白砂糖含量 (g)
sweetness_scores = [3, 4, 5, 4, 3]  # 甜度评分
flavor_scores = [2, 3, 4, 3, 2]  # 风味协调性评分
mouthfeel_scores = [4, 5, 4, 3, 2]  # 口感评分

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图表大小

# 绘制每条折线，并为每个数据点添加标记
plt.plot(sugar_amounts, sweetness_scores, marker='o', label='甜度评分', color='black', linestyle='-', linewidth=1.5)
plt.plot(sugar_amounts, flavor_scores, marker='s', label='风味协调性评分', color='black', linestyle='--', linewidth=1.5)
plt.plot(sugar_amounts, mouthfeel_scores, marker='^', label='口感评分', color='black', linestyle='-.', linewidth=1.5)

# 添加标题和标签
plt.title('白砂糖含量对果酱品质的影响', color='black')
plt.xlabel('白砂糖含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')

# 设置纵坐标范围和刻度
plt.ylim(0, 5)  # 设置评分范围为0到5
plt.yticks(range(0, 6), color='black')  # 设置评分刻度为0到5，步长为1

# 设置横坐标刻度
plt.xticks(sugar_amounts, color='black')  # 显示所有白砂糖含量的刻度

# 添加图例
plt.legend(loc='best', frameon=False)

# 移除网格背景
plt.grid(False)

# 显示图表
plt.show()