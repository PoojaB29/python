
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        r = []
        if len(s) < 10:
            return r
        map = {'A':0,'C':1,'G':2,'T':3}
        sum = 0
        for i in range(len(s)):
            sum = (sum * 4 + map[s[i]]) & 0xFFFFF
            if i < 9:
                continue
            d[sum] = d.get(sum,0)+1
            if d[sum] == 2:
                r.append(s[(i-9):(i+1)])
                
        return r