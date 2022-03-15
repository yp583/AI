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
