class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0]*26
            for char in word:
                index = ord(char)-ord("a")
                counts[index]+=1
            key = tuple(counts) # key-value
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
        
# Time O(m*n)