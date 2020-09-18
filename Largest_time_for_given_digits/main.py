from typing import List
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        maxmin = -1
        length = len(A)
        for hr1 in range(length):
            if A[hr1] > 2:
                continue
            for hr2 in range(length):
                if hr1 == hr2 or (A[hr1]==2 and A[hr2] > 3):
                    continue
                for min1 in range(length):
                    if hr1==min1 or hr2==min1 or A[min1] > 5:
                        continue
                    for min2 in range(length):
                        if hr1 == min2 or hr2 == min2 or min1 == min2:
                            continue
                        val = (A[hr1]*10 + A[hr2])*60 + A[min1]*10 + A[min2]
                        maxmin = max(maxmin, val)
        if maxmin == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(maxmin//60 , maxmin%60)

if __name__ == '__main__':
    A = [0,4,0,0]
    sol = Solution()
    ans = sol.largestTimeFromDigits(A)
    print(ans)