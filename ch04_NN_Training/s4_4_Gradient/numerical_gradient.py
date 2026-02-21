# 4.4.0 기울기

from ch04_NN_Training.s4_3_Numerical_Differentiation.partial_diff import function
import numpy as np

def numerical_gradient(f, x) :
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size) :
        tmp_val = x[idx]
        
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val
    
    return grad
    

if __name__ == "__main__" :
    print(f"점(3,4)에서 기울기를 구하시오")
    print(f"기울기 : {numerical_gradient(function, np.array([3.0, 4.0]))}")
    print(f"점(0,2)에서 기울기를 구하시오")
    print(f"기울기 : {numerical_gradient(function, np.array([0.0, 2.0]))}")
    print(f"점(3,0)에서 기울기를 구하시오")
    print(f"기울기 : {numerical_gradient(function, np.array([3.0, 0.0]))}")

