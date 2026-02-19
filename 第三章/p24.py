import numpy as np
a = np.array([1, 2, 3])
print(a)
print(a.size)
print(a.shape)
print(a.dtype)

b = np.array([1,2,3,4], dtype="uint8")
print(b)
print(b.dtype)
c = np.array([1,2,3,4], dtype="float32")

d = np.array([[1,2,3],
              [4,5]])
print(d.shape)
# print(d)  # This will raise an error because the inner lists have different lengths
d1 = np.array([[1,2,3],
               [4,5,6]])
print(d1.shape)