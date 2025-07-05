# 560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # -- Brute Force Approach--
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     summ = 0
        #     for j in range(i,n):
        #         summ +=nums[j]
        #         if (summ == k): count +=1
            
        # return count

        # -- Optimal Approach--
        n = len(nums)
        count = 0
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        m = defaultdict(int)

        for j in range(n):
            if prefixSum[j] == k:
                count +=1
            val = prefixSum[j] - k
            count +=m[val]

            m[prefixSum[j]] += 1
        
        return count
        