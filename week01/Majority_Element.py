class Solution:
    # TC: O(n)
    # MC: O(1)
    def majorityElement(self, nums):
        cnt = 0
        majorityElement = -1

        for num in nums:
            if cnt == 0:
                majorityElement = num
            if num == majorityElement:
                cnt += 1
            else:
                cnt -= 1

        return majorityElement 
