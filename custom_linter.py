with  open ("C:\\Users\\Admin\\Downloads\\my_name_snake_python.txt","r") as f:
    lst = f.readlines()
    for l in range(len(lst)):
        str2 = ""
        tpl = ("def","if","for","elif","else","class","while")
        for i in lst[l]:
            str2 += i
            if str2 in tpl:
                break
        if str2 in tpl:
            if lst[l + 1][:3] == "   ":
                pass
            elif str2[0] == " ":
                print("eror indentation1 ->",str2)
            else:
                print("eror indentation2 ->",lst[l + 1])
        else:
            str = "abcdefghijklmnopqrstuvwxyz"
            str1 = "abcdefghijklmnopqrstuvwxyz0123456789_"       
            for j in str2[:-1]:
                if str2[0] not in str:
                    print(str2)
                    print("eror naming conventions3 ->",str2[0])
                    break
                elif j in str1:
                    pass
                else:
                    print(str2)
                    print("eror naming conventions4 ->",j)