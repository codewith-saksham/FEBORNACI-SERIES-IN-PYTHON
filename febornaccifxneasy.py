def febornacci(num):
     if num==0:
         return 0
     elif num==1:
         return 1
     else:
        return febornacci(num-1)+febornacci(num-2)
num=int(input("enter a number "))
for i in range (num):
    print (febornacci(i), end=" ")
