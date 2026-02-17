# 4.3.2 수치 미분의 예

from ch04_NN_Training.s4_3_Numerical_Differentiation.differentiation import numerical_diff
import numpy as np
import matplotlib.pyplot as plt

def function_1(x) : 
    return 0.01 * x**2 + 0.1 * x

if __name__ == "__main__" :    
    print(f"주어진 함수 f(x)")

    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    plt.show()

    print(f"5에서의 미분값 : {numerical_diff(function_1, 5)}")
    print(f"10에서의 미분값 : {numerical_diff(function_1, 10)}")