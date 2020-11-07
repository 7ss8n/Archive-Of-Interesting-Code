class HumanPlayer1 :
    def __init__( self ) :
        self._token = "X"

    def getToken( self ) :
        return self._token

class HumanPlayer2 :
    def __init__( self ) :
        self._token = "O"

    def getToken( self ) :
        return self._token

value = 1
two = "two"

print( not type( value ) is int )

import math
print( math.floor( 8 / 3 ) )

cols = [ "x", "x", "o" ]

token = "x"

if all( cols ) == token :
    print( "Yes" )

import random

print( random.choice(cols) )

winner = "X"

if None == "X" :
    print( "No" )
