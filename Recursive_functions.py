def f(n):
    if n<= 1:
        return n
    else:
        return f(n-1) + f(n-2)


def g(x):
    if x > 0:
        return "" + g(x-3) + 1
    else:
        return 3 * x
    
def h(x):
    if x > 5:
        return h(x - 7) + 1
    elif 0 <= x <= 5:
        return x
    elif x < 0:
        return h(x + 3)
    
def painted_area(side):
    total_painted = 0
    num_squares = 1  # Start with 1 square
    
    while side >= 2:
        # Step 3 & 4: Divide into 4 and paint 1
        painted_this_step = num_squares * (side / 2)**2
        total_painted += painted_this_step
        
        # Step 5: Repeat for the 3 unpainted squares
        num_squares *= 3  # Each unpainted square splits into 3 more
        side /= 2         # Side length halves each time
        
    return total_painted