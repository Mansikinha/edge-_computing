def how_many_different_numbers(numbers):
    unique_count = 0
    seen_numbers = []
    
    for num in numbers:
        if num not in seen_numbers:
            seen_numbers.append(num)
            unique_count += 1
    
    return unique_count

print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))
