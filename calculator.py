f = open("myexem.txt", "r")
results = ""
for line in f:
    lst = line.split(" ")
    if lst[1] == "+":
        result = int(lst[0]) + int(lst[2])
        results += line[:-1] + str(result) + "\n"
    elif lst[1] == "-":
        result = int(lst[0]) - int(lst[2])
        results += line[:-1] + str(result) + "\n"
    elif lst[1] == "*":
        result = int(lst[0]) * int(lst[2])
        results += line[:-1] + str(result) + "\n"
    elif lst[1] == "/":
        result = int(lst[0]) / int(lst[2])
        results += line[:-1] + str(result) + "\n"
print(results)

f = open("myexem.txt","w")
f.write(results)