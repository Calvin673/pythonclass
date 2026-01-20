def calculate_painted_area(side):
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

print(calculate_painted_area(30))
print(calculate_painted_area(16))



