def longest_common_prefix(strs):
    if not strs:
        return ""
    # 拿到最短字符串，限制循环次数
    shortest = min(strs, key=len)
    prefix = ""
    # 遍历最短字符串的每一个下标
    for i in range(len(shortest)):
        char = shortest[i]
        # 判断：所有字符串的第i位都等于char
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    return prefix


# LeetCode 提交用的格式（类名/函数名必须照抄模板）
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        prefix = ""
        for i in range(len(shortest)):
            char = shortest[i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break
        return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))   # 期待 "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))      # 期待 ""
print(longest_common_prefix(["aa", "aa"]))                   # 期待 "aa"

