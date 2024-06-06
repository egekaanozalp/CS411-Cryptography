# Apply the algorithm in the slide 12 of Mathematical Background:
import math
import myntl

def find_solution(a, b, n):
    d = math.gcd(a, n)
    if d == 1:
        sol = b*(myntl.modinv(a, n)) % n
        print("There is exactly one solution:", sol)
    else:
        if b % d != 0:
            print("There is no solution!")
            print("gcd(a, n) =", d, "and it does not divide the b value!")
        else:
            a_to_d = a//d
            b_to_d = b//d
            n_to_d = n//d
            x_prime = (myntl.modinv(a_to_d, n_to_d) * b_to_d) % n_to_d
            solutions = [x_prime + (k * n_to_d) for k in range(d)]
            print("gcd(a, n) =", d, "and it divides the b value.")
            print("a/d =", a_to_d)
            print("b/d =", b_to_d)
            print("n/d =", n_to_d)
            print("x_prime =", x_prime)
            print("There are exactly " + str(d) + " solutions:")
            for sol in solutions:
                print(sol)

# Part A:
print()
n = 2163549842134198432168413248765413213216846313201654681321666
a = 790561357610948121359486508174511392048190453149805781203471
b = 789213546531316846789795646513847987986321321489798756453122
print("Part A:")
find_solution(a, b, n)
print()
print("-----------------------------------------------------------")
print()

# Part B:
n = 3213658549865135168979651321658479846132113478463213516854666
a = 789651315469879651321564984635213654984153213216584984653138
b = 798796513213549846121654984652134168796513216854984321354987
print("Part B:")
find_solution(a, b, n)
print()
print("-----------------------------------------------------------")
print()

# Part C:
n = 5465132165884684652134189498513211231584651321849654897498222
a = 654652132165498465231321654946513216854984652132165849651312
b = 987965132135498749652131684984653216587986515149879613516844
print("Part C:")
find_solution(a, b, n)
print()
print("-----------------------------------------------------------")
print()

# Part D:
n = 6285867509106222295001894542787657383846562979010156750642244
a = 798442746309714903987853299207137826650460450190001016593820
b = 263077027284763417836483408268884721142505761791336585685868
print("Part D:")
find_solution(a, b, n)
print()
print("-----------------------------------------------------------")