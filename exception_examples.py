def divis(a , b): 
    try: 
        c = a / b 
        print(c)
    except ZeroDivisionError: 
        print ("Can't divide by zero")

def read_file(path):  
    try:
        with open(path, "r") as f:
            f = open(path,"r")
            print(f.read())
    except FileNotFoundError:
        print("File does not exist")

def NegativeValueError(a):
    if a > 0:
        print(a)
    else:
        print("The input number is a negative ")
        

def main():
    divis(7,0)
    read_file("my_exem.txt")
    NegativeValueError(-12)


if __name__ == "__main__":
    main()