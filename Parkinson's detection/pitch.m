function [p,f] = pitch(a,b, c,fs)
%[a,fs]=audioread('train/1.wav');
[t,f]=shrp(a,fs);

%f
p=mean(f);
%p=p(1);
end

