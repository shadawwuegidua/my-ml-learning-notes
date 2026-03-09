import numpy as np
b = np.zeros((3,4), dtype="uint8")
c = np.zeros((3,4), dtype=np.uint8)
# zeros的dtype参数可以是字符串，也可以是numpy的类型对象，还可以是Python的原生类型，如int、float等。
print(b)
print()
print(b[1])
print()
print(c)

print("-" * 20)
# 1. 并没有 twos() 或 hundreds()，但可以使用 np.full() 创建指定值的数组
d = np.full((3, 4), 2, dtype=np.int16)  # 创建全为 2 的数组
e = np.full((3, 4), 100, dtype=np.int16) # 创建全为 100 的数组
print("np.full 创建的 twos:\n", d)
print("np.full 创建的 hundreds:\n", e)

print("-" * 20)
# 2. 展示 order='C' (行优先, C语言风格) vs order='F' (列优先, Fortran风格) 的区别
# 注意：由于 zeors/ones 元素值都一样，直接打印看不出区别，需要看内存步幅(strides)
f_c = np.ones((2, 3), order='C', dtype=np.int8)
f_f = np.ones((2, 3), order='F', dtype=np.int8)
print("Order='C' 的数组:\n", f_c)
print("Order='C' 的步幅 (strides):", f_c.strides) 
# (3, 1) -> 跨越一行需要走3个字节(3列*1字节)，跨越一列只需要走1个字节。说明数据是按行连续存储的。
print("Order='F' 的数组:\n", f_f)

print("Order='F' 的步幅 (strides):", f_f.strides)
# (1, 2) -> 跨越一行只需要走1个字节，跨越一列需要走2个字节(2行*1字节)。说明数据是按列连续存储的。

