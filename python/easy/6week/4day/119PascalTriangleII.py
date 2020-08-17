''':arg
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
Notice that the row index starts from 0.


https://leetcode.com/problems/pascals-triangle-ii/

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        int_list = []
        [int_list.append([1] * (i + 1)) for i in range(0, rowIndex + 1)]

        for r in range(2, rowIndex + 1):
            for z in range(1, r):
                int_list[r][z] = int_list[r - 1][z] + int_list[r - 1][z - 1]

        result_diction = {}
        for k, v in enumerate(int_list):
            result_diction[k] = v

        for r in result_diction.keys():
            if rowIndex == int(r):
                return result_diction[r]

        return


