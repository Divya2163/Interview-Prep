#User function Template for python3

class Solution:
    def reverse(self, s):
        # code here
        arr = list(s)
        res=""
        for i in s:
            if i.isalpha():
                res+=i
        res=res[::-1]
        count =0 
        for i in range(len(arr)):
            if arr[i].isalpha():
                arr[i]=res[count]
                count+=1
        res="".join(arr)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverse(s)
        print(ans)
# } Driver Code Ends