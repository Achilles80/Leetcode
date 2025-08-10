class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        low=0
        high=len(arr)-1
        ans=-1
        res=[]
        while (low<=high):
            mid=(low+high)//2
            if (arr[mid]<target):
                low=mid+1
            elif (arr[mid]>target):
                high=mid-1

            else:
                ans=mid
                high=mid-1
        res.append(ans)

        low=0
        high=len(arr)-1
        ans=-1
        while (low<=high):
            mid=(low+high)//2
            if (arr[mid]<target):
                low=mid+1
            elif (arr[mid]>target):
                high=mid-1

            else:
                ans=mid
                low=mid+1
        res.append(ans)
        return res