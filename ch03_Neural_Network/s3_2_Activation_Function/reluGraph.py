# 3.2.7 ReLU 함수

import numpy as np
import matplotlib.pyplot as plt
from .stepGraph import step_function
from .sigmoidGraph import sigmoid

def relu(x) :
    return np.maximum(0, x)

if __name__ == "__main__" :
    x = np.arange(-5, 5, 0.1)
    y1 = step_function(x)
    y2 = sigmoid(x)
    y3 = relu(x)

    plt.plot(x,y1,linestyle="--",color="RED")
    plt.plot(x,y2,linestyle="dotted",color="GREEN")
    plt.plot(x,y3,color="BLUE")
    plt.ylim(-0.1,3)
    plt.show()