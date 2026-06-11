#flattining the list out of nested list using list comprehension.

nested_list=[[1,2,3],[4,5],[6,7,8,9]]
flattened_list=[num for single_list in nested_list for num in single_list ]
print(flattened_list)


#completed

