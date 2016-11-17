function [pitch, detval, t, proc] = ceppitchest(xin,proc)
% This function applies Noll's cepstrum pitch detection algorithm to input signal 
% vector XIN with processing parameters in data structure PROC.  The function 
% returns vector containing resulting pitch contour vector (PITCH), with
% corresponding detection statistic vector (DETVAL) and time value vector (T).
% If processing parameters are not given in data structure PROC, then
% default values are assigned.  If PROC is in the output argument list
% then the data structure with processing parameters used is passed to
% the workspace.
%
%    [pitch, detval, t, proc] = ceppitchest(xin,proc)
%
% Args:
% XIN => input signal (single row or column vector)
% PROC => data structure with following fields (use all small case for the field variable):
%     FS = sampling frequency (default 44.1kHz)
%     CLIPTYPE => defines type of center clipping to perform on segment of
%     xin before autocorrelation: 'clc' = Soft Center Clip, 'clp' = Hard Center Clip,
%     'sig' = Hard Limit Clip, 'noclip' = no clipping (default no clipping)
%     CLPERCENT => percentage clipping level. 0 < cl < 1 (default .3)
%     ANALWIN =>  Frame size in seconds for pitch estimation (default 30ms)
%     OVERLAP =>  Percentage of ANALWIN for consecutive windows to overlap
%                 value must be greater than 0 and strictly less than 1
%                 (default .5)
%     FP_LOW => Frequency in Hz for lowest frequency that limits
%     pitch search (defaut 1/(.9*ANALWIN))
%     FP_HIGH => Frequency in Hz for highest frequency that limits
%     pitch search (Default FS*.8, i.e. 80% of Nyquist Frequency)
%     
%
% Algorithm: The speech signal is segmented into frames. For each
% frame, the cepstrum is computed and searched for a peak in the range
% of the expected pitch frequencies, defined by PROC.FP_LOW as the lowest
% frequency in Hz and PROC.FP_HIGH as the highest frequency in Hz.
% If a cepstral peak does not exist in this interval then both the corresponding
% elements of PITCH and DETVAL are set to zero. If the peak (detection statistic
% is relatively small, then it is less likely to be voiced, but not necessarily 
% likely to be unvoiced. In this case, a short time average zero 
% crossing rate can be used to assist the voiced/unvoiced decision
% (but this is not performed in this function).
%
%  written by Tim Black and updated by Kevin D. Donohue
%  (donohue@engr.uky.edu) updated April 2007
%

% Check for fields in processing parameter data structure, set defaults
% if field not present.
if nargin == 1  % if processing data struction not given, create one
    proc = struct;
end
% check for or set fields
if ~isfield(proc,'fs')
   proc.fs = 8e3;  %  Default sampling rate 8kHz
end
if ~isfield(proc,'analwin')
    proc.analwin = 20e-3;  % Default window size 20ms
end
if ~isfield(proc,'overlap')
    proc.overlap = .5;  % Default overlap 50%
end
if ~isfield(proc,'fp_low')
    proc.fp_low = 20;  % Default lower pitch limit is 20Hz of analysis window
end
if ~isfield(proc,'fp_high')
    proc.fp_high = .8*proc.fs/2;  % Default higher pitch limit is 80% of Nyquist rate
end
if ~isfield(proc,'cliptype')
    proc.cliptype = 'noclip';  % Default is no clipping
end
if ~isfield(proc,'clpercent')
    proc.clpercent = .3;  % If clipping is applied default level is 30% 
end
%  Test for valid values of fields
if proc.overlap >=1 || proc.overlap < 0
    error('Percentage of overlapping frames must be  >= 0 and <1 !')
end
if proc.fp_low >= proc.fp_high
    error('lower frequency search limit must be lower that higher frequency limit!')
end
if proc.clpercent >=1 || proc.overlap < 0
    error('Clip percentage of amplitudes must be  >= 0 and <1 !')
end


win = fix(proc.analwin*proc.fs);  % convert global analysis window (in seconds) to samples
wininc=(proc.analwin*(1-proc.overlap));  % distance between window starting points in seconds
hi_pind = (1/proc.fp_low); % convert largest period in pitch range to seconds 
lo_pind = (1/proc.fp_high); %  convert smallest period in pitch to seconds

tapwin = kaiser(win,2)';  %  Compute tapering window for segment

co=0;            %  Counter for number of analysis windows 

totlen = length(xin)/proc.fs;  % Len of total signal in seconds
stint = 0;  % start second of first interval
% Loop through the entire speech signal, frame by frame
% k corresponds to the first sample in the current win.
while stint+proc.analwin < totlen
    k= round(stint*proc.fs)+1;  %  convert start point to integer index   
    co = co + 1;	 % increment the estimation window counter, co
    %  Increment time vector
    t(co) = stint + proc.analwin*(1-proc.overlap);  
   % set silence threshold - Rabiner used 1/15 of the peak absolute 
   % signal value across the entire utterance
   %sthresh = (1/15)*max(abs(xin));
   
   % clip the data window if specified by argument cliptype
   if ~strcmp(proc.cliptype,'noclip'),
      x = cclip(detrend(xin(k:k+win-1)),proc.cliptype,proc.clpercent);
   else
      x = detrend(xin(k:k+win-1))';
   end
   if sum(abs(x)) < eps
       detval(co) = 0;
       pitch(co)=0;
   else
   x =  x/std(x);
   % apply rectangular time window to xin and compute cepstrum
   xcep = rceps(x.*tapwin); 
   xcep = xcep(1:floor(length(x)/2));
   xaxis = [0:length(xcep)-1]/proc.fs;  %  create array if indecies
   [mag, lind] = findpeaks(xcep);  % find Cepstral peaks
   pos = xaxis(lind);  %  Peak positions in seconds (1/Hz)
      % For speech:
   % Apply linear multiplicative weighting to current cepstrum 
   % frame over LO_PIND:HI_PIND region. This is done because 
   % the cepstral peaks decrease in amplitude with increasing 
   % quefrency. Actually, the higher-quefrency components in the
   % power spectrum decrease as the time window is convolved with
   % itself. So the higher-quefrency components in the logarithm
   % of the power spectrum decrease similarly. The weighting is 
   % 1 at LO_PIND and 5 at HI_PIND
   %subplot(3,1,2);plot(xcep);
   %xcep = linspace(1,5,length(xcep)).*xcep; 
   %subplot(3,1,3);plot(xcep);

   ptrmind = find(pos >= lo_pind & pos <= hi_pind);  % Find peaks an acceptable pitch range

    if ~isempty(ptrmind)   %  If pitches found in range save them in output pitch vector
       %  Trim peak points to those in range
       mag = mag(ptrmind);  
       pos = pos(ptrmind);
       [rmax, mimax] = max(mag);  % Find max peak point
       kpossible = find(mag >= rmax/2);  % Find all other within 50% of max hieght
       mag = mag(kpossible);         %  These are other possibilities
       pos = pos(kpossible);
       imax = pos(1);       %   The peak for the smallest period is the true one
       rmax = mag(1);
        detval(co) = rmax(1);
        pitch(co) = 1/imax; 
    else  %  IF not pitches found in range, set output to zeros
          detval(co) = 0;
          pitch(co)=0;
          imax = 0;
    end
   end
%  UNCOMMENT for Cepstrum on which peak analysis is done for each frame
%   plot(xaxis(1:end),abs(xcep(1:end)))
%   hold on
%   plot(pos,mag,'xr')
%   plot(imax,detval(co),'>g')
%   hold off
%   pause(.02)
  stint = stint + wininc;  %  Increment to next window starting point
end



function clipdata = cclip(xin,cliptype,clpercent)
%  This function applies various form of clipping to the input signal
%  based a percentage of its peak values.
%
%     [clipdata] = cclip(xin,cliptype,clpercent)
%
%  inputs:
%  xin      => Vector of input signal values
%  cliptype => a string indicating which cliptype to apply
%          'clc' = Soft Center Clip:
%          C[x(n)]=x(n)-Cl for (x(n)>=Cl), 0 for (|x(n)|<Cl),  and x(n)+Cl for (x(n)<=-Cl)
%          'clp' = Hard Center Clip:
%          C[x(n)]=x(n) for (|x(n)|>=Cl), and 0 for (|x(n)|<Cl)
%          'sig' = Hard Limit Center Clip:
%          C[x(n)]= 1 for (|x(n)|>=Cl), 0 for (|x(n)|<Cl), and   -1 for (x(n)<=-Cl)
%  clpercent => percentage of minimum of maximum positive or negative going peak values
%               clipping level must be between 0 < cl < 1
%
%   Written by Tim Black, updated by Kevin D. Donohue (donohue@engr.uky.edu) Jan 2006


% The Clipping level, cl, is set to the percentage of the smaller magnitude of the 
% positive and negative peaks 
if clpercent > 1 || clpercent < 0
    error('Precent of signal for clip threshold should be between 0 and 1')
end
effmag=min([abs(max(xin)),abs(min(xin))]);

cl=clpercent*effmag(1);
% Center clip xwin (the current window of xin) according to argument cliptype: 
clipdata=zeros(1,length(xin));  %  Initialize output to zeros
ind1=find(xin>=cl);     %  find all positive points greater than clip threshold 
ind2=find(xin<=-cl);    %  fild all negative points with magnitudes greater than clip threshold

if strcmp(cliptype,'clc')   %  Center soft clip
   clipdata(ind1)=xin(ind1)-cl;  %  Reduce amplitude by clip threshold (for positive values)
   clipdata(ind2)=xin(ind2)+cl;  %  Reduce amplitude by clip threshold (for negative values)
elseif strcmp(cliptype,'clp') %  Center hard clip
   clipdata(ind1)=xin(ind1);  % Pass positive values greater than threshold 
   clipdata(ind2)=xin(ind2); % Pass negative values with magnitudes greather than threshold
elseif strcmp(cliptype,'sig')   %  Hard limit center clip
   clipdata(ind1)=1;  %  Set postive values to 1;
   clipdata(ind2)=-1; %  Set negative values to -1;
else
    error('Clip Type not specified!  Use strings clc, clp, sig, for soft, hard, or hard limit center clip.')
end

