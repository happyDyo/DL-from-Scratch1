# 3.4.2 각 층의 신호 전달 구현하기

import numpy as np

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X,W1) + B1

if __name__ == "__main__" :
    print(f"\nX 형상 : {X.shape}")
    print(f"X : {X}\n")

    print(f"W1 형상 : {W1.shape}")
    print(f"W1 : {W1}\n")

    print(f"B1 형상 : {B1.shape}")
    print(f"B1 : {B1}\n")

    print(f"A1 형상 : {A1.shape}")
    print(f"A1 : {A1}\n")