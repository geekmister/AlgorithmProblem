"""
爬楼梯 (Climbing Stairs)

问题描述：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

使用场景：
- 动态规划的经典问题
- 组合数学
- 递归和记忆化

算法难度：简单

时间复杂度：O(n) - 只需遍历一次
空间复杂度：O(1) - 只使用常数级别的额外空间

其他信息：
- 这是一个斐波那契数列的变种问题
- 可以使用动态规划或递归的方法解决
- 递归方法可能会有栈溢出的风险，所以动态规划更高效
"""


def climb_stairs(n: int) -> int:
    """
    计算爬楼梯的不同方法数
    
    Args:
        n: 楼梯的阶数
    
    Returns:
        不同的爬楼梯方法数
    """
    # 处理特殊情况
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # 初始化前两个状态
    prev1, prev2 = 1, 2
    
    # 动态规划计算
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
    
    return prev2


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
        (20, 10946)
    ]
    
    for n, expected in test_cases:
        result = climb_stairs(n)
        print(f"Input: {n}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)