class Solution(object):
    '''
    题意：判断数字是否为回文数
    翻转数字比较相等即可
    注意负数不是回文数    
    '''
    def isPalindrome(self, x):
        if x < 0 :
            return False
        tmp = x
        rev = 0
        while tmp :
            rev = rev * 10 + tmp % 10
            tmp /= 10
        return rev == x
