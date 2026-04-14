"""
最长公共前缀 (Longest Common Prefix)

问题描述：
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

使用场景：
- 字符串处理和分析
- 搜索引擎中的自动完成
- 数据压缩

算法难度：简单

时间复杂度：O(n*m) - n是字符串数量，m是最短字符串的长度
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 可以使用水平扫描或垂直扫描方法
- 垂直扫描方法在处理短字符串时更高效
- 需要考虑空数组的情况
"""

from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    查找字符串数组中的最长公共前缀
    
    Args:
        strs: 字符串数组
    
    Returns:
        最长公共前缀
    """
    # 处理空数组情况
    if not strs:
        return ""
    
    # 以第一个字符串为基准
    prefix = strs[0]
    
    # 遍历其他字符串
    for s in strs[1:]:
        # 不断缩短前缀，直到找到公共前缀
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            # 如果前缀为空，直接返回
            if not prefix:
                return ""
    
    return prefix


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["apple", "app", "application"], "app"),
        (["hello", "hello", "hello"], "hello"),
        (["a"], "a"),
        ([], "")
    ]
    
    for strs, expected in test_cases:
        result = longest_common_prefix(strs)
        print(f"Input: {strs}")
        print(f"Expected: '{expected}'")
        print(f"Result: '{result}'")
        print(f"Pass: {result == expected}")
        print("-" * 50)