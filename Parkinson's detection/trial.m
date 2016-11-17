
f= dir(fullfile('Train/*.wav'));
cd('Train')

i=1;

for k=1:77
    k
    [a, fs, nbits]=wavread(f(k).name);
    b=1;
    e=250;
    c=1;
    flag=size(a);
    if flag(2)==2
        a=a(1);
        sizea=size(a);
        while e<=sizea(1)
            e
           % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
        alpha = 0.97;      % preemphasis coefficient
        R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( a(b:e), fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
         [pi,f]=pitch(a,b,e,fs);
         ji=jitter(a,b,e,fs);
         sh=shimmer(a,b,e,fs,pi);
         
         
            for j=1:13
               X(i,j)=MFCCs(j,1);
            end
            
            X(i,14)=pi;
            X(i,15)=ji;
            X(i,16)=sh;
            i=i+1;
             b=b+125+1;
         e=e+125;
        end
    
    end
    
    if flag(2)==1
        sizea=size(a);
        while e<=sizea(1)
            e
           % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
     alpha = 0.97;      % preemphasis coefficient
     R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( speech, fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
            [pi,f]=pitch(a,b,e,fs);
            ji=jitter(a,b,e, fs);
            sh=shimmer(a,b,e,fs,pi);
%            X(i)=zeros(16);
            for j=1:13
               X(i,j)=MFCCs(j,1);
            end
            
            X(i,14)=pi;
            X(i,15)=ji;
            X(i,16)=sh;
            i=i+1;
             b=b+125+1;
        e=e+125;
            
        end
       
    
    end
   
end

nc=i-1;


f= dir(fullfile('p/*.wav'));
cd('p')



for k=1:77
    k
    [speech, fs, nbits]=wavread(f(k).name);
    b=1;
    e=250;
    c=1;
    flag=size(a);
    if flag(2)==1
        sizea=size(a);
        while e<=sizea(1)
           % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
        alpha = 0.97;      % preemphasis coefficient
        R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( a(b:e), fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
         [pi,f]=pitch(a,b,e,fs);
         ji=jitter(a,b,e,fs);
         sh=shimmer(a,b,e,fs,pi);
         
         
            for j=1:13
               X(i,j)=MFCCs(j,1);
            end
            
            X(i,14)=pi;
            X(i,15)=ji;
            X(i,16)=sh;
            i=i+1;
             b=b+125+1;
        e=e+125;
        end
    
    end
    
    if flag(2)==2
        a=a(1);
        sizea=size(a);
        while e<=sizea(1)      % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
     alpha = 0.97;      % preemphasis coefficient
     R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( speech, fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
           [pi,f]=pitch(a,b,e,fs);
            ji=jitter(a,b,e,fs);
            sh=shimmer(a,b,e,fs,pi);

            for j=1:13
               X(i,j)=MFCCs(j,1);
            end
            
            X(i,14)=pi;
            X(i,15)=ji;
            X(i,16)=sh;
            i=i+1;
           b=b+125+1;
        e=e+125;  
        end
        
    
    end
   
end

T=zeros(i-1,2);

for k=1:nc
    T(k,1)=1;
end
for k=nc:i-1
    T(k,2)=1;
end
    
X=X';
T=T';
save('X','X')
save('Y','Y')

i=1
for k=78:100
    k
    [speech, fs, nbits]=wavread(f(k).name);
    b=1;
    e=250;
    c=1;
    flag=size(a);
    if flag(2)==1
        sizea=size(a);
        while e<=sizea(1)
           % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
        alpha = 0.97;      % preemphasis coefficient
        R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( a(b:e), fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
         [pi,f]=pitch(a,b,e,fs);
         ji=jitter(a,b,e,fs);
         sh=shimmer(a,b,e,fs,pi);
         
         
            for j=1:13
               XT(i,j)=MFCCs(j,1);
            end
            
            XT(i,14)=pi;
            XT(i,15)=ji;
            XT(i,16)=sh;
            i=i+1;
             b=b+125+1;
        e=e+125;
        end
    
    end
    
    if flag(2)==2
        a=a(1);
        sizea=size(a);
        while e<=sizea(1)      % rastaplp(a, fs)
        Tw = 25;           % analysis frame duration (ms)
        Ts = 10;           % analysis frame shift (ms)
     alpha = 0.97;      % preemphasis coefficient
     R = [ 300 3700 ];  % frequency range to consider
     M = 20;            % number of filterbank channels 
     C = 13;            % number of cepstral coefficients
     L = 22;            % cepstral sine lifter parameter
      
          % hamming 
    hamming = @(N)(0.54-0.46*cos(2*pi*[0:N-1].'/(N-1)));
      
          % Read speech samples, sampling rate and precision from file
    [ speech, fs, nbits ] = wavread( '1.wav' );
      
          % Feature extraction (feature vectors as columns)
    [ MFCCs, FBEs, frames ] = mfcc( speech, fs, Tw, Ts, alpha, hamming, R, M, C, L );
      
%    while(e<=size(a,1))
           [pi,f]=pitch(a,b,e,fs);
            ji=jitter(a,b,e,fs);
            sh=shimmer(a,b,e,fs,pi);

            for j=1:13
               XT(i,j)=MFCCs(j,1);
            end
            
            XT(i,14)=pi;
            XT(i,15)=ji;
            XT(i,16)=sh;
            i=i+1;
           b=b+125+1;
        e=e+125;  
        end
        
    
    end
   
end

TestT=zeros(i-1,2);

for k=1:i-1
    TestT(k,2)=1;
end
save('TestT','TestT')
save('TestX','TX')