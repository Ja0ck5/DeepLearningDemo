# coding=utf-8
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

# Read in the csv file and put features in a list of dict and list of class label
allElectronicsData = open(r'D:/Users/KY/PycharmProjects/DeepLearning/AllElectronics.csv', 'rb')
reader = csv.reader(allElectronicsData)
headers = reader.next()

print(headers)

featureList = []
labelList = []

for row in reader:
    # 添加每一行的最后一个值 即 class label
    labelList.append(row[len(row) - 1])
    # 为了取特征值
    rowDict = {}
    for i in range(1, len(row) - 1):
        # print row[i] 除了 rid 其他的特征值 key=header ,值为特征值
        rowDict[headers[i]] = row[i]
        # print 'rowDict : ',rowDict 添加到特征值列表中
    featureList.append(rowDict)

print featureList

# Vectorize features
vec = DictVectorizer()
# 转换成 分类器需要的格式
dummyX = vec.fit_transform(featureList).toarray()

print 'dummyX:', str(dummyX)
print 'vec feature name :', vec.get_feature_names()

print 'labelList:', str(labelList)

# Vectorize class labels
lb = preprocessing.LabelBinarizer()
# class label 转换成 分类器需要的格式
dummyY = lb.fit_transform(labelList)
print 'dummyY : ', str(dummyY)

# Using dicision tree for classfication
# clf = tree.DecisionTreeClassifier() 默认使用 CART 算法
# 改成使用信息熵 information gain
clf = tree.DecisionTreeClassifier(criterion='entropy')
# 构建决策树
clf = clf.fit(dummyX, dummyY)
print ('clf:' + str(clf))

# Visuliaze model
# with open('allEletronicGainiOri.dot', 'w') as f:
with open('allElectronicInformationGainOri.dot', 'w') as f:
    # f = tree.export_graphviz(clf,out_file=f)
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# 造一个新的信息,预测结果
oneRowX = dummyX[0, :]
print 'oneRowX: ', str(oneRowX)
# 取原来第一行
newRowX = oneRowX
# 随意更改两个值
newRowX[0] = 1
newRowX[2] = 0

print ('newRowX:' + str(newRowX))
# 变成二维数组
newRowX = newRowX.reshape(1, -1)
print ('reshape newRowX:' + str(newRowX))
# 预测结果
predictedY = clf.predict(newRowX)
print ('predictedY:' + str(predictedY))
