largest_so_far= -1

print('Before1', largest_so_far)
for the_num in [21, 31, 15, 23, 45]:
    if the_num>largest_so_far:
        largest_so_far= the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
