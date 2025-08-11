class Solution:
    def findMin(self, arr: List[int]) -> int:
        n=len(arr)
        low=0
        high=n-1
        m=arr[0]
        while(low<=high):
            mid=(low+high)//2
            if(arr[low]<=arr[mid]):
                m=min(arr[low],m)
                low=mid+1
            else:
                m=min(arr[mid],m)
                high=mid-1
        return m       
        