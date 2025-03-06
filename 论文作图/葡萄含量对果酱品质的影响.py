import matplotlib.pyplot as plt
import matplotlib

# 设置 matplotlib 支持中文的字体
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 系统中支持中文的字体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：葡萄含量和对应的评分（随机评分）
grape_amounts = [100, 150, 200, 250, 300]  # 葡萄含量 (g)
aroma_scores = [4, 4.5, 5, 4.8, 4.6]  # 果香浓郁度评分
texture_scores = [3, 3.5, 4, 3.8, 3.5]  # 质地浓稠度评分
mouthfeel_scores = [4, 4.2, 4.5, 4.3, 4.1]  # 口感评分

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图表大小

# 绘制每条折线，并为每个数据点添加标记
plt.plot(grape_amounts, aroma_scores, marker='o', label='果香浓郁度', color='black', linestyle='-', linewidth=1.5)
plt.plot(grape_amounts, texture_scores, marker='s', label='质地浓稠度', color='black', linestyle='--', linewidth=1.5)
plt.plot(grape_amounts, mouthfeel_scores, marker='^', label='口感', color='black', linestyle='-.', linewidth=1.5)

# 添加标题和标签
plt.title('葡萄含量对果酱品质的影响', color='black')
plt.xlabel('葡萄含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')

# 设置纵坐标范围和刻度
plt.ylim(0, 5)  # 设置评分范围为0到5
plt.yticks(range(0, 6), color='black')  # 设置评分刻度为0到5，步长为1

# 设置横坐标刻度
plt.xticks(grape_amounts, color='black')  # 显示所有葡萄含量的刻度

# 添加图例
plt.legend(loc='best', frameon=False)

# 移除网格背景
plt.grid(False)

# 显示图表
plt.show()