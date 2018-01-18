import random
a=["you are worst","you da best","you're my real og!"," you are the lamest","goobe","stop being a racist","hustle harder","you're a unicorn"]
while True:
    name=input("enter your name:")
    i=random.randint(0,7)
    print(name,a[i])
    ch=input("continue? y/n")
    if ch=="y":
        continue
    else:
        break
