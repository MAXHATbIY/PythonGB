# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')


# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()

# exit()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()    
exit()


