def binary_search(nums, n):
    lo = 0
    hi = len(nums)
    steps = 0

    while lo < hi:
        steps+=1
        mid = int((lo+hi)/2)

        if nums[mid] == n:
            print("step: ", steps)
            return mid
        elif nums[mid] < n:
            lo = mid+1
        else:
            hi = mid
    return -1

a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

index = binary_search(c, 3)
print(f"Índice do número: {index}")
