
# # exception and error handling 
# print(10 / 0)

print('start')
nums = [25, 31, 22, 9, 17]

try: 
    print(nums[5])
except IndexError as e:
    print(f'{e}')
finally:
    print('end')

