import sys
from itertools import permutations

input=sys.stdin.readline

numbers=str(input())

answer = 0
n=len(numbers)-1

    
num_arr=[]
for i in range(n):
    num_arr.append(int(numbers[i]))

number_list=[]
for i in range(1, n+1):
    nPi=list(permutations(num_arr,i))

    for p in nPi:
        number=""
        for j in range(len(p)):
            number+=str(p[j])
            number_list.append(int(number))
        


checking_double=[]
for num in number_list:
    if num not in checking_double:
        checking_double.append(num)

for num in checking_double:
    flag=True
    if num!=0 and num!=1:
        for i in range(2, num):
            if flag==True:
                if num%i==0:
                    flag=False
        if flag:
            answer+=1
        
print(answer)