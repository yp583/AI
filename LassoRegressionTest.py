import numpy as np
import matplotlib.pyplot as plt
class LassoRegressionAI:
    def __init__(self, dataIN, dataOUT, learningRate, l1Coeff):
        self.X = dataIN
        self.y = dataOUT
        self.lR = learningRate
        self.l1Coeff = l1Coeff
        self.weights = np.zeros(dataIN.shape[1])

    def clip(self, beta, alpha):
        clipped = np.minimum(beta, alpha)
        clipped = np.maximum(clipped, -alpha)

        return clipped

    def proxL1Norm(self, weights, learningRate, penalizeAll = True):

        out = weights - self.clip(weights, learningRate)

        if not penalizeAll:
            out[0] = weights[0]
            
        return out

    def solveLasso_proxGrad(self, maxIter = 300):

        #lR is learningRate , X is data in, y is predicted out
        costFuncVals = np.zeros(maxIter)

        for t in range(maxIter):
            grad = self.X.T @ (self.X @ self.weights - self.y)
            self.weights = self.proxL1Norm(self.weights - self.lR*grad, self.lR*self.l1Coeff)

            costFuncVals[t] = .5*np.linalg.norm(self.X @ self.weights - self.y)**2 + self.l1Coeff*np.sum(np.abs(self.weights))

    def getPredictedOutcome(x):
        return x @ self.weights
"""   
def initFakeData(N, d, nnz):
    np.random.seed(10)

    prm = np.random.permutation(d+1)
    betaTrue = np.zeros(d+1)
    betaTrue[prm[0:nnz]] = np.random.randn(nnz)

    X = np.random.randn(N, d)
    print(X.shape)
    X = np.insert(X, 0, 1, axis = 1)
    print(X.shape)

    noise = .001*np.random.randn(N)

    y = X @ betaTrue + noise
    
    return X, y, betaTrue

X, y, weightsTrue = initFakeData(10, 100, 50)

myLasso = LassoRegressionAI(X, y, .005, 10)
myLasso.solveLasso_proxGrad()
weights = myLasso.weights
X = myLasso.X
y= myLasso.y

plt.figure()
s = np.arange(10)
plt.plot(s, X @ weights)
plt.plot(s, y)

plt.show()
"""
