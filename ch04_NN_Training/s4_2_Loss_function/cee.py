# 4.2.2 교차 엔트로피 오차

import numpy as np

def cross_entropy_error(y, t) :
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

if __name__ == "__main__" :
    t = [0,0,1,0,0,0,0,0,0,0]
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    r1 = cross_entropy_error(np.array(y), np.array(t))

    y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    r2 = cross_entropy_error(np.array(y), np.array(t))

    print(f"정답은 2 입니다.")
    print(f"2라고 추정했을 때 교차엔트로피오차 : {r1}")
    print(f"7이라고 추정했을 때 교차엔트로피오차 : {r2}")
