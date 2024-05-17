def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_data = bubble_sort(data.copy())
print(f"Sorted Data (Bubble Sort): {sorted_data}")

sorted_data = quick_sort(data.copy())
print(f"Sorted Data (Quick Sort): {sorted_data}")

index = linear_search(data, 5)
print(f"Index of 5 (Linear Search): {index}")

index = binary_search(sorted_data, 5)
print(f"Index of 5 (Binary Search): {index}")
