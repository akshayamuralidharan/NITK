import time

tim = time.time()
ip=open("rosalind_eval.txt","r")
l=int(ip.readline())
st=ip.readline().strip()
arr=ip.readline().strip().split()
a=[float(i) for i in arr]
ip.close()
op=open("output_eval.txt","w")
gcc=st.count('G')+st.count('C')
atc=len(st)-gcc
for gc in a:
    x=((gc/2.0)**gcc)*(((1-gc)/2.0)**atc)*(l-len(st)+1)
    print x,
    op.write(str(x)+" ")
op.close()



f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()
