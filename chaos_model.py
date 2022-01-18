import math
import numpy as np
from scipy.linalg import expm
from scipy.linalg import inv
import matplotlib.pyplot as plt
class Chaos():
        #參數設定
    def __init__(self,a=35,d=3,b=35,timecut=0.001):
        self.A = []
        self.B = []
        self.G = []
        self.H = []
        self.setModulation(a, d, b, timecut)
    def setModulation(self,a=35,d=3,b=35,timecut=0.001):
        self.a = a
        self.d = d
        self.b = b
        self.timecut = timecut
        del self.A, self.B, self.G, self.H
        self.A = []
        self.B = []
        self.G = []
        self.H = []
        self.runModulation()
    def runModulation(self):
        self.A = np.array([[-self.a, self.a, 0],[self.b, 0, 0],[ 0, 0, -self.d]])
        self.B = np.array([[0, 0], [-1, 0], [0, 1]])
        self.G = expm(self.A*self.timecut)
        self.H = ((self.G- np.eye(3)).dot(inv(self.A))).dot(self.B)
    #混沌系統(離散後)
    def runChaos(self, x):
        t = np.array(self.G.dot(x) + self.H.dot(np.array([x[0]*x[2], x[0]*x[1]]).transpose()))
        return t
