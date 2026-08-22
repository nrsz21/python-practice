def contains_duplicate(nums):
    if len(set(nums))>=len(nums):
        return False
    else:
        return True

print(contains_duplicate([1, 2, 3, 1]))    # 期待 True
print(contains_duplicate([1, 2, 3, 4]))    # 期待 False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))   # 期待 True