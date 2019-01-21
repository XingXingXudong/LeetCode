# coding: utf-8
from pprint import pprint

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 
        if nums[0] == 0:
            sum_count= {nums[0] : 2}
        else:
            sum_count = {nums[0]: 1, -nums[0]: 1}
        for num in nums[1:]:
            cur_sum_count = {}
            for s, c in sum_count.items():
                cur_sum_count[s+num] = sum_count.get(s, 0) + cur_sum_count.get(s+num, 0)
                cur_sum_count[s-num] = sum_count.get(s, 0) + cur_sum_count.get(s-num, 0)
            sum_count = cur_sum_count
            pprint(sum_count)
        return sum_count.get(S, 0)


if __name__ == '__main__':
    # nums = [1, 1, 1, 1, 1]
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    S = 1
    slution = Solution()
    rtn = slution.findTargetSumWays(nums, S)
    print(rtn)
