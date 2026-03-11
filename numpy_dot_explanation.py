# -*- coding: utf-8 -*-
import numpy as np

# =============================================================================
# Numpy dot 函数详解与示例
# =============================================================================
# dot(a, b) 函数根据输入数组的维度不同，执行的操作也大不相同。
# 下面我们将分几种情况详细解释。

print("=" * 50)
print("1. 两个一维数组（向量）的情况")
print("=" * 50)

# 如果 a 和 b 都是一维数组，dot 执行的是向量点积（内积）。
# 也就是对应元素相乘，然后求和。
# 公式: sum(a[i] * b[i])

vec_a = np.array([1, 2, 3])
vec_b = np.array([4, 5, 6])

# 计算: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
dot_1d = np.dot(vec_a, vec_b)
print(f"向量 a: {vec_a}")
print(f"向量 b: {vec_b}")
print(f"np.dot(a, b) 结果: {dot_1d}")
print("-" * 30)


print("\n" + "=" * 50)
print("2. 二维数组（矩阵）的情况")
print("=" * 50)

# 如果 a 和 b 都是二维数组，dot 执行的是标准的矩阵乘法。
# 要求: a 的列数 (a.shape[1]) 必须等于 b 的行数 (b.shape[0])。
# 结果形状: (a.shape[0], b.shape[1])

mat_a = np.array([[1, 2], [3, 4]])  # 形状 (2, 2)
mat_b = np.array([[5, 6], [7, 8]])  # 形状 (2, 2)

# 计算过程 (以第一行第一列为例): 1*5 + 2*7 = 19
dot_2d = np.dot(mat_a, mat_b)
print(f"矩阵 a:\n{mat_a}")
print(f"矩阵 b:\n{mat_b}")
print(f"np.dot(a, b) 结果:\n{dot_2d}")
print("-" * 30)


print("\n" + "=" * 50)
print("3. 高维数组的情况 (N > 2)")
print("=" * 50)

# 这是最容易混淆的地方。np.dot 在高维时的规则如下：
# 规则: 它是 a 的“最后一个轴”与 b 的“倒数第二个轴”的乘积和。
# 
# 假设:
# a 的形状是 (..., M)
# b 的形状是 (..., M, K)  (注意这里倒数第二维是 M，用于匹配 a 的最后一维)
#
# 为了更清晰，让我们看一个具体的例子。
# 场景: 图像处理中可能遇到 (batch, height, width, channels)
# 为了演示简单，我们用较小的维度。

# 例子 1: (3, 4, 2) dot (2, 5)
# analysis:
# a.shape = (3, 4, 2) -> 最后一个轴大小是 2
# b.shape = (2, 5)    -> 倒数第二个轴大小是 2 (对于2D数组，行就是倒数第二轴)
# 匹配成功！
# 结果形状:
# 取 a 的前部分 (3, 4) + 取 b 的剩余部分 (5) -> 结果 (3, 4, 5)

print("--- 例子 3.1: (3, 4, 2) dot (2, 5) ---")
high_dim_a = np.ones((3, 4, 2))
high_dim_b = np.ones((2, 5))

res_3_1 = np.dot(high_dim_a, high_dim_b)
print(f"a 的形状: {high_dim_a.shape}")
print(f"b 的形状: {high_dim_b.shape}")
print(f"结果的形状: {res_3_1.shape}") 
# 解释: 结果相当于在每个 (3, 4) 的位置上，都做了一次 (2,) dot (2,5) 的运算。


# 例子 2: (2, 3, 4) dot (3, 4, 2) -> 注意这里会产生怎样的结果？
# analysis:
# a.shape = (2, 3, 4) -> 最后一维是 4
# b.shape = (3, 4, 2) -> 倒数第二维是 4
# 匹配成功！
# 结果形状:
# a的前面部分 (2, 3) + b的除倒数第二维外的部分 (3, 2) -> 结果 (2, 3, 3, 2)
# !!! 注意 !!! 
# np.dot 不会自动进行“广播”(broadcasting) 来对齐前面的维度 (比如这里的 3 和 3)。
# 它会把 b 的所有前面维度都保留下来。这是 np.dot 与 np.matmul (@) 的关键区别。

print("\n--- 例子 3.2: (2, 3, 4) dot (3, 4, 2) ---")
try:
    arr_a = np.random.randint(0, 10, (2, 3, 4))
    arr_b = np.random.randint(0, 10, (3, 4, 2))
    
    res_3_2 = np.dot(arr_a, arr_b)
    
    print(f"a 的形状: {arr_a.shape}")
    print(f"b 的形状: {arr_b.shape}")
    print(f"结果的形状: {res_3_2.shape}")
    print("解释: 结果维度是 (2, 3) + (3, 2) = (2, 3, 3, 2)")
    print("np.dot 并没有把中间的维度 3 进行对齐广播，而是全部堆叠了。")
    
except Exception as e:
    print(e)


print("\n" + "=" * 50)
print("4. 对比 np.matmul (或者 @ 运算符)")
print("=" * 50)

# 如果你期望的是像线性代数那样，前面的维度作为“批次”(batch) 进行广播，
# 而只在最后两个维度进行矩阵乘法，那你应该使用 np.matmul 或 @ 符号。

print("--- 对比: 使用 matmul 处理 (2, 3, 4) @ (2, 3, 4, 2) ---")
# 假设我们有两个 batch 的数据
# a: (2, 3, 4)  -> 意思是 2个 (3, 4) 的矩阵 (其实这不太准确，广播规则更灵活)
# 让我们构造一个标准的 batch matmul 例子
# a: (10, 3, 4) -> 10个 3x4 矩阵
# b: (10, 4, 5) -> 10个 4x5 矩阵

batch_a = np.ones((10, 3, 4))
batch_b = np.ones((10, 4, 5))

# 使用 dot
res_dot = np.dot(batch_a, batch_b)
# 形状: (10, 3) + (10, 5) -> (10, 3, 10, 5)
print(f"np.dot(a, b) 形状: {res_dot.shape} -> 维度通过笛卡尔积式堆叠")

# 使用 matmul (@)
# 规则: 前面的维度 (10) 视为 batch，进行广播对齐。
# 只对最后两维 (3, 4) 和 (4, 5) 做乘法。
res_matmul = np.matmul(batch_a, batch_b)
# 或者 res_matmul = batch_a @ batch_b
print(f"np.matmul(a, b) 形状: {res_matmul.shape} -> 维度进行了广播 (Batch MatMul)")


print("\n" + "=" * 50)
print("总结")
print("=" * 50)
# 1. 1D dot 1D -> 标量
# 2. 2D dot 2D -> 矩阵乘法
# 3. N-D dot M-D -> Sum product over last axis of a and second-to-last axis of b.
#    a 的 shape[:-1] + b 的 shape[:-2] + b 的 shape[-1]
# 4. 如果需要 Batch 矩阵乘法 (广播)，请使用 np.matmul 或 @，不要用 np.dot。
