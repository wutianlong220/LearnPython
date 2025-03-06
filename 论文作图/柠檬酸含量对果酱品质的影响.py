import matplotlib.pyplot as plt
import matplotlib

# 设置 matplotlib 支持中文的字体
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 系统中支持中文的字体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：柠檬酸含量和对应的评分（随机评分）
citric_acid_amounts = [1, 2, 3, 4, 5]  # 柠檬酸含量 (g)
acidity_scores = [2.5, 3, 4, 3.5, 3]  # 酸度评分
refreshing_scores = [3, 4, 4.5, 4, 3.5]  # 口感清爽度评分
shelf_life_scores = [4, 4.5, 5, 4.5, 4]  # 保质期评分

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图表大小

# 绘制每条折线，并为每个数据点添加标记
plt.plot(citric_acid_amounts, acidity_scores, marker='o', label='酸度', color='black', linestyle='-', linewidth=1.5)
plt.plot(citric_acid_amounts, refreshing_scores, marker='s', label='口感清爽度', color='black', linestyle='--', linewidth=1.5)
plt.plot(citric_acid_amounts, shelf_life_scores, marker='^', label='保质期', color='black', linestyle='-.', linewidth=1.5)

# 添加标题和标签
plt.title('柠檬酸含量对果酱品质的影响', color='black')
plt.xlabel('柠檬酸含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')

# 设置纵坐标范围和刻度
plt.ylim(0, 5)  # 设置评分范围为0到5
plt.yticks(range(0, 6), color='black')  # 设置评分刻度为0到5，步长为1

# 设置横坐标刻度
plt.xticks(citric_acid_amounts, color='black')  # 显示所有柠檬酸含量的刻度

# 添加图例
plt.legend(loc='best', frameon=False)

# 移除网格背景
plt.grid(False)

# 显示图表
plt.show()