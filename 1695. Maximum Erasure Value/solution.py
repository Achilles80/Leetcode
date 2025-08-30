class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen=set()
        i=0
        cur_sum=0
        maxi=0
        for j in range(len(nums)):
            while nums[j] in seen: 
                seen.remove(nums[i])
                cur_sum -= nums[i]
                i += 1
            seen.add(nums[j])
            cur_sum += nums[j]
            maxi = max(maxi, cur_sum)

        return maxi
