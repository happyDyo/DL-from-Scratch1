# 3.3.3 신경망에서의 행렬곱

import numpy as np

X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])

if __name__ == "__main__" :
    print(f"X : {X}")
    print(f"W : {W}")
    print(f"Y : {np.dot(X,W)}")