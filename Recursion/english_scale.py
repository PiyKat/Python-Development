#! python3
# Drawing english ruler using fractal patterns

#drawing the major tick lines


def draw_lines(major_tick_length,j = ''):

    line = "-"*major_tick_length
    if(j):
        line+=' ' + j

    print(line)

# Recursive function to be written later
def interval_draw(central_tick_length):

    if(central_tick_length>0):
        interval_draw(central_tick_length-1)
        draw_lines(central_tick_length)
        interval_draw(central_tick_length-1)

    
def draw_ruler(tick_length,no_of_inches):

    draw_lines(tick_length,'0')

    for j in range(1,no_of_inches +1):
        interval_draw(tick_length-1)
        draw_lines(tick_length,str(j))


draw_ruler(5,4)
