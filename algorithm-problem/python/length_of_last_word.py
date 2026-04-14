"""
最后一个单词的长度 (Length of Last Word)

问题描述：
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

使用场景：
- 文本处理
- 字符串分析
- 自然语言处理

算法难度：简单

时间复杂度：O(n) - 只需遍历字符串一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 需要处理字符串末尾有空格的情况
- 需要处理整个字符串都是空格的情况
- 从右向左遍历可以更高效地找到最后一个单词
"""


def length_of_last_word(s: str) -> int:
    """
    计算字符串中最后一个单词的长度
    
    Args:
        s: 包含大小写字母和空格的字符串
    
    Returns:
        最后一个单词的长度
    """
    # 初始化长度计数器
    length = 0
    # 从右向左遍历
    i = len(s) - 1
    
    # 跳过末尾的空格
    while i >= 0 and s[i] == ' ':
        i -= 1
    
    # 计算最后一个单词的长度
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        (" ", 0),
        ("a", 1),
        ("Hello", 5)
    ]
    
    for s, expected in test_cases:
        result = length_of_last_word(s)
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)