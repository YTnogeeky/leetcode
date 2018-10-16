def findMissingNumber(input):
    # O(n) time O(1)Space
    if not input:
        return 0
    
    for i in range(len(input)):
        if input[i] < len(input) and input[i] != input[input[i]] :
            
            tmp = input[i] 
            input[i], input[tmp] = input[tmp], input[i]
            print input
    for i in range(len(input)):
        if input[i] != i:
            return i
    return len(input)
        
            
             
    

def findMissingNumv1(input):
    # O(n)time, O(n)Space
    if not input:
        return 0
    
    visited = [-1] * (max(input) + 1)
    
    for num in input:
        visited[num] = num
    
    for i in range(len(visited)):
        if visited[i] == -1:
            return i
    return max(input) + 1
    
        



def findMissingNumv2(input):
    # O(n)time, O(n)Space
    if not input:
        return 0
    
    input = set(input)  
    count = 0
    while count in input:
        count = count + 1
        
    return count
