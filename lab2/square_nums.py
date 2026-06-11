# nums = [1,2,3,4,5]

# squared_nums=[num**2 for num in nums]
# print(squared_nums)


# nums=[2,3,4,5]
# squared=[num **2 for num in nums]
# print(squared)


nums=[2,4,1,3]

even_num_squared=[num if num%2!=0 else num**2 for num in nums]

print (even_num_squared)