# 3.5.2 개선된 소프트맥스 함수

import numpy as np

RED   = "\033[91m"  # 빨간색 (위험!)
BOLD  = "\033[1m"   # 굵게
RESET = "\033[0m"   # 색상 초기화 (이걸 안 하면 뒤에 글자도 다 빨개짐)


def softmax(a) :
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)

    return exp_a / sum_exp_a

def isoftmax(a) :
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)

    return exp_a / sum_exp_a

if __name__ == "__main__" :
    np.seterr(all = 'raise')
    try :
        a = np.array([1010, 1000, 990])

        print(f"\n==== 이론적 softmax ====\n")
        print(f"a : {a}")
        print(f"softmax(a) : {softmax(a)}")
    except Exception as e :
        print(f"\n🚨{RED}{BOLD} 에러 발생 !! {RESET}\n")
        print(f"{RED}에러 종류 : {type(e).__name__}")
        print(f"에러 내용 : {e}{RESET}\n\n")

    print(f"==== 개선된 softmax ====\n")
    print(f"a : {a}")
    print(f"isoftmax(a) : {isoftmax(a)}\n")



