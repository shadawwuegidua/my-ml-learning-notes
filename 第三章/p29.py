import numpy as np
a = np.arange(10)
print(a)
print(a[1:4])
print(a[0:8:2])
print(a[3:7:2])
print(a[:6])
print(a[5:])
print(a[-1])
print(a[-3:-1])
print(a[::-1])
print("--- 多维数组切片 ---")
b = np.arange(20).reshape(4,5)
print(b)
print() 
print(b[1:3, : ])
# 逗号前面是一个切片，就是1:3，代表第1，2个索引
# 逗号后面代表列的切片，这里是冒号，代表所有列
print()
print(b[2:, 2: ])

# === numpy.arange() 基本语法 ===
start = 0
stop = 10
step = 1
dtype = None
example = np.arange(start, stop, step, dtype=dtype)
print(example)
# start: 起始值（包含），默认为0
# stop: 结束值（不包含），必须提供
# step: 步长（两个相邻数值的差），默认为1
# dtype: 数组的数据类型

print("\n--- numpy.arange() 示例 ---")
# 1. 只指定 stop (默认 start=0, step=1)
print("np.arange(5):", np.arange(5))

# 2. 指定 start 和 stop (默认 step=1)
print("np.arange(3, 9):", np.arange(3, 9))

# 3. 指定 start, stop 和 step
print("np.arange(1, 10, 2):", np.arange(1, 10, 2))

# 4. 使用负数步长（倒序）
print("np.arange(10, 0, -2):", np.arange(10, 0, -2))

# 5. 使用浮点数步长（推荐使用 np.linspace 替代）
print("np.arange(0, 1.6, 0.5):", np.arange(0, 1.6, 0.5))

# === numpy.reshape() 基本语法 ===
# numpy.reshape(a, newshape, order='C') 
# 或者作为数组方法: ndarray.reshape(shape, order='C')
# newshape: 新的形状，必须与原数组元素总数相同！
#           可以是一个整数（退化为一维），或一个整数元组（如 (3, 4)）。
#           **特殊用法**：如果某一个维度指定为 -1，NumPy 会自动根据总元素个数和其他维度计算出这个维度的长度。
# order: 读取元素的顺序，'C'（C风格，按列），'F'（Fortran风格，按行），'A'，默认是 'C'。

print("\n--- numpy.reshape() 示例 ---")
# 创建一个包含 12 个元素的 1D 数组
c = np.arange(12)
print("原始数组 c:", c)

# 1. 1D 转换为 2D (例如：3行4列)
print("\n1. 转换为 3x4 的二维数组:")
print(c.reshape(3, 4))
# 或者用 np.reshape(c, (3, 4))

# 2. 1D 转换为 3D (例如：包含 2 个 2x3 的矩阵)
print("\n2. 转换为 2x2x3 的三维数组:")
print(c.reshape(2, 2, 3))

# 3. 使用 -1 自动推断维度
# 想把 c 变成 4 行，但不关心多少列（让 NumPy 自己算）
print("\n3. 使用 -1 自动计算列数 (4行，自动推断列):")
print(c.reshape(4, -1))

# 4. 将多维数组重新展平为一维
d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n4. 原始二维数组 d:")
print(d)
print("   使用 reshape(-1) 展平为一维:")
print(d.reshape(-1))