import math,time
fct=[1]
tim=time.time()


def comb(a,b):
    return fct[a]/(fct[b]*fct[a-b])
def bccdf(k,n,p):
    sm=0
    for i in range(int(k)):
        a=comb(n,i)
        b=(p**i)*((1-p)**(n-i))*a
        sm+=b
    return sm
def indc(n,k,p):
    bc = bccdf(k,n,p)
    if not bc:
        return 0.000
    return math.log(bc,10)
def result(n):
    result = []
    for k in range(2*n):        
        result.append(indc(2*n,k,0.5))
    return sorted(result,reverse=True)
ip=open("rosalind_indc_1_dataset.txt","r")
n=int(ip.readline())
ip.close()
for i in range(1,2*n + 1):
    fct.append(fct[i-1]*i)
op=open("output_indc.txt","w")
for i in result(n):
    if '%.3f'%i == '-0.000':
        op.write('0.000 ')
        print 0.000,
    else:
        op.write('%.3f'%i+' ')
        print '%.3f'%i,
op.close()



f=open("time.txt","w")
f.write("Exection Time: "+str(time.time()-tim))
f.close()
