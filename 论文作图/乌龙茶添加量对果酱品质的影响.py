import matplotlib.pyplot as plt
import matplotlib

# 设置 matplotlib 支持中文的字体
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 系统中支持中文的字体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：乌龙茶添加量和对应的评分
tea_amounts = [0, 2, 4, 6, 8]  # 乌龙茶添加量 (g)
color_scores = [4, 3.5, 3, 2.5, 2]  # 色泽评分
aroma_scores = [2, 3, 4, 3.5, 3]  # 香气评分
taste_scores = [3, 3.5, 4, 3, 2]  # 口感评分
texture_scores = [3, 3.5, 4, 3, 2.5]  # 质地评分

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图表大小

# 绘制每条折线，并为每个数据点添加标记
plt.plot(tea_amounts, color_scores, marker='o', label='色泽评分', color='black', markersize=6, linestyle='-', linewidth=1.5)
plt.plot(tea_amounts, aroma_scores, marker='s', label='香气评分', color='black', markersize=6, linestyle='--', linewidth=1.5)
plt.plot(tea_amounts, taste_scores, marker='^', label='口感评分', color='black', markersize=6, linestyle='-.', linewidth=1.5)
plt.plot(tea_amounts, texture_scores, marker='x', label='质地评分', color='black', markersize=6, linestyle=':', linewidth=1.5)

# 添加标题和标签
plt.title('乌龙茶添加量对果酱品质的影响', color='black')
plt.xlabel('乌龙茶添加量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')

# 设置纵坐标范围和刻度
plt.ylim(0, 5)  # 设置评分范围为0到5
plt.yticks(range(0, 6), color='black')  # 设置评分刻度为0到5，步长为1

# 设置横坐标刻度
plt.xticks(tea_amounts, color='black')  # 只显示0, 2, 4, 6, 8这几个刻度

# 添加图例
plt.legend(loc='best', frameon=False)

# 移除网格背景
plt.grid(False)

# 显示图表
plt.show()