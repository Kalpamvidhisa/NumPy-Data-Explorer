# NumPy Data Explorer Project
import numpy as np
import time

print("----- NumPy Data Explorer -----")

# 1️⃣ Array Creation
print("\n1. Array Creation")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

matrix = np.array([[1,2,3],[4,5,6]])
print("Matrix:\n", matrix)

# 2️⃣ Indexing & Slicing
print("\n2. Indexing & Slicing")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice 1:4 ->", arr[1:4])

# 3️⃣ Mathematical Operations
print("\n3. Mathematical Operations")
print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)
print("Column sum:", np.sum(matrix, axis=0))
print("Row sum:", np.sum(matrix, axis=1))

# 4️⃣ Statistical Operations
print("\n4. Statistical Operations")
data = np.array([5, 10, 15, 20, 25])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))

# 5️⃣ Reshaping & Broadcasting
print("\n5. Reshaping & Broadcasting")
reshaped = np.arange(1,10).reshape(3,3)
print("Reshaped 3x3 Matrix:\n", reshaped)

broadcast = reshaped + np.array([1,2,3])
print("Broadcasting Result:\n", broadcast)

# 6️⃣ Save & Load NumPy Arrays
print("\n6. Save & Load Arrays")
np.save("my_array.npy", arr)
loaded = np.load("my_array.npy")
print("Loaded Array:", loaded)

# 7️⃣ Performance Comparison
print("\n7. Performance Comparison")

python_list = list(range(1000000))
numpy_array = np.arange(1000000)

start = time.time()
python_result = [x*2 for x in python_list]
end = time.time()
print("Python list time:", end - start)

start = time.time()
numpy_result = numpy_array * 2
end = time.time()
print("NumPy array time:", end - start)

print("\nTask Completed Successfully!")