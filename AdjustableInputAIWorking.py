import numpy as np
from matplotlib import pyplot as plt

costs = np.array([])
costs_X = np.array([])
amountofinputs=2

def sigmoid(x, deriv = False):
    if deriv == True:
        return x*(1-x)
    return 1 / (1 + np.exp(-x))
def visData(x, x_name, y, y_name, title):
    fig = plt.figure()
    fig.subplots_adjust(bottom=-.8)
    ax = fig.add_subplot(211)
    ax.set_ylabel(y_name)
    ax.set_xlabel(x_name)
    ax.set_title(title)
    line = ax.plot(x, y)
    plt.show()
def replaceInArray(array, index, element):
    prevArray=array
    array = np.array([])
    print (array, prevArray)
    for i in range(len(prevArray)):
        if (i != index):
            array = np.append(array, prevArray[i])
        else:
            array = np.append(array, element)
    print(array)
    return array
def getCost(costMatrix):
    cost = 0
    for i in range(len(costMatrix)):
        cost+=costMatrix[i]
    return cost
def gradientDescent(x, y, epoch, learning_rate):
    global costs, costs_X
    inputs = x.T
    weights = np.array([])
    for i in range(amountofinputs):
        weights = np.append(weights, 0)
    b_curr = 0
    n = len(inputs)
    for i in range(epoch):
        weights_deriv = np.array([])
        q = np.empty((0, len(x)))
        z = np.array([])
        q_temp = []
        for j in range(amountofinputs):
            q_temp.append(inputs[j] * weights[j])
            q = np.asarray(q_temp)
#            print(q.T)
        for k in range(len(q.T)):
            z = np.append(z, np.sum(q.T[k]))
#            print(z, "  hello  ", q.T[k])
        y_predicted = z + b_curr
        if (i%100 == 0):
            cost = np.square(y-y_predicted)
            print (cost)
            costs = np.append(costs, getCost(cost))
            costs_X= np.append(costs_X, i)
        for l in range(amountofinputs):
            weights_deriv = np.append(weights_deriv, -(2/n)*sum(inputs[l]*(y-y_predicted)))
            weights[l] = weights[l] - (learning_rate * weights_deriv[l])
        bd = -(2/n)*sum((y-y_predicted))
        b_curr = b_curr - learning_rate * bd
    return weights, b_curr

X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]])
#X2 = np.array([1, 4, 2, 6])
y = np.array([1, 2, 3, 4])

np.random.seed(1)
testWeights, testBias = gradientDescent(X, y, 1000, 0.001)
z2 = np.array([])
q2 = 0

for i in range(amountofinputs):
        z2 = np.append(z2, np.dot([4.9, 5], testWeights[i]))
        q2 += z2[i]
out = q2 + testBias
print ("out: ", np.round(out, 1), "  cost: ~", np.round(costs[costs.size-1], 3))
visData(costs_X, "Iteration",costs, "Cost", "Cost Function")



