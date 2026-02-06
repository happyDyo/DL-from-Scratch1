# 3.4.2 각 층의 신호 전달 구현하기

# 3층 신경망 구현
import numpy as np

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

def identity_function(x) :
    return x


X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X,W1) + B1
Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])
A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3], [0.2,0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2,W3) + B3
Y = identity_function(A3)


if __name__ == "__main__" :
    print(f"\n==== 입력층 부터 1층 연산 ====")
    print(f"X : {X}\n")
    print(f"W1 : {W1}\n")
    print(f"B1 : {B1}\n")
    print(f"A1 : {A1}\n")
    print(f"Z1 : {Z1}\n\n")

    print(f"==== 1층 부터 2층 연산 ====")
    print(f"W2 : {W2}\n")
    print(f"B2 : {B2}\n")
    print(f"A2 : {A2}\n")
    print(f"Z2 : {Z2}\n\n")
    
    print(f"==== 2층 부터 출력층 연산 ====")
    print(f"W3 : {W3}\n")
    print(f"B3 : {B3}\n")
    print(f"A3 : {A3}\n")
    print(f"Y : {Y}\n\n")