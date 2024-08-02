import numpy as np

# 係数行列
A = np.array([[-2, 2, -5],
              [3, -4, 8],
              [-2, 6, -8]])

# 定数ベクトル
b = np.array([18, 24, 12])

# 方程式を解く
x = np.linalg.solve(A, b)

print("x =", x)