print("\n welcome to true friendship calculator! \n")
n = int(input("how many friend-pairs you want to check: "))
for i in range(1,n+1):
    print(f"\n Friend-Pair {i} \n")
    name1=input("please enter your full-name:  \n")
    name2=input("please enter other person's full-name:  \n")
    combine_name=name1+name2
    format_name=combine_name.lower()

    t=format_name.count("t")
    r=format_name.count("r")
    u=format_name.count("u")
    e=format_name.count("e")
    f=format_name.count("f")
    r=format_name.count("r")
    i=format_name.count("i")
    e=format_name.count("e")
    n=format_name.count("n")
    d=format_name.count("d")
    s=format_name.count("s")
    h=format_name.count("h")
    i=format_name.count("i")
    p=format_name.count("p")
    
    
    true_friend=t+r+u+e+f+r+i+e+n+d+s+h+i+p
    true_friend=int(true_friend)

    if true_friend>50:
        print(f"friends ur score is {true_friend} congrats! yo got ur real friend")
    elif true_friend>35:
        print(f"OH! friends your score is {true_friend} spend some time together and be true-friends forever!")
    elif true_friend>15:
        print(f"ur score is {true_friend},it seems {name2} and {name1} have sth to be true friends")
    elif true_friend>10:
        print(f"ur score is {true_friend}, {name1} dont let {name2} down. ")
    else:
        print("opps find some other person.")       
        
print(" well done!!! ")