
# file_name = 'sample.txt'

# with open(file_name, 'r') as file:
#     text = file.read()
#     print(text)


file1 = 'sample.txt'
file2 = 'another.txt'

with open(file1, 'r') as f1:
    text1 = f1.read()
    print(text1)

with open(file2, 'w') as f2:
    f2.write(text1)

with open(file2, 'r') as f2:
    t2 = f2.read()
    print((t2))
    
# with open(file2, 'a') as f2:
#     t2 = f2.read()
#     print((t2))




# file_name = 'sample.txt'

# with open(file_name, 'r') as file:
#     # text = file.read()
    
#     for line in file:
#         if line.strip() == 'line 2':
#             continue
#         print(line.strip())
    
    
    


