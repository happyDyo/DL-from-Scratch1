# 4.3.3 편미분

import numpy as np
import matplotlib.pyplot as plt

def function(x) :           # 변수가 여러개임에 주목
    return np.sum(x**2, axis = 0)

if __name__ == "__main__" :
    x0_line = np.arange(-3.0, 3.0, 0.1)
    x1_line = np.arange(-3.0, 3.0, 0.1)
    x0, x1 = np.meshgrid(x0_line, x1_line)
    x = np.array([x0,x1])
    z = function(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(x0, x1, z, cmap='viridis')

    ax.set_xlabel("x0")
    ax.set_ylabel("x1")
    ax.set_zlabel("f(x0, x1)")

    plt.show()

