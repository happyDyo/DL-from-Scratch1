import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet :
    def __init__(self) :
        self.W = np.random.randn(2,3)       # 초기 가중치를 적당히 설정

    def predict(self, x) :
        return np.dot(x, self.W)
    
    def loss(self, x, t) :
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss
    
if __name__ == "__main__" :
    net = simpleNet()
    print(f"net 생성 완료.\n")

    print(f"net 가중치")
    print(f"{net.W}\n")

    x = np.array([0.6, 0.9])
    print(f"입력 데이터 x : {x}\n")

    p = net.predict(x)
    print(f"예측값 p : {p}")
    print(f"유력 후보 인덱스 : {np.argmax(p)}\n")

    t = np.array([0, 0, 1])
    print(f"정답 레이블 : {t}\n")

    print(f"손실함수 값 : {net.loss(x, t)}\n")


    # def f(W) :
    #     return net.loss(x, t)

    f = lambda w : net.loss(x, t)
    
    dW = numerical_gradient(f, net.W)
    print(f"dw 값 :")
    print(f"{dW}")




