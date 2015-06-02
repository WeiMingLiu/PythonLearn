__author__ = 'I310242'
def primeJudege(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        p = n/2
        for i in range(2,p+1):
            if n%i == 0:
                return False
        return True

print primeJudege(523)