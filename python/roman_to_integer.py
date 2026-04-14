"""
罗马数字转整数 (Roman to Integer)

问题描述：
给定一个罗马数字，将其转换为整数。

使用场景：
- 历史数据处理
- 金融和会计系统
- 文化和教育应用

算法难度：简单

时间复杂度：O(n) - 只需遍历字符串一次
空间复杂度：O(1) - 使用固定大小的字典

其他信息：
- 罗马数字的基本字符：I(1), V(5), X(10), L(50), C(100), D(500), M(1000)
- 特殊情况：IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)
- 从右到左遍历可以更简单地处理特殊情况
"""


def roman_to_integer(s: str) -> int:
    """
    将罗马数字转换为整数
    
    Args:
        s: 罗马数字字符串
    
    Returns:
        对应的整数
    """
    # 定义罗马数字与整数的映射
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # 初始化结果
    result = 0
    # 记录前一个字符的值
    prev_value = 0
    
    # 从右到左遍历字符串
    for char in reversed(s):
        current_value = roman_map[char]
        
        # 如果当前值小于前一个值，说明是特殊情况（如IV、IX等）
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        # 更新前一个值
        prev_value = current_value
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("XXVII", 27),
        ("XLIX", 49)
    ]
    
    for s, expected in test_cases:
        result = roman_to_integer(s)
        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)