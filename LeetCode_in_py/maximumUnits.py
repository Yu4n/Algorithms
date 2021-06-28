class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: -x[1])
        res = 0
        for box in boxTypes:
            if box[0] > truckSize:
                res += truckSize * box[1]
                break
            if box[0] <= truckSize:
                res += box[1] * box[0]
                truckSize -= box[0]
        return res
