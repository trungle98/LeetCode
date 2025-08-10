#https://leetcode.com/problems/remove-element/?envType=problem-list-v2&envId=array
def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k


def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                if diff > ans and diff > 0:
                    ans = diff

        return ans

#https://leetcode.com/problems/pascals-triangle/?envType=problem-list-v2&envId=array
#118. Pascal's Triangle
def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        for i in range(2, numRows):
            newRow = [1]*(i+1)
            for j in range(1,len(newRow)-1):
                pre_row = ans[i-1]
                newRow[j] = pre_row[j-1]+pre_row[j]
            ans.append(newRow)
        return ans