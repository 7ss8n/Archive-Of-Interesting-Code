
# Implementation of the Queue ADT using a python list.
class Queue :
    # Creates an empty queue instance.
    def __init__( self ) :
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ) :
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ) :
        return len( self._qList )

    # Adds the given item into the queue.
    def enqueue( self, item ) :
        self._qList.append( item )

    # Removes and returns the first item in the queue.
    def dequeue( self ) :
        assert not self.isEmpty(), " Cannot dequeue an empty queue. "
        return self._qList.pop( 0 )



