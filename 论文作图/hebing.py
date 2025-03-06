import matplotlib.pyplot as plt
import matplotlib

# 设置 matplotlib 支持中文的字体
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'  # macOS 系统中支持中文的字体
matplotlib.rcParams['font.size'] = 12  # 设置字体大小
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 数据：乌龙茶添加量和对应的评分
tea_amounts = [0, 2, 4, 6, 8]  # 乌龙茶添加量 (g)
color_scores_tea = [4.5, 4.2, 4, 3.5, 3]  # 色泽评分
aroma_scores_tea = [2, 3, 4.5, 3.5, 3]  # 香气评分
taste_scores_tea = [2, 3, 4.5, 3, 2.5]  # 口感评分
texture_scores_tea = [4, 4, 4, 4, 4]  # 质地评分

# 数据：白砂糖含量和对应的评分
sugar_amounts = [40, 60, 80, 100, 120]  # 白砂糖含量 (g)
color_scores_sugar = [4, 4, 4, 3.8, 3.5]  # 色泽评分
aroma_scores_sugar = [3.5, 4, 4.5, 3.5, 3]  # 香气评分
taste_scores_sugar = [2.5, 3.5, 4.5, 3, 2]  # 口感评分
texture_scores_sugar = [3.5, 3.8, 4, 4.2, 4.5]  # 质地评分

# 数据：葡萄糖含量和对应的评分
glucose_amounts = [100, 150, 200, 250, 300]  # 葡萄糖含量 (g)
color_scores_glucose = [3.5, 3.8, 4, 3.8, 3.5]  # 色泽评分
aroma_scores_glucose = [2.5, 3.5, 4.5, 4, 3.5]  # 香气评分
taste_scores_glucose = [2.5, 3.5, 4.5, 3.5, 3]  # 口感评分
texture_scores_glucose = [3, 3.5, 4, 4.2, 4.5]  # 质地评分

# 数据：柠檬酸含量和对应的评分
citric_amounts = [1, 2, 3, 4, 5]  # 柠檬酸含量 (g)
color_scores_citric = [4, 4, 4, 3.8, 3.5]  # 色泽评分
aroma_scores_citric = [3, 3.5, 4, 3.5, 3]  # 香气评分
taste_scores_citric = [2.5, 3.5, 4.5, 3, 2]  # 口感评分
texture_scores_citric = [4, 4, 4, 4, 4]  # 质地评分

# 绘制乌龙茶添加量对评分的影响
plt.figure(figsize=(10, 6))
plt.plot(tea_amounts, color_scores_tea, marker='o', label='色泽评分', color='black', markersize=6, linestyle='-', linewidth=1.5)
plt.plot(tea_amounts, aroma_scores_tea, marker='s', label='香气评分', color='black', markersize=6, linestyle='--', linewidth=1.5)
plt.plot(tea_amounts, taste_scores_tea, marker='^', label='口感评分', color='black', markersize=6, linestyle='-.', linewidth=1.5)
plt.plot(tea_amounts, texture_scores_tea, marker='x', label='质地评分', color='black', markersize=6, linestyle=':', linewidth=1.5)
plt.title('乌龙茶添加量对果酱品质的影响', color='black')
plt.xlabel('乌龙茶添加量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')
plt.ylim(0, 5)
plt.yticks(range(0, 6), color='black')
plt.xticks(tea_amounts, color='black')
plt.legend(loc='best', frameon=False)
plt.grid(False)
plt.savefig('乌龙茶添加量对果酱品质的影响.png')  # 保存图像
plt.show()

# 绘制白砂糖含量对评分的影响
plt.figure(figsize=(10, 6))
plt.plot(sugar_amounts, color_scores_sugar, marker='o', label='色泽评分', color='black', markersize=6, linestyle='-', linewidth=1.5)
plt.plot(sugar_amounts, aroma_scores_sugar, marker='s', label='香气评分', color='black', markersize=6, linestyle='--', linewidth=1.5)
plt.plot(sugar_amounts, taste_scores_sugar, marker='^', label='口感评分', color='black', markersize=6, linestyle='-.', linewidth=1.5)
plt.plot(sugar_amounts, texture_scores_sugar, marker='x', label='质地评分', color='black', markersize=6, linestyle=':', linewidth=1.5)
plt.title('白砂糖含量对果酱品质的影响', color='black')
plt.xlabel('白砂糖含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')
plt.ylim(0, 5)
plt.yticks(range(0, 6), color='black')
plt.xticks(sugar_amounts, color='black')
plt.legend(loc='best', frameon=False)
plt.grid(False)
plt.savefig('白砂糖含量对果酱品质的影响.png')  # 保存图像
plt.show()

# 绘制葡萄糖含量对评分的影响
plt.figure(figsize=(10, 6))
plt.plot(glucose_amounts, color_scores_glucose, marker='o', label='色泽评分', color='black', markersize=6, linestyle='-', linewidth=1.5)
plt.plot(glucose_amounts, aroma_scores_glucose, marker='s', label='香气评分', color='black', markersize=6, linestyle='--', linewidth=1.5)
plt.plot(glucose_amounts, taste_scores_glucose, marker='^', label='口感评分', color='black', markersize=6, linestyle='-.', linewidth=1.5)
plt.plot(glucose_amounts, texture_scores_glucose, marker='x', label='质地评分', color='black', markersize=6, linestyle=':', linewidth=1.5)
plt.title('葡萄糖含量对果酱品质的影响', color='black')
plt.xlabel('葡萄糖含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')
plt.ylim(0, 5)
plt.yticks(range(0, 6), color='black')
plt.xticks(glucose_amounts, color='black')
plt.legend(loc='best', frameon=False)
plt.grid(False)
plt.savefig('葡萄糖含量对果酱品质的影响.png')  # 保存图像
plt.show()

# 绘制柠檬酸含量对评分的影响
plt.figure(figsize=(10, 6))
plt.plot(citric_amounts, color_scores_citric, marker='o', label='色泽评分', color='black', markersize=6, linestyle='-', linewidth=1.5)
plt.plot(citric_amounts, aroma_scores_citric, marker='s', label='香气评分', color='black', markersize=6, linestyle='--', linewidth=1.5)
plt.plot(citric_amounts, taste_scores_citric, marker='^', label='口感评分', color='black', markersize=6, linestyle='-.', linewidth=1.5)
plt.plot(citric_amounts, texture_scores_citric, marker='x', label='质地评分', color='black', markersize=6, linestyle=':', linewidth=1.5)
plt.title('柠檬酸含量对果酱品质的影响', color='black')
plt.xlabel('柠檬酸含量 (g)', color='black')
plt.ylabel('评分 (0-5)', color='black')
plt.ylim(0, 5)
plt.yticks(range(0, 6), color='black')
plt.xticks(citric_amounts, color='black')
plt.legend(loc='best', frameon=False)
plt.grid(False)
plt.savefig('柠檬酸含量对果酱品质的影响.png')  # 保存图像
plt.show()