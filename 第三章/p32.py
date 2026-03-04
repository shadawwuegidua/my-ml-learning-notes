"""算子和广播"""
import numpy as np
a = np.arange(5)
print(a)
b = np.arange(5)[::-1]

# === 切片紧跟 arange (链式调用) 原理讲解 ===
# numpy.arange(5)[::-1]
# 这种写法是 Python 的 "链式调用" (Chaining)。
# 
# 1. 并没有一个单独的函数叫 arange()[::-1]。
# 2. **执行顺序是从左到右**：
#    a. 第一步：先执行 `np.arange(5)`，生成一个临时的 ndarray 数组 [0, 1, 2, 3, 4]。
#    b. 第二步：立刻对这个临时数组执行切片操作 `[::-1]`（倒序）。
#    c. 第三步：将切片后的结果赋值给变量 b。
# 
# 这不仅适用于切片，也适用于 reshape 等其他数组方法：
# e.g. np.arange(9).reshape(3, 3)[::2]
print("\n--- 链式切片示例 ---")
print("np.arange(5)[::-1] ->", np.arange(5)[::-1])
print("np.arange(10)[2:8:2] ->", np.arange(10)[2:8:2])

print(a + b)
print(a * 3.14)
print(a * b)
print(a - b)
print(a / (b + 1))  # 注意这里加1是为了避免除以0的情况
print(a // (b + 1))  # 整除
print(a ** 2)   
# 在numpy中，使用标量（如3.14）与数组进行运算时，NumPy会自动将标量广播到数组的每个元素上进行运算。
# 这就是所谓的广播机制（Broadcasting），它允许不同形状的数组进行算术运算，而无需显式地复制数据。
print(a > 2)

print("--- 广播机制示例 ---")
a = np.arange(5)
b = np.arange(25).reshape((5 , 5))
print(a)
print(b)
print()
print(a * b)
print(a + b)
# 当我们执行 a * b 或 a + b 时，NumPy 会自动将一维数组 a 广播到二维数组 b 的每一行上进行运算。
# 这就是广播机制的强大之处，它使得我们可以轻松地对不同形状的数组进行算术运算，而不需要手动调整它们的形状或复制数据。