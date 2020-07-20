# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for e in range(i+1, len(arr)):
            if arr[smallest_index] > arr[e]:
                smallest_index = e
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps = 1
    while swaps != 0:
        swaps = 1
        for e in range(0,len(arr)-1):
            i = e+1
            if arr[e] > arr[i]:
                arr[e], arr[i] = arr[i], arr[e]
                swaps += 1
        if swaps == 1:
            swaps = 0

    return arr


def instertion_sort(input_list):
    for i in range(1, len(input_list)):
        current = input_list[i]
        j=i
        while j > 0 and current < input_list[j-1]:
            input_list[j] = input_list[j-1]
            j -= 1
        input_list[j] = current
    return input_list
    
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if maximum:
      count_list = [0]*(maximum+1)
    else:
      maximum = 0
      for e in arr:
        if e > maximum:
          maximum = e
      count_list = [0]*(maximum+1)
        
    new_list = [0]*(len(arr))
    prev = 0
    if arr:
      for e in arr:
        if e < 0:
          return "Error, negative numbers not allowed in Count Sort"
        count_list[e] += 1
      for e in range(0,len(count_list)):
        count_list[e] += prev
        prev=count_list[e]
      for e in arr:
        new_list[count_list[e]-1] = e
        count_list[e] -= 1
      arr = new_list
    return arr 
