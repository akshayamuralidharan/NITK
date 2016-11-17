X4=importdata('X.mat');
T4=importdata('T.mat');
testX=importdata('testX.mat');
testT=importdata('testT.mat');
setdemorandstream(491218382);
net = patternnet(30);

[net,tr] = train(net,X4,T4);

testY = net(testX);
testIndices = vec2ind(testY);
hist(testIndices);
st=size(testIndices);

accuracy=(100*sum(testIndices(:)==2))/st(2)
