# coding=utf-8
print(__doc__)

from sklearn import svm
import numpy as np
import pylab as pl

# create 40 separable points
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
print "X:", X
Y = [0] * 20 + [1] * 20
print "Y:", Y

# fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# get the separating hyperplane
w = clf.coef_[0]
print 'w:', w
a = -w[0] / w[1]
print 'a:', a
xx = np.linspace(-5, 5)
print 'xx:', xx
yy = a * xx - (clf.intercept_[0]) / w[1]
print 'yy:', yy

# plot the parallels to the separating hyperplane
# support vectors
b = clf.support_vectors_[0]
print 'b:', b
yy_down = a * xx + (b[1] - a * b[0])
print 'yy_down :', yy_down
b = clf.support_vectors_[-1]
print '-1 b : ', b
yy_up = a * xx + (b[1] - a * b[0])
print 'yy_up:', yy_up

pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')

pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()
