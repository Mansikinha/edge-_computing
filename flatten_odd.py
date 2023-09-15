def flatten_odd_integer(mylist):
    return [one_element
            for one_sublist in mylist 
            for one_element in one_sublist
            if isinstance(one_element, int) and one_element % 2 != 0]

print(flatten_odd_integer([[1, 6], [7, 9]]))
