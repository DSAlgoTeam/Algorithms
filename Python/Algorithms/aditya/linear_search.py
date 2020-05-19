
line = input('Input a list of numeric items')

line = list(map(int,line.strip().split()))

key = int(input("Enter the key"))
length = len(line)
loc =-1
for each_number in range(length) :
    if key == line[each_number]:
        loc = each_number
        break

if loc == -1 :
    print("item not found")
else :
    print("item {} found at {} location ".format(key,loc))

