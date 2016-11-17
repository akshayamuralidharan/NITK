import time

f=open("rosalind_nkew_4_dataset.txt","r+")

l=f.read().split('\n')
d={}

i=0
cntr=0
while i<len(l):

    d[l[i]]=l[i+1]
    i=i+3

f=open("output.txt","w")
t1=time.time()

for ele in d:
    a=l[cntr+1].split()
    ele=l[cntr]
    cntr=cntr+3
    cm=[k for k, letter in enumerate(ele) if letter == ',']
    sc=[k for k, letter in enumerate(ele) if letter == ':']
    cb=[i for i, letter in enumerate(ele) if letter == ')']
    ob=[i for i, letter in enumerate(ele) if letter == '(']

    i=ele.find(a[0])

    temp=filter(lambda x: x>i,sc)
    if temp:
        sc1=temp[0]
    
    
    temp=filter(lambda x: x>i,cb)
    if temp:
        cb1=temp[0]
    else:
        cb1=len(ele)

    temp=filter(lambda x: x>i,cm)
    if temp:
        cm1=temp[0]
    else:
        cm1=len(ele)
    

    sm=0
    
    trp=int(ele[sc1+1:min(cb1,cm1)])
 
    sm=sm+trp
    i=ele.find(a[1])

    temp=filter(lambda x: x>i,sc)
    sc1=temp[0]

    temp=filter(lambda x: x>i,cb)

    if temp:
        cb1=temp[0]
    else:
        cb1=len(ele)

    temp=filter(lambda x: x>i,cm)

    if temp:
        cm1=temp[0]
    else:
        cm1=len(ele)
    
    sm=sm+int(ele[sc1+1:min(cb1,cm1)])



    i=len(ob)-1
    
    while i>0:
        temp=filter(lambda x: x>ob[i],cb)
        temp=temp[0]
  #      print temp
       # print ele[ob[i]:temp],a[0],a[1]
        
        if a[0] in ele[ob[i]:temp] and a[1] in ele[ob[i]:temp]:
            break
        
        
        tempq=filter(lambda x: x>temp,cb)
        
        if tempq:
            cb1=tempq[0]
        else:
            cb1=len(ele)

        tempq=filter(lambda x: x>temp,cm)
        if tempq:
            cm1=tempq[0]
        else:
            cm1=len(ele)
            

        tmp=ele[temp+2:min(cb1,cm1)]
        
        if a[0] in ele[ob[i]:temp] or a[1] in ele[ob[i]:temp]:
            #print a[0],a[1], ele[ob[i]:temp],tmp
            sm=sm+int(tmp)

        i=i-1

        del cb[cb.index(temp)]
        
       
    print sm,
    f.write(str(sm)+" ")

t2=time.time()
f.close()
    

    

f=open("time.txt","w")
f.write("Exection Time: "+str(t2-t1))
f.close()
