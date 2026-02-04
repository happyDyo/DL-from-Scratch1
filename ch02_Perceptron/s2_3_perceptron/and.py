
def AND(x1, x2) :
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp > theta :
        return 1
    else :
        return 0
    
print("AND 연산자를 만들었습니다.")
print(f"AND(0, 0) : {AND(0, 0)}")
print(f"AND(0, 1) : {AND(0, 1)}")
print(f"AND(1, 0) : {AND(1, 0)}")
print(f"AND(1, 1) : {AND(1, 1)}")
