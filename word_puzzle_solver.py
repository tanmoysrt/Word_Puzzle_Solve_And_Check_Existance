import collections
f=open('word.txt','r+')
data=str(f.read())
f.close()
data=list(map(str,data.split('\n')))
x=list(input('Enter the alphabets : '))
index=[]
temp=[]
final=[]
#print(len(data[0]))
for i in range(0,len(data)):
    if len(x)==len(data[i]):
        index.append(i)
for i in index:
        temp.append(list(data[i]))
for i in range(0,len(temp)):
    if collections.Counter(x)==collections.Counter(temp[i]):
        result=""
        for i in temp[i]:
            result+=i
        final.append(result)
if final!=[]:
    print("\nThe Possible Words Are : ")
    for i in range(0,len(final)):
        print(final[i])
else :
    print("\n!!!!!!!! No word with these alphabets exists !!!!!!!!!")