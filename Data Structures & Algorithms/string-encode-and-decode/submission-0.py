class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        separator = "|"
        for s in strs:
            count = len(s)
            res += str(count) + separator + s
        return res;

    def decode(self, s: str) -> List[str]:
        res = []
        separator = "|"
        i = 0
        while i < len(s):
            j = i
            while s[j] != separator:
                j+=1
                l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i = j+1+l
        return res;