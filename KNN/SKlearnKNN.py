# coding=utf-8

from sklearn import neighbors
from sklearn import datasets

# knn 分类器
knn = neighbors.KNeighborsClassifier()

# 加载 iris 数据集
iris = datasets.load_iris()

print iris

# 建立模型 # 特征值：iris.data 。目标结果：iris.target
knn.fit(iris.data, iris.target)

# 将被预测的数据
exData = [[0.1, 5.2, 5.3, 5.4]]
# 预测
predictedLabel = knn.predict(exData)

print predictedLabel
