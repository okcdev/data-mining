'''
Created on 2016-11-20

@author: xue
'''
import numpy as np
class Filter(object):
    '''
    classdocs
    Filter类保存了卷积层的参数以及梯度，
    并且实现了用梯度下降算法来更新参数
    '''


    def __init__(self, width, height, depth):
        self.weights = np.random.uniform(-1e-4, 1e-4, (depth, height, width))
        self.bias = 0
        self.weights_grad = np.zeros(self.weights.shape)
        self.bias_grand = 0
        
    def __repr__(self):
        return 'filter weights:\n%s\nbisa:\n%s' % (repr(self.weights), repr(self.bias))
    
    def get_weights(self):
        return self.weights
    
    def get_bias(self):
        return self.bias
        
    def update(self, learning_rate):
        self.weights -= learning_rate * self.weights_grad
        self.bias -= learning_rate * self.bias_grand
        
        
        
        
        
        
        
        
        
        