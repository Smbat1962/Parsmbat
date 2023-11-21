KEYWORDS = ("def", "if", "for", "elif", "else", "class", "while")
KEYWORDS1 = ("as", "assert", "break", "continue", "del", "except", "False", "finally", "from", "global", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "with", "yield")



def log_error_indentation(err):
    print("Eror indentation1 ->", err)


def check_lst_syntax(lst):
    for l in range(len(lst)):
        str2 = ""
        for i in lst[l]:
            str2 += i
            if str2 in KEYWORDS:
                break
        if str2 in KEYWORDS:
            if str2[0] == " ":
                log_error_indentation(str2)
            elif lst[l + 1][:3] != "   ":
                log_error_indentation(lst[l+1])
        else:
            check_function_name(str2)
        str3 = ""
        for i in lst[l]:
            if i != " ":
                str3 += i
        else:
            chec_variable_name(str3)


def check_file_syntax(path):
    with open(path, "r") as f:
        lst = f.readlines()
        check_lst_syntax(lst)


def check_function_name(str2):
    str0 = "abcdefghijklmnopqrstuvwxyz"
    str1 = "abcdefghijklmnopqrstuvwxyz0123456789_"
    for j in str2[:-1]:
        if str2[0] not in str0:
            print(str2)
            print("eror naming conventions3 ->", str2[0])
            break
        elif j in str1:
            pass
        else:
            print(str2)
            print("eror naming conventions4 ->", j)
            

def chec_variable_name(str3):
    str0 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz_"
    str1 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz_0123456789."
    if str3[:-1] in KEYWORDS1:
        print(str3)
        print("eror naming conventions5 ->",str3)
    for j in str3[:-1]:
        if str3[0] not in str0:
            print(str3)
            print("eror naming conventions6 ->", str3[0])
            break
        elif j in str1:
            pass
        else:
            print(str3)
            print("eror naming conventions7 ->", j)

#Enter the path of your file

def main():
    check_file_syntax("path")


if __name__ == "__main__":
    main()
