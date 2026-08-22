import random

def partition(array, start, end):
    pivot = random.randint(start, end)
    pivot_value = array[pivot]

    array[pivot], array[end] = array[end], array[pivot]

    left = start
    for i in range(start, end):
        if array[i] < pivot_value:
            array[i], array[left] = array[left], array[i]
            left += 1

    array[left], array[end] = array[end], array[left]
    return left

def quickselect(array, target):
    left = 0
    right = len(array) - 1

    while True:
        if left == right:
            return array[left]

        pivot = partition(array, left, right)

        if pivot == target:
            return array[target]
        
        if pivot < target:
            left = pivot + 1
        elif pivot > target:
            right = pivot - 1

if __name__ == "__main__":
    arr = [7,3,2,8,5,4,1,6,10,9]
    # arr = [89,34,86,2,25,52,69,66,48,77,95,30,34,73,13,11,88,27,95,36]
    print(sorted(arr))
    print(quickselect(arr, round(len(arr)/2 - 1)))