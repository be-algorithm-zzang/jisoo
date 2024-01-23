N=int(input())
words=[]

for i in range(N):
    words.append(str(input()))

group=0
for word in words:
    alphabet=[]
    alphabet.append(word[0])
    for i in range(1, len(word)):
        if word[i]!=word[i-1]:
            alphabet.append(word[i])
    
    array=[]
    for a in alphabet:
        if a not in array:
            array.append(a)
    if array==alphabet:
        group+=1

print(group)
