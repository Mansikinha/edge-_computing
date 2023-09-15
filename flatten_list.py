def flatten(mylist):
    return [one_element 
            for one_sublist in mylist
            for one_element in one_sublist]

result = flatten([[1, 2], [3, 4]])
print(result)
