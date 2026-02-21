# 4.4.1 경사 하강법 예제

from ch04_NN_Training.s4_4_Gradient.gradient_descent import gradient_descent
import numpy as np

def function_2(x) :
    return x[0]**2 + x[1]**2

if __name__ == "__main__" :
    init_x = np.array([-3.0, 4.0])
    print(f"초기 x : {init_x}\n")
    final = gradient_descent(function_2, init_x, 0.1, 100)
    print(f"최소값의 좌표 : {final}")
