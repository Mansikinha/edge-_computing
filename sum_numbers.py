def sum_numbers(numbers):
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())

print(sum_numbers('1 2 3 a b c d e f 4 6 8'))
