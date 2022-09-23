class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        word=[word[::-1] for word in words]
        return ' '.join(word)