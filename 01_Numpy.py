'''
NumPy Practice
'''
import numpy as np
my_list = [1,2,3]
print('List :',my_list)
OneD = np.array(my_list)
print('\nNumPy 1-D Array :',OneD)
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
TwoD = np.array(my_mat)
print("\nNumPy 2-D array:", my_mat)
print('\n1-D Array using Range(): - ',np.array(range(1,10)))
print('\nEven Numbers 1D Array using Range(): - ',np.array(range(0,11,2)))
print('\nNumPy array of zeros:',np.zeros(3))
print('\nNumpy Array using Tuples:\n',np.zeros((2,3)))
print('\nNumPy array of ones:',np.ones(3))
print('\nNumPy array of ones using tuples:\n',np.zeros((3,4)))
print('\nNumPy array using linspace ():\n',np.linspace(0,5,10))
print('\nNumPy array with diagonal as one:\n',np.eye(7))
ranarr = np.random.rand(5,5)
print('\nNumPy array using random ():\n',ranarr)
print('\nNumPy array using randn ():\n',np.random.randn(2))
print('\nNumPy array using randint ():\n',np.random.randint(1,100, 10))
arr = np.arange(25)
print('\nNumPy 1D array using arrange():\n',arr)
print('\nNumPy array using randint:\n',np.random.randint(0,100,10))
print('\nNumPy re-shaped array using reshape():\n',arr.reshape(5,5))
print('Numpy max value from an array:',ranarr.max())
print('Numpy INDEX OF max value from an array:',ranarr.argmax())
print('Numpy min value from an array:',ranarr.min())
print('Numpy INDEX OF MIN value from an array:',ranarr.argmin())
print('Numpy shape of an array using shape:',ranarr.shape)
print('Numpy data type of an array:',ranarr.dtype)
