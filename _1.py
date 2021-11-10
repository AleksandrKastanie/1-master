#28 задание по лотарее ---------------------------
from random import *
print("Loterii".center(50,"*"))
computer=randint(1,100)
chel=int(input("введите число "))
while chel!=computer: 
    chel=input("вы проиграли "+ chel+ " попробуйте снова")
print("Вы отгадали")


##задание с while 
#loom=input("купи слона! ")
#while loom.title()!="Слон": #upper(), lower() 
#    loom=input("Все говорят: "+ loom+"! А ты купи!!!")
#print("С вас 1.000.000 евро")
##17
#for rjady in range(1,10):
#    for stroka in range(1,10):
#       if rjady==stroka:
#           print("x",end=" ")
#       elif stroka==1:
#           print("x", end=" ")
#       else:
#           print("0", end=" ")
#    print()

##16
#for rjady in range(1,10):
#    for stroka in range(1,10):
#       if rjady==stroka:
#           print(stroka,end=" ")
#       else:
#           print("0", end=" ")
#    print()

##15
#for rjady in range(10):
#    for stroka in range(10):
#        print(stroka, end=" ")
#    print()
#13--------------------------------------
#k=0
#summa=0
#for i in range(100, 1001):
#    if i %7==0:
#        print(i)#ekraanile
#        k+=1#kogus suurendame
#        summa+=i# i-de summa, misjagatakse 7-ga
#print("kogus summa: ", summa)
#print("summa: ", summa)

##9--------------------------------------
#Summa=float(input("Sisesta summa: "))
#N=int(input("Mitu Aastat: "))
#for aasta in range(1,N+1):
#    Summa*=1.03
#    print(aasta,"aastapärast tulemus on", round(Summa,2))

#3--------------------------------------
#korrutis=1
#for i in range(8):
#    A=float(input("число: "))
#    if A>0:
#        korrutis*=A
#    print(korrutis)

##2-------------------------------------
#A=input("Sisesta arv")
#while int(A)<=1:
#    try:
#        A=int(input("Sisesta "+str(i+1)+" arv"))
#    except:
#        TypeError
#summa=0
#for i in range(1,int(A)+1):
#    summa+=i
#print("summa võrdub ", summa)

#8----------------------
#for i in range(1,21):
#    print("Дюймы = ",i*2.5, "CM")

#from random import *
#p=0
#n=0
#N=randint(1,10)
#print(N)
#for i in range(N):
#    arv=int(input("Sisesta arv"))
#    if arv>0:
#        p+=1
#    elif arv<0:
#        n+=1
#print("Neg: "+str(n))
#print("Pos: "+str(p))
#print("Nullid: "+str(N-n-p))


#7-------------------------
#from random import *
##A<B
#A=randint(10,100)
#B=randint(100,1000)
#print("A="+str(A))
#print("B="+str(B))
#K=int(input("K: "))
#for i in range(A,B+1):
#    if i%K==0: print(i)
#4----------------------
#for i in range(10,21):
   # print(i**2)

#1----------------------------
#p=0;
#for i in range(15):#i=0,1,2,3...
#    A=0
#    while type(A)!=float:
#        try:
#            A=float(input("Sisesta "+str(i+1)+" arv"))
#        except TypeError:
#            print("Mmmmmmm!")
#    if A==round(A):
#        p+=1
#        print(str(A)+"on täisarv")
#    else:
#        print(str(A)+" ei ole täisarv")

#print (str(p)+" Täisarvud")


