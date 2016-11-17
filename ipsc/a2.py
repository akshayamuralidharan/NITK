f=open('a2.in','r')

n=int(f.readline().strip())
f.readline().strip()
num=[]

for i in range(n):
    num.append(map(lambda x: int(x),f.readline().strip()))
    f.readline().strip()
   # print num
f.close()
f=open('a2.out','w')
for i in range(n):
    
    num[i].sort()
    s=num[i][0]
    t=1
    for j in range(1,len(num[i])):
        s=s+num[i][j]*t
        t=t*10
        
    f.write(str(s))
    f.write('\n')
f.close()
