import RSA_OAEP as rsop
from tqdm import tqdm

c = 15563317436145196345966012870951355467518223110264667537181074973436065350566
e = 65537
N = 73420032891236901695050447655500861343824713605141822866885089621205131680183

# Brute-Force Attack:
# The possible values of R: R ∈ [1-255] and R ∈ Z.
# The possible values of the pin: P ∈ [0000-9999] and P ∈ Z.
# Based on these two information, encrypt all possible pin values
# with the help of each possible R values.
pbar = tqdm(total=255, position=0, leave=True)
print()
pin = -1
for R in range(1, 256):
    for P in range(10000):
        if(rsop.RSA_OAEP_Enc(P, e, N, R) == c):
            pbar.clear()
            pbar.close()
            pin = P
            print("The pin is:", P)
            print("The R value is:", R)
            break
    pbar.update(1)
print()
# Since this code block takes a while, the answer is:
# The pin: 1308
# The R value: 206