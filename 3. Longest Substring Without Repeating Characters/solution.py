class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        count=0
        maxi=0
        l,r=0,0
        n=len(s)
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                count-=1
                l+=1
            seen.add(s[r])
            count+=1
            maxi=max(maxi,count)
        return maxi