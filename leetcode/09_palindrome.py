def is_palindrome(x):
    if x < 0:                  # 负数直接返回 False
        return False
    s = str(x)                 # 转成字符串
    return s == s[::-1]        # 正序==倒序？返回 True/False

print(is_palindrome(121))     # 期待 True
print(is_palindrome(-121))    # 期待 False
print(is_palindrome(10))      # 期待 False
print(is_palindrome(0))       # 期待 True（0 也是回文）
