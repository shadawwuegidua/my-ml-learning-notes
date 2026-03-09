import numpy as np
from PIL import Image
from sklearn.datasets import load_sample_images

# load_sample_images 是 scikit-learn (sklearn) 提供的一个内置函数。
# 它用于加载一组标准的测试图像（sklearn内置了包含一张中国风景照和一张花朵照的数据集）。
# 它常用于图像处理、计算机视觉或者机器学习算法的测试示例。
# 
# 是的，调用 .images[0] 和 .images[1] 后，获取到的 china 和 flower 直接就是 NumPy 数组 (ndarray)。
# 这个 NumPy 数组中保存的是图像的像素矩阵，通常形状(shape)为 (高度, 宽度, 3)，其中的3代表RGB三个颜色通道。
china = load_sample_images().images[0]
flower = load_sample_images().images[1]

# 打印图像 numpy 数组的形状 (例如可能是 427x640 像素，3个通道)
print("china shape:", china.shape)
print("flower shape:", flower.shape)

# Image.fromarray() 是 PIL (Pillow) 库中的一个重要函数。
# 由于通过 sklearn 加载出来的是 numpy 数组，Pillow 无法直接显示和保存数组，
# 所以需要用这个函数将 numpy 数组"反转"回 PIL 的 Image 图片对象。
imChina = Image.fromarray(china)
imFlower = Image.fromarray(flower)

# .show() 会调用操作系统自带的默认图片浏览器来弹出并显示这几张图片。
imChina.show()
imFlower.show()

# .save() 作用是将内存中的 PIL 图片对象写入到本地磁盘中。
# 它会根据你给定的文件名后缀（这里是 .jpg）自动决定图片的编码保存格式。
imChina.save("china.jpg")
imFlower.save("flower.jpg") 

# Image.open() 则是读取操作，从本地磁盘读取指定的图片文件，解析为一个 PIL 的 Image 对象。
im = Image.open("china.jpg")
im.show()

# --- 关于修改 numpy shape 和灰度化 ---
# 1. shape 确实是一个 tuple (元组)。但你不能直接通过改变 shape 从 3 改成 1 或 2 来实现灰度化。
#    这是因为 numpy 数组的总像素数据量是不变的 (高度 * 宽度 * 3)。如果强行更改 shape，会导致数据对齐错乱，甚至报错。
# 2. 灰度图不是 2 个通道，而是 1 个通道（或者干脆去掉了最后一个维度，变成了二维数组：高度 * 宽度）。
# 3. 真正的灰度化需要将 RGB 三个通道的数值按照一定的权重（如常用的心理学公式：R*0.299 + G*0.587 + B*0.114）进行数学计算或者求平均。

# 下面演示如何直接使用 numpy 的矩阵运算，把 numpy 数组（china）转成灰度图：
import numpy as np

# ---------------- 详细切片与 dot 函数复习 ----------------
# 1. 切片复习： china[..., :3]
#    - `china` 的 shape 是 (高度, 宽度, 通道数)，比如通道数通常是 3 (RGB) 或 4 (RGBA 包含了 Alpha 透明度通道)。
#    - `...` (Ellipsis 省略号)：代表前面所有的维度完全保留。在这里等价于 `:, :`，也就是保留所有的行和列（即所有像素点的位置）。
#    - `:3` ：指的是最后一个维度（颜色通道）的切片，表示取索引 0、1、2 这前三个元素。
#      这就确保了哪怕原图是带透明度的 RGBA 四通道图像，我们也只取出 R, G, B 这三个通道参与计算。
#    - 因此，`china[..., :3]` 提取出来的是一个形状依然为 (高, 宽, 3) 的、只包含 RGB 三色的部分。
#
# 2. dot 函数复习： np.dot(A, B)
#    - `np.dot` 是矩阵点积操作。在这里，A 是形状为 (高, 宽, 3) 的 NumPy 数组，B 是一维的权重数组 [0.2989, 0.5870, 0.1140]。
#    - 当多维数组（A）和一维数组（B）进行 dot 运算时，NumPy 会自动将 A 的**最后一个维度**的每一个元素，与 B 的元素进行一一对应的相乘并相加。
#    - 相当于对图像中的每一个独立的像素点 (R, G, B)，都自动执行了这个算术运算： R*0.2989 + G*0.5870 + B*0.1140。
#    - 结果：原本是 (高, 宽, 3) 的三维数组，因为第三个维度被点积“消化并合并”求和成了一个数值，最后直接变成了一个形状为 (高, 宽) 的二维数组，也就是我们需要的灰度图。
# --------------------------------------------------------

# 按照灰度公式 Y = 0.2989*R + 0.5870*G + 0.1140*B 计算
gray_china_array = np.dot(china[..., :3], [0.2989, 0.5870, 0.1140])
print("纯 numpy 计算后的灰度图 shape:", gray_china_array.shape) # 结果会是没有通道数的 (height, width) 二维数组

# 可以将 numpy 灰度数组再转回 PIL Image 并显示
Image.fromarray(gray_china_array.astype(np.uint8)).show()


img = np.array(im)
print("从 china.jpg 重新加载的图像数组形状:", img.shape)
# 通过 Image.open() 重新加载的图像文件，经过 PIL 解析后，得到的 img 仍然是一个 NumPy 数组，形状和原来加载的 china 数组应该是一样的 (427, 640, 3)，其中包含了图像的像素数据。    
gray = im.convert("L")  # 转换为灰度图像
gray.show()

g = np.array(gray)
print("灰度图像数组形状:", g.shape)
print("灰度图像数组数据类型:", g.dtype)