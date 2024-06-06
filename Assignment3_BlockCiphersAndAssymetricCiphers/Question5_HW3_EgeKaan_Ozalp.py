import client
import BitVector

'''
a_x, b_x = client.get_poly()
'''
a_x = BitVector.BitVector(bitstring='01101101')   # 1 + x^2 + x^3 + x^5 + x^6
b_x = BitVector.BitVector(bitstring='00011001')   # 1 + x^3  x^4
mod = BitVector.BitVector(bitstring='111000011')  # 1 + x + x^6 + x^7 + x^8

result_a = a_x.gf_multiply_modular(b_x, mod, 8)
print(result_a)

client.check_mult(result_a)

result_b = a_x.gf_MI(mod, 8)
print(result_b)

client.check_inv(result_b)