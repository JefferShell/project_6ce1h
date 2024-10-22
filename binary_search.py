
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 测试
if __name__ == "__main__":
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(test_arr, target)
    print(f"目标 {target} 的索引是: {result}")
