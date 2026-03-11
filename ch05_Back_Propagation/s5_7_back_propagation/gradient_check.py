# 5.7.3 오차역전파법으로 구한 기울기 검증하기

import numpy as np
from dataset.mnist import load_mnist
from ch05_Back_Propagation.s5_7_back_propagation.twolayernet import TwoLayerNet


# 데이터 읽기
(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size = 784, hidden_size = 50, output_size = 10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)


# 각 가중치의 차이의 절댓값을 구한 후, 그 절댓값들의 평균을 낸다.
for key in grad_numerical.keys() :
    diff = np.average(np.abs(grad_backprop[key] - grad_numerical[key]))
    print(f"{key} : {str(diff)}")