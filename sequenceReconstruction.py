from collections import defaultdict
class Solution:
    # @param {int[]} org a permutation of the integers from 1 to n
    # @param {int[][]} seqs a list of sequences
    # @return {boolean} true if it can be reconstructed only one or false
    def sequenceReconstruction(self, org, seqs):
        # Write your code here
        
        d = defaultdict(list)
        ind = defaultdict(int)
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
            for i in xrange(len(seq)):
                if i == 0:
                    ind[seq[i]] += 0
                if i < len(seq) - 1:
                    d[seq[i]].append(seq[i + 1])
                    ind[seq[i + 1]] += 1
      
        q = [k for k in ind if ind[k] == 0]
        res = []

        while len(q) == 1:
            tmp = q.pop(0)
            res.append(tmp)
            for node in d[tmp]:
                ind[node] -= 1
                if ind[node] == 0:
                    q.append(node)
        if len(q) > 1:
            return False
        
        return len(res) == len(nodes) and res == org
