# MNIST 데이터셋

from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten = True, normalize = False)


print(f"x_train : {x_train.shape}")
print(f"t_train : {t_train.shape}")
print(f"x_test : {x_test.shape}")
print(f"t_test : {t_test.shape}")

