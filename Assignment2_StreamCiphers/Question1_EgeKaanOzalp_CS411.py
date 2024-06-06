from client import getQ1, checkQ1a, checkQ1b, checkQ1c
from math import gcd

'''
# Starting with getting the n and t numbers:
n, t = getQ1()
print(n)
print(t)
'''

# Assign the given values from the server to the n and t values:
n = 922
t = 23

#-------------------------------------------------------------------------------------------------------

# This is the Part A of the first question:
# To create the group Z*_n, I need to find nums ∈ {1...n-1} s.t. gcd(num, n)=1.

group_a = set(num for num in range(1, n) if gcd(num, n)==1)
print("The answer of Part A:", len(group_a))
checkQ1a(len(group_a))
# Now we have group_a representing the Z*_n.

#-------------------------------------------------------------------------------------------------------

# This is the Part B of the first question:
# Finding an element e ∈ Z*_n s.t. Z*_n can be created using the powers of e.
generator = 0
for num in group_a:
  pows = set()
  for p in range(1, n):
    pows.add(pow(num, p, n))
  if pows == group_a:
    generator = num
    break
print("The answer of Part B:", generator)
checkQ1b(generator)

#-------------------------------------------------------------------------------------------------------

# This is the Part C of the first question:
# Finding a num such that num^i % n != 1 for i < t and num^t % n = 1
for num in group_a:
  control = False
  for i in range(1, t):
    if pow(num, i, n) == 1:
      control=True
      break
  if pow(num, t, n) == 1 and control == False:
    print("The answer of Part C:", num)
    checkQ1c(num)
    break