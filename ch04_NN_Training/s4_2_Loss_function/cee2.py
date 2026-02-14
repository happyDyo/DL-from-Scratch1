# 4.2.4 (배치용) 교차 엔트로피 오차 구현하기

import numpy as np

# 정답이 원-핫 인코딩 되어있을 때

def cross_entropy_error(y, t) :
    if y.ndim == 1 :
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

# 정답이 숫자 레이블로 주어졌을 때

def cross_entropy_error(y, t) :
    if y.ndim == 1 :
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size),t] + 1e-7)) / batch_size