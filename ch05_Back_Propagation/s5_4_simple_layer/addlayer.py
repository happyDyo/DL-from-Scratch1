# 덧셈 계층
from ch05_Back_Propagation.s5_4_simple_layer.mullayer import MulLayer


class AddLayer :
    def __init__(self) :
        pass

    def forward(self, x, y) :
        out = x + y
        return out
    
    def backward(self, dout) :
        dx = dout * 1
        dy = dout * 1
        return dx, dy
    

if __name__ == "__main__" :
    apple = 100
    apple_num = 2
    orange = 150
    orange_num = 3
    tax = 1.1


    # 계층들
    mul_apple_layer = MulLayer()
    mul_orange_layer = MulLayer()

    add_apple_orange_layer = AddLayer()

    mul_tax_layer = MulLayer()


    # 순전파
    apple_price = mul_apple_layer.forward(apple, apple_num)
    orange_price = mul_orange_layer.forward(orange, orange_num)

    all_price = add_apple_orange_layer.forward(apple_price, orange_price)

    price = mul_tax_layer.forward(all_price, tax)

    print(f"가격 : {price}\n")


    # 역전파
    dprice = 1
    dall_price, dtax = mul_tax_layer.backward(dprice)

    dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)

    dapple, dapple_num = mul_apple_layer.backward(dapple_price)
    dorange, dorange_num = mul_orange_layer.backward(dorange_price)

    print(f"dapple : {dapple} | dapple_num : {dapple_num} | dorange : {dorange} | dorange_num : {dorange_num} | dtax : {dtax}")
