# pip install datasketch

# from datasketch import HyperLogLog

# # Create HLL with error of ~2%
# hll = HyperLogLog(p=10)

# # Let's simulate a lot of data!
# for i in range(100000):
#     hll.update(str(i).encode("utf-8"))

# print("Estimated unique items:", len(hll))


import hashlib
import math

def hash_binary(value):
    h = hashlib.sha1(value.encode()).hexdigest()
    bin_str = bin(int(h, 16))[2:].zfill(160)
    return bin_str

def count_leading_zeroes(bits):
    return len(bits) - len(bits.lstrip('0')) + 1 # Add 1 as per HLL

def hyperloglog_basic(data, p_bits=10):
    """Basic Hyperloglog Algo."""
    m = 2 ** p_bits
    registers = [0] * m

    for item in data:
        hash_bits = hash_binary(item)
        bucket = int(hash_bits[:p_bits], 2)
        
        rest = hash_bits[p_bits:]
        lz = count_leading_zeroes(rest)

        registers[bucket] = max(registers[bucket], lz)

    print(registers)
    
    # Bias correction
    alpha_m = 0.7213 / (1 + 1.079 / m)
    indicator = sum([2 ** -reg for reg in registers])
    raw_estimate = alpha_m * m ** 2 / indicator

    # Range correction
    if raw_estimate <= 2.5 * m:
        V = registers.count(0)
        if V > 0:
            return m * math.log(m / V)
    return raw_estimate

if __name__ == "__main__":
    data = [str(i) for i in range(100000)]
    print(hyperloglog_basic(data, p_bits=10))


        