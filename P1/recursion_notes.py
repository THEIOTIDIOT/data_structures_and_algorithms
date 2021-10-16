import matplotlib.pyplot as plt
import statistics
import time



def sum_array_index(array, index):
    
    # Base Cases
    length = len(array)
    if length - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))

# Graph the results
#plt.scatter(x=array_sizes, y=times)
#plt.ylim(top=max(times), bottom=min(times))
#plt.xlabel('Array Size')
#plt.ylabel('Time (seconds)')
#plt.plot()