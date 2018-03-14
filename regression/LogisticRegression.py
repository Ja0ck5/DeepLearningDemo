import numpy as np
import random


# m denotes the number of examples here,not the number of features
def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        print("Interation : %d /Cost : %f" % (i, cost))
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta


def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    # basically a straight line
    for i in range(0,numPoints):
        # bias features
        x[i][0] = 1
        x[i][1] = i
        # target variable
        y[i] = (i+bias)+random.uniform(0,1) * variance

    return x,y

x,y = genData(100,25,10)
print "x:"
print x
print "y:"
print y

m,n = np.shape(x)




