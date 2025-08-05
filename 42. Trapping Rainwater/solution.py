class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        rmax=lmax=l=tot=0
        r=n-1
        while(l<r):
            if (arr[l]<=arr[r]):
                if lmax>arr[l]:
                    tot+=lmax-arr[l]
                else:
                    lmax=arr[l]
                l+=1
            else:
                if rmax>arr[r]:
                    tot+=rmax-arr[r]
                else:
                    rmax=arr[r]
                r-=1
        return tot       

        