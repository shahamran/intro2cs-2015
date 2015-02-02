import turtle
#the input for the maximum branch length
max_length = int(input())
MIN_BRANCH = 10

#this function is not really necessery for this specific application,
#but I thought it was a good idea in general.
def draw_line(length):
    '''Draws a line in the size of [length] and lifts
       the pen up to prevent re-drawing  '''
    turtle.down()
    turtle.forward(length)
    turtle.up()


def draw_tree(length=200):
    '''Recursive function that draws a tree. First draws a line, then turns
       30 degrees to the left and draws a smaller tree, then turns
       60 degrees (30 in absolute terms) to the right and draws another
       smaller tree. Then returns to it's original point.
       Default value if no length was entered = 200 '''
    if length < MIN_BRANCH:
        return # stops when the branch length is smaller than a certain value
    draw_line(length)
    turtle.left(30)
    draw_tree(length * 0.6)
    turtle.right(60)
    draw_tree(length * 0.6)
    turtle.left(30) # we turn again so we will return straight backwards
    turtle.backward(length)

# Let the Tree-Drawing begin!
draw_tree(max_length)
turtle.done()
