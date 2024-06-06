import lfsr

# All implementations are based on the 10th slide of the Stream Ciphers presentation.

# X1:
print()
x1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
print("Expected linear complexity of the sequence of x1:", (len(x1)/2) + 2/9)
print("The complexity of x1 based on BMA is:", lfsr.BM(x1)[0])
if lfsr.BM(x1)[0] >= (len(x1)/2) + 2/9:
    print("Since the complexity of x1 >= the expected complexity, x1 is not predictable.")
else:
    print("Since the complexity of x1 < the expected complexity, x1 is predictable.")

print()
print("--------------------------------------------------------------------------------")
print()

# X2:
x2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]
print("Expected linear complexity of the sequence of x2:", (len(x2)/2) + 2/9)
print("The complexity of x2 based on BMA is:", lfsr.BM(x2)[0])
if lfsr.BM(x2)[0] >= (len(x2)/2) + 2/9:
    print("Since the complexity of x2 >= the expected complexity, x2 is not predictable.")
else:
    print("Since the complexity of x2 < the expected complexity, x2 is predictable.")

print()
print("--------------------------------------------------------------------------------")
print()

# X3:
x3 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
print("Expected linear complexity of the sequence of x3:", (len(x3)/2) + 2/9)
print("The complexity of x3 based on BMA is:", lfsr.BM(x3)[0])
if lfsr.BM(x3)[0] >= (len(x3)/2) + 2/9:
    print("Since the complexity of x3 >= the expected complexity, x3 is not predictable.")
else:
    print("Since the complexity of x3 < the expected complexity, x3 is predictable.")

print()
print("--------------------------------------------------------------------------------")
print()