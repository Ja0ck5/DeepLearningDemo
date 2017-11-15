# coding=utf-8
from sklearn import svm

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]
clf = svm.SVC(kernel='linear')
clf.fit(x, y)

print clf

# get support vector
print 'support_vectors_:', clf.support_vectors_

# get indices of support vectors 支持向量所在的数组的索引位置
print 'support_:', clf.support_

# get number of support vectors for each class 支持向量 分别的个数
print 'n_support_:', clf.n_support_
