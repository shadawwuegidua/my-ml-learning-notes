import numpy as np
example = np.arange(27).reshape(3, 3, 3)
print(example)
print()

example2 = np.ones((3,3))
print(np.ones((3,3)).dtype)
# 这里默认是 float64 类型的数组，如果需要整数类型，可以指定 dtype 参数：
example2 = np.ones((3,3), dtype=np.uint8)
print(example2)
print()

example[1, :, :] = example2
print(example)
# === 省略号 (...) 用法说明 ===
print("\n--- 省略号 (...) 用法示例 ---")
# 省略号 (Ellipsis) 在 NumPy 切片中无论是用 `...` 还是 `Ellipsis` 对象表示
# 它代表 "之前或之后所有的未指定维度"。
# 尤其在处理高维数组时非常方便，不需要数到底有多少个冒号。

# 下面三种写法是完全等价的：
# 1. 显式写出所有维度的冒号
print("\n1. 使用显式冒号切片 example[1, :, :]:")
print(example[1, :, :])

# 2. 使用省略号代替后面的维度
print("\n2. 使用省略号切片 example[1, ...]:")
print(example[1, ...])

# 3. 省略号也可以用在中间或前面
print("\n3. 取所有维度的第1列 example[..., 1]")
# 相当于 example[:, :, 1]
print(example[..., 1])

example[0, ...] = example2
print(example)