"""
Exponential Search Algorithm
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    index = 1
    n = len(arr)

    while index < n and arr[index] <= target:
        index *= 2

    return binary_search(arr, index // 2, min(index, n - 1), target)


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 55, 60]
    target = 10
    print("Element found at index:", exponential_search(arr, target))
