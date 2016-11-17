function demo1pitch

% Demo 1:Pitch extraction		
% Aims: To study the diverse tools available in the toolbox for pitch
%extraction.
% In the following exercises, we will try to extract the pitch contents of various audio files using diverse techniques. All the audio files are included in the ?MIRtoolbox_Demos? folder.

%% 1. Analyis of a single chord

% Load the audio file 'Amin3.wav'.
%a = miraudio('A.wav','Extract',1,4,'s')
a=miraudio('Assertive.wav');
p = mirpitch(a,'Frame')
energy('Assertive.wav')
a=miraudio('Excamatory.wav');
energy('Excamatory.wav')
p = mirpitch(a,'Frame')
a=miraudio('Imperative.wav');
energy('Imperative.wav')
p = mirpitch(a,'Frame')
a=miraudio('Interrogative.wav');
energy('Interrogative.wav')
p = mirpitch(a,'Frame')

%and play it:
%mirplay(a)

% Observe the periodicities contained in the signal by computing the autocorrelation function:
%ac = mirautocor(a);
% The autocorrelation function can also be displayed in the frequency domain (?Freq?), and the frequency range can be specified, for instance between 75 and 2400 Hz:
%ac = mirautocor(ac, 'Freq','Min',75,'Hz','Max',2400,'Hz');

% The peaks of the curve indicates the most important periodicities:
%pac = mirpeaks(ac)
% But the two peaks at the start and end of the curves are meaningless, so should be removed:
%pac = mirpeaks(ac, 'NoBegin','NoEnd');
%pac(1)
% The corresponding pitch height are given by:


% The actual numerical data (here, the frequency of each pitch) is given by:
%mirgetdata(p)
%mirpitch(
% The resulting pitches can be finally played:
%mirplay(p)

% So far, the results do not seem very convincing, do they?

pause, close all
