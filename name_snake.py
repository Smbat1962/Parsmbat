f = open ("C:\\Users\\Admin\\Desktop\\Parsmbat\\my_name_snake.txt","r")
str = "abcdefghijklmnopqrstuvwxyz"
str1 = "abcdefghijklmnopqrstuvwxyz0123456789_"
for line in f:
    if line[0] not in str:
        print("eror",line[0])
    for j in line:
            if j in str1:
                pass
            else:
                print("eror",j)
else:
    print(line)

