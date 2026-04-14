"""
单词搜索 (Word Search)

问题描述：
给定一个 m x n 的二维字符网格 board 和一个字符串单词 word。如果 word 存在于网格中，返回 true；否则，返回 false。

使用场景：
- 矩阵操作
- 算法设计
- 回溯算法

算法难度：中等

时间复杂度：O(m * n * 4^L) - m和n是网格的行数和列数，L是单词的长度
空间复杂度：O(L) - 递归调用栈的深度

其他信息：
- 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中"相邻"单元格是那些水平或垂直相邻的单元格
- 同一个单元格内的字母不允许被重复使用
- 可以使用回溯算法，从每个单元格开始搜索
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    检查单词是否存在于网格中
    
    Args:
        board: 二维字符网格
        word: 要搜索的单词
    
    Returns:
        单词是否存在于网格中
    """
    m, n = len(board), len(board[0])
    L = len(word)
    
    # 回溯函数
    def backtrack(i, j, k):
        # 如果已经找到单词，返回True
        if k == L:
            return True
        
        # 检查边界条件
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        # 检查当前字符是否匹配
        if board[i][j] != word[k]:
            return False
        
        # 标记当前单元格为已访问
        temp = board[i][j]
        board[i][j] = '#'
        
        # 向四个方向搜索
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            if backtrack(i + dx, j + dy, k + 1):
                return True
        
        # 回溯，恢复当前单元格
        board[i][j] = temp
        
        return False
    
    # 从每个单元格开始搜索
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    
    return False


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCCED",
            True
        ),  # 单词存在
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "SEE",
            True
        ),  # 单词存在
        (
            [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']
            ],
            "ABCB",
            False
        ),  # 单词不存在
        (
            [['a']],
            "a",
            True
        ),  # 单个字符
        (
            [['a']],
            "b",
            False
        )  # 单个字符，不匹配
    ]
    
    for board, word, expected in test_cases:
        result = exist(board, word)
        print(f"Input: word={word}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Pass: {result == expected}")
        print("-" * 50)