class Solution:
    def rec(self,i,s,ans,l):
        if(i==len(s)):
            l.append(ans[:len(ans)-1])
        if(i<len(s) and int(s[i:i+1])>=0 and int(s[i:i+1])<=255):
            self.rec(i+1,s,ans+s[i:i+1]+".",l)
        
        if(i+1<len(s) and int(s[i:i+2])>=0 and int(s[i:i+2])<=255):
            if(not s[i:i+2].startswith("0")):
                self.rec(i+2,s,ans+s[i:i+2]+".",l)
        
        if(i+2<len(s) and int(s[i:i+3])>=0 and int(s[i:i+3])<=255):
            if(not s[i:i+3].startswith("0")):
                self.rec(i+3,s,ans+s[i:i+3]+".",l)
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        l=[]
        ans=""
        self.rec(0,s,ans,l)
        ans=[]
        print(l)
        for i in l:
            #print(i.split("."))
            if(len(i.split("."))==4):
                ans.append(i)
        return ans
        