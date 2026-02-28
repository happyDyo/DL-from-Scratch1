# 4.5.1 예제

from ch04_NN_Training.s4_5_Learning_Algorithm.two_layer_net import TwoLayerNet
import numpy as np

if __name__ == "__main__" :
    print(f"net 생성\n")
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

    print(f"W1 형상 : {net.params['W1'].shape}")
    print(f"b1 형상 : {net.params['b1'].shape}")
    print(f"W2 형상 : {net.params['W2'].shape}")
    print(f"b2 형상 : {net.params['b2'].shape}")

    x = np.random.rand(100, 784)            # 더미 입력 데이터(100장 분량)
    y = net.predict(x)
    print(f"입력 x의 형상 : {x.shape}")
    print(f"예측 y의 형상 : {y.shape}")

    t = np.random.rand(100, 10)             # 더미 정답 레이블(100장 분량)
    print(f"정답 t의 형상 : {t.shape}")
    
    print(f"\n\n가중치 기울기 계산 시작")
    grads = net.numerical_gradient(x, t)
    print(f"W1 의 기울기 형상 : {grads['W1'].shape}")
    print(f"b1 의 기울기 형상 : {grads['b1'].shape}")
    print(f"W2 의 기울기 형상 : {grads['W2'].shape}")
    print(f"b2 의 기울기 형상 : {grads['b2'].shape}")

