
def fibonacci( n ) :
    if n <= 1 :
        print( n )
        return n

    else :
        return fibonacci( n - 2 ) + fibonacci( n - 1 )

#print( fibonacci( 30 ) )

def goodFibonacci( n ) :
    if n <= 1 :
        return n, 0

    else :
        a, b = goodFibonacci( n - 1 )
        return a + b, a

print( goodFibonacci( 600 ) )