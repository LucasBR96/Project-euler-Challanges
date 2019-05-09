import time
import random

def colleatz( n ):

    values = [n]
    while n != 1:

        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1

        values.append(n)
    return values

def findBiggestDumb( N ):

    maxidx = 1
    maxLen = 1

    i = 1
    while i < N:

        c = len( colleatz(i) )
        if c > maxLen:
            maxLen = c
            maxIdx = i
        i += 1

    return maxIdx,maxLen


def findBiggestSmart( N ):

    proxs = {2:1}
    tests = []

    n = 3
    while n < N:

        if n in proxs:
            n += 1
            continue
        
        tests.append(n)
        # if len(tests)%100 == 0:
        #     print(tests[-1])

        if n%2 == 0:
            nxt = n//2
        else: 
            nxt = 3*n + 1

        proxs[n] = nxt

        while (proxs.get(nxt) == None):

            if nxt%2 == 0:
                proxs[nxt] = nxt//2

            else: 
                proxs[nxt] = 3*nxt + 1
            nxt = proxs[nxt]

        n += 1

    maxSize = -1

    for x in tests:

        size = 1
        aux = x

        while aux != 1:
            aux = proxs[aux]
            size += 1
            
        if size > maxSize:
            maxSize = size
            result = x
    
    return result

if __name__=="__main__":

    print("size \t smart \t dumb")

    cDumb = 0
    cSmart = 0

    x = 1000
    end = 50000
    step = 25
    while x < end:

        s = str(x)
        
        t = time.time()
        findBiggestSmart( x )
        cSmart += time.time() - t
        s += '\t' + str ( cSmart )

        t = time.time()
        findBiggestDumb( x )
        cDumb += time.time() - t
        s += '\t' + str( cDumb )

        print(s)
        x += step