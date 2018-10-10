class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def findOrder(self, numCourses, prerequisites):
        res = []
        map = [[] for x in range(numCourses)]
        ind = [0 for x in range(numCourses)]
         
        for p in prerequisites:
            if p[0] not in map[p[1]]:
                ind[p[0]] += 1
                map[p[1]].append(p[0])
        q = []
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        count = 0
        while q:
            tmp = q.pop(0)
            res .append(tmp)
            count += 1
            for i in map[tmp]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
                         
        if count < numCourses:
            return []
        else: 
            return res
