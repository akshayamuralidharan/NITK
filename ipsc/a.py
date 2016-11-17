f=open('a1.in','r')

n=int(f.readline().strip())
f.readline().strip()
num=[]

for i in range(n):
    num.append(map(lambda x: int(x),f.readline().strip()))
    f.readline().strip()
   # print num
f.close()
f=open('a1.out','w')
for i in range(n):
    f.write(str(sum(num[i])+(max(num[i])*9)))
    f.write('\n')
f.close()
