import random
import time
from itertools import permutations

ls=[0,1,2,3,4,5,6,7,8]


dic={
        0:'00',
        1:'01',
        2:'02',
        3:'10',
        4:'11',
        5:'12',
        6:'20',
        7:'21',
        8:'22',

        }

mat=[['_','_','_'],['_','_','_'],['_','_','_']]


#ml
ux=[]
co=[]
win=[]
su=''

def file():
    x=open('user.txt','a+')
    x.close()




def play(y):
    global i1,i2,ls
    i1=int(dic[y][0])
    i2=int(dic[y][1])
    ls.remove(y)



s=''
def complay():
    global ls
    global s
    global win
    global su
    x=random.choice(ls)
    #x=int(input())
    if len(ls)==9:
        x=4
    if len(ls)==7:
        x=5

    if len(ls)<=5:
    
        for i in range(0,len(win)):
            print(s[-2:])
            if s[-2:] in win[i]:
                print('Computer')
                z=win[i]
                x=list(z)
                
                
                x.remove(s[-1])
                x.remove(s[-2])
                
                x=int(x[0])
                
                print('s:',s)
                print('win:',z)
                print('compx:',x)
                
                break
            
            if su[-2:] in win[i]:
                
                z=win[i]
                x=list(z)

                x.remove(su[-1])
                x.remove(su[-2])

                x=int(x[0])


                print('su:',su)
                print('win:',z)
                print('x:',x)
                break
            
            else:
                
                pass
               


    if x in ls:
        play(x)
        mat[i1][i2]='O'
        co.append(str(x))
        print('COMPUTER TURN:',x)

        for var in mat:
            print(*var)
    else:
        
        x=random.choice(ls)
        play(x)
        mat[i1][i2]='O'
        co.append(str(x))
        print('COMPUTER TURN:',x)

        for var in mat:
            print(*var)
    
    s+=str(x)

   
    
    

def usrplay():
    global ux
    global su
   

    n=int(input('Your Turn:'))
    su+=str(n)
    #ux.append(str(n))
    if n in ls:
        play(n)
        mat[i1][i2]='X'
        for var in mat:
            print(*var) 

    else:
        print('This number is already taken')
        usrplay()

    

def check():
    if(mat[0][0]=='X' and mat[0][1]=='X' and mat[0][2]=='X'):
        print('\nYou Won the Match');main()
    elif(mat[1][0]=='X' and mat[1][1]=='X' and mat[1][2]=='X'):
        print('\nYou Won the Match');main()
    elif(mat[2][0]=='X' and mat[2][1]=='X' and mat[2][2]=='X'):
        print('\nYou Won the Match');main()
    
    elif(mat[0][0]=='O' and mat[0][1]=='O' and mat[0][2]=='O'):
        print('\nYou loss the Match');main()
    elif(mat[1][0]=='O' and mat[1][1]=='O' and mat[1][2]=='O'):
        print('\nYou loss the Match');main()
    elif(mat[2][0]=='O' and mat[2][1]=='O' and mat[2][2]=='O'):
        print('\nYou loss the Match');main()
    
    elif(mat[0][0]=='X' and mat[1][0]=='X' and mat[2][0]=='X'):
        print('\nYou Won the Match');main()
    elif(mat[0][1]=='X' and mat[1][1]=='X' and mat[2][1]=='X'):
        print('\nYou Won the Match');main()
    elif(mat[0][2]=='X' and mat[1][2]=='X' and mat[2][2]=='X'):
        print('\nYou Won the Match');main()
    
    elif(mat[0][0]=='O' and mat[1][0]=='O' and mat[2][0]=='O'):
        print('\nYou loss the Match');main()
    elif(mat[0][1]=='O' and mat[1][1]=='O' and mat[2][1]=='O'):
        print('\nYou loss the Match');main()
    elif(mat[0][2]=='O' and mat[1][2]=='O' and mat[2][2]=='O'):
        print('\nYou loss the Match');main()
    
    elif(mat[0][0]=='X' and mat[1][1]=='X' and mat[2][2]=='X'):
        print('\nYou Won the Match');main()
    elif(mat[2][0]=='X' and mat[1][1]=='X' and mat[0][2]=='X'):
        print('\nYou Won the Match');main()
    
    elif(mat[0][0]=='O' and mat[1][1]=='O' and mat[2][2]=='O'):
        print('\nYou loss the Match');main()
    elif(mat[2][0]=='O' and mat[1][1]=='O' and mat[0][2]=='O'):
        print('\nYou loss the Match');main()
   

def main():
    global ls
    global mat
    global ux,co

    ch = input('\n\nWanna play Tic Tac Toe(y/n)? - > ')
    if ch =='y' or ch=='Y':
        ls=[0,1,2,3,4,5,6,7,8]
        
        mat=[['_','_','_'],['_','_','_'],['_','_','_']]

        while True:
            
            ux=[]
            co=[]

            complay()
            
            check()

            if(len(ls)==0):
                print('The match is draw')
                main()
    

            usrplay()
            check()
            
    elif ch=='n' or ch=='N':
        exit(0)
    else:
        print('Invalid input')
        main()
            
def win1():
    global win
    win2=['012','345','678','036','147','258','642','048']

    for i in win2:
        win.append(list(permutations(i,3)))
    win2=[]

    for i in win:
        for j in i:
            y=''.join(j)
            win2.append(y)

    

    win=win2
    print(win)
    


win1()
main()   

