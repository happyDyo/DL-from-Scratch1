import numpy as np

def AND(x1, x2) :
    x = np.array([x1, x2])      # input
    w = np.array([0.5, 0.5])    # weight
    b = -0.7                    # bios
    
    tmp = b + np.sum(x*w)
    if tmp > 0 :
        return 1
    else :
        return 0
    
def NAND(x1, x2) :
    x = np.array([x1, x2])      # input
    w = np.array([0.5, 0.5])    # weight
    b = -0.7                    # bios
    
    tmp = b + np.sum(x*w)
    if tmp > 0 :
        return 0
    else :
        return 1
    

def OR(x1, x2) :
    x = np.array([x1, x2])      # input
    w = np.array([0.5, 0.5])    # weight
    b = -0.4                    # bios
    
    tmp = b + np.sum(x*w)
    if tmp > 0 :
        return 1
    else :
        return 0
    
if __name__ == "__main__" :
    print("\n연산 결과\n")
    #AND 연산
    print(f"AND(0,0) = {AND(0,0)}")
    print(f"AND(1,0) = {AND(1,0)}")
    print(f"AND(0,1) = {AND(0,1)}")
    print(f"AND(1,1) = {AND(1,1)}\n")

    #NAND 연산
    print(f"NAND(0,0) = {NAND(0,0)}")
    print(f"NAND(1,0) = {NAND(1,0)}")
    print(f"NAND(0,1) = {NAND(0,1)}")
    print(f"NAND(1,1) = {NAND(1,1)}\n")

    #OR 연산
    print(f"OR(0,0) = {OR(0,0)}")
    print(f"OR(1,0) = {OR(1,0)}")
    print(f"OR(0,1) = {OR(0,1)}")
    print(f"OR(1,1) = {OR(1,1)}\n")