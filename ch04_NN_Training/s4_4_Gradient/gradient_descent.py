# 4.4.1 경사 하강법

from ch04_NN_Training.s4_4_Gradient.numerical_gradient import numerical_gradient
import numpy as np

def gradient_descent(f, init_x, lr=0.01, step_num = 100) :
    x = init_x

    for i in range(step_num) :
        grad = numerical_gradient(f, x)
        x -= lr * grad
    
    return x