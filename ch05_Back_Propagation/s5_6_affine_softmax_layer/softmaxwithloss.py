# 5.6.3 Softmax-with-Loss 계층

from ch03_Neural_Network.s3_5_OutputLayerDesign.softmax2 import isoftmax
from ch04_NN_Training.s4_2_Loss_function.cee2 import cross_entropy_error

class SoftmaxWithLoss :
    def __init__(self) :
        self.loss = None    # 손실함수
        self.y = None       # softmax의 출력
        self.t = None       # 정답 레이블(원-핫 벡터)

    def forward(self, x, t) :
        self.t = t
        self.y = isoftmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss
    
    def backward(self, dout = 1) :
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size     # 우리는 오차의 '평균'을 전달

        return dx