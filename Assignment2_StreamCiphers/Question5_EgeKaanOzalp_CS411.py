import lfsr
import random

# For p_1:
# Max period is 2^7 - 1 = 127
print("--------------------------------------------------")
print()
length = 256
L = 7
C = [0]*(L+1)
S = [0]*L
C[0] = C[1] = C[3] = C[5] = C[7] = 1

for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print("P1:")
print ("Initial state: ", S)

keystream = [0]*length
for i in range(0,length):
     keystream[i] = lfsr.LFSR(C, S)

print ("First period: ", lfsr.FindPeriod(keystream))
print("Since max period is 127 and the period of p_1 is 127, it generates the maximum period sequence.")
#print ("L and C(x): ", lfsr.BM(keystream))
#print ("keystream: ", keystream)

print()
print("--------------------------------------------------")
print()

# For p_2:
# Max period is 2^6 - 1 = 63

length = 256
L = 6
C = [0]*(L+1)
S = [0]*L
C[0] = C[2] = C[5] = C[6] = 1

for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print("P2:")
print ("Initial state: ", S)

keystream = [0]*length
for i in range(0,length):
     keystream[i] = lfsr.LFSR(C, S)

print ("First period: ", lfsr.FindPeriod(keystream))
print("Since max period is 63 and the period of p_2 is 21, it does not generate the maximum period sequence.")
#print ("L and C(x): ", lfsr.BM(keystream))
#print ("keystream: ", keystream)

print()
print("--------------------------------------------------")
print()

# For p_3:
# Max period is 31:

length = 256
L = 5
C = [0]*(L+1)
S = [0]*L
C[0] = C[1] = C[3] = C[4] = C[5] = 1

for i in range(0,L):            # for random initial state
    S[i] = random.randint(0, 1)
print("P3:")
print ("Initial state: ", S)

keystream = [0]*length
for i in range(0,length):
     keystream[i] = lfsr.LFSR(C, S)

print ("First period: ", lfsr.FindPeriod(keystream))
print("Since max period is 31 and the period of p_3 is 31, it generates the maximum period sequence.")
#print ("L and C(x): ", lfsr.BM(keystream))
#print ("keystream: ", keystream)

print()
print("--------------------------------------------------")
print()