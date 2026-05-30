def bubble_otimizado(nums):
    size = len(nums)

    for j in range(size - 1):
        is_sorted = True
        print(nums)

        for i in range(size - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorted = False

        if is_sorted:
            return


print("--- Testando com [5, 4, 3, 2, 1] ---")
bubble_otimizado([5, 4, 3, 2, 1])