import time
import copy

class SHA512:
    def __init__(self):
        self.H = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b,
                  0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
                  0x510e527fade682d1, 0x9b05688c2b3e6c1f,
                  0x1f83d9abfb41bd6b, 0x5be0cd19137e2179]
        self.M = []
        self.total_length = 0

    def ROTR(x, n):
        return ((x >> n) | (x << 64 - n)) % 2 ** 64

    def SHR(x, n):
        return x >> n

    def Ch(x, y, z):
        return (x & y) ^ (~x & z)

    def Maj(x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def byte_to_word(self):
        n = 0
        for i in range(8):
            n += self.M[i] << (8 - 1 - i) * 8
        del self.M[0:8]
        return n

    def word_to_byte(n):
        p = []
        for i in range(8):
            p.append((n >> (8 - 1 - i) * 8) % 2 ** 8)
        return p

    block_size = 128

    digest_size = 64

    def Σ0(x):
        return SHA512.ROTR(x, 28) ^ SHA512.ROTR(x, 34) ^ SHA512.ROTR(x, 39)

    def Σ1(x):
        return SHA512.ROTR(x, 14) ^ SHA512.ROTR(x, 18) ^ SHA512.ROTR(x, 41)

    def σ0(x):
        return SHA512.ROTR(x, 1) ^ SHA512.ROTR(x, 8) ^ SHA512.SHR(x, 7)

    def σ1(x):
        return SHA512.ROTR(x, 19) ^ SHA512.ROTR(x, 61) ^ SHA512.SHR(x, 6)

    K = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
        0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
        0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
        0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
        0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
        0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
        0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
        0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
        0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
        0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
        0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
        0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
        0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
        0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
        0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
        0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
        0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
        0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
        0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
        0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]

    def block_round(self):
        
        W = []
        for i in range(16):
            W.append(SHA512.byte_to_word(self))
        for t in range(16, 80):
            W.append((SHA512.σ1(W[t - 2]) + W[t - 7] + SHA512.σ0(W[t - 15]) + W[t - 16]) % 2 ** 64)

        a = self.H[0]
        b = self.H[1]
        c = self.H[2]
        d = self.H[3]
        e = self.H[4]
        f = self.H[5]
        g = self.H[6]
        h = self.H[7]

        for t in range(80):
            T1 = (h + SHA512.Σ1(e) + SHA512.Ch(e, f, g) + SHA512.K[t] + W[t]) % 2 ** 64
            T2 = (SHA512.Σ0(a) + SHA512.Maj(a, b, c)) % 2 ** 64
            h = g
            g = f
            f = e
            e = (d + T1) % 2 ** 64
            d = c
            c = b
            b = a
            a = (T1 + T2) % 2 ** 64

        self.H[0] = (self.H[0] + a) % 2 ** 64
        self.H[1] = (self.H[1] + b) % 2 ** 64
        self.H[2] = (self.H[2] + c) % 2 ** 64
        self.H[3] = (self.H[3] + d) % 2 ** 64
        self.H[4] = (self.H[4] + e) % 2 ** 64
        self.H[5] = (self.H[5] + f) % 2 ** 64
        self.H[6] = (self.H[6] + g) % 2 ** 64
        self.H[7] = (self.H[7] + h) % 2 ** 64

    def update(self, input):
        self.M.extend(input)
        self.total_length += len(input)

        while len(self.M) >= SHA512.block_size:
            SHA512.block_round(self)

    def final(self):
        self.M.append(0x80)
        
        n = 0
        if len(self.M) + 17 <= SHA512.block_size:
            n = SHA512.block_size - 8
        else:
            n = SHA512.block_size * 2 - 8
        while len(self.M) != n:
            self.M.append(0x00)

        self.total_length *= 8
        self.M.extend(SHA512.word_to_byte(self.total_length))

        while len(self.M) > 0:
            SHA512.block_round(self)

        output = []
        for i in range(8):
            output.extend(SHA512.word_to_byte(self.H[i]))

        return output

class HMAC:
    def __init__(self, key):
        self.outer_hash = SHA512()
        self.inner_hash = SHA512()
	
        if len(key) > SHA512().block_size:
            key = SHA512(key)
        else:
            while len(key) != SHA512().block_size:
                key.append(0x00)   
        
        opad_key = []
        for i in key:
            opad_key.append(i ^ 0x5c)
        self.outer_hash.update(opad_key)
        
        ipad_key = []
        for i in key:
            ipad_key.append(i ^ 0x36)
        self.inner_hash.update(ipad_key)
            
    def update(self, input):
        self.inner_hash.update(input)
        
    def final(self):
        self.outer_hash.update(self.inner_hash.final())
        return self.outer_hash.final()       

def pbkdf2(password, salt, count):
    temp = HMAC(password)

    prf = copy.deepcopy(temp)
    prf.update(salt)
    prf.update([0, 0, 0, 1])
    out = prf.final()

    buf = copy.deepcopy(out)
    for i in range(1, count):
        prf = copy.deepcopy(temp)
        prf.update(buf)
        buf = prf.final()
        for r in range(64):
          out[r] ^= buf[r]
    return out

def print_hex(value):
    i = 0
    for x in value:
        if (i != 0) & (i % 4 == 0):
            print(' ', sep = '', end = '')
        print(format(x >> 4, 'X'), sep = '', end = '')
        print(format(x & 0x0f, 'X'), sep = '', end = '')
        i = i + 1


def main():
    print_hex(pbkdf2([0x61, 0x62, 0x63], [0x61, 0x62, 0x63], 0xffff))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\n%sms" % ((time.time() - start_time) * 1000))
    
