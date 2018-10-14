class Solution(object):
    def numSquares(self, n):
        if n < 2:
            return n
        factor = []
        i = 1
        while i * i <= n:
            factor.append( i * i )
            i += 1
        cnt = 0
        q = [n]
        while q:
            cnt += 1
            temp = []
            for x in q:
                for y in factor:
                    if x - y == 0:
                        return cnt
                    elif x - y > 0:
                        temp.append(x-y)
            q = temp

        return cnt
