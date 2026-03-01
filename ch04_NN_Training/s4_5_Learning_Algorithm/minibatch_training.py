# 4.5.2 미니배치 학습 구현하기

import numpy as np
from dataset.mnist import load_mnist
from ch04_NN_Training.s4_5_Learning_Algorithm.two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

# 하이퍼 파라미터
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
trial = 0

print(f"x_train = {x_train.shape}")
print(f"t_train = {t_train.shape}")

network = TwoLayerNet(input_size = 784, hidden_size=50, output_size=10)

for i in range(iters_num) :
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 기울기 계산
    grad = network.numerical_gradient(x_batch, t_batch)

    # 매개변수 갱신
    for key in ('W1', 'b1', 'W2', 'b2') :
        network.params[key] -= learning_rate * grad[key]

    # 학습 경과 기록
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    trial += 1

    print(f"{trial}번째 학습 완료, loss = {loss}")



