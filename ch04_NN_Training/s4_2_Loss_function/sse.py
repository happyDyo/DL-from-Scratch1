# 4.2.1 오차제곱합

import numpy as np

def sum_squares_error(y, t) :
    return 0.5 * np.sum((y - t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]   # 정답 2

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]   # 2 추정
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]   # 7 추정

print(f"정답은 2 입니다.")
print(f"2라고 추정했을 때 오차제곱합 : {sum_squares_error(np.array(y1), np.array(t))}")
print(f"7라고 추정했을 때 오차제곱합 : {sum_squares_error(np.array(y2), np.array(t))}")