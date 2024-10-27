a = input("enter a word:")
for i in a:
    if i == 'a' or 'b' or 'c':
        print("the letter is found ?(a or b or c)")
        break
    else:
        print("letter not found (a or b or c)")
#continue "pass"
for i in range(50):
    if i % 2 == 0:
        print(i)
    elif i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        pass