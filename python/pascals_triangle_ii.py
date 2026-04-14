"""
杨辉三角 II (Pascal's Triangle II)

问题描述：
给定一个非负索引 k，返回杨辉三角的第 k 行。

使用场景：
- 数学计算
- 组合数学
- 动态规划

算法难度：简单

时间复杂度：O(k^2) - k是行数
空间复杂度：O(k) - 只使用一个数组来存储结果

其他信息：
- 杨辉三角的第k行有k+1个元素
- 可以使用滚动数组的思想来优化空间复杂度
- 从后向前计算可以避免覆盖之前的值
"""

from typing import List


def get_row(row_index: int) -> List[int]:
    """
    返回杨辉三角的第row_index行
    
    Args:
        row_index: 行索引（从0开始）
    
    Returns:
        杨辉三角的第row_index行
    """
    # 初始化结果数组
    row = [1] * (row_index + 1)
    
    # 从第二行开始计算
    for i in range(1, row_index + 1):
        # 从后向前计算，避免覆盖之前的值
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
    
    return row


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (3, [1, 3, 3, 1]),
        (0, [1]),
        (1, [1, 1]),
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1])
    ]
    
    for row_index, expected in test_cases:
        result = get_row(row_index)
        print(f"Input: {row_index}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)