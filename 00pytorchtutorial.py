# -*- coding: utf-8 -*-
"""00PyTorchTutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_4QCir6eoRoDNestFc4m8S-EYMtHYfB

# 00.PyTorch Fundementals

Resource notebook: https://www.learnpytorch.io/00_pytorch_fundamentals/

If you have a question: https://github.com/mrdbourke/pytorch-deep-learning/discussions
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

"""## Introduction to Tensors

### Creating tensors

PyTorch tensors are created using `torch.Tensor()` = https://pytorch.org/docs/stable/tensors.html
"""



# scalar
scalar = torch.tensor(7)
scalar

scalar.ndim

# Get tensor back as Python int
scalar.item()

# Vector
vector = torch.tensor([7,7])
vector

vector.ndim

vector.shape

# MATRIX
MATRIX = torch.tensor([[7,8] ,
                       [9,10]])
MATRIX

MATRIX.ndim

MATRIX[1]

MATRIX.shape

# TENSOR
TENSOR = torch.tensor([[[1],
                       [2],
                       [3],
                       [4],
                       [5]],
                       [[1],
                       [2],
                       [3],
                       [4],
                       [5]],
                       [[1],
                       [2],
                       [3],
                       [4],
                       [5]],
                       [[1],
                       [2],
                       [3],
                       [4],
                       [5]]])
TENSOR

TENSOR.ndim

TENSOR.shape

TENSOR[0]

"""### Random tensors

Why random tensors?

Random tensors are important because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those random numbers to better represent the data

`Start with random numbers -> look at data -> update random numbers -> look at data -> update random numbers`

Torch Random Tensors - https://pytorch.org/docs/stable/generated/torch.rand.html
"""

# Create a random tensor of size/shape (3,4)
RandTensor = torch.rand(2, 5)
RandTensor

# Create a random tensor with similar shape to an image tensor
randImageSizeTensor = torch.rand(size=(3,224,224)) # height, width, colour channels (R, G, B)
randImageSizeTensor.shape, randImageSizeTensor.ndim

"""### Zeros and Ones"""

# Create a tensor of all zeros
zeros = torch.zeros(size = (2,5))
zeros

# Create a tensor of all ones
ones = torch.ones(size = (2,5))
ones

ones.dtype

"""### Creating a Range of Tensors and Tensors-like
Torch Arange Tensors - https://pytorch.org/docs/stable/generated/torch.arange.html
"""

# Use torch.range()
one_to_ten = torch.arange(0,1000,100)
one_to_ten

# Creating tensors like
ten_zeroes = torch.zeros_like(one_to_ten)
ten_zeroes

"""### Tensor Datatypes
**Note:** Tensor datatypes is one of the 3 big errors you'll run into with PyTorch & deep learning
1. Tensors are not the right datatype
2. Tensors are not the right shape
3. Tensors are not on the right device

Precision in computing - https://en.wikipedia.org/wiki/Precision_(computer_science)

Torch Device - https://pytorch.org/docs/stable/tensor_attributes.html#torch.device
"""

# Float 32 tensor
float_32_tensor = torch.tensor([3.0,6.0,9.0],
                               dtype = None, # What datatype is the tensor (float32, float64, etc.)
                               device = None, # What device is the tensor on?
                               requires_grad = False) # Whether or not to track gradients with tensors operations
float_32_tensor

float_32_tensor.dtype

float_16_tensor = float_32_tensor.type(torch.float16)
float_16_tensor

float_16_tensor * float_32_tensor

int_32_tensor = torch.tensor([3,6,9], dtype=torch.long)
int_32_tensor

float_32_tensor * int_32_tensor

"""### Getting information from tensors (Tensor Atrributes)

1. To get the datatype from a tensor, use `tensor.dtype`
2. To get the shape from a tensor, use `tensor.shape`
3. To get the device from a tensor, use `tensor.device`
"""

# Create a tensor
some_tensor = torch.rand(3,4)
some_tensor

print(some_tensor)
print("The Datatype of the Tensor is: " + str(some_tensor.dtype))
print("The Shape of the Tensor is: " + str(some_tensor.shape))
print("The Device of the Tensor is: " + str(some_tensor.device))

"""### Manipulating Tensors (tensor operations)

Tensor Operations include:
* Addition
* Subtraction
* Multiplication (element-wise)
* Division
* Matrix Multiplication
"""

# Create a tensor and add 10 to it
tensor = torch.tensor([1,2,3])
tensor + 10

# Multiply tensor by 10
tensor * 10

# Subtract 10
tensor - 10

# Try out PyTorch in-built functions
torch.mul(tensor, 10)

torch.add(tensor, 10)

"""### Matrix Multiplication

Two main ways of performing multiplication in neural networks and deep learning:
1. Element-wise multiplication
2. Matrix miltiplication (dot product)

More information on multiplying matrices - https://www.mathsisfun.com/algebra/matrix-multiplying.html

There are 2 main rules that performing matrix multiplication needs to satisfy:
1. The **inner dimensions** must match:
* `(3,2) @ (3,2)` will NOT work.
* `(3,2) @ (2,3)` will work.
* `(2,3) @ (3,2)` will also work.
2. The resulting matrix will have the shape of the **outer dimensions**:
* `(3,2) @ (2,3)` -> `(2,2)`
* `(2,3) @ (3,2)` -> `(3,3)`

A good website for Matrix Multiplication - http://matrixmultiplication.xyz/
"""

# Element Wise Multiplication
print(str(tensor) + " * " + str(tensor))
print("equals: " + str(tensor * tensor))

# Commented out IPython magic to ensure Python compatibility.
# # Matrix multiplication
# %%time
# torch.matmul(tensor,tensor)

tensor @ tensor

# Commented out IPython magic to ensure Python compatibility.
# %%time
# value = 0
# for j in tensor:
#   value += j * j
#

"""### Shape Errors"""

#Shapes for Matrix Multiplication
tensor_A = torch.tensor([[1,2,8],
                         [3,4,3],
                         [5,6,2],
                         [5,6,1]])
tensor_B = torch.tensor([[6,10,1],
                         [7,11,10],
                         [8,12,15],
                         [9,13,14]])
# torch.mm is the same as torch.matmul
# torch.mm(tensor_A, tensor_B) returns an error

tensor_A.shape, tensor_B.shape

"""To fix our tensor shape issues, we can manipulate the shape of one of our tensors using a **transpose** .

A **transpose** switches the axes or dimensions of a given tensor.
"""

tensor_B, tensor_B.shape

tensor_B.T, tensor_B.T.shape

# Commented out IPython magic to ensure Python compatibility.
# %%time
# # The matrix multiplication operation works when tensor_B is transposed
# print("Original shapes: \ntensor_A = " + str(tensor_A.shape) + ", tensor_B = " + str(tensor_B.shape) )
# print("New shapes: \ntensor_A = " + str(tensor_A.shape) + ", tensor_B.T = " + str(tensor_B.T.shape) )
# print("Multiplying: \n" + str(tensor_A.shape) + " @ " + str(tensor_B.T.shape) + " <- inter dimensions must match")
# print("Output:\n")
# output = torch.matmul(tensor_A, tensor_B.T)
# print(output)
# print("Output Shape: " + str(output.shape))

"""## Tensor Aggregation
Finding the min, max, mean, sum, etc.
"""

# Create a tensor
x = torch.arange(0,100,10)
x

# Find the min
torch.min(x), x.min()

# Find the max
torch.max(x), x.max()

# Find the mean - note: the torch.mean() function requires a tensor of float32 datatype to work
torch.mean(x.type(torch.float)), x.type(torch.float).mean()

# Find the sum
torch.sum(x), x.sum()

"""## Finding the positional min and max"""

x[0] = 10
x[1] = 0
x

# Find the position in tensor that has the minimum value with argmin() -> returns index position of target tensor where the minimum value occurs
x.argmin()

x[0]

# Find the position in tensor that has the maximum value with argmax() -> returns index position of target tensor where the maximum value occurs
x.argmax()

x[9]

"""## Reshaping, Stacking, Squeezing, and Unsqueezing Tensors

* Reshaping - Reshapes and input tensor to a defined shape
* View - Return a view of an input tensor of certain shape but keep the same memory as the original tensor
* Stacking - Combine multiple tensors on top of each other (vstack)
* Squeeze - Removes all `1` dimensions from a tensor
* Unsqueeze - Add a `1` dimension to a target tensor
* Permute - Return a view of the input with dimensions permuted (swapped) in a certain way

"""

# Let's create a tensor
import torch
x = torch.arange(1.,10.)
x, x.shape

# Reshape - Add an extra dimension (all numbers must multiply up to given)
x_reshaped = x.reshape(1,9)
x_reshaped, x_reshaped.shape

# View - Change the view
z = x.view(3,3)
z, z.shape

# Changing z changes x (because a view of a tensor shares the same memory as the original input)
z[:, 0] = 5
z, x

# Stacking - Stack tensors on top of each other
x_stacked = torch.stack([x,x,x,x], dim = 1)
x_stacked

# Squeeze - Remove all single dimensions from target vector
print("Old Tensor: " + str(x_reshaped))
print("Old Shape: " + str(x_reshaped.shape) + "\n")

print("New Tensor: " + str(x_reshaped.squeeze()))
print("New Tensor: " + str(x_reshaped.squeeze().shape))

# Unsqueeze - Adds a single dimension to a target tensor at a specific dimension (dim)
print("Old Tensor: " + str(x_reshaped))
print("Old Shape: " + str(x_reshaped.shape) + "\n")

print("New Tensor: " + str(x_reshaped.unsqueeze(1)))
print("New Tensor: " + str(x_reshaped.unsqueeze(1).shape) + "\n")

print("New Tensor: " + str(x_reshaped.unsqueeze(2)))
print("New Tensor: " + str(x_reshaped.unsqueeze(2).shape) + "\n")

# Permute - Rearranges the dimensions of a target tensor in a specified order
x_original = torch.rand(224,224,3) # [height, width, colour_channels]

# Permute the original tensor to rearrange the axis (or dim) order
x_permuted = x_original.permute(2,0,1) # [colour_channels, height, width]

x_original.shape, x_permuted.shape

x_original[0, 0, 0] = 728218
x_original[0, 0, 0], x_permuted[0, 0, 0]

"""## Indexing (selecting data from tensors)

Indexing with PyTorch is similar to indexing with NumPy
"""

# Create a tensor
import torch
x = torch.arange(1,10)
print(x, x.shape)
x = x.reshape(1,3,3)
print(x, x.shape)

# Indexing on the new tensor
x[0]

# Indexing on the middle brack (dim=1)
x[0][0] # same as x[0,0]

# Indexing on the last brack (dim=2)
x[0][0][0] # same as x[0,0,0]

"""## PyTorch Tensors & NumPy
NumPy is a popular scientific Python numerical computing library

And because of this,  PyTor h has functionality to interact with it
* Data in NumPy, want in PyTorch tensor -> `torch.from_numpy(ndarray)`
* PyTorch Tensor -> NumPy -> `torch.from_numpy(ndarray)`
"""

# NumPy array to tensor
import torch
import numpy as np

array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array).type(torch.float32)
array, tensor

# Change the value of array, what will this do to `tensor`?
array = array + 1
array, tensor

# Tensor to NumPy array
tensor = torch.ones(7)
numpy_tensor = tensor.numpy()
tensor, numpy_tensor

# Change the value of tensor, what will this do to `numpy_tensor`?
tensor = tensor + 1
tensor, numpy_tensor

"""## Reproducibility (Trying to take random out of random)

How a neural network learns:
`Start with random numbers -> tensor operations -> update random numbers to try and make them better representations of the data -> repeat...`

To reduce randomness in neural networks and PyTorch, you have to use a **random seed**

A random seed is used to "flavor" the randomness.

To better understand reproducibility:

* Randomness in PyTorch: https://pytorch.org/docs/stable/notes/randomness.html

* Random Seed Wikipedia: https://en.wikipedia.org/wiki/Random_seed

"""

import torch

# Create 2 random tensors
randTensor1 = torch.rand(3,4)
randTensor2 = torch.rand(3,4)

print(randTensor1)
print(randTensor2)
print(randTensor1 == randTensor2)

# Let's make some ranodm but reproducible tensors
import torch

# Set the random seed
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
randTensor3 = torch.rand(3,4)
torch.manual_seed(RANDOM_SEED)
randTensor4 = torch.rand(3,4)

print(randTensor3)
print(randTensor4)
print(randTensor3 == randTensor4)

"""## Running Tensors and PyTorch objects on GPUs

GPUs = faster computation on numbers done with CUDA, NVIDIA hardware, and PyTorch themselves working behind the scenes

### 1. Getting a GPU

* Google Colab - Allows for a free GPU with options to upgrade
* Creating own GPU - Takes a little bit of setup and requires the investment of purchasing a GPU.
* Use Cloud Computing - GCP (Google Cloud Platform), AWS (Amazon Web Services), Azure (Microsoft), allow you to rent computers on  the cloud and access them

FOr 2,3 PyTorch + GPU drivers (CUDA) takes a little bit of setting up, to do this, refer to PyTorch setup documentation https://pytorch.org/get-started/locally/
"""

!nvidia-smi



















