numbers=[5,-3,8,-1,0,-7,4]

negative_nums_replaced=[number if number>0 else 0 for number in numbers]
print(negative_nums_replaced)