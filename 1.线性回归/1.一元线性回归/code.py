#!/usr/bin/python
# -*- coding: gb2312 -*-
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\Windows\Fonts\MSYHMONO.ttf", size=10)


def runplt():
    plt.figure()
    plt.title('文化水平与犯罪', fontproperties=font)
    plt.xlabel('受教育年限(年)', fontproperties=font)
    plt.ylabel('犯罪率(%)', fontproperties=font)
    plt.axis([0, 25, 0, 10])
    plt.grid(True)
    return plt


# 训练样本
x1 = [[0], [3], [6], [10]]
y1 = [[5], [3], [2], [1]]

# 测试样本
x2 = [[1], [5], [8], [12]]
y2 = [[4], [3], [2], [1]]

x3 = [[0], [4], [8], [12], [16]]

plt = runplt()
model = LinearRegression()
model.fit(x1, y1)
y3 = model.predict(x3)
score = model.score(x2, y2)  # R方检验
plt.plot(x1, y1, 'k.')
plt.plot(x3, y3, 'r-')
plt.show()
print(score)