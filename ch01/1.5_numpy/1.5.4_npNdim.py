import numpy as np

A = np.array([[1,2],[3,4]])

print(A)
print(A.shape)
print(A.dtype)

# 행렬 산술연산
B = np.array([[3,0],[0,6]])
print(f"A + B = {A+B}")
print(f"A * B = {A*B}")

# 브로드캐스트
print(f"A = {A}")
print(f"A / 2 = {A/2}")