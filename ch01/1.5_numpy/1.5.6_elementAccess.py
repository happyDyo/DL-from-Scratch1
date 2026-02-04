import numpy as np

#원소 접근

X = np.array([[51, 55], [14, 19], [0, 4]])

print(f"X = {X}")
print(f"X[0] = {X[0]}")
print(f"X[0][1] = {X[0][1]}")


#for문 활용

for row in X :
    print(row)


# flatten() 활용

X = X.flatten()
print(f"평탄화된 X = {X}")
print(f"0, 2, 4 원소 값 : {X[np.array([0,2,4])]}")

# Y = {}
# for i in X :
#     Y[i] = i>15
# print(f"15보다 큰가? : {Y}")

# 딕셔너리 컴프리헨션 사용
Y = {i : i>15 for i in X}
print(f"Y보다 큰가? : {Y}")