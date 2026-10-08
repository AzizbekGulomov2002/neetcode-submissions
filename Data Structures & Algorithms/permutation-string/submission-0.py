class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        need=[0]*26
        window=[0]*26

        for char in s1:
            index = ord(char)-ord('a')
            need[index]+=1
        left=0

        for right in range(len(s2)):
            index=ord(s2[right]) - ord('a')
            window[index]+=1
            if right - left + 1 > len(s1):
                left_index = ord(s2[left]) - ord('a')
                window[left_index]-=1
                left+=1
            if right-left+1==len(s1):
                if window==need:
                    return True
        return False