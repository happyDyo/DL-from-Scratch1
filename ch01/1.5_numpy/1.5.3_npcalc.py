import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# 브로드캐스트
x = np.array([1.0, 2.0, 3.0])

print(x/2)