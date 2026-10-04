class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not self.is_alpha_num(s[left]):
                left+=1
            while left < right and not self.is_alpha_num(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
        
    
    def is_alpha_num(self,s):
        return (
            'a' <= s <= 'z' or
            'A' <= s <= 'Z' or
            '0' <= s <= '9'
        )