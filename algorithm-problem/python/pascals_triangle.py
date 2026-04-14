"""
杨辉三角 (Pascal's Triangle)

问题描述：
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

使用场景：
- 数学计算
- 组合数学
- 动态规划

算法难度：简单

时间复杂度：O(n^2) - n是行数
空间复杂度：O(n^2) - 需要存储整个杨辉三角

其他信息：
- 杨辉三角的每个数是它左上方和右上方的数的和
- 每行的第一个和最后一个数都是1
- 可以使用动态规划的思想来生成杨辉三角
"""

from typing import List


def generate(num_rows: int) -> List[List[int]]:
    """
    生成杨辉三角的前num_rows行
    
    Args:
        num_rows: 行数
    
    Returns:
        杨辉三角的前num_rows行
    """
    # 处理特殊情况
    if num_rows == 0:
        return []
    
    # 初始化结果
    result = []
    
    # 生成每一行
    for i in range(num_rows):
        # 初始化当前行
        row = [1] * (i + 1)
        
        # 计算中间的数
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        
        # 添加当前行到结果中
        result.append(row)
    
    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (0, []),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (6, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    ]
    
    for num_rows, expected in test_cases:
        result = generate(num_rows)
        print(f"Input: {num_rows}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)