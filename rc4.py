import sys

s = int(sys.argv[1])
S=[]
T=[]

##Input Key
k = [3,1,4,1,5]
##Intialze T
for i in range(0,s):
    S.append(i)
    d = i % len(k)
#    print(k[d])
    T.append(k[d])

print("S: %s" % S,",","T: %s"  % T)


##Permutation 
j = 0

for i in range(0,s):
    
    q = j+S[i]+T[i]
    j = q % s
    S[i],S[j] = S[j], S[i]
    print(i,j,S)


print("Stream Genration")


##Stream Genration

j = 0
i = 0

PT=[6,1,5,4]

ks=[]
for h in PT:
    i = (i+1) % s
    j = ( j + S[i]) % s
    S[i],S[j] = S[j], S[i]
    t = (S[i] + S[j]) % s
    ks.append(S[t])
    print(i,j,t,S[t],S)

print("####CT")
ct=[]
for i in range(0,len(PT)):
    ci = PT[i] ^ ks[i]
    ct.append(ci)
print(ct)
    







