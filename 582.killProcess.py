class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        myTree = dict()
        for i, parent in enumerate(ppid):
            myTree[parent] =  myTree.get(parent,[])
            myTree[parent].append(pid[i])
        
        res = []
        stack = [kill]
        while stack:
            cur = stack.pop(0)
            res.append(cur)
            stack.extend(myTree.get(cur,[]))
            
        return res
