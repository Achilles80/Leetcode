class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=0
        rsum=0
        maxi=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxi=lsum
        rightInd=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum=lsum-cardPoints[i]
            rsum+=cardPoints[rightInd]
            rightInd-=1
            maxi=max(maxi,lsum+rsum)
        return maxi
