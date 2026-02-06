# 3.2.4 시그모이드 함수 구현하기

import numpy as np
import matplotlib.pyplot as plt
from .stepGraph import step_function

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__" :
    x = np.arange(-5, 5, 0.1)
    y1 = sigmoid(x)
    y2 = step_function(x)

    plt.plot(x,y1)
    plt.plot(x,y2,linestyle='--')
    plt.ylim(-0.1, 1.1)
    plt.show()