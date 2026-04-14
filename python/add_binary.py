"""
二进制求和 (Add Binary)

问题描述：
给定两个二进制字符串，返回它们的和（用二进制表示）。

使用场景：
- 二进制数的运算
- 计算机科学中的位操作
- 数字电路设计

算法难度：简单

时间复杂度：O(max(n,m)) - n和m分别是两个字符串的长度
空间复杂度：O(max(n,m)) - 需要存储结果

其他信息：
- 输入的字符串只包含 '0' 和 '1' 字符
- 可以从右向左逐位相加，处理进位
- 最后需要将结果反转
"""


def add_binary(a: str, b: str) -> str:
    """
    计算两个二进制字符串的和
    
    Args:
        a: 第一个二进制字符串
        b: 第二个二进制字符串
    
    Returns:
        二进制和的字符串表示
    """
    # 初始化指针和进位
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    
    # 从右向左逐位相加
    while i >= 0 or j >= 0 or carry:
        # 获取当前位的值
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # 计算当前位的和
        total = digit_a + digit_b + carry
        
        # 计算当前位的结果和进位
        current_digit = total % 2
        carry = total // 2
        
        # 将当前位添加到结果中
        result.append(str(current_digit))
        
        # 移动指针
        i -= 1
        j -= 1
    
    # 反转结果并返回
    return ''.join(reversed(result))


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "1", "10"),
        ("1111", "1111", "11110")
    ]
    
    for a, b, expected in test_cases:
        result = add_binary(a, b)
        print(f"Input: a = '{a}', b = '{b}'")
        print(f"Expected: '{expected}'")
        print(f"Result: '{result}'")
        print(f"Pass: {result == expected}")
        print("-" * 50)