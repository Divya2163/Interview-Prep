class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (word == word.capitalize() or word == word.lower() or word==word.upper())