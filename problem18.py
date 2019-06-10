import numpy

def loadPiramid():
    N = int( input() )
    piramid = numpy.zeros( ( N , N ) )
    
    val = int( input() )
    piramid[ 0 , 0 ] = val 

    for n in range( 1 , N ):
        piramid[ n , : n + 1 ] =  numpy.array( [int(x) for x in input().split() ] )
    
    return piramid

if __name__ == "__main__":

    P = loadPiramid()

    pathSum = numpy.zeros( P.shape )
    pathSum[ 0 , 0 ] = P[ 0 , 0]

    for n in range( 1 , P.shape[0] ):

        pathSum[ n , 0 ] = P[ n , 0 ] + pathSum[ n - 1 , 0]
        for i in range( 1 , n + 1):
            bestChoice = max( pathSum[ n - 1 , i ] , pathSum[ n - 1 , i - 1 ] )
            pathSum[ n , i ] = P[ n , i ] + bestChoice
    
    print()
    print( pathSum[ 0 , 0 ] )
    for n in range( 1 , P.shape[0] ):
        print( *[ pathSum[ n , i ] for i in range( n + 1 )], sep = " " )

    print()
    print("max sum: {}".format( max(pathSum[ - 1 ]) ) ) 


