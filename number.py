number = input("Enter a number: ")
length = len(str(number))
num_str = str(number)
sum_of_num = sum(int(digit) for digit in str(number))
print(length)
print(sum_of_num)
total_sum = 0
for i in range(1, len(number), 2):
    total_sum += int(number[i])
print(total_sum)


occurrences = str(number).count("4")
print(occurrences)


middle_index = length//2
middle_digit = num_str[middle_index]
print(middle_digit)





