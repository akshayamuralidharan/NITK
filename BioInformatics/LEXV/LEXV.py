import sys
import time

ip=open("rosalind_lexv.txt")
alpha=ip.readline().strip().split()
num=int(ip.readline())
ip.close()
dep=sys.getrecursionlimit()   
sys.setrecursionlimit(num+1500)
tim = time.time()
def getalpha(alpha,l,s,result):
    if l:
        for c in alpha:   
            result.append(s+c)
            getalpha(alpha,l-1,s+c,result)

    return result

fin="\n".join(getalpha(alpha,num,"",[])) 
tim2 = time.time()
op=open("output_lexv.txt","w")
op.write(fin)
op.close()
print fin
sys.setrecursionlimit(dep)



f=open("time.txt","w")
f.write("Execution Time: "+str(tim2-tim))
f.close()
