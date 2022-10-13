n = int(input())
arr = list(map(int, input().split()))
bike_price = int(input())

def binary_search(arr, x, left, right):
    # [left, right)

    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x:
        # print("left ", left, " right ", right, " mid", mid, " arr[mid] >= x")
        if mid == 0 or arr[mid - 1] < x:
            return mid + 1

    if arr[mid] >= x: 
        # Will be searching leftwards from the middle
        return binary_search(arr, x, left, mid)
    else:
        # Will be searching in rightwards from the middle
        return binary_search(arr, x, mid + 1, right)

print(binary_search(arr, bike_price, 0, len(arr)), binary_search(arr, bike_price * 2, 0, len(arr)))
