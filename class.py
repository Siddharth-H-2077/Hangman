#to make use of the "random.choice" function
import random
import winsound
import getpass
#importing colorama
from colorama import*
init()
#list of words in easy mode
class level_easy:
    def animals(self):
        return ['mouse','rhino','lion','tiger','leopard','jaguar','panther']
    def birds(self):
        return ['owl','dove','parrot','flamingo','sparrow','crow','parakeet']
    def tree(self):
        return ['banyan','eucalyptus','coconut','palm',]
    def fruits(self):
        return['apple','orange','peach','banana','mango','strawberry','fig']
    def transport(self):
        return ['plane','train','jet','tank','submarine','jeep','bike','tonga']
    def beverages(self):
        return ['tea','coffee','pepsi','coke','boost']
    def occupation(self):
        return ['wrestler','engineer','architect','doctor','surgeon','manager','security','police','army','navy']
#list of words for the hard mode
class level_hard:
    def words(self):
        return['mouse','rhino','lion','tiger','leopard','jaguar','panther','wrestler','engineer','architect','doctor','surgeon','manager','security','police','army','navy','apple','orange','peach','banana','mango','strawberry','fig']
import os
def cls():
    os.system('CLS')

def questions(a):
    global point
    point=0
    wletter=[]
    answer=list(a)
    word=[]
    t=[]
    wcount=len(answer)
    t.extend(answer)
    kn=0
    for i in range (len(t)) :
        t[i]=" _ "
    print(' '.join(t))
    while kn<len(answer):
        print()
        gans=input(Fore.GREEN+"pls enter a alphabet  ")
        if gans in wletter:
            print(Fore.WHITE,Back.RED+"you already wrote this alphabet")
            print(Fore.RESET,Back.RESET)
            winsound.PlaySound("smb_warning.wav",winsound.SND_ASYNC)
            continue
        else:
            gans=gans.lower()
            wletter.append(gans)
            if gans not in answer:
                point=point+1
                print(Fore.WHITE,Back.RED+"oops you guessed wrong")
                print(Fore.RESET,Back.RESET)
                winsound.PlaySound("smb_mariodie.wav",winsound.SND_ASYNC)
            else:
                print(Fore.RED,Back.CYAN+"you guessed right")
                print(Fore.RESET,Back.RESET)
                cls()
            for i in range(wcount):
                if answer[i]==gans:
                    t[i]=gans
                    kn=kn+1
            word=' '.join(t)
            print(word)
            print()
    print(Fore.RED,Back.YELLOW+"you win")
    print(Fore.GREEN+"you made ",point,"wrong choice(s)")
    print(Fore.RESET,Back.RESET)

print(Fore.GREEN+"|    |       / \      |\         |           _____        /\        /\            /\         |\        |")
print(Fore.GREEN+"|____|     /    \     |   \      |         /             /   \    /    \        /     \      |    \     |")
print(Fore.GREEN+"|     |  /________\  |      \   |                 _    /       \/       \       /______ \    |     \   |")
print(Fore.GREEN+"|     |/             \|        \|          \___|  |    /                 \ /             \ |         \|" )
winsound.PlaySound("smb_world_clear.wav",winsound.SND_ASYNC)
print()
print()
print("press enter")
derp=input()

print("WELCOME TO  HANGMAN")


def login():
    un=input("enter your name \t")
    pw=getpass.getpass("enter the pw ")
    file=open("games.txt","r")
    a=file.readlines()
    file.close()
    global pwd
    pwd=1
    for line in a:
        login_info=line.split()
        if(un in login_info[0] and pw in login_info[1]):
            pwd=1
            break
        else:
            pwd=0
            
    if pwd==1:
        print(Back.GREEN+"logged in")
        print(Back.RESET)
        winsound.PlaySound("smb_stage_clear.wav",winsound.SND_ASYNC)
        global kk
        kk=1
        fummy=input()
        cls()
    else:
        print(Back.RED+"unable to login")
        print(Back.RESET)
        winsound.PlaySound("smb_mariodie.wav",winsound.SND_ASYNC)
        fummy=input()
        cls()
            

#login register for new user
def regester():
    print("REGISTER")
    un=input("enter your name pls\t")
    pw=input("enter the designated password\t")
    file=open("games.txt","a")
    file.write(un)
    file.write("\t ")
    file.write(pw)
    file.write("\n")
    file.close()
    login()
    

print("enter 1 to login 2 to regester")
thing=int(input("make your choice"))
if thing==1:
    login()
else:
    regester()
if kk==1:
    x=level_easy()
    y=level_hard()
    words=[]
    print("1. for easy mode")
    print("2.for hard mode")
    kt=int(input("please make your choice"))
    #for grading of the player
    class List:
        def __init__(self):
                #determining the no. of turns
            self.lista=[5,7,10,13]
                #grading system 
            self.listb=['S','A','B','C','D']
        def ranklist (self,t):
            if self.lista[-1]<=t:
                print(Fore.WHITE,Back.RED+"you came at the last position")
                print("your garde is",self.listb[-1])
            for i in self.lista:
                 if i>t:
                    pl=self.lista.index(i)
                    print("you are given",self.listb[pl] ,"rank :3")
                    break
    lis=List()
    class STACK:
        def __init__(self):
            self.stack=[]
        def push(self,no):
            self.stack.append(no)
        def pop(self):
            return self.stack.pop()
        def length(self):
            return len(self.stack)
    stack=STACK()
    stack_value=1
        #if user enters y he/ she cann play else they quit the game and get their pionts
    while True:
        print(Fore.GREEN+"to get the question press- Y-,to quit press any other button")
        choice=input()
            #user can make choice in the easy mode
        if choice=="Y"or choice=="y":
            if kt==1:
                print(Fore.GREEN+"please enter :")
                print(Fore.GREEN+"1.for animals")
                print(Fore.GREEN+"2.for birds")
                print(Fore.GREEN+"3.for trees")
                print(Fore.GREEN+"4.for fruits")
                print(Fore.GREEN+"5.for transport")
                print(Fore.GREEN+"6.for beverages")
                print(Fore.GREEN+"7.for occupation")
                p=int(input())
                if p==1:
                    words=x.animals()
                elif p==2:
                    words=x.birds()
                elif p==3:
                    words=x.tree()
                elif p==4:
                    words=x.fruits()
                elif p==5:
                    words=x.transport()
                elif p==6:
                    words=x.beverages()
                elif p==7:
                    words=x.occupation()
                k=random.choice(words)
                    
                        
            else:
                print(Fore.GREEN+"are you redy for it...")
                print(Fore.GREEN+"enter 1 to get your question:")
                l=input()
                if l=="1":
                    wordk=y.words()
                    k=random.choice(wordk)
                else:
                    print(Fore.WHITE,Back.RED+"you pressed the wrong button ")
                    print(Fore.RESET,Back.RESET)
                cls()
            print(Fore.GREEN+"this is your question")
            questions(k)
            lis.ranklist(point)
            stack_value=point
            stack.push(stack_value)
                #average point calculation
        else:
            count=0
            if stack.length()>1:
                while stack.length()!=1:
                    a=stack.pop()
                    b=stack.pop()
                    c=a+b
                    stack.push(c)
                    count=count+1
                addition=stack.pop()
                lis.ranklist(addition//count)
                print(Fore.GREEN,Back.YELLOW+"the above is the average score for your total tries")
                winsound.PlaySound("smb_world_clear.wav",winsound.SND_ASYNC)
                print(Fore.RESET,Back.RESET)
                break
else:
    print(Fore.GREEN+"please follow the  instructions to follow the game properly")
    winsound.PlaySound("smb_warning.wav",winsound.SND_ASYNC)
            
                
dummy=input()



        
