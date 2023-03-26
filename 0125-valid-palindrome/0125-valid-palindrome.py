class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        s=s.lower()
        for i in s:
            if i.isalnum():
                res=res+i
        return res==res[::-1]
                
            
            