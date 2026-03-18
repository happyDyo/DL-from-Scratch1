# 6.5.1 검증 데이터

from dataset.mnist import load_mnist
from common.util import shuffle_dataset

(x_train, t_train), (x_test, t_test) = load_mnist()

# 훈련 데이터를 뒤섞는다.
x_train, t_train = shuffle_dataset(x_train, t_train)

# 20%를 검증 데이터로 분할
validation_rate = 0.20
validation_num = int(x_train.shape[0] * validation_rate)

x_val = x_train[ : validation_num]
t_val = t_train[ : validation_num]
x_train = x_train[validation_num : ]
t_train = t_train[validation_num : ] 