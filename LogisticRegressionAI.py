import numpy as np

from sklearn.datasets import load_iris
data = load_iris()



class SentimentAI:
    def __init__(self):
        self.nothing = 0

#y = m1x1+m2x2+m3x3+b

def sigmoid(x):
    return (1.0)/(1.0+np.exp(-x))
def sigmoidDeriv(x):
    return (sigmoid(x))*(1-sigmoid(x))

maxIter = 300

nodes = []
biases = []
weights = []

def initStuff():
    global layers, nodes, biases, weights
    for t in range(len(layers)-1):
        
        weights.append(0.5 * np.ones((layers[t+1], layers[t])))
        nodes.append(np.zeros((layers[t], 1)))
        biases.append(np.zeros((layers[t+1], 1)))
        
    nodes.append(np.zeros((layers[-1], 1)))

def updateWeightsandBiases(errors, nodes, learningRate):
    global weights, layers, biases
    #print(nodes, "\n\n", weights, "\n\n")
    for i in range(len(layers)-1):
        weights_change = 0
        biases_change = 0
        for j in range(len(errors)):
            weights_change += errors[j][i+1] @ nodes[j][i].T
            biases_change += errors[j][i+1]
        
        weights[i] -= (weights_change * learningRate)/(len(errors))
        biases[i] -= (biases_change * learningRate)/(len(errors))
    #print(errors)
    #print(errors)

def feedforward(x, y=[], training = True):
    global layers, nodes, biases, weights
    nodes[0] = x.reshape((len(x), 1));

    nodes_z = []
    nodes_z.append(x.reshape((len(x), 1)))
    
    errors = []

    
    
    for i in range(len(layers)-1):

        weights_curr = weights[i]
        biases_curr = biases[i]
        nodes_curr = nodes[i]

        nodes_z.append((weights_curr @ nodes_curr) + biases_curr)

        nodes_next = sigmoid(nodes_z[-1])
        
        nodes[i+1] = nodes_next
        
    if (training):
        outputDiff = (nodes[-1] - y.reshape((len(y), 1)))
        errors.append(outputDiff * sigmoidDeriv(nodes_z[-1]))
        
        for i in range(len(layers)-2, -1, -1):
            error_i = ((np.asarray(weights[i]).T) @ errors[0]) * sigmoidDeriv(nodes_z[i])
            errors = [error_i] + errors

        
        return nodes, errors 
   
    return nodes[-1]


def main(readFile = False):
    x = data['data'][:99]
    y = data['target'][:99]

    #print(y)
    global layers, weights
    layers = [4, 1]
    initStuff()
    if (readFile == False):
        for i in range(10000):
            for k in range(10):
                errors_batch = []
                nodes_batch = []
                for j in range(len(x)//10):
                    nodes, errors = feedforward(x[j + k*(len(x)//10)], np.asarray([y[j + k*(len(x)//10)]]))
                    cost = 0.5 * ((nodes[-1][0] - y[j + k*(len(x)//10)]) ** 2)
                    #print(cost)
                    nodes_batch.append(nodes)
                    errors_batch.append(errors)
                updateWeightsandBiases(errors_batch, nodes_batch, .001)
    else:
        weights, biases = pickle.load(open('weights&biases.stf', 'rb')

    print(feedforward(x[80], [], False))
    print(y[80])

    
    #cost = .5 * np.sum((y-output)**2)
    #print(cost)


import pickle

main(True)

pickle.dump([weights, biases], open('weights&biases.stf', 'wb'))

    
       
"""
weights_1 = np.zeros((2, 10))

    biases_1 = np.zeros((2, 1))

    nodes_1 = np.zeros((10, 1))

    nodes_2 = sigmoid(weights_1 @ nodes_1 + biases_1).reshape((2, 1))
"""
