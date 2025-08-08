class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n=len(arr)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==target):
                return mid
            if(arr[low]<=arr[mid]):
                if(target<arr[mid] and target>=arr[low]):
                    high=mid-1
                else:
                    low=mid+1
            else:
                if(target>arr[mid] and target<=arr[high]):
                    low=mid+1
                else:
                    high=mid-1
        return -1
            