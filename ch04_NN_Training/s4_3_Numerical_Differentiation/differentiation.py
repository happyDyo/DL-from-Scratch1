# 4.3.1 미분

# 나쁜 구현 예시
def numerical_diff(f, x) :
    h = 1e-50
    return (f(x+h) - f(x)) / h

# 개선 예시
def numerical_diff(f, x) :
    h = 1e-4            # 반올림 오차 개선, 보편적으로 1e-4 정도의 값이 좋은 결과를 얻는다고 알려져있음.
    return (f(x+h) - f(x-h)) / h    # 중심 차분 혹은 중앙 차분을 통해 오차 줄이자.