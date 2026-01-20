def f(n):
    if n<= 1:
        return n
    else:
        return f(n-1) + f(n-2)


def problem2(x):
    if x > 0:
        return problem2(x-3) + 1
    else:
        return 3 * x
    
def problem3(x):
    if x > 5:
        return problem3(x - 7) + 1
    elif 0 <= x <= 5:
        return x
    elif x < 0:
        return problem3(x + 3)
    

    


