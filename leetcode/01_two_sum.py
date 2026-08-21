# LeetCode 第 1 题：两数之和

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):   # j 从 i 后面开始，保证两个是不同的数
                if nums[i] + nums[j] == target:
                    return [i, j]

# 本地测试
print(Solution().twoSum([2, 7, 11, 15], 9))    # 期待 [0, 1]
print(Solution().twoSum([3, 2, 4], 6))         # 期待 [1, 2]
print(Solution().twoSum([3, 3], 6))            # 期待 [0, 1]
