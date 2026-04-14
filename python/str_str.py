"""
实现 strStr() (Implement strStr())

问题描述：
实现 strStr() 函数。给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

使用场景：
- 字符串搜索
- 文本处理
- 模式匹配

算法难度：简单

时间复杂度：O(n*m) - n是haystack的长度，m是needle的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 当 needle 是空字符串时，返回 0
- 可以使用暴力匹配或KMP算法
- 暴力匹配虽然时间复杂度较高，但对于短字符串来说足够高效
"""


def str_str(haystack: str, needle: str) -> int:
    """
    在haystack中查找needle的第一个出现位置
    
    Args:
        haystack: 主字符串
        needle: 子字符串
    
    Returns:
        needle在haystack中的第一个出现位置，不存在则返回-1
    """
    # 处理空needle的情况
    if not needle:
        return 0
    
    # 处理needle长度大于haystack的情况
    if len(needle) > len(haystack):
        return -1
    
    # 暴力匹配
    for i in range(len(haystack) - len(needle) + 1):
        # 检查从i开始的子字符串是否与needle匹配
        if haystack[i:i+len(needle)] == needle:
            return i
    
    # 未找到匹配
    return -1


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("a", "a", 0),
        ("mississippi", "issip", 4),
        ("leetcode", "leeto", -1)
    ]
    
    for haystack, needle, expected in test_cases:
        result = str_str(haystack, needle)
        print(f"Input: haystack = '{haystack}', needle = '{needle}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)