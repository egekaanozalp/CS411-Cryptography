import sympy

n = 9244432371785620259
c = 655985469758642450
e = 65537

# We need to find the p and q s.t. p*q = n.
# However, it takes very long time to find
# such prime numbers without using any library.
# Without any library, here is a method that
# I have initially tried:

# Since n%2 == n%3 == n%5 != 0:
# possible_prime_factors = [i for i in range(3, n+1, 2) if i%3 != 0 and i%5 != 0 and n%i == 0]
# However it tooks a lot of time, hence i will use sympy only for this part of the question:
primes = sympy.factorint(n)
p = list(primes.keys())[0]
q = list(primes.keys())[1]
print("p:", p)
print("q:", q)
print("Checking if the values are correct:", p*q == n)

# Since d = e**-1 mod phi(n), we first need to find phi(n):
phi_n = (p-1) * (q-1)
print("phi(n):", phi_n)
d = pow(e, -1, phi_n)
print("private key is d =", d)

# Final move, finding the message:
m = pow(c, d , n)
print("m value is:", m)
decoded_m = m.to_bytes((m.bit_length()//8 + 1), byteorder="big").decode("utf-8")
print()
print("The message is:", decoded_m)
print()