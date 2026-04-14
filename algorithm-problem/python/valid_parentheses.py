"""
有效的括号 (Valid Parentheses)

问题描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

使用场景：
- 语法分析
- 代码编辑器中的括号匹配检查
- 编译器和解释器

算法难度：简单

时间复杂度：O(n) - 只需遍历字符串一次
空间复杂度：O(n) - 最坏情况下需要存储所有字符

其他信息：
- 有效的括号必须满足：左括号必须用相同类型的右括号闭合，左括号必须以正确的顺序闭合
- 使用栈来解决这个问题是最直观的方法
- 需要考虑空字符串的情况（空字符串是有效的）
"""


def is_valid(s: str) -> bool:
    """
    判断字符串中的括号是否有效
    
    Args:
        s: 包含括号的字符串
    
    Returns:
        括号是否有效
    """
    # 定义括号的映射关系
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # 使用栈来存储左括号
    stack = []
    
    # 遍历字符串
    for char in s:
        # 如果是右括号
        if char in bracket_map:
            # 取出栈顶元素，如果栈为空则使用一个特殊值
            top_element = stack.pop() if stack else '#'
            # 检查是否匹配
            if bracket_map[char] != top_element:
                return False
        else:
            # 如果是左括号，压入栈中
            stack.append(char)
    
    # 最后栈应该为空
    return not stack


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False)
    ]
    
    for s, expected in test_cases:
        result = is_valid(s)
        print(f"Input: '{s}'")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)