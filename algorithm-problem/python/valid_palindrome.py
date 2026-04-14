"""
验证回文串 (Valid Palindrome)

问题描述：
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

使用场景：
- 文本处理
- 字符串分析
- 验证用户输入

算法难度：简单

时间复杂度：O(n) - 只需遍历字符串一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 回文串是指正着读和倒着读都一样的字符串
- 需要过滤掉非字母和数字的字符
- 需要将字母转换为小写进行比较
"""


def is_palindrome(s: str) -> bool:
    """
    验证字符串是否是回文串
    
    Args:
        s: 字符串
    
    Returns:
        是否是回文串
    """
    # 初始化左右指针
    left, right = 0, len(s) - 1
    
    while left < right:
        # 找到左侧的字母或数字
        while left < right and not s[left].isalnum():
            left += 1
        # 找到右侧的字母或数字
        while left < right and not s[right].isalnum():
            right -= 1
        
        # 比较字符（忽略大小写）
        if s[left].lower() != s[right].lower():
            return False
        
        # 移动指针
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("12321", True),
        ("123ab321", True),
        ("!@#$%^&*()", True)  # 只包含非字母和数字的字符
    ]
    
    for s, expected in test_cases:
        result = is_palindrome(s)
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)