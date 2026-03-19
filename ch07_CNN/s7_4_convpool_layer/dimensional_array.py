# 7.4.1 4차원 배열

import numpy as np

x = np.random.rand(10, 1, 28, 28)

print(f"x의 형상 : {x.shape}")
print(f"x의 첫 번째 데이터 형상 : {x[0].shape}")
print(f"x의 첫 번째 데이터의 첫 채널 : {x[0][0]}")