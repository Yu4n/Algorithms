class Solution:
    def readBinaryWatch(self, turnedOn: int) -> [str]:
        def countBit(num):
            cnt = 0
            while num != 0:
                num = num & (num - 1)
                cnt += 1
            return cnt

        res = []
        for i in range(12):
            for j in range(60):
                if countBit(i) + countBit(j) == turnedOn:
                    res.append(str(i) + ':' + str(j).zfill(2))
        return res
