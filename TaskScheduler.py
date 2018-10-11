from collections import *
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks).values()
        max_count = max(counts)
        max_items = counts.count(max_count)
    
        
       
        return max(len(tasks), (max_count - 1) * (n + 1) + max_items)
