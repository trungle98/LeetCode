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