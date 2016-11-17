function p = jitter(a, b, c, fs)
%p=size(a)+b+c;
[~,f]=shrp(a,fs);

p=std(f);

