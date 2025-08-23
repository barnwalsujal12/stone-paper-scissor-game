p1=input("Enter first player name: ")
p2="Computer"
n="y"
x,y=0,0
f=open("score.txt","w")
f.writelines(["\n\n","\t\tSCORE BOARD \n","\t\t","_"*len('SCORE BOARD'),"\n\n"])
f.close()
while n=='y':
    a=input(f"Enter for {p1}: ")
    print(f"{p1}{(len(p2)-len(p1))*" "}:  {a} ")
    import random
    ch=("stone","paper","scissor")
    b=random.choice(ch)
    print(f"Computer:  {b}")
    if (a=='stone' and b=='scissor') or (a=="paper" and b=="stone") or (a=="scissor" and b=="paper"):
        print(p1,"won 🥳")
        x+=1
    elif(b=='stone' and a=='scissor') or (b=="paper" and a=="stone") or (b=="scissor" and a=="paper"):
        print(p2,"won")   
        y+=1
    elif a==b:
        print("The match is tie")
    n=input("Do you want to continue(y/n)?")
f=open("score.txt","a")
f.write(f"{p1} score:{x} \n{p2} score:{y} ")
f.close()
if n=="n":
    f= open("score.txt")
    print(f.read())
     
