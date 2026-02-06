# 3.3.1 다차원 배열

import numpy as np

A = np.array([1, 2, 3, 4])
B = np.array([[1,2],[3,4],[5,6]])

if __name__ == "__main__" :
    print(f"A : {A}")
    print(f"A의 차원 : {np.ndim(A)} ")
    print(f"A의 형상 : {A.shape}")
    print(f"A의 인덱스0 형상 : {A.shape[0]}\n")
    
    print(f"B : {B}")
    print(f"B의 차원 : {np.ndim(B)} ")
    print(f"B의 형상 : {B.shape}")
    print(f"B의 인덱스0 형상 : {B.shape[0]}\n")