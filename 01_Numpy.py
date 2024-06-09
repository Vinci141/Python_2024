'''
NumPy Practice
'''
import array

import numpy as np

# import numpy as np
# my_list = [1,2,3]
# print('List :',my_list)
# OneD = np.array(my_list)
# print('\nNumPy 1-D Array :',OneD)
# my_mat = [[1,2,3],[4,5,6],[7,8,9]]
# TwoD = np.array(my_mat)
# print("\nNumPy 2-D array:", my_mat)
# print('\n1-D Array using Range(): - ',np.array(range(1,10)))
# print('\nEven Numbers 1D Array using Range(): - ',np.array(range(0,11,2)))
# print('\nNumPy array of zeros:',np.zeros(3))
# print('\nNumpy Array using Tuples:\n',np.zeros((2,3)))
# print('\nNumPy array of ones:',np.ones(3))
# print('\nNumPy array of ones using tuples:\n',np.zeros((3,4)))
# print('\nNumPy array using linspace ():\n',np.linspace(0,5,10))
# print('\nNumPy array with diagonal as one:\n',np.eye(7))
# ranarr = np.random.rand(5,5)
# print('\nNumPy array using random ():\n',ranarr)
# print('\nNumPy array using randn ():\n',np.random.randn(2))
# print('\nNumPy array using randint ():\n',np.random.randint(1,100, 10))
# arr = np.arange(25)
# print('\nNumPy 1D array using arrange():\n',arr)
# print('\nNumPy array using randint:\n',np.random.randint(0,100,10))
# print('\nNumPy re-shaped array using reshape():\n',arr.reshape(5,5))
# print('Numpy max value from an array:',ranarr.max())
# print('Numpy INDEX OF max value from an array:',ranarr.argmax())
# print('Numpy min value from an array:',ranarr.min())
# print('Numpy INDEX OF MIN value from an array:',ranarr.argmin())
# print('Numpy shape of an array using shape:',ranarr.shape)
# print('Numpy data type of an array:',ranarr.dtype)
#
#
#

'''
Numpy Indexing & selection
'''
# arr = np.arange(0,11)
# print(arr)
# print(arr[1:5])
# print(arr[5:])
# slice_or_arr = arr[0:5] ## new refernce to original Array NOT A a copy so any change in reference will impact original array
# print(slice_or_arr)
# slice_or_arr[:] = 99
# print(slice_or_arr)
# print(arr)
#
#
# # to copy array, use copy()
#
# copy_array = arr.copy()
# print(copy_array)
# copy_array[:] = 1 # changes are made to copy of array
# print(copy_array)
# print(arr) #Original array is uneffected
# #
# arr[0:3] = 100 # Broadcase value 100 to first 3 elements of array
# print(arr)

arr_2d = np.array([[10,15,20],[25,30,35],[40,45,50]])
#print(arr_2d)
#print(arr_2d.shape)

# 2 ways to fetch values from 2D arrays, as follows:
#print(arr_2d[0][0]) # print 1st element of 1st row
#print(arr_2d[0,0]) # print 1st element of 1st row

# print('\n',arr_2d[:2,1:]) # slice notation

# #print(arr_2d[1,]) # slice notation
# arr_1d=np.arange(1,11)
# # print(arr_1d)
# bool_array=arr_1d>5
# # print(bool_array )
# print(arr_1d[bool_array])
# print(arr_1d[arr_1d<3])

arr_5=np.arange(50).reshape(5,10)
print(arr_5)
print('\n',arr_5[1:3,3:5])
