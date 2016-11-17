import time

f=open("rosalind_ctbl.txt","r")
l=f.read().split('\n')
print l
i=1
s1=""

while l[i][0]!='>':
        s1=s1+l[i]
        i=i+1

i=i+1
s2=""
while l[i]!='':
        s2=s2+l[i]
        i=i+1




f.close()


m=[]

for i in range(len(s1)+1):
        m.append([])

        for j in range(len(s2)+1):
                m[i].append(0)

for j in range(len(s2)+1):
        m[0][j]=j

for j in range(len(s1)+1):
        m[j][0]=j



f=open("output.txt","w")
t=time.time()

for i in range(1,len(s1)+1):
        
        for j in range(1,len(s2)+1):
                if s1[i-1]==s2[j-1]:
                        m[i][j]=min(m[i-1][j-1],m[i-1][j]+1,m[i][j-1]+1)
                
                else:
                        m[i][j]=min(m[i-1][j-1]+1,m[i-1][j]+1,m[i][j-1]+1)

a=""
b=""
i=len(s1)
j=len(s2)

#for ele in m:
#        print ele

f.write(str(m[i][j])+"\n")

while i>0 and j>0:
        #print i,j
        
        if m[i-1][j-1]==m[i][j] and s1[i-1]==s2[j-1]:
                a=s1[i-1]+a
                b=s2[j-1]+b
                i=i-1
                j=j-1
                
        elif m[i-1][j-1]==m[i][j]-1 and s1[i-1]!=s2[j-1]:
                a=s1[i-1]+a
                b=s2[j-1]+b
                i=i-1
                j=j-1
                
        elif m[i-1][j]==m[i][j]-1:
                b="-"+b
                a=s1[i-1]+a
                i=i-1
        else:
                a="-"+a
                b=s2[j-1]+b
                j=j-1
        #print i,j

while i>0:
        b="-"+b
        a=s1[i-1]+a
        i=i-1

while j>0:
        a="-"+a
        b=s2[j-1]+b
        j=j-1


print a
print b

f.write(a+"\n")
f.write(b+"\n")               

		
t2=time.time()
f.close()

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t))
f.close()
