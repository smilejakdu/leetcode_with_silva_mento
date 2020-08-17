''':arg
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

''':arg
answer1
'''

num = 5


class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            sub = self.generate(numRows - 1)
            left = sub[-1] + [0]
            right = [0] + sub[-1]
            sub.append([a + b for a, b in zip(left, right)])
            return sub


s = Solution()
print(s.generate(num))

''':arg
answer2
개인적으로 answer2 가 조금 더 바람직한 답변 같습니다.
'''


class Solution(object):
    def generate(self, numRows):
        ret = [[1] * (i + 1) for i in range(numRows)]
        for r in range(2, numRows):
            for c in range(1, r):
                ret[r][c] = ret[r - 1][c] + ret[r - 1][c - 1]
        return ret


s = Solution()
print(s.generate(num))
