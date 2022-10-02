class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        sam=""
        for i in words:
            sam+=i
            if sam==s:
                return True 
        return False