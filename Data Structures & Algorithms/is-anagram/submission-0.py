class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqmap = {}
        for char in s:
            freqmap[char] = freqmap.get(char, 0) + 1
        print(freqmap)
        for char in t:
            if char not in freqmap or freqmap[char]==0:
                return False
            else:
                freqmap[char]-=1
        return True
