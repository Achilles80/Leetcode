class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        st=[]
        maxArea=0
        n=len(arr)
        for i in range(n):
            while(len(st)!=0 and arr[st[-1]]>arr[i]):
                element=st[-1]
                st.pop()
                nse=i
                if (len(st)==0):
                    pse=-1
                else:
                    pse=st[-1]
                maxArea=max(maxArea,((nse-pse-1)*arr[element]))
            st.append(i)
        while(len(st)!=0):
            element=st[-1]
            st.pop()
            nse=n
            if (len(st)==0):
                pse=-1
            else:
                pse=st[-1]
            maxArea=max(maxArea,((nse-pse-1)*arr[element]))
        return maxArea