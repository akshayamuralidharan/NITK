import time

alp=[] 
mas=[] 

ip=open("mass.txt","r")
for lin in ip:
    alp.append(lin.split()[0])
    mas.append(float(lin.split()[1]))
ip.close()  
def closest(mas,m):
    dif=1000
    ind=-1
    for i in range(len(mas)):
        if abs(mas[i]-m)<dif:
            ind=i
            dif=abs(mas[i]-m) 
    return ind  
ip=open("rosalind_spec.txt","r")
fin=""
k=-1
tim = time.time()
for lin in ip:
    k+=1
    if not k:
        d=float(lin) 
    else:
        fin+=alp[closest(mas,float(lin)-d)]
        d=float(lin)  
tim2 = time.time()
ip.close()
op=open("output_spec.txt","w")
op.write(fin)
op.close()


f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()

