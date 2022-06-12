import numpy as np

def getX_Y(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    return x, y
    # print("x: ",x)
    # print("y: ",y)
def add(x,y):
    return x+y