class Solution:
    def LargestHistogram(self,arr):
        n=len(arr)
        maxArea=0
        st=[]
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea=0
        n=len(matrix)
        m=len(matrix[0])
        psum=[[0]*m for _ in range(n)]
        for i in range(m):
            s=0
            for j in range(n):
                s+=int(matrix[j][i])
                if matrix[j][i]=="0":
                    s=0
                psum[j][i]=s
        for i in range(n):
            maxArea=max(maxArea,self.LargestHistogram(psum[i]))
        return maxArea

        
        