# 4.4.1 경사 하강법 예제

from ch04_NN_Training.s4_4_Gradient.gradient_descent import gradient_descent
import numpy as np

def function_2(x) :
    return x[0]**2 + x[1]**2

if __name__ == "__main__" :
    init_x = np.array([-3.0, 4.0])
    print(f"초기 x : {init_x}\n")

    print(f"학습률 클 때, lr=10.0")         # 발산할 것
    final = gradient_descent(function_2, init_x, 10.0, 100)
    print(f"최소값의 좌표 : {final}")

    print(f"적당한 학습률, lr=0.1")         # 정확한 결과
    init_x = np.array([-3.0, 4.0])
    final = gradient_descent(function_2, init_x, 0.1, 100)
    print(f"최소값의 좌표 : {final}")

    print(f"학습률이 작을 때, lr=1e-10")    # 낮은 갱신률
    init_x = np.array([-3.0, 4.0])
    final = gradient_descent(function_2, init_x, 1e-10, 100)
    print(f"최소값의 좌표 : {final}")
