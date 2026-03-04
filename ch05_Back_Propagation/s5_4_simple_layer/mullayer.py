# 5.4.2 곱셈 계층

class MulLayer :
    def __init__(self) :
        self.x = None
        self.y = None

    def forward(self, x, y) :
        self.x = x
        self.y = y
        out = x * y

        return out
    
    def backward(self, dout) :
        dx = dout * self.y
        dy = dout * self.x
        
        return dx, dy
    

if __name__ == "__main__" :
    apple = 100
    apple_num = 2
    tax = 1.1

    print(f"사과 가격 : {apple} | 사과 개수 : {apple_num} | 소비세 : {tax}")

    # 계층들
    mul_apple_layer = MulLayer()
    mul_tax_layer = MulLayer()

    # 순전파
    apple_price = mul_apple_layer.forward(apple, apple_num)
    price = mul_tax_layer.forward(apple_price, tax)

    print(f"최종 가격 : {price}\n")

    # 역전파
    dprice = 1
    dapple_price, dtax = mul_tax_layer.backward(dprice)
    dapple, dapple_num = mul_apple_layer.backward(dapple_price)

    print(f"dapple : {dapple} | dapple_num : {dapple_num} | dtax : {dtax}")
