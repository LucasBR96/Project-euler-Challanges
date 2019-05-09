import time
import numpy

if  __name__ ==  "__main__":

    start = time.time()
    seq = list( range( 1 , 11 )  )
    s1 = sum( seq )**2 #Square of the sum
    seq2 = numpy.array( seq ).reshape( 1 , 10 )
    s2 = seq2@seq2.T
    print( s1 - s2 )
    end = time.time()
    print( end - start)
    pass



    


