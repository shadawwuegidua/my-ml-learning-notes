import numpy as np

a = np.loadtxt("abc.txt")
print(a)

a = np.loadtxt("abc_tab.txt")
print(a)

a = np.loadtxt("abc.csv", delimiter=",")
# a1 = np.loadtxt("abc.csv")
print(a)
# print(a1)
# 注意：如果我们不指定delimiter参数，loadtext会默认使用空格作为分隔符，这可能会导致解析错误，尤其是当数据文件使用了其他分隔符（如制表符或逗号）时。
# 因此，在使用loadtext读取数据时，务必根据文件的实际格式正确设置delimiter参数，以确保数据被正确解析成NumPy数组。

# 这三个例子使用loadtext，它读取文本文件并从中产生NumPy数组。
# 默认情况下，loadtext会将文件中的数据解析为浮点数，并且假设数据是以空格分隔的。
# 如果文件中的数据使用了不同的分隔符（如制表符或逗号），我们可以通过delimiter参数来指定正确的分隔符，以确保数据被正确解析成数组。

# 使用 np.save (而不是 savetxt) 将数组以二进制格式保存到 .npy 文件中
np.save("ABC.npy", a)
b = np.load("ABC.npy")
print("b:\n", b)
# 关于 .npy 文件格式的说明：
# .npy 文件是 NumPy 专用的二进制文件格式，用于存储单个 NumPy 数组。
# 它的主要优点包括：
# 1. 效率高：读写速度快，占用空间比文本文件（如 .txt, .csv）小。
# 2. 信息完整：保存了数组的形状（shape）、数据类型（dtype）等元数据，加载时无需重新指定。
# 3. 跨平台：可以在不同的操作系统和架构之间正确读取。
# 使用 np.load("ABC.npy") 可以重新读取该文件。

# --- np.save 和 np.load 函数详解 ---
# np.save(file, arr, allow_pickle=True, fix_imports=True)
# - 功能：将一个数组以 NumPy 的 .npy 二进制格式保存到磁盘文件中。
# - 参数 file: 文件名或文件对象。如果文件名没有 .npy 扩展名，会自动添加。
# - 参数 arr: 要保存的数组数据。
# - 示例：np.save("my_array.npy", my_array)

# np.load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
# - 功能：从 .npy, .npz 或 pickled 文件中加载数组或 pickled 对象。
# - 参数 file: 要读取的文件名或文件对象。
# - 这里的 .npy 格式包含了数组的形状(shape)和数据类型(dtype)信息，
#   所以读取时不需要像 loadtxt 那样指定分隔符或数据类型，它会自动还原出原模原样的数组。
# - 示例：loaded_array = np.load("my_array.npy")

# --- np.save 与 np.savetxt 的区别 ---
# 1. 存储格式不同：
#    - np.save: 使用 NumPy 专用的二进制格式 (.npy) 保存。
#      优点：读写速度快，文件体积小，保留数据类型和形状信息。
#      缺点：人类不可读，只能用 NumPy 读取。
#    - np.savetxt: 使用纯文本格式 (.txt, .csv) 保存。
#      优点：人类可读，通用性强，可以用 Excel 或其他文本编辑器打开。
#      缺点：读写速度慢，文件体积大，丢失精度和元数据（形状、类型）。

# --- np.savetxt 函数详解 ---
# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
# - 功能：将数组保存到文本文件中。
# - 参数 fname: 文件名。
# - 参数 X: 要保存的 1D 或 2D 数组。
# - 参数 fmt: 数据格式，例如 '%.2f' 保留两位小数，'%d' 为整数。
# - 参数 delimiter: 分隔符，例如 ',' 用于 CSV 文件。
# - 示例：np.savetxt("data.csv", my_array, delimiter=",", fmt="%.2f")
np.savetxt("ABC_savetxt.csv", b, delimiter=",", fmt="%.2f")