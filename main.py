#defalt argument
def greeting(wish,word = "good"):
    return word + wish
msg = input("type your message:")
print(greeting(msg))
