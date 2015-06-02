# -*- encoding: utf-8 -*-
'''
Created on 2015-05-04
Author: Aran
Description: review
'''
class Solution:
    # @param {integer} n
    # @return {integer}

    def isPrime(self,n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            p = n/2
            for i in range(2,p+1):
                if n%i ==0:
                    return False
            return True

    def countPrimes(self, n):
        num = 0
        for i in range(1,n):
            if self.isPrime(i) == True:
                num = num + 1
        return num


s = Solution()
print s.countPrimes(213231)