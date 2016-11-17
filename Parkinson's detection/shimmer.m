function p = shimmer(a, b, c,fs,pi)

cc=floor(fs/pi);
i=b;
j=1;
while i<=c
    arr(j)=max(a(i:i+cc));
    i=i+cc;
    j=j+1;
end

p=std(arr);