'''
import numpy as np
# 创建简单的列表
a = [1, 2, 3, 4]
# 将列表转换为数组
b = np.array(a)

#数组元素的个数
#b.size
#数组形状
#b.shape

#创建一个10行10列的浮点数为1的矩阵
array_one = np.ones([10, 10])
#创建一个10行10列的数值为0.的矩阵
array_zero = np.zeros([10, 10])

# 建立一个两列五行的矩阵
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# stus_score > 80
#每一列的最大值
result_axis0 = np.amax(stus_score, axis=0)
#每一行的最大值
result_axis1 = np.amax(stus_score, axis=1)

#所有数据都加上5
#stus_score+5

#矩阵乘法
x = np.array([[1., 2.], [4., 5.]])
y = np.array([[6., 23.], [-1, 7]])
#np.dot(x, y)  点乘
#np.linalg.inv(x) #求逆
#x.T  #转置
'''


# 1.Create a null vector of size 10
import numpy as np
array_zero = np.zeros([10, 1]) # creat a null column vector
print(array_zero) # check the value
print("\n")

# 2.Create a null vector of size 10 but the fifth value which is 1
array_zero[4] = 1
print(array_zero) # check the fifth value
print("\n")

# 3.Create a vector with values ranging from 10 to 49
array01 = np.zeros([40, 1])
a = 0
num01 = 10
while a < 40:
	array01[a] = num01
	num01 += 1
	a += 1
print(array01)  # check the matrix
# we get a column vector sized 40×1 and the elements inside range from 10 to 49
print("\n")

# 4. Create a 3x3 matrix with values ranging from 0 to 8
array02 = np.random.randint(0, 9, size = (3, 3))
print(array02)  # check the matrix
print("\n")

# 5. Create a 10x10 array with random values and find the minimum and maximum values
array03 = np.random.randint(0, 9, size = (10, 10))
print(array03) # print the matrix
print(array03.max()) # get the maximum value through the whole matrix
print(array03.min()) # get the minimum value through the whole matrix
print("\n")
print(array03.max(axis=0)) # get the maximum value from all columns
print("\n")

# 6. Create a 2d array with 1 on the border and 0 inside
array04 = np.ones([4, 3])
array04[1:-1, 1:-1] = 0  # 从第二行到倒数第二行以及第二列到倒数第二列填充0
print(array04)
print("\n")

# 7. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
array05 = np.random.randint(0, 9, size = (5, 3))
print("Matrix array05:")
print(array05)
array06 = np.random.randint(0, 9, size = (3, 2))
print("Matrix array06:")
print(array06)
array07 = np.dot(array05, array06)
print("Their result:")
print(array07)
print("\n")
