# 4.5.1 예제

from ch04_NN_Training.s4_5_Learning_Algorithm.two_layer_net import TwoLayerNet

if __name__ == "__main__" :
    print(f"net 생성\n")
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

    print(f"W1 형상 : {net.params['W1'].shape}")
    print(f"b1 형상 : {net.params['b1'].shape}")
    print(f"W2 형상 : {net.params['W2'].shape}")
    print(f"b2 형상 : {net.params['b2'].shape}")

