# Angel vs Devil
# On a 12x12 board, devils try to kill the angel who tries
# to get across the board. 
# The angel starts on an edge not including a corner and
# walks in a straight line across the board. Devils can be
# anywhere. The starting point of all pieces are given.
# The devils have powers:

# LUCIQUARE (L): His starting point can be on any of the 
# four borders of the board. He leaves a poison trail and 
# moves in shape such that it is possible to create the 
# biggest square along with the borders of the board Square 
# may or may not be formed in 12 seconds within which the 
# angel crosses from one end of the board to other
# Wherever he starts, he must make a square with his path
# and the edges of the board

# THREE LEGGED EEK (E): She is a large three legged devil. 
# She crushes the angel if he comes into any of those 3 
# boxes where her legs are placed She can only walk 
# diagonally and starts moving towards the cell A1. If she 
# reaches the border she returns on the same path and keeps 
# moving to and fro like this.

# For example the image below she is where its mentioned E1 
# in the 1 second, she is at E2 in the 2nd second, E3 in 
# the 3d second, in the 4th second she is again in the 
# squares where E2 is mentioned, in the 5th second she is 
# again in the squares where El is mentioned, in the second 
# she is in the squares where E6 is mentioned in the 7th 
# second she is in the quares where E7 is mentioned since 
# she has reached border of the board she will move back 
# again in the same path

# MUTO (M). He can be move to other cells without the need 
# to traverse the path He can be present at vertically. 
# diagonally, horizontally opposite cells at subsequent 
# seconds. He makes these moves in clockwise manner If angel 
# comes on the same cell as him, he will convert the Angel 
# into a Muto.

# Angel wins if they get to the other side of the board
# print "WON"
# Angel dies if it clashes with two devils at the same time
# or walks through Luciquare's trail (?)
# print the cell number
# print "MUTO" if the angel is converted

# moves the simulation based on the time delta of 1 second
def update():
    