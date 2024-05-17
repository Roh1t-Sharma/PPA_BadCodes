from abc import ABC, abstractmethod

# Strategy Interfaces
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, data, target):
        pass

# Concrete Sorting Strategies
class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Concrete Searching Strategies
class LinearSearchStrategy(SearchStrategy):
    def search(self, data, target):
        for i in range(len(data)):
            if data[i] == target:
                return i
        return -1

class BinarySearchStrategy(SearchStrategy):
    def search(self, data, target):
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

# Context Classes
class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

class SearchContext:
    def __init__(self, strategy: SearchStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SearchStrategy):
        self._strategy = strategy

    def search(self, data, target):
        return self._strategy.search(data, target)

# Example usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sorting
sort_context = SortContext(BubbleSortStrategy())
sorted_data = sort_context.sort(data.copy())
print(f"Sorted Data (Bubble Sort): {sorted_data}")

sort_context.set_strategy(QuickSortStrategy())
sorted_data = sort_context.sort(data.copy())
print(f"Sorted Data (Quick Sort): {sorted_data}")

# Searching
search_context = SearchContext(LinearSearchStrategy())
index = search_context.search(data, 5)
print(f"Index of 5 (Linear Search): {index}")

search_context.set_strategy(BinarySearchStrategy())
index = search_context.search(sorted_data, 5)
print(f"Index of 5 (Binary Search): {index}")
