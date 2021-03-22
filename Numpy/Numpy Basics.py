#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Constructing numpy array from list

list1 = [1,2,3,4,5,8]
list2 = [2,3,4,5,6,2]
list3 = [9,7,5,0,3,5]

arr1 = np.array([list1,list2,list3])
print(arr1)
arr = np.array([1,2,3,4,5])
print(arr)

# conditional masking

arr[arr<3]


# In[95]:


## The Shape and Reshaping of NumPy Array
#NumPy Attributes
#1. ndim - Number of dimensions.
#2. shape - The size of each dimension.
#3. size - The total size of the array.
#4. dtype - The data type of array elements.
#5. itemsize - Byte size of each array element.
#6. nbytes - Total size of the array. It is equal to itemsize times size.

#Dimensions of NumPy array
print('Dim of array arr {} and arr1 {}'.format(arr.ndim,arr1.ndim))

#Shape of NumPy array
print(' shape of the array',arr1.shape)
#Size of NumPy array

print('size of array',arr1.size)

#Reshape the array 
print('reshaoe array to 6X3 ',arr1.reshape(6,3))

# Flattening a NumPy array

a = np.ones((2,2))
b = a.flatten()
c = a.ravel()
print('Original shape :', a.shape)
print('Array :','\n', a)
print('Shape after flatten :',b.shape)
print('Array :','\n', b)
print('Shape after ravel :',c.shape)
print('Array :','\n', c)

# Transpose of a NumPy array
print('\n original array \n {} and \n transpose is \n {}'.format(arr1,arr1.T))


# In[ ]:


# Array Slicing

# 1d

# Nd

a=np.array( [[2,3,5,8,7],
             [4,1,0,9,6],
             [6,3,4,0,6]] )

# 2 rows 3 columns
a[ :2, :3]
# 3 rows 2 columns
a[ :3, :2]


# In[73]:


## appending/concateneting and spliting numpy array 

# Appending data to numpy 1d

arr1 = np.array(list1)
arr2 = np.array(list2)

##adding it horizontally
np.append(arr1,arr2)

# Appending numpy array nd

arr3 = np.array(list1).reshape(2,3)
print('arr3 '+str(arr3))
arr4 = np.array(list2).reshape(2,3)
print('\n arr4'+str(arr4))

## adding it vertically
print('\n New array appended vertically '+str(np.append(arr3,arr4,axis=1)))

## adding it horizontally
print('\n New array appended horizontally '+str(np.append(arr3,arr4,axis=0)))


## adding it vertically with vstack
print('\n New array appended vertically vstack '+str(np.vstack((arr3,arr4))))

## adding it vertically with hstack
print('\n New array appended vertically hstack '+str(np.hstack((arr3,arr4))))

## Splitting data in numpy numpy array

# 1d
x= [1,2,3,99,99,3,2,1]

x1, x2, x3 = np.split(x,[3,5])
print('Split ',x1,x2,x3)

# nd
a=np.arange(16).reshape((4,4))
print(a)

upper,lower =np.vsplit(a,[2])
print('Upper',upper)
print('lower',lower)

left, right = np.hsplit(a,[2])
print('left ',left)
print('right ',right)

a2 = np.split(a,2,1)
print('split vertically ',a2)
a3 = np.split(a,2,0)
print('split horizontally ',a3)


# In[62]:


# Cpoying numpy array 
## There are 3 ways to copy a array to another array. 1) View 2) copy 3) assingment 
## 1. In View it create two array with different memory loc but change in themain array will change the copy 
## 2. In copy a separate copy of the array will be created and nay change to any element will no change the copy. (Deep copy)
## 3. In general for assingment the smae memory location is accessed so called shallow copy.
arr = np.array([2, 4, 6, 8, 10]) 

#1. Assigment 

nc = arr
nc[0] = 12
print('Memory location of the original array',id(arr))
print('Memory location of the copied array',id(nc))

print('Print values of the original array',arr)
print('Print values of the copied array',arr)

#2. View 

view1 = arr.view()
view1[1] = 18 

print('Memory location of the original array',id(arr))
print('Memory location of the copied array',id(view1))

print('Print values of the original array',arr)
print('Print values of the copied array',view1)

#2. Copy

c = arr.copy() 

c[2] = 5
 
print('Copy --Memory location of the original array',id(arr))
print('Copy --Memory location of the copied array',id(c))
print('Copy --Print values of the original array',arr)
print('Copy --Print values of the copied array',c)


# In[15]:


# Sorting in NumPy Arrays

srt = np.random.randint(10,size=10)
print(srt)

print('the sorted array ',np.sort(srt))
print('indices of the sorted array ',np.argsort(srt))

srt.sort()
print(' Python sort method for in-place sort ',srt)


# In[78]:


# Printing Identity Matrix

print('Identity Integer matrix ',np.eye(3,3,dtype=int))

print('Identity Float matrix ',np.eye(3,3))


# In[83]:


#Printing an array filled with zeros and ones

np.zeros(3,dtype=int)

np.ones((3,2),dtype=int)


# In[112]:


#Aggregation
#Finding the max, min and sum of an array:
#Finding the mean, median, variance and standard deviation of an array: In different axis

# 1d
a = np.random.random(10)
print(a)

print('Sum ',np.sum(a))
print('Min ',np.min(a))

print('\nMax ',a.max())

# n d

b = np.random.random(10).reshape(2,5)
print(b)

# python sum fn not numpy
print('\n Sum by python fn ',sum(b))

# Python function 
marks = np.random.randint(20,100, size=(4,6))
print('\n',marks)

#Sum of student marks (sum row wise)
print('\n sum row wise',np.sum(marks,axis=1))

#Min Max of each subject 
print('\n min of column wise ',np.min(marks,axis=0))
print('\n max of column wise',np.min(marks,axis=0))
np.argmax(marks,axis=1)


# In[5]:


#Broadcasting in Numpy Arrays
#We have already seen NumPy universal functions at the very beginning. Broadcasting is another means of applying ufuncs but 
#on arrays of different sizes. Broadcasting is nothing but a set of rules applied by NumPy to perform unfuncs on arrays of 
#different sizes.

m = np.ones((3,3),dtype=int)
print('m :',m)
print('shape of m ',m.shape)

n = np.array([1,2,3])
print('n :',n)
print('shape of n ',n.shape)

add = m + n
print('add ',add)
print('shape of add ',add.shape)


# In[ ]:


# NumPy Ufuncs
#If we loop through the array it takes lot of time as well as lot of code to write. Hene this universal function help to perform 
#operations such ad addition, sub,multi,divsion faster by havng a wrapper class within it (wraper class - np.add(),bp.subtract(),np.multiply())


# In[24]:


# Fancy Indexing

# 1 d
x = np.random.randint(100,size=10)

print('x :',x)

# to get different subset of records from an array
print('normal indexing ',[x[2],x[4],x[6]])

print('fancy indexing ',x[[2,4,6]])

# n d

y = np.random.randint(100,size=(3,5))

print([y[2,3],y[1,3],y[2,1]])

print('fancy indexing for n d ',y[[2,1,2],[3,3,1]])

