import numpy as np
x = np.zeros((2,3,4))
print(x)
# 假设 shape = (d0, d1, d2, d3)：

# Axis 0 (d0)：最外层的“块”或“组”的数量。
# Axis 1 (d1)：每个“块”里面包含的下一级子结构的数量。
# ...
# Axis -1 (最后一个)：最内层、也最基础的元素（通常指一行里的列数）。

# 假设有一个 shape 为 (2, 3, 4) 的数组。
# 你可以把它理解为 2 个大小为 3x4 的矩阵叠在一起。
x = np.ones((2,3,4),dtype = "uint32")
print(x)

y = 10 * np.ones((2,3,4))
print(y)
print(y.dtype)
y = y.astype("uint8")
print(y)
print(y.dtype)

"""
Python中列表和字典对象是通过引用传递的，将一个对象赋值给另一个变量时，
实际上是创建了一个新的引用，而不是复制对象本身。"""

a = np.arange(10)
print(a)
b = a
print(b)
b[0] = 100
c = a.copy()
d = a.view()
e = a[:]
print(a)
# 可以看到更改b[0]的值会影响a，因为b和a引用同一个数组对象。
# 但是更改c[0]的值不会影响a，因为c是a的一个独立副本。
c[0] = 200
print(a)
# 更改d[0]的值会影响a，因为d是a的一个视图，它与a共享数据。
d[0] = 300
print(a)
# 更改e[0]的值会影响a，因为e是a的一个切片，它与a共享数据。
e[0] = 400
print(a)