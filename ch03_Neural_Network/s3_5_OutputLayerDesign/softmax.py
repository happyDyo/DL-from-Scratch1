# 3.5.1 소프트맥스 함수 구현하기

import numpy as np

def softmax(a) :
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)

    return exp_a / sum_exp_a

if __name__ == "__main__" :
    a = np.array([0.3, 2.9, 4.0])
    print(f"a : {a}")
    print(f"softmax(a) : {softmax(a)}")

