class Solution:
    def helper(self,nums,k):
        count=0
        l=0
        r=0
        oddsum=0
        if(k<0):
            return 0
        while(r<len(nums)):
            if(nums[r]%2!=0):
                oddsum+=1
            while(oddsum>k):
                if(nums[l]%2!=0):
                    oddsum-=1
                l+=1
            count+=(r-l+1)
            r+=1
        return count
            
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k)-self.helper(nums,k-1)

        