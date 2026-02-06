# 3.3.2 행렬의 곱

import numpy as np

RED   = "\033[91m"  # 빨간색 (위험!)
BOLD  = "\033[1m"   # 굵게
RESET = "\033[0m"   # 색상 초기화 (이걸 안 하면 뒤에 글자도 다 빨개짐)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

C = np.array([[1,2,3],[4,5,6]])
D = np.array([[1,2],[3,4],[5,6]])

E = np.array([1,2])

if __name__ == "__main__" :
    print(f"====== 행렬의 곱 예시 ======\n")
    print(f"A : {A}")
    print(f"B : {B}")
    print(f"A ∙ B : {np.dot(A,B)}\n")

    print(f"====== 형상이 다른 행렬곱 ======\n")
    print(f"C : {C}")
    print(f"D : {D}")
    print(f"C ∙ D : {np.dot(C,D)}\n")

    print(f"====== 잘못된 예시 ======\n")
    print(f"A : {A}")
    print(f"D : {D}")
    try :
        print(f"A ∙ D : {np.dot(A,D)}\n")
    except Exception as e:
        print(f"\n🚨 {RED}{BOLD}에러 발생!!{RESET}")
        print(f"{RED}에러 종류 : {type(e).__name__}")
        print(f"에러 내용 : {e}{RESET}\n")
    
    print(f"====== 행렬과 배열 곱 ======\n")
    print(f"A : {A}")
    print(f"E : {E}")
    print(f"A ∙ E : {np.dot(A,E)}\n")

    

