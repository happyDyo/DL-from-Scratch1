# 4.3.2 수치 미분의 예

from ch04_NN_Training.s4_3_Numerical_Differentiation.differentiation import numerical_diff
import numpy as np
import matplotlib.pyplot as plt

def function_1(x) : 
    return 0.01 * x**2 + 0.1 * x

x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()