import time
import random

def product(factors):
    result = 1
    for x in factors:
        result *= x
    return result


def preprocess( N ):
    seqs = []
    for x in N.split( sep = "0"):
        if x != '':
            seqs.append(  tuple([int(y) for y in x]) )
    return seqs

def largestProd( seq , n ):

    maxProd = product( seq[:n] )

    prod = maxProd
    i = 0
    j = n
    while j < len( seq ):

        prod *= seq[j]
        prod //= seq[i]

        if prod > maxProd:
            maxProd = prod
        
        i += 1
        j += 1
    return maxProd

def smart( n , N ):

    # n = input()
    # N = input()

    maxProd = -1
    seq = preprocess( N )
    
    for x in seq:
        
        if len(x) >= n:
            prod = largestProd( x , n)
            if prod > maxProd:
                maxProd = prod
    return prod


def solve():

    N = '73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557'
    N1 = '66896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776'
    N2 = '65727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474'
    N3 = '82166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408'
    N4 = '07198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    S = N + N1 + N2 + N3 + N4 
    n = 13

    print( smart( n , S ) )


def benchmark():

    digits = '01234589'
    maxTime = 20*60
    cumTime = 0 

    size = 1000
    S = ''.join( random.choices( digits, k = size ) )
    n = 10

    while cumTime < maxTime:

        t = time.time()
        smart( n , S)
        dt = time.time() - t
        cumTime += dt

        print("{} + {} + {}".format(size, dt, cumTime) )

        S += ''.join( random.choices( digits, k = 200 ) )
        size += 200
        
if __name__ == "__main__":
    
    #solve()
    benchmark()
   
