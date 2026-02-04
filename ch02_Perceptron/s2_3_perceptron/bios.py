import numpy as np

x = np.array([0, 1])        # input
w = np.array([0.5, 0.5])    # weight
b = -0.7                    # bios

print(f"x * w = {x*w}")
print(f"총합 = {np.sum(x*w)}")
print(f"최종값 = {b + np.sum(x*w)}")
