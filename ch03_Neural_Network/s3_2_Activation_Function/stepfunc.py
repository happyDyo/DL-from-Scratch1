# 예제 3.2.2 계단함수 구현하기
import numpy as np

def step_function(x) :
    x = np.array(x)
    y = x > 0
    return y.astype(int)

if __name__ == "__main__" :
    print(f"-1 을 계단함수에 넣은 결과 : {step_function(-1)}")
    print(f"1 을 계단함수에 넣은 결과 : {step_function(1)}")