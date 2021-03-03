def countBits(num):
    bits = [0]
    for i in range(1, num + 1):
        a = i >> 1
        b = i & 1
        bits.append(bits[i >> 1] + (i & 1))
    return bits
countBits(16)