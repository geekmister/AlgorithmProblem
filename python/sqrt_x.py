"""
Sqrt(x) (平方根)

问题描述：
实现 int sqrt(int x) 函数。计算并返回 x 的平方根，其中 x 是非负整数。

使用场景：
- 数学计算
- 几何运算
- 物理模拟

算法难度：简单

时间复杂度：O(log x) - 使用二分查找
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 返回的结果只保留整数部分，小数部分将被舍去
- 可以使用二分查找来高效地找到平方根
- 需要考虑 x=0 和 x=1 的特殊情况
"""


def sqrt_x(x: int) -> int:
    """
    计算非负整数的平方根（整数部分）
    
    Args:
        x: 非负整数
    
    Returns:
        x的平方根的整数部分
    """
    # 处理特殊情况
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    # 初始化二分查找的范围
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        # 计算mid的平方
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            # 记录当前的结果，因为可能没有完全平方数
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (4, 2),
        (8, 2),  # 8的平方根是2.828...，返回2
        (0, 0),
        (1, 1),
        (16, 4),
        (25, 5),
        (26, 5)  # 26的平方根是5.099...，返回5
    ]
    
    for x, expected in test_cases:
        result = sqrt_x(x)
        print(f"Input: {x}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)