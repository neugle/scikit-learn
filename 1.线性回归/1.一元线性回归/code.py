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


x = [[0], [1], [3], [5], [6], [8], [10], [12]]
y1 = [[5], [4], [3], [3], [2], [2], [1], [1]]

plt = runplt()
model = LinearRegression()
model.fit(x, y1)
y2 = model.predict(x)
score = model.score(x, y1)  # R方检验
plt.plot(x, y1, 'k.')
plt.plot(x, y2, 'r-')
plt.show()
print(score)
